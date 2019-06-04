# -*- coding: UTF-8 -*-

import socket

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("0.0.0.0", 31000))
sock.listen(5)

conn1, addr1 = sock.accept()
conn1_info = addr1[0] + "|" + str(addr1[1]) + "|0"
print(addr1[0], addr1[1])
conn1.sendall("#first connect\n".encode())
conn2, addr2 = sock.accept()
conn2_info = addr2[0] + "|" + str(addr2[1]) + "|1"
print(addr2[0], addr2[1])
conn2.sendall("#second connect\n".encode())

conn1.sendall(conn2_info.encode())
conn2.sendall(conn1_info.encode())

conn1.close()
conn2.close()
sock.close()