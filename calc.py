from tokenize import Number
import os
import PySimpleGUI as sg
import average_deviation as deviation
import quartis as quart

#Global variable
numbers = []
amount = 0

#menu screem
def main_screen():
    sg.theme("Topanga")
    layout = [
        [sg.Text("Calculadora")],
        [sg.Text("Escolha qual operação deseja fazer:")],
        [sg.Checkbox("Devio medio", key = "IN")],
        [sg.Checkbox("Quartis", key = "IN2")],
        [sg.Button("Iniciar Operação")]
    ]
    return sg.Window('Calculadora SW', layout = layout, finalize = True)

#building the operation screen and insert number screem
def operation_screen():
    sg.theme("Topanga")
    layout = [
        [sg.Text("Desvio Médio")],
        [sg.Text("Digite os números:"), sg.Input(key = "number", size = (10,1))],
        [sg.Button("Adicionar número")],
        [sg.Output(size = (100,30), key = '___output___')],
        [sg.Button("Resetar"),sg.Button("Calcular")]
    ]
    return sg.Window('Operação', layout = layout, finalize = True)

def quartis_screen():
    sg.theme("Topanga")
    layout = [
        [sg.Text("Quartis")],
        [sg.Text("Digite os números:"), sg.Input(key = "numberq", size = (10,1))],
        [sg.Button("Adicionar número")],
        [sg.Output(size = (60,20), key = '___output___')],
        [sg.Button("Resetar"),sg.Button("Calcular")]
    ]
    return sg.Window('Quartis', layout = layout, finalize = True)

#fuction to insert number in the array
def insert_number(num):
    global amount
    amount = amount + 1
    numbers.append(num)

def reset():
    global amount
    numbers.clear()
    amount = 0

#inicialing the windows
windowsOne, windowsTwo, windowsThree = main_screen(), None, None


while(True):

    windows, event, values = sg.read_all_windows()

    #when the window is closed
    if windows == windowsOne and event == sg.WIN_CLOSED:
        break

    if windows == windowsTwo and event == sg.WIN_CLOSED:
        break

    if windows == windowsThree and event == sg.WIN_CLOSED:
        break

    #trade the windows
    if windows == windowsOne and event == 'Iniciar Operação':      
        if values ["IN"] == True:
            windowsTwo = operation_screen()
            windowsOne.hide()
        elif values ["IN2"] == True:
            windowsThree = quartis_screen()
            windowsOne.hide()
        
    #adding number in the array "numbers" as soon as there is a click on the "Adicionar número" button
    if windows == windowsTwo and event == 'Adicionar número':
        num = values['number'] # receive the value
        num = float(num)
        insert_number(num) #fuction to insert number in the array

    #calculating the average deviation
    if windows == windowsTwo and event == 'Calcular':
        deviation.operation_deviation(numbers, amount)

    #adding number in the array "numbers" as soon as there is a click on the "Adicionar número" button
    if windows == windowsThree and event == 'Adicionar número':
        num1 = values['numberq'] # receive the value
        num1 = float(num1)
        insert_number(num1) #fuction to insert number in the array
    
    #calculating the quartis
    if windows == windowsThree and event == 'Calcular':
        quart.operation_quartis(numbers)
    
    if windows == windowsThree and event == 'Resetar':
        quart.reset()
        windowsThree.FindElement('___output___').Update('')
        reset()
        
    if windows == windowsTwo and event == 'Resetar':
        deviation.reset()
        windowsTwo.FindElement('___output___').Update('')
        reset()
