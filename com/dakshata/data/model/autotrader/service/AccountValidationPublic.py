# -*- coding: utf-8 -*-
"""
Represents the result of validating one trading account, as returned by
validate_all_accounts().
"""

class AccountValidationPublic:

    def __init__(self, tradingAccId=None, pseudoAccId=None, valid=None, \
        result=None, message=None, tradingAccLoginId=None, \
        sessionState=None, *args, **kwargs):

        self.tradingAccId = tradingAccId
        self.pseudoAccId = pseudoAccId
        self.valid = valid
        # SUCCESS, FAILURE or PENDING
        self.result = result
        self.message = message
        self.tradingAccLoginId = tradingAccLoginId
        # MISSING, LOGGED_IN, LOGGED_OUT or ERROR
        self.sessionState = sessionState

    def __str__(self):
        return "AccountValidationPublic [tradingAccLoginId=%s, valid=%s, " \
            "result=%s, sessionState=%s, message=%s, tradingAccId=%s]" % \
            (self.tradingAccLoginId, self.valid, self.result, \
            self.sessionState, self.message, self.tradingAccId)

    def __repr__(self):
        return self.__str__()
