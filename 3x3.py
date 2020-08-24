#lets try 3x3 first

board = [[" "]*3 for i in range(3)]

def display():
    for i in range(3):
        for j in range(3):
            print("| "+board[i][j]+" |",end=" ")
        print()
        print("-----------------")

def insert(position,sign,box):
    if(position<=0 or position>9):
        print("Invalid Position Try between 1 to 9")
        return False
    row=0
    if(position<=3):
        row = 0
    elif(position>=4 and position<=6):
        row=1
    else:
        row = 2
    col = (position%3)-1
    if(box[row][col]==" "):
        box[row][col] = sign
        return True
    else:
        print("Position already filled")
        return False
    

def check(board):
    if(board[0][0] == board[0][1] == board[0][2] !=" "):
        return board[0][0]
    elif(board[1][0] == board[1][1]== board[1][2] !=" "):
        return board[1][0]
    elif(board[2][0] == board[2][1]== board[2][2]!=" "):
        return board[2][0]
    elif(board[0][0] == board[1][0]== board[2][0]!=" "):
        return board[0][0]
    elif(board[0][1] == board[1][1]== board[2][1] !=" "):
        return board[0][1]
    elif(board[0][2] == board[1][2]== board[2][2]!=" "):
        return board[1][2]
    elif(board[0][0] == board[1][1]== board[2][2] !=" "):
        return board[0][0]
    elif(board[0][2] == board[1][1]== board[2][0] !=" "):
        return board[0][2]
    else:
        return False



player1 = input('Player1 choose x or o ').upper()

player2=''

if(player1=='X'):
    player2='O'
else:
    player2='X'

display()

count=0

while(True):
    if(count%2==0):
        pos = int(input('Player 1 enter the position'))
        result = insert(pos,player1,board)
        if(result):
            count+=1
            display()
    else:
        pos = int(input('Player 2 enter the position'))
        result = insert(pos,player2,board)
        if(result):
            count+=1
            display()
    if(count==9):
        ans = check(board)
        if(not ans):
            print("Match Draw")
            print()
            display()
            break
    elif(count>=5):
        ans = check(board)
        if(not ans):
            continue
        elif(ans=='O'):
            display()
            print()
            if(player1=='O'):
                print('Player1 Wins')
                break
            else:
                print('Player2 Wins')
                break
        else:
            print()
            display()
            print()
            if(player1=='X'):
                print('Player1 Wins')
                break
            else:
                print('Player2 Wins')
                break
            
        
        


    
    
    
    
