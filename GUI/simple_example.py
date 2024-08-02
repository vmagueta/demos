import PySimpleGUI as sg

sg.theme("Python")

def soma(x: int, y: int) -> int:
    return x + y

# Widgets
layout = [
    [sg.Text("Número x"), sg.In(key="x", enable_events=True, size=(5,1))],
    [sg.Text("Número y"), sg.In(key="y", enable_events=True, size=(5,1))],
    [sg.Text("", key="result")],
    [sg.Button("Calcula")],
    [],
    [sg.Button("Sair")]
]

window = sg.Window(title="Calculadora", layout=layout, margins=(100, 50))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Sair"):
        break
    if event == "Calcula":
        x = int(values["x"].strip())
        y = int(values["y"].strip())
        result = soma(x, y)
        window["result"].update(result)


window.close()
