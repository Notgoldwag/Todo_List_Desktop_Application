import functions
import time
import PySimpleGUI as sg
import os

if os.path.exists("todos.txt") == False:
    with open("todos.txt", "w"):
        pass

sg.theme("GreenMono")

clock = sg.Text('', key="time")
test = sg.Text('')
test = sg.Text('')
label = sg.Text("Type in a todo")
input = sg.InputText(tooltip="Enter a todo", key="todo")
add = sg.Button("Add", tooltip="Add a todo", key="Add")
exit = sg.Button("Exit")

todos = functions.get_todos()
for todo in todos:
    index = todos.index(todo)
    todos[index] = todo.strip("\n")


list_box = sg.Listbox(values=functions.get_todos(), key="show_todos", enable_events=True, size=[65,15])
edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete", tooltip="Complete a todo", key="Complete")

window = sg.Window("Todo List", layout=[[clock],[label, input, add],[list_box, edit_button], [complete_button,exit]],
                   font=("Times New Roman", 15))

edit = ""

while True:
    event, value = window.read(timeout=1000)
    now = time.strftime("%a, %b %d, %Y %H:%M:%S")
    window["time"].update(value=now)
    window["Add"].Widget.config(width=10, height = 1)
    window["Complete"].Widget.config(width=10, height=1)

    #the event takes either the label of the widget or the key of the widget
    if event == "Add":
        todos = functions.get_todos()
        todos.append(value["todo"] + "\n")
        functions.write_todos(todos)
        window["show_todos"].update(values=todos)

    elif event == sg.WINDOW_CLOSED:
        break
    elif event == "show_todos":
        item = value["show_todos"][0]
        window["todo"].update(value=item.strip("\n"))

    elif event == "Edit":
        try:
            todo_edit = value["show_todos"][0]
            new_todo = value["todo"] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_edit)
            todos[index] = new_todo

            functions.write_todos(todos)
            window["show_todos"].update(values=todos)
        except IndexError:
            sg.popup("Please choose an item first.", font=("Times New Roman", 15))
    elif event == "Complete":
        try:
            finish = value["show_todos"][0]
            todos = functions.get_todos()
            todos.remove(finish)

            functions.write_todos(todos)
            window["show_todos"].update(values=todos)
            window["todo"].update(value="")
        except IndexError:
            sg.popup("Please choose an item first.", font=("Times New Roman", 15))

    elif event == "Exit":
        break
window.close()
