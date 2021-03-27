#coding:utf-8

import FonctionBag
import MyClassForm
import TextPrint

TextPrint.TextHomePage()

reponse = True
while reponse == True:
    print("Good evening what do you want to do ?")
    choose = input("1 --> Add a new task \t 2 --> Print all task \n3 --> Delete a Task \t 4 --> Update a Task \n*****Your choice : ")
    choose = int(choose)
    try:
        if (choose != 1) and (choose != 2) and (choose != 3) and (choose != 4):
            raise ValueError("incompatible choice...")
        if (choose == 1) or (choose == 2) or (choose == 3) or (choose == 4):
            if choose == 1:
                FonctionBag.CreateToDoList()
            elif choose == 2:
                FonctionBag.ReadToDoList()
            elif choose == 3:
                FonctionBag.ReadToDoList()
                a = input("Enter the number of the task to delete : ")
                a = str(a)
                FonctionBag.DeleteTodoList(a)
            else:
                FonctionBag.ReadToDoList()
                a = input("Enter the number of the task to modify : ")
                a = str(a)
                FonctionBag.UpdateToDOList(a)
    except ValueError:
        print("Error : ")