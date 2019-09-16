checklist = list()
# CREATE
def create(item):
    checklist.append(item)
    checklist[0]


# READ
def read(index):
    print(checklist[index])
    return checklist[index]


# UPDATE
def update(index, item):
    checklist[int(index)] = str(item)

# DESTROY
def destroy(index):
    checklist.pop(int(index))

# TO LIST EVERY ITEM IN THE LIST
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1
# TO MARK COMPLLETED WITH "√"
def mark_completed(index):
    checklist[(index)] = "{} {}".format("√", checklist[int(index)])


def select(function_code):
    # Create item
    if function_code.upper() == "C":
        input_item = user_input('\033[31m' +"Input item: ")
        create(input_item)
    # Delete item
    elif function_code.upper() == "D":
        item_index = user_input("Index number?: ")
        destroy(item_index)

     # Update item
    elif function_code.upper() == "U":
        item_index = user_input("Index number?: ")
        input_item = user_input("Input Item: ")
        update(item_index, input_item)

       # Mark as complete
    elif function_code.upper() == "M":
        item_index = user_input("Index number?: ")
        mark_completed(item_index)
    # Read item
    elif function_code.upper() == "R":
        item_index = int(user_input("Index Number?: "))
    # Remember that item_index must actually exist or our program will crash.
        read(int(item_index))
    # Print all items
    elif function_code.upper() == "P":
        list_all_items()
    # Stop the loop
    elif function_code.upper() == "Q":
         return False

    # Catch all
    else:
        print("\033[31m" +"Unknown Option")
    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

# TEST
# def test():
#     # First Test Code
#     create("purple sox")
#     create("red cloak")
#
#     print(read(0))
#     print(read(1))
#
#     update(0, "purple socks")
#     destroy(1)
#
#     print(read(0))
#     list_all_items()
#     # New Test Code 2
#     select("C")
#     list_all_items()
#     select("R")
#     list_all_items()
#
#     user_value = user_input("Please Enter a value:")
#     print(user_value)
#
# test()
running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list, U to update list item, D to delete list item, P to display list, and Q to quit: ")
    running = select(selection)
