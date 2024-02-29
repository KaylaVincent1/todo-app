import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")  # first git comment
print("it is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]  # slicing method reads 4 points forward
        # todo = input("Enter a todo: ") + "\n"
        # file = open("todos.txt", 'r')
        # todos = file.readlines() simplified below

        todos = functions.get_todos()

        todos.append(todo.title() + "\n")
        # means write_todos(filepath = "todos.txt", todos_arg = todos)
        # default write_todos(todos, "todos.txt") is not necessary cause filepath="todos.txt" is default argument.
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            # overwrite the item value
            item = item.strip('\n')
            # print(index, '-', item)
            row = f"{index + 1}.{item}"  # fstring syntax - f"{}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo.title() + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print(f"The Todo {todo_to_remove} was removed from the list.")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye!")
