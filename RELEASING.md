# Releasing

Maintainer notes for publishing this library to PyPI as
[`AutoTrader-Web-API-Stocks-Developer`](https://pypi.org/project/AutoTrader-Web-API-Stocks-Developer/).

Last verified: **2026-08-08** (release 1.4.0).

**Publishing is keyless.** [`.github/workflows/publish.yml`](.github/workflows/publish.yml) does it,
using a PyPI [trusted publisher](https://docs.pypi.org/trusted-publishers/): the job requests a
short-lived GitHub OIDC token, PyPI validates it against the publisher registered for this project,
and issues a temporary token for that one upload. **No API token is stored in this repository or
anywhere else**, so there is nothing to rotate and nothing to leak.

## Releasing

**1. Bump the version.** One place only — `version=` in `setup.py`.

**2. Commit, then tag and push the tag.**

```bash
git commit -am "Release 1.5.0"
git push
git tag v1.5.0 && git push origin v1.5.0
```

The tag must match `setup.py` — the build compares them and fails if they disagree. That matters
here more than most places, because **a PyPI version can never be re-uploaded**, even after deleting
the release.

**3. Watch the run** under the repo's Actions tab, then confirm the install:

```bash
python -m pip install --upgrade AutoTrader-Web-API-Stocks-Developer
```

The workflow runs `twine check` before uploading, so a long description that would not render on
PyPI fails the build instead of being discovered after the upload is permanent.

## One-time setup

Done once per project, and needed before the first keyless release.

On PyPI: **Your projects → Manage → Publishing → GitHub**, then add:

| Field | Value |
|---|---|
| Owner | `stocks-developer` |
| Repository name | `autotrader-python-lib` |
| Workflow name | `publish.yml` |
| Environment | *(leave empty — this workflow does not use a GitHub environment)* |

PyPI strongly encourages a GitHub environment for the extra approval gate. This workflow does not use
one, to keep the setup simple. To add it later: create an environment in the repo settings, put
`environment: <name>` on the `publish` job, and set the same name in the PyPI publisher — all three
must agree or the upload is rejected.

### Checking the publisher works

Run the workflow manually (`workflow_dispatch`) without bumping the version. It will build the
current version and try to upload it, and the **error tells you what you need to know**:

- `400 File already exists` — **the publisher is configured correctly.** PyPI authenticated the
  workflow and would have accepted the upload; it only refused because that version is already
  published.
- `403 Forbidden` — the publisher is wrong or missing. Check the owner, repository, workflow name and
  environment all match exactly.

A deliberately failed run of the first kind is in this repo's history from 2026-08-08. That is what it
was for.

Successful runs also publish **Sigstore attestations** to a public transparency log, so a release can
be traced back to this workflow in this repository. That comes with trusted publishing and needs no
setup.

## Publishing by hand

Should not be needed, and is discouraged — a stored token is exactly what trusted publishing removes.
The steps below are kept for the case where GitHub Actions is unavailable.

### Before you start

- Every change is committed and pushed. The build packages the working tree, so anything uncommitted
  would ship unreviewed.
- Check what is already published, and pick the next version from that — not from `setup.py`, which
  can lag:

  ```bash
  curl -s https://pypi.org/pypi/AutoTrader-Web-API-Stocks-Developer/json | python -c "import json,sys; print(json.load(sys.stdin)['info']['version'])"
  ```

  New API calls are a minor bump (1.3.5 -> 1.4.0); a fix is a patch bump.

> **A PyPI version can never be re-uploaded.** Deleting a release does not free the number. Get it
> right before you upload, and use `twine check` to catch metadata problems first.

### Steps

**1. Bump the version.** One place only — `version=` in `setup.py`.

**2. Install/refresh the build tooling.**

```bash
python -m pip install --upgrade build twine
```

**3. Clean, then build.** Stale artifacts in `dist/` get uploaded too, so remove them.

```bash
rm -rf dist build *.egg-info      # Windows: rmdir /s /q dist build & del /q *.egg-info
python -m build
```

This produces both a wheel and an sdist in `dist/`.

**4. Verify before uploading.**

```bash
python -m twine check dist/*
```

`PASSED` for both files means the long description will render on PyPI. Also confirm the artifact
really contains what you are releasing — a wheel is a zip:

```bash
python -c "import zipfile,sys; z=zipfile.ZipFile(sys.argv[1]); print(z.read('com/dakshata/autotrader/api/AutoTrader.py').decode('utf-8').count('def place_'))" dist/*.whl
```

**5. Upload.**

```bash
python -m twine upload dist/*
```

The username is the literal `__token__` and the password is a PyPI API token. Prefer environment
variables so the token never enters your shell history:

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD="<your PyPI API token>"
python -m twine upload dist/*
```

Use a **project-scoped** token, never an account-wide one. Never commit a token or paste one into an
issue, a chat or a document.

**6. Confirm the release installs.**

```bash
python -m pip install --upgrade AutoTrader-Web-API-Stocks-Developer
python -c "import com.dakshata.autotrader.api.AutoTrader as m; print('ok')"
```

## Gotchas

- **`setup.py` must read `README.md` with `encoding="utf-8"`.** It does now. Before 2026-08-08 it used
  a bare `open()`, which falls back to the platform codec — so once the README gained a rupee sign and
  emoji, every build on Windows died with `UnicodeDecodeError: 'charmap' codec can't decode byte 0x81`.
  If you ever see that, this is why.
- **Bump the version before building, not after.** `python -m build` bakes the version into the
  filenames; building first and bumping after silently republishes the old number.
- **Update the website after a release.** The Python setup page installs "latest", so nothing breaks
  if you forget — but the page states the current version in two places ("The current version is
  X.Y.Z" and the minimum version for a feature), and a stale number there misleads people into
  thinking they are up to date. Page:
  `stocksdev-website/src/content/docs/client-setup/python-library.md`. Bump `lastUpdated` in the same
  edit. A brand-new API call should also get a "needs version X.Y.Z" note on its API reference page.
