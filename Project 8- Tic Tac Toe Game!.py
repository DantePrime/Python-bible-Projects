board = [" "for i in range(9)]
#Print board

def print_board():
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print("\n"+row1+"\n"+row2+"\n"+row3+"\n")

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice-1] == " ":
        board[choice-1]=icon
    else:
        print("\n That space is taken ")

def is_victory(icon):
    if(board[0]==board[1]==board[2]==icon)or\
      (board[3]==board[4]==board[5]==icon)or\
      (board[6]==board[7]==board[8]==icon)or\
      (board[0]==board[3]==board[6]==icon)or\
      (board[1]==board[4]==board[7]==icon)or\
      (board[2]==board[5]==board[8]==icon)or\
      (board[0]==board[4]==board[8]==icon)or\
      (board[2]==board[4]==board[6]==icon):
        return True
    else:
        return False
                                              
def is_draw():
    if " "not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X Wins! Congratulations")
        break
    elif is_draw():
        print("Its a draw!")
    
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O Wins! Congratulations")
        break
    elif is_draw():
        print("Its a draw")
    
    
          
