import PySimpleGUI as sg
susunan=[[sg.VPush()],
         [sg.Text("UNISKA MAB", font=("helvetica", 24))],
         [sg.Text("BANJARMASIN", font=("courier", 28))],
         [sg.VPush()]]

window = sg.Window(title="Elemen Text", layout=susunan, element_justification="center", size=(430,200))

window.read()
window.close()