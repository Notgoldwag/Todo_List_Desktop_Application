import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input = sg.InputText(tooltip="Enter a todo")
add = sg.Button("Add")

window = sg.Window("Todo List", layout=[[label],[input, add], []])
window.read()
window.close()
