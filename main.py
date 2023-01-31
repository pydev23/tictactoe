import random
from sys import exit
global wincond
wincond = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
global S
S = ['-','-','-','-','-','-','-','-','-']
def playerinp():
    while True:
        a = (tuple(map(int, (input('Введите положение по осям х и у через пробел').split()))))
        x = a[0]
        y = a[1]
        if not S[y*3+x] == '-':
            print('Занято, выберите другую клетку')
            pass
        else:
            S[y*3+x] = 'x'
            break
def printout():
    print('  0 1 2')
    print('0', *S[:3])
    print('1', *S[3:6])
    print('2', *S[6:])

def pcmove():
    while True:
        i = random.randrange(9)
        if not S[i] == '-':
            pass
        else:
            S[i] = 'o'
            break

def wincheck():
    for c in wincond:
        if all((S[c[0]]=='x', S[c[1]]=='x', S[c[2]]=='x')):
            printout()
            exit('player wins')
        elif all((S[c[0]]=='o', S[c[1]]=='o', S[c[2]]=='o')):
            printout()
            exit('computer wins')
        else:
            pass
printout()
for i in range(9):
    print('ход игрока')
    playerinp()
    wincheck()
    printout()
    print('ход компьютера')
    pcmove()
    wincheck()
    printout()
