import PySimpleGUI as sg
sg.theme("Darkteal1")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="latihan pertama",
                   layout=[[sg.Text("NPM    :2210010245")], 
                           [sg.Text("NAMA   :MUHAMMAD RIFKI HATASA")],
                           [sg.Text("KELAS  :5O REGULER BANJARMASIN")],
                           [sg.Text("MATKUL :PEMROGRAMAN VISUAL 3")]],
                   size=(400,200),
                    font=("Times", 18))
window()
window.close()