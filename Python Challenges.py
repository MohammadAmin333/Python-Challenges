'''def main():  
    board = [[' ' for _ in range(3)] for _ in range(3)]  
    current_player = "X"  

    while True:  
        print_board(board)  
        try:  
            row = int(input(f"Player {current_player}, enter the row (0-2): "))  
            col = int(input(f"Player {current_player}, enter the column (0-2): "))  
        except ValueError:  
            print("Invalid input. Please enter numbers only.")  
            continue  

        if board[row][col] == ' ':  
            board[row][col] = current_player  
            winner = check_winner(board)  
            if winner:  
                print_board(board)  
                print(f"Player {winner} wins!")  
                break  
        else:  
            print("That position is already taken. Try again.")  

        if all(cell != ' ' for row in board for cell in row):  
            print_board(board)  
            print("It's a draw!")  
            break  

        
    def print_board(board):
        for row in board:
         print(" | ".join(row))
         print("-" * 9)

    def check_winner(board):
        for i in range (3):
         if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
         if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
        
        if board [0][0] == board[1][1] == board[2][2] != ' ':
         return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != ' ':
         return board[0][2]

        return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)




if __name__ == '__main__':
    main()

'''

import random
characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password_length = int(input("Enter the length of password: "))
password=[]
for i in range(password_length):
    password.append(random.choice(characters))
print("".join(password))
print("Your password is: "+ password )