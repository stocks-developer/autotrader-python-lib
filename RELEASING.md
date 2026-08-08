# Releasing

Maintainer notes for publishing this library to PyPI as
[`AutoTrader-Web-API-Stocks-Developer`](https://pypi.org/project/AutoTrader-Web-API-Stocks-Developer/).

Last verified: **2026-08-08** (release 1.4.0).

## Before you start

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

## Steps

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
- The website's Python setup page installs "latest" and does **not** pin a version, so a release needs
  no website change. Only the Java library page pins a version.
