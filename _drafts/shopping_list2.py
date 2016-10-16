# have a HELP command
# have a SHOW command
# clean code up in general

# make a list to hold onto our items
shopping_list = []

def show_help():
    # print out instructions on how to use the app
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")

def show_list():
    # 6 print out the list
    print("Here's your list:")

    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    # 4 add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

show_help()

# create infinite asking list
while True:
    # 3 ask for new items
    new_item = input("> ")

    # 5 be able to quit the app
    # NOTE: app is quit before assigning input to new_item list
    if new_item == 'DONE':
        break

    # have a HELP command
    elif new_item == 'HELP':
        show_help()
        continue

    elif new_item == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)


show_list()
