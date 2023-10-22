import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input = sg.InputText(tooltip="Enter a todo", key="todo")
add = sg.Button("Add")

window = sg.Window("Todo List", layout=[[label],[input, add], []], font=("Times New Roman", 15))
while True:
    event, value = window.read()
    if event == "Add":
        todos = functions.get_todos()
        todos.append(value["todo"] + "\n")
        functions.write_todos(todos)
    if event == sg.WINDOW_CLOSED:
        break

window.close()
