import PySimpleGUI as sg
sg.theme("Darkteal1")
window = sg.Window(title="Latihan Kedua",
                   layout=[[sg.Text("NPM    :2210010245")], 
                           [sg.Text("NAMA   :MUHAMMAD RIFKI HATASA")],
                           [sg.Text("KELAS  :5O REGULER BANJARMASIN")],
                           [sg.Text("MATKUL :PEMROGRAMAN VISUAL 3")]],
                   size=(400,200))
window.read()
window.close()