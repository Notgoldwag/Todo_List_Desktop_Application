def get_todos():
    """ This is a doc string """
    with open("todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="files/todos.txt"):
    with open("todos.txt", "w") as file_local2:
        file_local2.writelines(todos_arg)


if __name__ == "__main__":
    print("you are currently running this file directly")
else:
    #print("THis file is being imported")
    pass