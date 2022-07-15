print("""
Hi, this is your to-do list app.
Keep the good work today!

Remember:
"Success isn't about being the best. 
It's about always getting better."
-Behance 99U
""")

to_do_list = []
user_input = 0

def show_menu():
    print("""
    MENU:
    1. Add an item to your to-do list.
    2. Mark an item as done. 
    3. View your to-do list.
    4. Exit
    """)

while user_input != 4:
    show_menu()
    user_input = input('Choose the menu: ')

    try:
        user_input = int(user_input)
    except:
        user_input = -1

    if user_input == 1:
        item = input('What are you gonna do today? ')
        to_do_list.append(item)
        print(f'[INFO] "{item}" is added to the list.')
    elif user_input == 2:
        item = input('what do you want to mark as done? ')
        if item in to_do_list:
            to_do_list.remove(item)
            print(f'[INFO] "{item}" is removed from the list.')
        else:
            print(f'There is no "{item}" in your list.')
    elif user_input == 3:
        print('TO-DO LIST:')
        if len(to_do_list) == 0:
            print('(empty)')
        else: 
            for item in to_do_list:
                print(f'- {item}')
    elif user_input == 4:
        print('Great job today!')
    else:
        print('Please enter only 1, 2, 3, or 4.')

# Created on 2022-07-15 by Sri Hartini.
# - inspired by a project done in: 
#   "Create Your First Python Program From UST" by Coursera,
# - modified by adding the try/except structure 
#   taught in "Scientific Computing with Python" at freeCodeCamp.