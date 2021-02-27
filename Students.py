#####################################
from sqlite3.dbapi2 import Cursor
from time import sleep
import sqlite3 as sql
import os
#####################################
def clean():
    os.system("cls")
#####################################
def dbconnect():
    global db, sqlcursor                                                                       #db = database
    db = sql.connect("Students.sqlite")
    sqlcursor = db.cursor()
def dbselectall():
    global students_list        # students_list is list of the Students
    
    sqlcursor.execute("""SELECT * FROM students""")
    
    students_list = []
    
    students_sql=sqlcursor.execute("""SELECT * FROM students""")  
    
    for data in students_sql:
        students_list.append(data)
def dbclose():
    db.commit()
    db.close()
#####################################
def addStudent():
    global number
    
    clean()
    dbconnect()
    
    registeration = []
    number = input("Student Number: ")
    
    numCheck()                          #if there is student with same number gives notification
    
    name = input("Name: ")
    surname = input("Surname: ")
    student_class = input("Class: ")
    amount_Lesson = int(input("Amount of Lessons: "))
    price = int(input("Price per Lesson: "))
    total = int(input("Total income: "))
    
    registeration = [(number,name,surname,student_class,amount_Lesson,price,total)]
    
    for data in registeration:
        sqlcursor.execute("""INSERT INTO students VALUES (?,?,?,?,?,?,?)""",data)
    
    dbclose()
def addMoney():
    dbconnect()
    
    student = chooseStudent()
    
    clean()
    
    amount = int(input(f"\n{student[1]} öğrencisine eklemek istediğiniz miktar: "))
    oldTotal = student[6]
    newTotal = oldTotal+amount
    
    print(f"""
    Old Total={oldTotal}
    New Total={newTotal}""")
    
    sqlcursor.execute("""UPDATE students SET Total=? WHERE Number=?""",(newTotal,student[0]))
    
    dbclose()
def chooseStudent():
    global number
    
    clean()
    dbconnect()
    dbselectall()
    
    for data in students_list:
        print(f"{data[0]}-){data[1]}")
    
    number = input("\nType student number: ")
    sqlcursor.execute("""SELECT * FROM students WHERE Number=?""",(number,))
    person = sqlcursor.fetchone()
    
    return person
def chooseAction():
    global number
    
    clean()
    dbconnect()
    
    print("""
    1-)Change Number
    2-)Change Name
    3-)Change Surname
    4-)Change Class
    5-)Change Amount of Lessons
    6-)Change Price per Lesson
    7-)Change Total
    """)
    
    choose = int(input("Type action number: "))
    
    if choose == 1:
        clean()
        
        person = chooseStudent()
        number = input("\nType new number: ")
        
        numCheck()
        
        sqlcursor.execute(f"""UPDATE students SET Number=? WHERE Name=?""",(number,person[1]))
    if choose == 2:
        clean()
        
        person = chooseStudent()
        newValue = input("\nType new name: ")
        
        sqlcursor.execute("""UPDATE students SET Name=? WHERE Name=?""",(newValue,person[1]))
    if choose == 3:
        clean()
        
        person = chooseStudent()
        newValue = input("\nType new surname: ")
        
        sqlcursor.execute("""UPDATE students SET Surname=? WHERE Name=?""",(newValue,person[1]))
    if choose == 4:
        clean()
        
        person = chooseStudent()
        newValue = input("\nType new class: ")
        
        sqlcursor.execute("""UPDATE students SET Class=? WHERE Name=?""",(newValue,person[1]))
    if choose == 5:
        clean()
        
        person = chooseStudent()
        newValue = int(input("\nType new amount of lessons: "))
        
        sqlcursor.execute("""UPDATE students SET AmountOfLessons=? WHERE Name=?""",(newValue,person[1]))
    if choose == 6:
        clean()
        
        person = chooseStudent()
        newValue = int(input("\nType new price per lesson: "))
        
        sqlcursor.execute("""UPDATE students SET PricePerLesson=? WHERE Name=?""",(newValue,person[1]))
    if choose == 7:
        clean()
        
        person = chooseStudent()
        newValue = int(input("\nType new total: "))
        
        sqlcursor.execute("""UPDATE students SET Total=? WHERE Name=?""",(newValue,person[1]))
    dbclose()
def numCheck():
    dbconnect()
    dbselectall()
    
    for data in students_list:
        if number == str(data[0]):
            print("\nBu öğrenci numbersı kullanılmaktadır.")
            input("\nAna menüye dönmek için enter tuşuna basınız.")
            main()
            break
def informations():
    clean()
    dbconnect()
    
    students_list = []
    overall_Total = 0
    students_sql = sqlcursor.execute("""SELECT * FROM students""")
    for data in students_sql:
        students_list.append(data)
    
    for data in students_list:
        print(f"\nNumber: {data[0]} | Name: {data[1]} | Surname: {data[2]} | Class: {data[3]} | Amount of lessons: {data[4]} | Price per Lesson: {data[5]} |Total: {data[6]}")
        overall_Total+=int(data[6])
    print(f"\nOverall Total: {overall_Total}")
    dbclose()
def main():
    clean()
    menuPrint()
    
    choose = int(input("Type action number: "))
    if choose == 1:
        addMoney()
        input("Press Enter for return to the menu.")
        main()
    if choose == 2:
        addStudent()
        input("\n\nPress Enter for return to the menu.")
        main()
    if choose == 3:
        informations()
        input("\n\nPress Enter for return to the menu.")
        main()
    if choose == 4:
        chooseAction()
        input("\n\nPress Enter for return to the menu.")
        main()
    if choose == 5:
        quit()    
#####################################                
def menuPrint():
    print("""
 Welcome to the Student Database. Please choose action.    

 1-)Add Money
 2-)Add Student
 3-)Student Informations
 4-)Information Updates
 5-)Quit

    """) 
#####################################
main()
    
    