import sys
from hbase import *
from hbase import ttypes
# sys.path.append('/home/hadoop/Documents/thrift/gen-py/hbase') # 引入正确的生成文件gen-py路径

from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol
transport = TSocket.TSocket('193.169.100.33',2181)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Hbase.Client(protocol)
transport.open()

client.getTableNames()