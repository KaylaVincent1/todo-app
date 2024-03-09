import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter the to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])  # key to identify each value
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 10))  # has to pass widget types ie label,window, etc. Each list represents a row
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"  # gets the value of the key="todo"
            todos.append(new_todo.title())
            functions.write_todos(todos)
            window['todos'].update(values=todos) # when an item is added update the window in real time

        case "Edit":
            todo_to_edit = values['todos'][0]  # write 0 to only get the action not the []s or ''s
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo.title()
            functions.write_todos(todos)
            window['todos'].update(values=todos) # when an item is added update the window in real time

        case "Complete":
            todo_to_complete = values['todo'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todo_to_complete)
            window['todo'].update(values='')

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
