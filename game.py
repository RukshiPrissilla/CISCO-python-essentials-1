#cisco give it. i like to explore it & it helps me to understand how it works
from random import randrange

def display_board(board):
    print("+-------"*3,"+",sep="")
    for row in range(3):
        print("|      n"*3,"|",sep="")
        for col in range (3):
            print("|       " + str(board[row][col])+"" ,  end="")
        print("|")
        print("|       "*3,"|",sep="")
        print("+-------"*3,"+",sep="")

def enter_move(board):
    ok=False  #fake assumption - we need it to enter the loop
    while not ok:
        move=input("Enter your move: ")
        ok=len(move)==1 and move >="1" and move<="9" #is users input valid?
        if not ok:
            print("bad move!repeat ur input") 
            continue
        move=int(move) -1 # cell's number from 0 to 8
        row=move // 3 #cell's row
        col=move % 3 #cell's coloumn
        sign=board[row][col]  #check the selected square
        ok=sign not in ['0','x']
        if not ok:#its occupied - to the input again
            print("field already occupied-repeat ur input!")
            continue
        board[row][col]='0' #set '0' at the selected square

def make_list_of_free_fields(board):
    free=[]
    for row in range(3):#iterate through rows
        for col in range(3):#iterate through coloumns
            if board[row][col] not in ['0','x']:#is the cell free?
                free.append((row,col)) #yes it append new tuple to the list
    return free

def victory_for(board,sgn):
    if sgn=='x':#are we looking for 'x'?
        who='me' #yes it's computer's side
    elif sgn == '0':
        who='you' #yes-it's our side
    else:
        who=None #we should not fall here
    cross1=cross2=True #for diagonals
    for rc in range(3):
        if board[rc][0]==sgn and board[rc][1] == sgn and board [rc][2] == sgn:  #check row rc
            return who
        if board[0][rc]==sgn and board[1][rc]==sgn and board[2][rc]==sgn: #check coloumn rc
            return who
        if board[rc][rc] !=sgn: #check first diagonal
            cross1==False
        if board[2-rc][2-rc] != sgn: #check scond diagonal
            cross2==False
    if cross1 or cross2:
        return who
    return None

def draw_move(board):
    free=make_list_of_free_fields(board)  #make a list of free fields
    cnt=len(free)
    if cnt>0:
        this=randrange(cnt)
        row,col=free(this)
        board[row][col]="x"

board=[[3*j+i+1 for i in range(3)]for j in range(3)]
board[1][1]='x'  #set first 'x' in the middle
free=make_list_of_free_fields(board)
human_turn=True #which turn is it now?
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor=victory_for(board,'0')
    else:
        draw_move(board)
        victor=victory_for(board,'x')
    if victor != None:
        break
    human_turn=not human_turn
    free=make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
    print("you won!")
elif victor == 'me':
    print('i won!')
else:
    print('tie')





