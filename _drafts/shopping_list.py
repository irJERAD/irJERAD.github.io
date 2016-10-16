# 1 make a list to hold onto our items
# 2 print out instructions on how to use the app
# 3 ask for new items
# 4 add new items to our list
# 5 be able to quit the app
# 6 print out the list

# 1 make a list to hold onto our items
shopping_list = []

# 2 print out instructions on how to use the app
print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items.")

# create infinite asking list
while True:
    # 3 ask for new items
    new_item = input("> ")

    # 5 be able to quit the app
    # NOTE: app is quit before assigning input to new_item list
    if new_item == 'DONE':
        break

    # 4 add new items to our list
    shopping_list.append(new_item)

# 6 print out the list
print("Here's your list:")

for item in shopping_list:
    print(item)
