import PySimpleGUI as sg
sg.theme("Darkteal1")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",

layout=[[sg.Text("SELAMAT DATANG DI KELAS",

font=("Arial",25))],
[sg.Text("NPM    :2210010245")], 
[sg.Text("NAMA   :MUHAMMAD RIFKI HATASA")],
[sg.Text("KELAS  :5O REGULER BANJARMASIN")],
[sg.Text("MATKUL :PEMROGRAMAN VISUAL 3")]],

size=(500,200),
font=("Times", 18))

window()
window.close()