"""print('hi please choose the options!!!!')

print("1. Add task")
print('2.remove task')
print('3.view task')

tasks = []

option =int(input('enter Your option :'))

if option==1:
    task = input('enter your task :')
    tasks.append(task)
    print('task added')
elif option==2:
    print('select the task to remove!!')
    print(tasks)
    option = int(input('select the task :'))
    tasks.pop(option-1)
elif option==3:
    for i in tasks:
        print(i)
else:
    print('invalid option')
    """
my_list = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(my_list, start=10):
    print(index,":", fruit)

print("________________________________------------------_________________----------------------")
print('Hi! Please choose an option:')
print('1. Add task')
print('2. Remove task')
print('3. View tasks')

tasks = []  # This list will store the tasks

while True:
    option = int(input('Enter your option: '))

    if option == 1:
        task = input('Enter your task: ')
        tasks.append(task)
        print('Task added!')
        
    elif option == 2:
        if len(tasks) == 0:
            print('No tasks to remove.')
        else:
            print('Select the task to remove:')
            for index, task in enumerate(tasks, start=1):
                print(f'{index}. {task}')
            task_index = int(input('Enter task number: '))
            if 1 <= task_index <= len(tasks):
                removed_task = tasks.pop(task_index - 1)
                print(f'Removed task: {removed_task}')
            else:
                print('Invalid task number.')
        
    elif option == 3:
        if len(tasks) == 0:
            print('No tasks.')
        else:
            print('Tasks:')
            for index, task in enumerate(tasks, start=1):
                print(f'{index}. {task}')
        
    else:
        print('Invalid option. Please choose again.')

    continue_or_not = input('Do you want to continue (yes/no)? ').lower()
    if continue_or_not != 'yes':
        break

print('Task manager closed.')

