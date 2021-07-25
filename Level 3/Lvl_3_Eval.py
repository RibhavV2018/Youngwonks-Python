from pprint import pprint
'''
Template
'''
'''
print("Template:")
class template: #defining a class
    c = [1, 2, 3]#class variable
    def __init__(self, a, b):# __init__ method
        self.a = a#instance variables
        self.b = b
    #functions
    def function1(self):
        return self.a
    def function2(self):
        return self.b
    def function3(self):
        return self.c

t = template(4, 5)
x = t.function1()
y = t.function2()
z = t.function3()
print(x)
print(y)
print(z)
print()
print()
'''
'''
OOP Principles
'''

'''
Polymorphism:
Polymorphism in OOP means using the same name for many things, attributes of
a class, which makes it easier to group information without having to use
different names for different classes

Overloading:
Overloading is when you have two functions with the same name, but with
different amounts of arguments. In Python, this does not work because the
function that was defined last will overwrite the first one, and will  be the
one recognized.
'''
'''
print("Polymorphism:")
#example
class Triangle:
    sides = 3
    polygon = True
    name = "Triange"
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        return self.height*self.width


class Square:
    sides = 4
    polygon = True
    name = "Square"
    def __init__(self,length):
        self.length = length
        
    def area(self):
        return self.length * self.length

shapes = [Triangle(4, 5), Square(3)]
for shape in shapes:
    print(shape.name + ":")
    print(shape.sides)
    print(shape.polygon)
    print(shape.area())
    print()
print()
print()
'''
'''
Encapsulation:
Encapsulation is the process of hiding data from the user that is not neccessary
to operate it, or private data that must be kept hidden. For example, if someone
was using your class in a program, you could hide data that is not relevant to
the program using encapsulation so they are not confused.
'''
'''
print("Encapsulation:")
#example
class Animal:
    legs = 3
    def __init__(self,size,name ):
        self.__size = size
        self.name = name
    def size(self):
        return self.__size, self.__names()
    def __names(self):
        return self.name

a = Animal(6, "Dog")

##Printing a.__size will not work, as it is a private variable, and will return
## error. Printing a.name will work, as it is not private.

print(a.name)
#print(a.__size)

##Printing a.__names() will not work, as it is a private function, and will 
## return an error, but printing a.size() will work, as it is not private.

print(a.size())
#print(a.__names())
print()
print()
'''
'''
Inheritence:
Inheritence is the concept of using a template parent class, so that you can
many of the same children classes with slight differences, without rewriting
the entire class
'''
'''
#example
print("Inheritance:")
class Country:
    name = "country"
    def __init__(self, population, size):
        self.population = population
        self.size = size
    def populations(self):
        return self.population
    def sizes(self):
        return self.size

class America(Country):
    name = "America"
    def __init__(self, population, size, food):
        self.population = population
        self.size = size
        self.food = food
    def foods(self):
        return self.food

a = America(700000000, 1000000000, "pizza")
print(a.name)
print(a.populations())
print(a.sizes())
print(a.foods())
print()
print()
'''
'''
Abstraction:
Abstraction is the concept of only showing neccesary data and methoda to the
user, and hiding uneccesary data and methods.
'''
'''
print("Abstraction:")
import abc
from abc import ABC, abstractmethod

class book(ABC):
    def __init__(self, pages, title):
        self.pages = pages
        self.title = title
    def name(self):
        print(self.title, self.pages)
    @abc.abstractmethod
    def story(self):
        pass
    @abc.abstractmethod
    def characters(self):
        pass
    

class The_Book_Theif(book):
    def __init__(self, pages, title):
        super().__init__(pages, title)
    def story(self):
        return "short"
    def characters(self):
        return "people"


class Star_Wars(book):
    def __init__(self, pages, title):
        super().__init__(pages, title)
    def story(self):
        return "long"
    def characters(self):
        return "aliens"


books = [The_Book_Theif(400, "The Book Theif"), Star_Wars(800, "A New Hope")]
for book in books:
    book.name()
    print(book.story())
    print(book.characters())
print()
print()


class animal(ABC):
    @abc.abstractmethod
    def sound(self):
        pass

class lion(animal):
    def sound(self):
        print("roar")

class wolf(animal):
    def sound(self):
        print("howl")

att = [wolf(), lion()]

for thing in att:
    thing.sound()

print()
print()
'''

