from heap import MaxHeap

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
                print("You chose create")
                break
            elif start.lower() == 'delete':
                print("you chose delete")
                break
            elif start.lower() == 'select':
                print("You chose select")
                break
            elif start.lower() == 'exit':
                print("bye bye")
                break
            else:
                print("I didn't recognize that, please try again.")
        except:
            continue

program_start()

