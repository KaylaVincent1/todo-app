import functions
import PySimpleGUI as sg
import time

sg.theme("BlueMono")

clock = sg.Text("", key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter the to-do", key="todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])  # key to identify each value
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 10))  # has to pass widget types ie label,window, etc. Each list represents a row
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"  # gets the value of the key="todo"
            todos.append(new_todo.title())
            functions.write_todos(todos)
            window['todos'].update(values=todos)  # when an item is added update the window in real time

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]  # write 0 to only get the action not the []s or ''s
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo.title()
                functions.write_todos(todos)
                window['todos'].update(values=todos)  # when an item is added update the window in real time
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 10))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 10))
        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