'''
Tkinter
'''

'''
from tkinter import messagebox
from tkinter import *
from pprint import pprint

def submit(i, f, g, h, E1):
    score = 0
    if i.get() == 3:
        score = score + 1
    else:
        pass
    if f.get() == 1 and g.get() == 1 and h.get() ==1:
        score = score + 1

    if E1.get() == "42":
        score = score + 1
    print(score)
    root = Tk()
    root.title('score')
    c1 = Canvas(root,  )
    
    label23 = Label(root, text = "You got a %d" %(score), font = ("Arial", 20, "bold"))
    label23.pack()
    c1.pack()
name = StringVar()
name.set("Quiz")
messagebox.showwarning("OK", "You can only submit your answers once, which will be final")
frame1 = Frame(root, width = 200, height = 200)

label = Label(frame1, text = str(name.get()), font = ("Arial", 20, "bold"))




frame2 = Frame(root, width = 100, height = 100)

label2 = Label(frame2, text = "2. 1+1", font = ("Arial", 10))
i = IntVar()
radio = Radiobutton(frame2, text = "2", variable = i, value = 3)


radio2 = Radiobutton(frame2, text = "5", variable = i, value = 1)





frame3 = Frame(root, width = 200, height = 200)


label3 = Label(frame3, text = "1. 13984*0(select all that apply)", font = ("Arial", 10))

f = IntVar()
check = Checkbutton(frame3, text = "0", variable = f)
g = IntVar()
check2 = Checkbutton(frame3, text = "0", variable = g)
h = IntVar()
check3 = Checkbutton(frame3, text = "0",  variable = h)

label4 = Label(frame2, text = "3. 6*7", font = ("Arial", 10))
E1 = Entry(frame2)
E1.insert(0, "Answer here")
button2 = Button(frame2, text = "Clear", command = lambda: E1.delete(0,END))

button = Button(frame1, text = "Submit", command = lambda: submit(i, f, g, h, E1))

frame1.pack()
label.pack()
button.pack()

frame2.pack()
label4.grid(row = 0, column = 3)
E1.grid(row = 1, column = 4)
button2.grid(row = 2, column = 4)
label2.grid(row = 0, column = 1)
radio.grid(row=2, column = 2)
radio2.grid(row=3, column = 2)
frame3.place(x = 0, y = 40)
label3.place(x = 5, y =15)
check.place(x = 10, y = 35)
check2.place(x = 10, y = 55)
check3.place(x = 10, y = 75)

root.mainloop()
'''
'''

from tkinter import messagebox
from tkinter import *
from pprint import pprint
root = Tk()
root.title('Quiz')
c1 = Canvas(root)
c1.create_line((10, 50), (200, 36), width = 2)
c1.create_rectangle(100, 200, 20, 100, width = 2)
c1.create_oval(300, 100, 200, 200, width = 2)
c1.create_arc(200, 20, 300, 40, start = 0, extent = 90, width = 2)
c1.create_polygon([200, 200, 200, 250, 250, 250, 270, 220 ], outline = "blue", width = 1)
c1.pack()

root.mainloop()

'''


'''
Sqlite 3
'''

