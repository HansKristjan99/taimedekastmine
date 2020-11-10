import PySimpleGUI as sg
sg.theme("Darkgreen1")
layout = [[sg.Text("Sisesta oma taime nimi ladina keeles:")],
[sg.Input(key = "-NIMI-")], [sg.Text("Our output will go here",size=(30,1),key= "-OUT-")] ,[sg.Button("Otsi")]]
window = sg.Window("Title", layout)
while True:
    event,values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    window["-OUT-"].update(values["-NIMI-"])
window.close()
