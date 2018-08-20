lis=[]
lis=(lis.append(i) for i in range(1,1000))
print(lis)
import random
global c
print("Welcome to Tic Tac Toe!! Game")
k = 0
player1 =" "
player2 =" "
k = random.randint(0,40)
if k%2 == 0:
    player1 = "x"
    player2 = "o"
    print(" player 1 have to fill with x \n    \n  player 2 have to fill with o")
else:
        player1 = "o"
        player2 = "x"
        print("   player 1 have to fill with o \n    \n  player 2 have to fill with x")
l =[" "]*9
def displayboard(l):
    print(" %s | %s | %s " %(l[0],l[1],l[2]))
    print("------------")
    print(" %s | %s | %s " %(l[3],l[4],l[5]))
    print("------------")
    print(" %s | %s | %s " %(l[6],l[7],l[8]))
def status(l):

    if((l[0] == l[1] == l[2] == 'x') or (l[3] == l[4] == l[5] == 'x')or (l[6] == l[7] == l[8] == 'x')or(l[0] == l[3] == l[6] == 'x')or(l[1] == l[4] == l[7] == 'x')or(l[2] == l[5] == l[8] == 'x')):
        print("player x won the match")
        return 1
    elif((l[0] == l[4] == l[8] == 'x') or (l[2] == l[4] == l[6] == 'x')):
        print("player x won the match")
    if ((l[0] == l[1] == l[2] == 'o') or (l[3] == l[4] == l[5] == 'o') or (l[6] == l[7] == l[8] == 'o') or (l[0] == l[3] == l[6] == 'o') or (l[1] == l[4] == l[7] == 'o') or (l[2] == l[5] == l[8] == 'o')):
        print("player o won the match")
        return 1
    elif ((l[0] == l[4] == l[8] == 'o') or (l[2] == l[4] == l[6] == 'o')):
        print("player o won the match")
        return 1
displayboard(l)
c = k
while c <= k+9:
    if c % 2 == 0:
        print(k)
        print(player1 + " player turn ")
        while True:
            p = int(input("enter at which position you want to fill"))
            if l[p-1] != ' ':
               print("error space is already taken ")
            else:
                l[p - 1] = player1
                displayboard(l)
                c = c + 1
                break
    else:

        print(player2 + " player turn")
        while True:
            p = int(input("enter at which position you want to fill"))
            if l[p - 1] != ' ':
                print("error space is already taken ")
            else:
                l[p - 1] = player2
                displayboard(l)
                c = c + 1
                break
    r=status(l)
    if r==1:
        break


