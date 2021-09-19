from pprint import pprint
from tkinter import messagebox
from tkinter import *
from pprint import pprint
from datetime import datetime
from threading import Thread
import socket
import random
import time


def addLog(cmd):
    with open('Logs.txt', 'a') as file:
        d = datetime.now()
        time = datetime.strftime(d, "%m/%d/%Y, %H:%M:%S:")
        file.write('\n{} {}'.format(time, cmd))



class server:
    def __init__(self):
        self.GET = 'HTTP/1.1 GET'
        self.OK = 'HTTP/1.1 200 OK: '
        host = '0.0.0.0'
        port = 1514
        self. s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        print("Server Started")
        
    def connect(self):
        while True:
            self.s.listen(1)
            self.conn, self.addr = self.s.accept()
            print('connection from: ', self.addr)
            addLog("CONNECTION ACCEPTED: "+ str(self.addr))
            Thread(target = self.sendRandomNums).start()
    def recieve(self):
        data = self.conn.recv(1024).decode()
        if not data:
            return False
    
        print('Recieved from client: ', repr(data))
        return str(data)
    def sendRandomNums(self):
        print(1)
        while True:
            if self.recieve() == self.GET:
                addLog('Recieved: '+ self.GET)
                randomNums = ''.join([str(random.randint(1, 10)) for i in range (10)])
                print('random', randomNums, datetime.strftime(datetime.now(), "%m/%d/%Y, %H:%M:%S:"))
                self.conn.send(self.OK.encode())
                addLog('Sent: ' + self.OK)
                self.conn.send(randomNums.encode())
                addLog(randomNums)
            else:
                break
    def close(self):
        self.conn.close()
        
s = server()
s.connect()
s.close()
