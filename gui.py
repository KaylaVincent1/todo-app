import functions
import PySimpleGUI as sg

label = sg.Text("Enter a to-do")
input_box = sg.InputText(tooltip="Enter the to-do")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()
