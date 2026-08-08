# -*- coding: utf-8 -*-
"""
Represents a trading account under your user, as returned by
fetch_all_trading_accounts(). Never carries credentials or any other
sensitive field.
"""

class TradingAccountPublic:

    def __init__(self, loginId=None, pseudoAccName=None, broker=None, \
        platform=None, licenseExpiryDate=None, live=None, systemId=None, \
        systemIdOfPseudoAcc=None, licenseDaysLeft=None, *args, **kwargs):

        self.loginId = loginId
        self.pseudoAccName = pseudoAccName
        self.broker = broker
        self.platform = platform
        self.licenseExpiryDate = licenseExpiryDate
        self.live = live
        self.systemId = systemId
        self.systemIdOfPseudoAcc = systemIdOfPseudoAcc
        self.licenseDaysLeft = licenseDaysLeft

    def __str__(self):
        return "TradingAccountPublic [loginId=%s, pseudoAccName=%s, broker=%s, " \
            "platform=%s, live=%s, licenseExpiryDate=%s, licenseDaysLeft=%s, " \
            "systemId=%s]" % (self.loginId, self.pseudoAccName, self.broker, \
            self.platform, self.live, self.licenseExpiryDate, \
            self.licenseDaysLeft, self.systemId)

    def __repr__(self):
        return self.__str__()
