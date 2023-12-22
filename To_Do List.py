import datetime
import os
global Daly_Task,current_data
Daly_Task=[] 
current_data=datetime.datetime.now()
def Add_Task():
    tasks_date=current_data.time()
    while True: 
        try:
           Tasks=input('Enter Task :- ')
           Daly_Task.append(Tasks)
           print('---Task Added--- ')  
           user_ask=input('you want to add mose Tasks -Y|N- ') 
           if user_ask=='n':break
        except ValueError:
            print('plese enter a valid input')             
def Remove_Task():
    if len(Daly_Task)==0:
        print('No task is Avalable!')
    else:
        print('current task')
        for i ,task in enumerate(Daly_Task):
            print(f'{i+1})-- {task}')
        try :
            index=int(input('enter the number of the a task you want to dalete:-'))-1
            if 0 <= index < len(Daly_Task):
                delete=Daly_Task.pop(index)
                print(f'-- ||{delete}|| -->  has been delete ')
            else:
                print('invalid number')
        except ValueError:
            print('invalid input')  
def Display_Task():
    Show_Date() 
    if  len(Daly_Task)==0:
        print('No task is Avalable!')
    else:
        for i ,task in enumerate(Daly_Task):
            print('-------------------------')
            print(f'{i+1}) -- {task}')
def Display():
    try:
        with open("TO_Do_App.txt","r") as file:
            tasks_data=file.readlines()
            if not tasks_data:
                print('Your To-Do-list is Empty')
            else:
                print('--To-Do-List--')
                for i ,tasks_data in enumerate(tasks_data,start=1):
                    print(f'{i})--{tasks_data.strip()}')
    except FileNotFoundError:
        print(f' file not found ,your To-Do-list is empyty')
def Save_Tasks():
        for i ,task in enumerate(Daly_Task):  save=f'{i+1}) -- {task}'
        with open("TO_Do_App.txt","a") as file: file.write(save+'\n') 
        print('Saved...')
def Show_Date():
    print(f'-- Date = {current_time.day}||{current_time.month}|{current_time.year} --')      
def Delete_all():
    with open("TO_Do_App.txt","w") as file: 
        pass
    print('...Removed....')
while True:
    current_time=datetime.datetime.now()
    print(f'{Show_Date()}')   
    print('----------| To Do List |----------')
    print('1| Add Tasks')
    print('2| Remove Tasks')
    print('3| View Tasks') 
    print('4| Display Tasks')
    print('5| Save')
    print('6| Delete')
    print('7| Quit')
    print('---------------------------------')
    try:
        UserInput=input('Enter your Option :- ')
        if UserInput=='1':
            Add_Task()
        elif UserInput=='2':
            Remove_Task()
        elif UserInput=='3':
            Display_Task()
        elif UserInput=='4':
            Display()
        elif UserInput=='5':
            Save_Tasks()
        elif UserInput=='6':
            Delete_all()
        elif UserInput=='7':
            print('thanks ')
            break
        else:
            print(' Invalide UserInput')
    except FileNotFoundError:
        print(f'Enter a Number Only..')