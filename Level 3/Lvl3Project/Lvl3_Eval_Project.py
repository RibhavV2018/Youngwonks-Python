from pprint import pprint
from tkinter import messagebox
from tkinter import *
from pprint import pprint
import socket
import time
import sqlite3
from datetime import datetime

class RandomNumsDataBase:
    def __init__(self):
        self.conn = sqlite3.connect("RandomNums.db", timeout=10)
        self.c = self.conn.cursor()
    def CreateColumns(self):
        self.c.execute('CREATE TABLE RandomNumbers(Numbers INTEGER,Time NVARCHAR(255) PRIMARY KEY,SortedNumbers INTEGER DEFAULT "N/A",TimeSorted NVARCHAR(255) DEFAULT "N/A")' )
    def insertInfo(self, nums):
        print(1)
        d = datetime.strftime(datetime.now(), "%m/%d/%Y, %H:%M:%S")
        cmd = f'INSERT INTO RandomNumbers (Numbers, Time, SortedNumbers, TimeSorted) VALUES ({nums}, "{d}", "N/A", "N/A")'
        self.c.execute(cmd)
        self.dtt = d
        self.conn.commit()
    def updateSorted(self, nums):
        d = datetime.strftime(datetime.now(), "%m/%d/%Y, %H:%M:%S")
        cmd = f'UPDATE RandomNumbers SET SortedNumbers = {nums}, TimeSorted = "{d}" WHERE Time == "{self.dtt}"'
        self.c.execute(cmd)
        self.conn.commit()
        
    def selectAll(self):
        self.c.execute('SELECT * FROM RandomNumbers')
        rows=self.c.fetchall()
        for r in rows:
            ht =[]
            for item in range(0, 4):
                    ht.append(str(r.__getitem__(item)))
            print("|".join(ht))

db = RandomNumsDataBase()

db.selectAll()


class client:
    def __init__(self):
        self.HOST = '192.168.1.114'
        self.PORT = 1514
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.root = Tk()
        self.root.title('Random Numbers')
        self.root.geometry('400x100')
        self.root.columnconfigure(0, weight = 2)
        self.root.columnconfigure(1, weight = 2)
        self.root.columnconfigure(2, weight = 2)
        self.frame1 = Frame(self.root, width = 200, height = 200)
        self.frame2 = Frame(self.root, width = 200, height = 200)
        b1 = Button(self.frame2, text = "GET", command = self.sendGetRequest)
        b2 = Button(self.frame2, text = "SORT", command = self.sortRandomNums)
        b3 = Button(self.frame2, text = "QUIT", command = self.root.destroy)
        self.frame1.pack()
        self.frame2.pack()
        self.label1 = Label(self.frame1, text = '?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ', font = ('Arial', 10))
        self.label1.pack(side = TOP)
        b1.grid(column = 0, row = 0)
        b2.grid(column = 1, row = 0)
        b3.grid(column = 2, row = 0)
    def connect(self):
        self.s.connect((self.HOST, self.PORT))
        self.s.sendall('Connection establish'.encode())
        self.s.close()
    def newSocket(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))
    def recieve(self):
        data = self.s.recv(1024).decode()
        if not data:
            return False
    
        print('Received from server', repr(data))
        return [True, data]
    def sortRandomNums(self):
        y =[]
        for num in self.x:
            if num == ' ':
                continue
            else:
                y.append(num)
        for i in range(1, len(y)):
            key = y[i]
            numLess = i-1
            while numLess >=0 and key < y[numLess]:
                y[numLess+1] = y[numLess]
                numLess -= 1
            y[numLess+1] = key
        ttt = ''.join(y)
        db.updateSorted(ttt)
        y = '   '.join(y)
        self.label1.destroy()
        self.label1 = Label(self.frame1, text = y, font = ('Arial', 10))
        self.label1.pack()
    def sendGetRequest(self):
        ##HTTP/1.1 GET
        self.newSocket()
        
        self.s.sendall('HTTP/1.1 GET'.encode())
        print('sent get reuest')
        while True:
            if c.recieve():
                self.x = c.recieve()[1]
                lt = self.x
                db.insertInfo(self.x)
                self.x = []
                for num in lt:
                    self.x.append(num)
                self.x = '   '.join(self.x)
                
                self.label1.destroy()
                self.label1 = Label(self.frame1, text = self.x, font = ('Arial', 10))
                self.label1.pack(side = TOP)
                self.s.close()
                break
            else:
                continue
            
c = client()
c.connect()
c.s.close()
