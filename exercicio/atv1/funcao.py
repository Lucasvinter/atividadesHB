from pessoa_classe import Pessoa

def pessoas_dados():
    cab = ['nome', 'telefone', 'email', 'idade']

    pess = [
        ['Alex', 'Paulo', 'Pedro', 'Mateus', 'Carlos', 'João', 'Joaquim'],
        ['4799991', '4799992', '4799993', '4799994',
            '4799995', '4799996', '4799997'],
        ['a@a.com', 'b@b.com', 'c@c.com', 'd@d.com',
            'e@e.com', 'f@f.com', 'g@g.com'],
        ['18', '25', '40', '16', '15', '19', '17']
    ]

    for n in range(7):
        if int(pess[3][n]) >= 18:
            p = Pessoa(pess[0][n], pess[1][n], pess[2][n], pess[3][n])
            for i in range(4):
                print(f'{cab[0]} = {p.nome}')
                print(f'{cab[1]} = {p.telefone}')
                print(f'{cab[2]} = {p.email}')
                print(f'{cab[3]} = {p.idade}\n')
                print('-'*20)


pessoas_dados()
