#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:27:03 2018

@author: whitestallion
"""

import sys
import socket
import struct
import array
import datetime
import inspect
import time
import argparse
import os.path
from ibapi import wrapper
import ibapi.decoder
import ibapi.wrapper
from ibapi.common import *
from ibapi.ticktype import TickType, TickTypeEnum
from ibapi.comm import *
from ibapi.message import IN, OUT
from ibapi.client import EClient
from ibapi.connection import Connection
from ibapi.reader import EReader
from ibapi.utils import *
from ibapi.execution import ExecutionFilter
from ibapi.scanner import ScannerSubscription
from ibapi.order_condition import *
from ibapi.contract import *
from ibapi.order import *
from ibapi.order_state import *

class TestApp(wrapper.EWrapper, EClient):
    def __init__(self):
        wrapper.EWrapper.__init__(self)
        EClient.__init__(self, wrapper=self)
        
    def nextValidId(self, orderId:int):
            print("setting nextValidOrderId: ", orderId)
            self.nextValidOrderId = orderId
            #here is where you start using api
            contract = Contract()
            contract.localSymbol = "ESM8"
            contract.secType = "FUT"
            contract.currency = "USD"
            contract.exchange = "GLOBEX"
            self.reqRealTimeBars(1, contract, 5, "TRADES", False, "XYZ")
    
    @iswrapper
    def error(self, reqId:TickerId, errorCode:int, errorString:str):
        if errorCode == 2016 :
            print("ashley is bae")
        print("Error. Id: " , reqId, " Code: " , errorCode , " Msg: " , errorString)
            
    @iswrapper
    def realtimeBar(self, reqId:int, time:int, open:float, high:float, low:float, close:float, volume:int, wap:float, count:int):
        super().realtimeBar(reqId, time, open, high, low, close, volume, wap, count)
        print("RealTimeBars. ", reqId, ": time ", time, ", open: ",open, ", high: ", high, ", low: ", low, ", close: ", close, ", volume: ", volume, ", wap: ", wap, ", count: ", count)

def main():
    app = TestApp()
    app.connect("127.0.0.1", 4001, 1)
    print("serverVersion:%s connectionTime:%s" % (app.serverVersion(), app.twsConnectionTime()))
    print("initilaizing run... please wait")
    app.run()
    
if __name__ == "__main__":
    main()
