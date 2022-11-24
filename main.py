import PySimpleGUI as sg

class App:
    def __init__(self):

        theme = sg.theme('Black')

        layout = [

        [sg.Text('Nome:', size=(15,0)), sg.Input(size=(25,0), key='nome')],
        
        [sg.Text('Sobrenome:', size=(15,0)), sg.Input(size=(25,0), key='sobrenome')],

        [sg.Text('Turma:', size=(15,0)), sg.Input(size=(25,0), key='turma')],
        
        [sg.Text('Data:', size=(15,0)), sg.Input(size=(25,0), key='data')],
        
        [sg.Text('Hora:', size=(15,0)), sg.Input(size=(25,0), key='hora')],
        
        [sg.Button('Confirmar')],

        [sg.Text('', size=(0,1), key='output')]

        ]

        self.window = sg.Window('Cadastro', layout)
    
    def inicio(self):
        while True:
            event, values = self.window.read()

            self.nome = values['nome']
            self.sobrenome = values['sobrenome']
            self.turma = values['turma']
            self.data = values['data']
            self.hora = values['hora']

            if event == sg.WINDOW_CLOSED:
                break
            
            if event == 'Confirmar':
                self.window['output'].update(value=f'{self.nome} {self.sobrenome} da turma {self.turma} foi cadastrado!')


app1 = App()
app1.inicio()