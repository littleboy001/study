import struct
from socket import *
import os
	
def main():
	#1.输入下载文件名
	request_name = input("请输入要下载的文件名:")

	#2.对发送的请求信息格式化
	request_data = struct.pack("!H%dsb5sb"%len(request_name),1,request_name,0,"octet",0)

	#3.建立套接字
	udp_socket = socket(AF_INET,SOCK_DGRAM)

	#4.发送请求
	udp_socket.sendto(request_data,("192.168.119.215",69))

	#5.创建文件来接收信息
	f = open(request_name,"w")
	num = 0
	Flag = True

	while True:
		receive_data = udp_socket.recvfrom(1024)

		#6.对信息进行分割，取出IP及端口
		tftp_data,server_info = receive_data

		#7.对操作序号和顺序号进行分割并格式化
		op_num = struct.unpack("!H",tftp_data[:2])
		packet_num = struct.unpack("!H",tftp_data[2:4])

		#8.对操作序号进行判别是否为3，并用一个数记录顺序号
		#用于判别是否和接收的顺序号一致，一致则接收，超过65536需重置为0
		print("op_num=%d")
		if op_num[0] == 3:
			num += 1

			if num == 65536:
				num = 0

			if num == packet_num[0]:
				f.write(tftp_data[4:])


		#9.发送回馈信息4给获得的IP和port
		ack_data = struct.pack("!HH",4,packet_num[0])
		udp_socket.sendto(ack_data,server_info)

		#10.对操作序号进行判别是否为5，是则输出提示信息表明错误并对操作标志进行修改为False
		if op_num[0] == 5:
			print("sorry，没有这个文件")
			Flag = False
		#11.判断长度是否小于516是则说明传输结束break
		if len(tftp_data) < 516:
			break

	#12.利用判断标志判断是否为对文件操作结束，是则关闭文件，否则删除创建的文件
	if Flag == True:
		f.close()
	else:
		os.unlink(request_name)

#13.运行main函数
if __name__ == '__main__':
	main()