#coding:utf-8

import datetime

class ToDoList:
    id = 0
    def __init__(self):
        self.id += 1
        self.idClass = self.GeneratorPassWord(self.id)
        self.nameToDo = "List"
        self.labelToDo = "This a task"
        self.dateCreate = datetime.date.today()
        self.dateRunList = datetime.date.today()

    def GeneratorPassWord(self, ide): # Function allowing to generate an Identifier with 5 characters
        self.sizeVar = 5
        self.sizeId = int(len(str(ide)))
        self.addZero = self.sizeVar - self.sizeId
        self.zeroAdd =""
        for self.i in range(self.addZero):
            self.zeroAdd = self.zeroAdd + '0'
        self.zeroAdd += str(ide)
        return self.zeroAdd
