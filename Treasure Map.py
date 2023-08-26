row1=['⬜','⬜','⬜']
row2=['⬜','⬜','⬜']
row3=['⬜','⬜','⬜']
def printMap():
    print(row1)
    print(row2)
    print(row3)

flag=1
while flag==1:
    printMap()
    coordinates=input('Where you will hide the treasure: ')
    if len(coordinates)==2:
        flag=0
    else:
        print('Invalid coordenate, try again')

coordinate_x=int(coordinates[0])
coordinate_y=int(coordinates[1])

if coordinate_y ==1:
    row1[coordinate_x-1]='X'
elif coordinate_y==2:
    row2[coordinate_x - 1] = 'X'
elif coordinate_y==3:
    row3[coordinate_x - 1] = 'X'
else:
    print('Invalid coordinate')

printMap()