'''
import sqlite3
from os import listdir
from os.path import isfile, join


class database:
    def __init__(self):
        self.mypath = 'C:\\Users\\barna\\Documents\\YoungWonks\\Level 3'
        self.onlyfiles = [f for f in listdir(self.mypath) if isfile(join(self.mypath, f))]
        self.databases = []
        self.data_options = []
        for file in self.onlyfiles:
            if ".db" in file:
                self.databases.append(file)
        for index, database in enumerate(self.databases):
            self.data_options.append(str(index+1) + ") " + database)
            print(str(index+1) + ") " + database)
        x = input()
        for data in self.data_options:
            data1 = data.split(" ")
            for thing in data1:
                if data1.index(thing) == 0:
                    if x in thing:
                        self.conn = sqlite3.connect(str(data1[data1.index(thing) + 1]), timeout=10)
                        self.c = self.conn.cursor()

    def create_database(self):
        self.c.execute('CREATE TABLE Peoples (StudentID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,StudentName NVARCHAR(255),ParentName NVARCHAR(255),City  NVARCHAR(255),Country NVARCHAR(255) , GPA FLOAT(4,2), dateStarted DATE)' )
        self.c.execute('INSERT INTO Peoples (StudentName,ParentName, City,Country  , GPA, dateStarted) VALUES ("Tanya Anand","Amit Anand","Delhi","India",3.31,"2015-01-12")');
        self.c.execute('INSERT INTO Peoples (StudentName,ParentName, City,Country  , GPA ,  dateStarted) VALUES ("Ishita Reddy","Aditya Reddy","Bangalore","India",3.12,"2013-10-23")');
        self.c.execute('INSERT INTO Peoples (StudentName,ParentName, City,Country  , GPA , dateStarted) VALUES ("Ankit Babu","Raj Babu","Banerjee","India",2.73,"2015-04-05")');
        self.c.execute('INSERT INTO Peoples (StudentName,ParentName, City ,Country  , GPA ,  dateStarted) VALUES ("Random1","Random2","Bangalore","India",2.57,"2014-10-22")');
        self.c.execute('INSERT INTO Peoples (StudentName,ParentName, City ,Country  , GPA ,  dateStarted) VALUES ("Random3","Random4","Delhi","India",4.00,"2011-07-21")');
        self.c.execute('INSERT INTO Peoples (StudentName,ParentName, City ,Country  , GPA ,  dateStarted) VALUES ("Random5","Random6","Delhi","India",4.20,"2015-03-07")');
        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Random7","Random8","Bangalore","India",3.74,"2016-04-19")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA ,  dateStarted) VALUES ("Angel Puri","Anusha Puri","Bangalore","India",3.52,"2017-08-25")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA ,  dateStarted) VALUES ("Niti Pandey","Pavithra Pandey","Delhi","India",4.40,"2012-04-11")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA ,  dateStarted) VALUES ("Shreya Singh","Mayank Singh","Mumbai","India",2.71,"2016-02-09")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Rohan Pandey","Parth Pandey","Bangalore","India",2.33,"2017-01-20")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Nikita Singh","Karan Singh","Bangalore","India",2.94,"2015-10-02")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Ayushi Pandey","Pavithra Pandey","Delhi","India",2.45,"2012-04-11")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Mary Singh","Rohan Singh","Mumbai","India",2.97,"2017-10-09")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Sam Pandey","Ram Pandey","Bangalore","India",3.61,"2017-04-11")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Nick He","Mike He","Shanghai","China",3.34,"2015-07-11")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Mary Lee","Henry Lee","Seoul","South Korea",3.12,"2013-11-22")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Lily Wang","Mary Wang","Hongzhou","China",3.61,"2015-05-11")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Steve Liu","Sam Liu","Beijing","China",2.34,"2015-11-30")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("James Tang","Kelly Tang","Hong Kong","China",4.12,"2016-08-29")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Ricky Ma","Jack Ma","Shanghai","China",3.33,"2015-05-23")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Eric Zhou","Edward Zhou","Shanghai","China",4.21,"2017-05-12")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Jessica Lu","Andy Lu","Beijing","China",3.75,"2017-06-10")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Alice Chen","Jacky Chen","Seoul","South Korea",3.49,"2015-02-25")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Ethan Roberson","Sue Roberson","San Jose","USA",3.21,"2017-12-31")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("John Smith","Eve Smith","San Francisco","USA",4.05,"2016-04-15")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Grace Davis","Bill Davis","San Jose","USA",2.71,"2015-06-23")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("William Johnson","Sean Johnson","San Jose","USA",2.39,"2017-06-21")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Ken Nelson","Nick Nelson","San Francisco","USA",3.51,"2015-10-04")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Michell Cook","King Cook","San Jose","USA",2.87,"2017-05-19")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Anna Neckson","Amy Neckson","San Jose","USA",2.53,"2014-07-22")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Sophie Brown","Sue Brown","San Francisco","USA",4.32,"2013-09-05")');
##        self.c.execute('INSERT INTO Student (StudentName,ParentName, City ,Country  , GPA , dateStarted) VALUES ("Bob Smith","Susan Smith","San Jose","USA",3.34,"2016-07-05")');
        self.conn.commit()
        self.c.close()

    def choose_option(self, option, x):
        for op in option:
                option1 = op.split(" ")
                for thing in option1:
                    if option1.index(thing) == 0:
                        if x in thing:
                            return str(option1[option1.index(thing) + 1])
    def tables_create(self):
        table  = list()
        tables = list()
        table2 = list()
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        for name in self.c.fetchall():
            if "<sqlite3.Row object at " in  str(name):
                name = name.__getitem__(0)
            name=str(name)
            name=name.strip('(,)')
            tables.append(name)
        for t in tables:
            if tables.index(t) < int(len(tables) - 1):
                table.append(t)
            else:
                continue
        for index, t in enumerate(table):
            table2.append(str(index + 1) + ") " + t)
        return table2
    def column_maker(self, x):
        self.c.row_factory = sqlite3.Row
        cursor = self.c.execute('select * from '+x)
        row = cursor.fetchone()
        names = row.keys()
    
        return names

    def print2(self, select, yy, zz):
        self.c.execute(select)
        rows=self.c.fetchall()
        for r in rows:
            if "*" in select:
                ht =[]
                for item in range(0, len(zz) - 1):
                        ht.append(str(r.__getitem__(item)))
                        
                print("|".join(ht))
            else:
                ct = 0
                ht = []
                for item in yy:
                    ht.append(str(r.__getitem__(ct)))
                    ct = ct + 1
                print("|".join(ht))
    def SELECT(self):
        
        print()
        print()
        print()
        self.operator = ["1) =", "2) >", "3) <", "4) >=", "5) <=", "6) BETWEEN"]
        self.yes_no = ["1) YES", "2) NO"]
        
        self.select_state = 'SELECT '
        
        print("Is this a join?")
        for thing in self.yes_no:
            print(thing)

        txtx = input()
        
        if txtx == "1":
            joins = ['1) LEFT', '2)INNER ']
            print('columns to join(choose 2, comma in between, no spaces)')
            tables = self.tables_create()
            for table in tables:
                print(table)
            x = input()
            x = x.split(',')
            txxt = []
            for item in x:
                txxt.append(self.choose_option(tables, item))
                
            for item in joins:
                print(item)

            xtxt = input()
            xtxt = self.choose_option(joins, xtxt)
            if xtxt == 'INNER' or xtxt == ' INNER':
                xtxt = ''
            
            print("Primary Key:")
            zztz = input()

            self.select_state = "SELECT * FROM " + txxt[0] + " " + xtxt + " JOIN " + txxt[1] + " using(" + zztz + ")"
            print(self.select_state)
            print()
            print()
            self.c.execute(self.select_state)
            rows=self.c.fetchall()
            for r in rows:
                r = list(r)
                h = []

                for thing in r:
                    h.append(str(thing))
                print("|".join(h))
        if txtx == '2':


            
            tables = self.tables_create()
            for table in tables:
                print(table)
            x = input()
            self.z = self.choose_option(tables, x)
            print()
            print()
            print()
            print()
            print('Columns to select: Mulitple Answers Allowed, 1 comma, no spaces')
            columns1 = []
            for column in self.column_maker(str(self.z)):
                print(str(self.column_maker(str(self.z)).index(column) + 1) + ") " + str(column))
                columns1.append(str(self.column_maker(str(self.z)).index(column) + 1) + ") " + str(column))
                
            print(str(len(self.column_maker(str(self.z))) + 1) + ") *")
            columns1.append(str(len(self.column_maker(str(self.z))) + 1) + ") *")
            
            y = input()
            self.yy = y.split(",")
            columns2 = []
            for item in self.yy:
               columns2.append(str(self.choose_option(columns1, item)) + ", ")
            for column in columns2:
                if str(column) == str(columns2[len(columns2) - 1]):
                    self.select_state = self.select_state + str(column.strip(", "))
                else:
                    self.select_state = self.select_state + str(column)
            self.select_state = self.select_state + " FROM " + str(self.z.strip("''"))
            print()
            print()
            print()
            print()
            print("Do you want a where condition?")
            for thing in self.yes_no:
                print(thing)
            ztt = input()
            if ztt =="1":
                self.select_state = self.select_state + " WHERE "
                print(self.select_state)
                print()
                print()
                print()
                print()
                print('Columns in Where condition: Mulitple Answers Allowed, 1 comma, no spaces')
                columns1 = []
                for column in self.column_maker(str(self.z)):
                    print(str(self.column_maker(str(self.z)).index(column) + 1) + ") " + str(column))
                    columns1.append(str(self.column_maker(str(self.z)).index(column) + 1) + ") " + str(column))
                    
                print(str(len(self.column_maker(str(self.z))) + 1) + ") *")
                columns1.append(str(len(self.column_maker(str(self.z))) + 1) + ") *")
                
                ltt = input()

                ltt = ltt.split(",")
                columns3 = []
                columns4 = []
                for item in ltt:
                   columns3.append(str(self.choose_option(columns1, item)))

                for item in columns3:
                    columns4.append(str(columns3.index(item) + 1) + ") " + str(item))
                print()
                print()
                print()
                print()
                for column in columns4:
                    self.select_state = self.select_state + str(column[3:]) 
                    print("Is this a not condition?")
                    for item in self.yes_no:
                        print(item)
                    aaa = input()
                    if aaa == "1":
                        self.select_state = self.select_state + " NOT"
                    print()
                    print()
                    print("Which Operator:")
                    for operators in self.operator:
                        print(operators)
                    ttt = input()
                    for operators in self.operator:
                        if str(ttt) in operators:
                             self.select_state = self.select_state + operators.strip(ttt + ") ")
                    print()
                    print()
                    value = input("Value of your where condition:")
                    self.select_state = self.select_state + "\"" + value + "\""
                    
                    if len(columns4) >= 2:
                        if columns4.index(column) + 1 < len(columns4):
                            print()
                            print()
                            opt = ["1) AND", "2) OR"]
                            
                            print("Which Operator between your conditions?")
                            for opts in opt:
                                print(opts)
                            i = input()
                            if i == "1":
                                self.select_state = self.select_state + " AND "
                            elif i == "2":
                                self.select_state += " OR "
                            print()
                            print()
            print()
            print()
            print()
            print()
            print("Do you want an ORDER BY?")
            print("1) YES")
            print("2) NO")
            llt = input()
            print()
            print()
            
            if llt == "1":
                print("Which Column?")
                columns1 = []
                for column in self.column_maker(str(self.z)):
                    print(str(self.column_maker(str(self.z)).index(column) + 1) + ") " + str(column))
                    columns1.append(str(self.column_maker(str(self.z)).index(column) + 1) + ") " + str(column))
                    
                print(str(len(self.column_maker(str(self.z))) + 1) + ") *")
                columns1.append(str(len(self.column_maker(str(self.z))) + 1) + ") *")
                zzt = input()
                oot = self.choose_option(columns1, zzt)
                self.select_state += " ORDER BY " + str(oot)
            print()
            print()
            print(self.select_state)
            print()
            print()
            self.print2(self.select_state, self.yy, self.column_maker(str(self.z)) )
        
    def INSERT(self):
        self.yes_no = ["1) YES", "2) NO"]
        tables = self.tables_create()
        
        for table in tables:
            print(table)
        x = input()
        self.rts = self.choose_option(tables, x)
        
        print()
        print()
        print()
        print()
        values = []
        print("Values for all the columns:")
        for column in self.column_maker(str(self.rts)):
            print(str(self.column_maker(str(self.rts)).index(column) + 1) + ") " + str(column)  +  ":")
            values.append("\"" + input()  + "\"" )

        columns89 = self.column_maker(str(self.rts))
        tjt = ''
        for column in columns89:
            tjt = tjt + str(column)
            if columns89.index(column) < len(columns89) - 1:
                tjt = tjt + ","

        values2 = ''
        for column in values:
            values2 = values2 + str(column)
            if values.index(column) < len(values) - 1:
                values2 = values2 + ","
        self.insert_state = "INSERT INTO "  + str(self.rts) + " (" + tjt + ") VALUES (" + values2 + ")"
        self.c.execute(self.insert_state)
        print(self.insert_state)
        print('...execute...')
        #print(self.insert_state)
        self.conn.commit()
        print('...commit...')
        print()
        
    def print3(self):
        lrows=self.c.fetchall()
        for lr in lrows:
            ct = 0
            ht = []
            for item in values:
                ht.append(str(lr.__getitem__(ct)))
                ct = ct + 1
            print("|".join(ht))
    def UPDATE(self):
        self.operator = ["1) =", "2) >", "3) <", "4) >=", "5) <=", "6) BETWEEN"]
        self.yes_no = ["1) YES", "2) NO"]
        self.update_state = 'UPDATE '
        tables = self.tables_create()
        
        for table in tables:
            print(table)
        x = input()
        self.fff = self.choose_option(tables, x)
        
        print()
        print()
        print()
        print()
         
        self.update_state += str(self.fff) + ' SET '
        print()
        print()
        print()
        print()
        print('Columns in to set: Mulitple Answers Allowed, 1 comma, no spaces')
        columns1 = []
        for column in self.column_maker(str(self.fff)):
            print(str(self.column_maker(str(self.fff)).index(column) + 1) + ") " + str(column))
            columns1.append(str(self.column_maker(str(self.fff)).index(column) + 1) + ") " + str(column))
            
        print(str(len(self.column_maker(str(self.fff))) + 1) + ") *")
        columns1.append(str(len(self.column_maker(str(self.fff))) + 1) + ") *")
        
        ltt = input()

        ltt = ltt.split(",")
        columns3 = []
        columns4 = []
        valuesss = []
        print("Values:")
        for item in ltt:
            columns3.append(str(self.choose_option(columns1, item)))
        for item in columns3:
            print(str(item) + ":")
            ztz = input()
            valuesss.append(ztz)
            print()   
        for l in range(0, len(valuesss), 1):
            self.update_state += columns3[l-1] + " = \"" + valuesss[l-1] + "\""
        print(self.update_state)
                
            
        for item in columns3:
            columns4.append(str(columns3.index(item) + 1) + ") " + str(item))
        print()
        print()
        print()
        print()
        self.update_state += " WHERE "
        print('Columns in Where condition: Mulitple Answers Allowed, 1 comma, no spaces')
        columns1 = []
        for column in self.column_maker(str(self.fff)):
            print(str(self.column_maker(str(self.fff)).index(column) + 1) + ") " + str(column))
            columns1.append(str(self.column_maker(str(self.fff)).index(column) + 1) + ") " + str(column))
            
        print(str(len(self.column_maker(str(self.fff))) + 1) + ") *")
        columns1.append(str(len(self.column_maker(str(self.fff))) + 1) + ") *")
        
        ltt = input()

        ltt = ltt.split(",")
        columns3 = []
        columns4 = []
        for item in ltt:
           columns3.append(str(self.choose_option(columns1, item)))

        for item in columns3:
            columns4.append(str(columns3.index(item) + 1) + ") " + str(item))
        print()
        print()
        print()
        print()
        for column in columns4:
            self.update_state  = self.update_state + str(column[3:]) 
            print("Is this a not condition?")
            for item in self.yes_no:
                print(item)
            aaa = input()
            if aaa == "1":
                self.update_state  = self.update_state + " NOT"
            print()
            print()
            print("Which Operator:")
            for operators in self.operator:
                print(operators)
            ttt = input()
            for operators in self.operator:
                if str(ttt) in operators:
                     self.update_state  = self.update_state  + operators.strip(ttt + ") ")
            print()
            print()
            value = input("Value of your where condition:")
            self.update_state  = self.update_state  + "\"" + value + "\""
            
            if len(columns4) >= 2:
                if columns4.index(column) + 1 < len(columns4):
                    print()
                    print()
                    opt = ["1) AND", "2) OR"]
                    
                    print("Which Operator between your conditions?")
                    for opts in opt:
                        print(opts)
                    i = input()
                    if i == "1":
                        self.update_state  = self.update_state  + " AND "
                    elif i == "2":
                        self.update_state  += " OR "
                    print()
                    print()
        print(self.update_state)
        print()
        print()
        
        self.c.execute(self.update_state)
        self.conn.commit()
    def DELETE(self):
        self.operator = ["1) =", "2) >", "3) <", "4) >=", "5) <=", "6) BETWEEN"]
        self.yes_no = ["1) YES", "2) NO"]
        self.delete_state = 'DELETE FROM '
        tables = self.tables_create()
        
        for table in tables:
            print(table)
        x = input()
        self.ftf = self.choose_option(tables, x)
        self.delete_state += str(self.ftf)
        self.delete_state += " WHERE "
        print('Columns in Where condition: Mulitple Answers Allowed, 1 comma, no spaces')
        columns1 = []
        for column in self.column_maker(str(self.ftf)):
            print(str(self.column_maker(str(self.ftf)).index(column) + 1) + ") " + str(column))
            columns1.append(str(self.column_maker(str(self.ftf)).index(column) + 1) + ") " + str(column))
            
        print(str(len(self.column_maker(str(self.ftf))) + 1) + ") *")
        columns1.append(str(len(self.column_maker(str(self.ftf))) + 1) + ") *")
        
        ltt = input()

        ltt = ltt.split(",")
        columns3 = []
        columns4 = []
        for item in ltt:
           columns3.append(str(self.choose_option(columns1, item)))

        for item in columns3:
            columns4.append(str(columns3.index(item) + 1) + ") " + str(item))
        print()
        print()
        print()
        print()
        for column in columns4:
            self.delete_state +=  str(column[3:]) 
            print("Is this a not condition?")
            for item in self.yes_no:
                print(item)
            aaa = input()
            if aaa == "1":
                self.delete_state += " NOT"
            print()
            print()
            print("Which Operator:")
            for operators in self.operator:
                print(operators)
            ttt = input()
            for operators in self.operator:
                if str(ttt) in operators:
                     self.delete_state += operators.strip(ttt + ") ")
            print()
            print()
            value = input("Value of your where condition:")
            self.delete_state  += "\"" + value + "\""
            
            if len(columns4) >= 2:
                if columns4.index(column) + 1 < len(columns4):
                    print()
                    print()
                    opt = ["1) AND", "2) OR"]
                    
                    print("Which Operator between your conditions?")
                    for opts in opt:
                        print(opts)
                    i = input()
                    if i == "1":
                        self.delete_state  += " AND "
                    elif i == "2":
                        self.delete_state  += " OR "
                    print()
                    print()
        print(self.delete_state)
        print()
        print()
        self.c.execute(self.delete_state)
        self.conn.commit()


        
        print()
        print()
        print()
        print()  


    def call(self):
        while True:
            self.options = ["1) SELECT", "2) INSERT", "3) UPDATE", "4) DELETE"]
            print()
            print()
            for option in self.options:
                print(option)
            x = input()
            self.chosen = self.choose_option(self.options, x)

            if self.chosen == 'SELECT':
                self.SELECT()

            elif self.chosen == 'INSERT':
                self.INSERT()

            elif self.chosen == 'UPDATE':
                self.UPDATE()

            elif self.chosen == 'DELETE':
                self.DELETE()
    
            
d = database()
d.call()
d.c.close()

'''

