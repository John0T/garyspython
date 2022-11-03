# coc-pyright settings:
# type: ignore

import PySimpleGUI as sg
from datetime import date

# Theme
sg.theme('DarkAmber')

# Variable declaration
today = date.today().strftime("%m/%d/%y")

# Column definition
first_column = [[sg.Text('Date:', size=(21,1)), sg.Text(today)],
                [sg.Text('Beginning Cash on Hand:', size=(21, 1)), sg.Text("tmp")],
                [sg.Text('Sales:', size=(21, 1)), sg.Input(s=15)],
                [sg.Text('Layaways:', size=(21, 1)), sg.Input(s=15)],
                [sg.Text('Total Register Sales:', size=(21, 1)), sg.Text("tmp")],
                [sg.Text('Pawn Fees:', size=(21, 1)), sg.Input(s=15)],
                [sg.Text('Pawn Redeem:', size=(21, 1)), sg.Input(s=15)],
                [sg.Text('Wholesale/Giftcard:', size=(21, 1)), sg.Input(s=15)],
                [sg.Text('Register Tax:', size=(21, 1)), sg.Input(s=15)],
                [sg.Text('Layaway Tax:', size=(21, 1)), sg.Input(s=15)],
                [sg.Text('Total Tax Collected:', size=(21, 1)), sg.Input(s=15)],
                [sg.Text('Total:', size=(21, 1)), sg.Text("tmp")]]

second_column = [[sg.Text('Total Cash on Hand:', size=(21, 1)), sg.Input(s=15)],
                 [sg.Text('Purchase:', size=(21, 1)), sg.Input(s=15)],
                 [sg.Text('New Mdde. Purchase:', size=(21, 1)), sg.Input(s=15)],
                 [sg.Text('New Pawns:', size=(21, 1)), sg.Input(s=15)],
                 [sg.Text('Bank Deposits:', size=(21, 1)), sg.Input(s=15)],
                 [sg.Text('Cash PD Out Supplies:', size=(21, 1)), sg.Input(s=15)],
                 [sg.Text('Freight & Postage:', size=(21, 1)), sg.Input(s=15)],
                 [sg.Text('Gift Card Redeemed:', size=(21, 1)), sg.Input(s=15)],
                 [sg.Text('Miscellaneous Expense:', size=(21, 1)), sg.Input(s=15)],
                 [sg.Text('Yard & Pest Control: ', size=(21, 1)), sg.Input(s=15)]]

bottom_column = [[sg.Text('Layaways Including Tax:', size=(21, 1)), sg.Text("tmp")]]

###################
# Column | Column #
# --------------- #
#  Bottom Column  #
# --------------- #
#     Buttons     #
###################
# Layout
layout = [[sg.Column(first_column),
           sg.VerticalSeparator(),
           sg.Column(second_column)],
          [sg.HorizontalSeparator()],
          [sg.Column(bottom_column)],
          [sg.HorizontalSeparator()],
          [sg.Button('Calculate')]]

# Create the window
window = sg.Window('Garys Pawn - Daily Report', layout) 
#window = sg.Window('Garys Pawn - Daily Report', layout, element_justification='center', resizable=True)

# Event loop
while True:
    event, values = window.read()
    # On calculate, add required things
    if event == 'Calculate':
        break
    # End program is window closed
    if event == sg.WIN_CLOSED:
        break

# event, values= window.read()

# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()