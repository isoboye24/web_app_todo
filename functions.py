FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_list:
        todos_list = file_list.readlines()
    return todos_list


def write_todos(todos_arg, filepath_arg=FILEPATH):
    with open(filepath_arg, "w") as file_local:
        file_local.writelines(todos_arg)


# this line can only be executed when this current file is run - this is a way of protecting this line to run when this
# file is called in another file.
if __name__ == "__main__":
    print("hello")