import PySimpleGUI as sg

select = sg.Text("Choose files to compress")
input1 = sg.InputText(tooltip="Choose files")
button1 = sg.FilesBrowse("Choose")

location = sg.Text("Choose destination")
input2 = sg.InputText(tooltip="Choose location")
button2 = sg.FolderBrowse("Choose")

compressButton = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[[select,input1,button1],[location,input2,button2],[compressButton]])
window.read()
window.close()