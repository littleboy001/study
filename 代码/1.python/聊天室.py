from socket import *
from threading import Thread


#1.发送信息
def send_data():
	while True:
		sendinfo = input("<<")
		udpSocket.sendto(sendinfo.encode("gb2312"),(destip,destport))

#2.接收信息
def receive_data():
	while True:
		recvinfo = udpSocket.recvfrom(1024)
		print(">>%s:%s"%(str(recvinfo[1]),recvinfo[0]))


#3.主函数，建立套接字
udpSocket = None
destip = ""
destport = 0
def main():

	global udpSocket
	global destip
	global destport

	destip = input("请输入目的IP:")
	destport = input("请输入目的端口:")

	udpSocket = socket(AF_INET,SOCK_DGRAM)
	udpSocket.bin("",4567)

	send = Thread(target = send_data)
	receive = Thread(target = receive_data)

	send.start()
	receive.start()

	send.join()
	receive.join()

if __name__ == '__main__':
	main()
