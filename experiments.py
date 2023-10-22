import PySimpleGUI as sg

feet = sg.Text("Enter feet:")
feet_input = sg.Input()

inches = sg.Text("Enter inches: ")
inches_input = sg.Input()

convert = sg.Button("Convert")
window = sg.Window("Height converter", [[feet, feet_input],[inches,inches_input],[convert]])
window.read()
window.close()