'''
Sockets

1.	List out all socket terminologies.

2.	Give an example of a basic server template

3.	Give an example of a basic client template

4.	Give an example of a one-way socket communication

5.	Give an example of a turn-based socket communication

6.	Give an example of a two-way threaded communication
'''


'''
Server Template
'''
'''
import socket
host = ''
port = 123454
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(host, port))
'''

'''
Client Template
'''

'''
import socket
host = '192.168.1.73'
port = 123454
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
'''

'''
One way communication
'''
'''
#server
import socket
host = ''
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

backlog = 5
s.listen(backlog)
conn, addr = s.accept()
print('got connection from ', addr)
while True:
    name = input("send:")
    conn.send(name.encode())
s.close()
'''
'''
#client
import socket
host = '192.168.1.73'
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    data = s.recv(1024).decode()  
    print('Received from server', repr(data))
s.close()
'''

'''
Two way communication(in turns)
'''
'''
#server
import socket
host = ''
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

backlog = 5
s.listen(backlog)
conn, addr = s.accept()
print('got connection from ', addr)
while True:
    name = input("send:")
    conn.send(name.encode())
    print("waiting for response")
    data = conn.recv(1024).decode()  
    print('Received from client', repr(data))
s.close()
'''
'''
#client
while True:
    data = s.recv(1024).decode()  
    print('Received from server', repr(data))
    name = input("send:")
    s.send(name.encode())
    print("waiting for response")
'''
#server
##import socket
##import threading
##HOST = '0.0.0.0'
##PORT = 1234
##
##
##def start(s):
##    conn, addr = s.accept()
##    with conn:
##        print('Connected by', addr)
##    while True:
##        conn.sendall(input("server").encode())
##        data = conn.recv(1024).decode()
##        print("recieved from client: ", data)
##
##
##with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
##    s.bind((HOST, PORT))
##    s.listen(1)
##    threading.Thread(target=start, args=([s])).start()
##  

