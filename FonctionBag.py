#coding:utf-8

import datetime


import MyClassForm
import TextPrint

# Function to Create ToDoList
def CreateToDoList():
    TextPrint.CreationListToDoList()
    toDoListObject = MyClassForm.ToDoList() # Create a new Object ToDoList from MyClassForm files
    toDoListObject.nameToDo = input("Enter a title for your task: ")
    toDoListObject.nameToDo = str(toDoListObject.nameToDo)
    toDoListObject.labelToDo = input("Enter a label for your task: ")
    toDoListObject.labelToDo = str(toDoListObject.labelToDo)
    toDoListObject.dateCreate = datetime.date.today()
    toDoListObject.dateRunList =  GetDateToDoList()
    TextPrint.AcceptSave()
    SaveToDoList(toDoListObject)

# Function to Save Any ToDoList
def SaveToDoList(toDoListObject):
    ToDoListSave = open("ToDoListData.txt", "a")
    DataListSave = str("\n{} ** {} ** {} ** {} ** {}".format(toDoListObject.idClass, toDoListObject.nameToDo, toDoListObject.labelToDo, toDoListObject.dateCreate, toDoListObject.dateRunList))
    try:
        ToDoListSave.write(DataListSave)
    except:
        print("****** Registration Fail...")
        
    ToDoListSave.close()

# Function to get Data of ToDoList Execute
def GetDateToDoList():
    errorDataDate = True
    dateVarNow = datetime.date.today()
    while errorDataDate:
        try:
            yearR = input("Entry Year : ")
            yearR = int(yearR)
            if len(str(yearR)) < 4 or yearR < dateVarNow.year:
                raise ValueError("Year is Incorrect...")
            month = input("Entry Month : ")
            month = int(month)
            if month < 1 or month > 12:
                raise ValueError("Month is Incorrect...")
            day = input("Entry Day : ")
            day = int(day)
            if day < 1 or day > 31:
                raise ValueError("Day is Incorrect...")
        except ValueError:
            print("Erreur : ")
        else:
            DateDayInput = str("{}-{}-{}".format(yearR, month, day))
            errorDataDate = False 
            return DateDayInput


# Function to print all List
def ReadToDoList():
    ToDoListSave = open("ToDoListData.txt", "r")
    Line = ToDoListSave.readlines()
    countLine = len(Line) - 1
    print("There are {} task(s) in your Database".format(countLine))
    if countLine == 0:
        print("There are no tasks available")
    else:
        for lineRead in Line:
            print(lineRead)

    ToDoListSave.close()

# Function to search one element to File ToDoList
def SearchToDoList(identify):
    ToDoListSave = open("ToDoListData.txt", "r")
    line = ToDoListSave.readlines()
    search = False
    for lineFor in line:
        for wordSearch in lineFor:
            if identify == wordSearch:
                try:
                    print(line)
                    search = True
                    break
                except:
                    print("Error while searching...")
        if search:
            break
    if search:
        print("Search perform successfullys...")
    else:
        print("No task with this clue has been found...")

# Function to Delete one element in File ToDoList
def DeleteTodoList(identify):
    ToDoListSave = open("ToDoListData.txt", "a")
    Line = ToDoListSave.readlines()
    deleteVar = False
    for lineRead in Line:
        if identify in lineRead:
            try:
                ToDoListSave.write("\r\n".join(Line))
                deleteVar = True
            except:
                print("Error during deletion...")
    if deleteVar:
        print("Deletion performed successfully...")
    else:
        print("No task with this clue has been found...")

# Function to update a selection Task
def UpdateToDOList(identifiant):
   ToDoListSave = open("toDoListData.txt", "a")
    LineR = ToDoListSave.readlines()
    findD = False
    for line in LineR:
        if identifiant in line:
            try:
                toDoListObject.nameToDo = input("Enter a title for your task: ")
                toDoListObject.nameToDo = str(toDoListObject.nameToDo)
                toDoListObject.labelToDo = input("Enter a label for your task: ")
                toDoListObject.labelToDo = str(toDoListObject.labelToDo)
                toDoListObject.dateCreate = datetime.date.today()
                toDoListObject.dateRunList =  GetDateToDoList()
                TextPrint.AcceptSave()
                SaveToDoList(toDoListObject)
                findD = True
            except:
                print("Error during modification...")
    if findD:
        print("Modification carried out successfully...")
    else:
        print("No stain with this index has been found...")