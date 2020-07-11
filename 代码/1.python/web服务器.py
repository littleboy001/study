from socket import *
from multiprocessing import Process

#接收客户端信息
def func(client_socket):
	recv_info = ""
	while  True:
		acquire_info = client_socket.recv(1024)
		if len(acquire_info)>0:
			print(acquire_info)
			recv_info += str(acquire_info)
		else:
			break

	#用HTTP协议分析请求信息
	if recv_info[:3] =="GET":

		#返还信息给客户端
		web_info = "HTTP/1.1 200 OK\r\n\r\nhello!"
		client_socket.send(web_info)
		client_socket.close()

def main():	
	#创建套接字
	web_socket = socket(AF_INET,SOCK_STREAM)
	#web_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	#绑定端口
	web_socket.bind(("",7777))

	#监听
	web_socket.listen(100)

	#接收客户端套接字
	while True:
		client_socket,client_info = web_socket.accept()
		p = Process(target = func,args = (client_socket,))
		p.start()
	
	#关闭服务器
	web_socket.close()

if __name__ == '__main__':
	main()