#client
##import socket
##import threading
##
##HOST = '192.168.1.114'
##PORT = 1234
##
##def start(s):
##    while True:
##        data = s.recv(1024).decode()  
##        print('Received from server', repr(data))
##        name = input("send:")
##        s.send(name.encode())
##
##       
##with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
##    s.connect((HOST, PORT))
##    s.sendall('Connection establish'.encode())
##    threading.Thread(target=start, args=([s])).start()
##
##
'''
Algorithms
'''
import time
import random
LIST_ONE = [random.randint(0,1000) for i in range(1000)]
'''
Linear Search
'''
l = [random.randint(0,1000) for i in range(10000)]
x = int(input("num: "))
def linearSearch(t, l):
    for num in l:
        if num == t:
            return True, l.index(num)
    return False, None

status, index = linearSearch(x, l)

if status == True:
    
    print("{} found at {}".format(x,index))
else:
    print(value, "not found")

'''
Bianary Search
'''
def binarySearch(listTwo,x, high, low):
    if high>=low:
        mid = (high + low)//2
        if listTwo[mid] == x:
            return mid
        elif listTwo[mid] > x:
            return binarySearch(listTwo, x, mid-1, low)
        elif listTwo[mid] < x:
            return binarySearch(listTwo, x, high, mid+1)
    else:
        return "List Nonexistent"

