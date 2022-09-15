
import PySimpleGUI as sg
sg.theme('DarkAmber')

layout = [  [sg.Button('Відкрити')],
            [sg.Button('Перейменувати')],
            [sg.Button('Копіювати')],
            [sg.Button('Видалити')],
            [sg.Button('Створити'), 
            sg.Combo(['Папку', 'Файл'])]  ]

window = sg.Window('',layout)

window.read()

window.close()
