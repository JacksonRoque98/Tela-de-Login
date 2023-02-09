import PySimpleGUI as sg

#Criando Layout
layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')]
]

#Adicionando Layout em uma janela
window = sg.Window('Login', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        senha_correta = '123456'
        usuario_correto = 'Jackson Roque'
        usuario = values['usuario'].title()
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login feito com sucesso')
        else:
            window['mensagem'].update('senha ou usuario errado')
