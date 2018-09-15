# -*- coding: utf-8 -*-

from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import *
import pymongo
import hashlib
import time
from datetime import datetime
class HBaseOperator():
    def __init__(self):
        self.host = "193.169.100.33"
        self.port = 2181
        self.transport = TBufferedTransport(TSocket(self.host, self.port))
        self.transport.open()
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = Hbase.Client(self.protocol)
    def __del__(self):
        self.transport.close()
    def getAllTablesInfo(self):
        #get table info
        listTables = self.client.getTableNames()
        print ("="*40)
        print ("Show all tables information....")
        for tableName in listTables:
            print ("TableName:" + tableName)
            listColumns = self.client.getColumnDescriptors(tableName)
            print (listColumns)
            listTableRegions = self.client.getTableRegions(tableName)
            print (listTableRegions)
            print ("+"*40)
if __name__ == '__main__':
    s=HBaseOperator()
    # s.getAllTablesInfo()
    from thrift.transport import TSocket, TTransport
    from thrift.protocol import TBinaryProtocol
    from hbase import Hbase

    # thrift默认端口是9090
    socket = TSocket.TSocket('193.169.100.33', 2181)
    socket.setTimeout(5000)

    transport = TTransport.TBufferedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    client = Hbase.Client(protocol)
    socket.open()

    print(client.getTableNames())  # 获取当前所有的表名