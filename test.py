
lista=[
    [0,1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

def buscarID(idno):
    for list in lista:
        for id in list:
            if id == idno:
                print(f'[{lista.index(list)}][{list.index(id)}]')

numeroEstudiante=int(input("Ingrese numero a buscar: "))
buscarID(numeroEstudiante)