checklist = list()
# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    item = checklist[index]
    return item

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

# TO LIST EVERY ITEM IN THE LIST
def list_all_items():
    index = 0
    for list_item in checklist:
        # print(str(index) + list_item)
        print("{} {}".format(index, list_item))
        index += 1
#TO MARK COMPLLETED WITH "√"
def mark_completed(index):
    checklist[(index)] = "{} {}".format("√", checklist[(index)])

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")
# # TEST
# def test():
#     # Your testing code here
#     # ...
#     # Call your new function with the appropriate value
#     select("C")
#     # View the results
#     list_all_items()
#     # Call function with new value
#     select("R")
#     # View results
#     list_all_items()
#     # Continue until all code is run
# test()
