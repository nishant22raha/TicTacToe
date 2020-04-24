from random import randint
def run():
    board=[]
    board.append(' ')
    def init(board):
        for i in range(1,10):
            board.append(' ')        
    def display(board):
        print('__________')
        print(board[1]+' | '+board[2]+' | '+board[3])
        print('__________')
        print(board[4]+' | '+board[5]+' | '+board[6])
        print('__________')
        print(board[7]+' | '+board[8]+' | '+board[9])
        print('__________')
    def check(board):
        return (board[1]==board[2]==board[3]!=' ' or board[4]==board[5]==board[6]!=' ' or board[7]==board[8]==board[9]!=' ' or board[1]==board[5]==board[9]!=' ' or board[3]==board[5]==board[7]!=' ' or board[1]==board[4]==board[7]!=' ' or board[2]==board[5]==board[8]!=' ' or board[3]==board[6]==board[9]!=' ')
    def isfull(board):
        m=0
        for i in range(1,10):
            if board[i]==' ':
                m=m+1
                break
        return (m==0)
    def play(board,a,p1,p2):
        if a==1:
            c=int(input('enter the position by player 1'))
            board[c]=p1
            display(board)
            for i in range(2,10):
                if ~isfull(board):
                    if i%2==0:
                        c=int(input('enter the position by player 2'))
                        board[c]=p2
                        display(board)
                        if check(board):
                            print('game won by player 2')
                            break
                    else:
                        c=int(input('enter the position by player 1'))
                        board[c]=p1
                        display(board)
                        if check(board):
                            print('game won by player 1')
                            break
            if isfull(board):
                    print('The game ended in draw')
                    
        else:
            c=int(input('enter the position by player 2'))
            board[c]=p2
            display(board)
            for i in range(2,10):
                if ~isfull(board):
                    if i%2==0:
                        c=int(input('enter the position by player 1'))
                        board[c]=p1
                        display(board)
                        if check(board):
                            print('game won by player 1')
                            break
                    else:
                        c=int(input('enter the position by player 2'))
                        board[c]=p2
                        display(board)
                        if check(board):
                            print('game won by player 2')
                            break
            if isfull(board):
                    print('the game ended in draw')
                        
                    
    init(board)
    print('the initial board is :')
    display(board)
    a=randint(1,2)
    if a==1:
        print('player 1 starts the game')
    else:
        print('player 2 starts the game')
    p1=' '
    p2=' '
    if a==1:
        p1=input('player 1 choose the symbol')
        if p1=='X':
            p2='O'
        else:
            p2='X'
    else:
        p2=input('player 2 choose the symbol')
        if p2=='X':
            p1='O'
        else:
            p1='X'        
    play(board,a,p1,p2)        
    






                
