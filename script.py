from heap import MaxHeap

project_lists = []

def program_start():
    print("Welcome ot the program tracker, what would you like to do?")
    
    while True:
        try:
            start = input("""
            'create': create a new project list
            'delete': delete list
            'select': select a list to view or edit
            'exit': exit program
            """)
            if start.lower() == 'create':
                create_list()
            elif start.lower() == 'delete':
                print("you chose delete")
                break
            elif start.lower() == 'select':
                print_projects()
                program_start()
                break
            elif start.lower() == 'exit':
                print("bye bye")
                return 
            else:
                print("I didn't recognize that, please try again.")
        except:
            continue

def create_list():
    print("You chose create a new list")
    name = input("What should the name of your new list be?\nTo go back to the main menu type 'back'\n")
    if name.lower() == 'back':
        program_start()
    else:
        confirm = input(f"You chose to name your list {name}, is that correct?(yes/no)")
        if confirm.lower() == 'yes':
            project_lists.append(MaxHeap(name.lower()))
            print(f"{name} created!")
            program_start()
        else:
            create_list()
        
def print_projects():
    lst = []
    for node in project_lists:
        lst.append(node.name)
    print(lst)

program_start()

