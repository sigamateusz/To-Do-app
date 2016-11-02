from ast import literal_eval
import os
os.system('clear')


def load_list():
    global todo_list
    f = open('task_list.txt', 'r')
    todo_list = [list(literal_eval(line)) for line in f]
    f.close()


def save_list():
    global todo_list
    f = open('task_list.txt', 'w+')
    for i in todo_list:
        f.write('{}\n'.format(i))
    f.close()


def show_list():
    """Show all task in list"""
    global todo_list
    for i in range(len(todo_list)):
        print("{}. {} {}".format(i+1,todo_list[i][0],todo_list[i][1]))
    print("")


def add_task():
    """Add a new task to the end of the list"""
    todo_list.append(['[ ]',input('Add an item: ')])
    save_list()
    print("")


def mark_task():
    """Marks made the task"""
    global todo_list
    print('You saved the following to-do items:')
    show_list()
    try:
        x = int(input("Which one you want to mark as comp\
leted (or type 'x' to quite): ")) - 1
        print("")
    except ValueError:
        main()
    if x < len(todo_list):
        todo_list[x][0]='[x]'
        save_list()
    else:
        #if number is o
        print('There is no such number')
        mark_task()


def archive_tasks():
    """Deletes tasks performed"""
    for i in range(len(todo_list)):
        if todo_list[i][0] == '[x]':
            todo_list.pop(i);
            archive_tasks()
            break


todo_list = []


def main():
    load_list()
    while True:
        choice = input('Please specify a command [list, add, mark, archive]: ')

        if choice == 'list':
            show_list()

        elif choice == 'add':
            add_task()

        elif choice == 'mark':
            mark_task()

        elif choice == 'archive':
            archive_tasks()
            print('All completed tasks got deleted.\n')
            save_list()
        else:
            print("I can't understand You\n")

if __name__ == '__main__':
    main()