start = time.time()
print("num found at: " + str(binarySearch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18, 19], int(input('num')), 18, 0)))
end = time.time()
print("elapsed time: "+ str(end - start))
print()
print()

'''
Bubble Sort
'''
def bubbleSort(listThree):
    FLAG = 0
    while FLAG == 0:
        FLAG = 1
        check = listThree
        for i in range(len(listThree)-1):
            a = listThree[i]
            b = listThree[i+1]
            if a > b:
                FLAG = 0
                listThree[i], listThree[i+1] = listThree[i+1],listThree[i]
                
    return listThree

start = time.time()
print(bubbleSort(l))
end = time.time()
print("elapsed time: "+ str(end - start))
print()
print()

'''
Selection Sort
'''
def selectionSort(listFour):
    smallestNum = 0
    for i in range(len(listFour)):
        for x in range(i + 1, len(listFour)):
            if listFour[smallestNum] > listFour[x]:
                smallestNum = x

        listFour[i], listFour[smallestNum] = listFour[smallestNum], listFour[i]
    return listFour

start = time.time()
print(selectionSort(l))
end = time.time()
print("elapsed time: "+ str(end - start))
print()
print()

'''  
Insertion Sort
'''

def insertionSort(listFive):
    for i in range(1, len(listFive)):
        key = listFive[i]
        numLess = i-1
        while numLess >=0 and key < listFive[numLess]:
            listFive[numLess+1] = listFive[numLess]
            numLess -= 1
        listFive[numLess+1] = key
    return listFive



start = time.time()
print(insertionSort(l))
end = time.time()
print("elapsed time: "+ str(end - start))
print()
print()

    



