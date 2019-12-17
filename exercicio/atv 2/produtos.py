from model.produtos_classe import ProdutosClasse

lista = [
    ['frutas', 'verduras', 'legumes', 'preço'],
    ['mamão', 'abacaxi', 'laranja', 'uva', 'pera', 'maçã', 'vergamota'],
    ['alface crespa', 'alface lisa', 'rúcula',
        'almeirão', 'repolho', 'salsinha', 'couve'],
    ['feijão', 'ervinha', 'lentilha', 'vagem',
        'feijão branco', 'grão de bico', 'soja'],
    [[10.00, 2.56, 5.25, 9.5, 10.05, 15, 5.75], [2.99, 2.95, 3.5, 3.25, 5.89, 2.9, 2.5],
     [9.0, 5.0, 7.5, 1.75, 10.9, 5.99, 3.55]
     ]
]

mercado = ProdutosClasse()

for f in range(len(lista[1])):
    mercado.set_frutas(lista[1][f])
    # print(mercado.frutas)


for v in range(len(lista[2])):
    mercado.set_verduras(lista[2][v])
    # print(mercado.verduras)

for l in range(len(lista[3])):
    mercado.set_legumes(lista[3][l])
    # print(mercado.legumes)




# print(lista[4][1])

# print(lista[4][2])
