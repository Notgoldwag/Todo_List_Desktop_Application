import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input = sg.InputText(tooltip="Enter a todo", key="todo")
add = sg.Button("Add")

todos = functions.get_todos()
for todo in todos:
    index = todos.index(todo)
    todos[index] = todo.strip("\n")


list_box = sg.Listbox(values=todos, key="show_todos", enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window("Todo List", layout=[[label, input, add],[list_box, edit_button]], font=("Times New Roman", 15))

edit = ""

while True:
    event, value = window.read()
    print(1, event)
    print(2, value)
    print(3, value["show_todos"])
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(value["todo"] + "\n")
            functions.write_todos(todos)
            window["show_todos"].update(values=todos)

        case sg.WINDOW_CLOSED:
            break

        case "Edit":
            todo_edit = value["show_todos"][0]
            new_todo = value["todo"] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_edit)
            todos[index] = new_todo

            functions.write_todos(todos)
            window["show_todos"].update(values=todos)
window.close()
