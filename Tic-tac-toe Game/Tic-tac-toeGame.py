import tkinter as tk

window = tk.Tk()

window.columnconfigure([0, 1, 2,3], minsize=200)
window.rowconfigure([0, 1,2], minsize=200)

# Constants
circle = 1
cross = 2

tie = False

circleScore = 0
crossScore = 0

current="O"

buttons ={}
# resets the board and creates the buttons
def resetGame():
    global board
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]
    create_buttons()

# Changes the player turn "O" to "X", "X" to "O"
def player_turn():
    global current
    turnLabel = tk.Label(
        text=" turn:\n" + current,
        font=50
    )
    turnLabel.grid(row=1,column=3,sticky="nswe")
    current = "O" if current == "X" else "X"

# What to do when the game ended
def game_ended():
    global current, crossScore, circleScore, tie
    # winner = current
    
    winnerLabel = tk.Label(
        
        font=100
    )
    winnerLabel.grid(row=1,column=1,sticky="nswe")
    
    if tie == False:
        if current == "O":
            circleScore+=1
        else:
            crossScore+=1
        winnerLabel["text"]=current + " won the game"
    else:
        winnerLabel["text"]= "tie"
    
    destroy_buttons()
    
    crossScoreLabel = tk.Label(
        text="X Score:\n" + str(crossScore),
        font= 50,
        foreground= "red"
    )
    crossScoreLabel.grid(row=0, column=3, sticky="wsen")
    
    circleScoreLabel = tk.Label(
        text="O Score:\n" + str(circleScore),
        font= 50,
        foreground= "green"
    )
    circleScoreLabel.grid(row=2, column=3, sticky="wsen")

# Checks is there a winner or a tie
def check_win():
    global current, board, tie
    intCurrent = circle if current=="O" else cross
    
    # Check tie
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                tie = False
                shouldBreak = True
                break
            else:
                tie = True
                shouldBreak = False
        if shouldBreak == True:
            break
    
    # Calculates all the winning posibilities
    for i in range(3):
        if board[i][0] == intCurrent and board[i][1] == intCurrent and board[i][2] == intCurrent:
            tie = False
            game_ended()
            break
        if board[0][i] == intCurrent and board[1][i] == intCurrent and board[2][i] == intCurrent:
            tie = False
            game_ended()
            break
        
    if board[0][0] == intCurrent and board[1][1] == intCurrent and board[2][2] == intCurrent:
        tie = False
        game_ended()
    if board[2][0] == intCurrent and board[1][1] == intCurrent and board[0][2] == intCurrent:
        tie = False
        game_ended()
        
    if tie == True:
        game_ended()
    print(tie)
            
def handle_click(row, col):
    global current, board
        
    if board[row][col] == 0:
        player_turn()
        buttons["button{0}".format(str(row)+str(col))]["text"] = current
        board[row][col] = circle if current == "O" else cross
        check_win()

# Destroys all the buttons
def destroy_buttons():
    for i in range(3):
        for j in range(3):
            buttons["button{0}".format(str(i)+str(j))].destroy()
                
# Creates the game board
def create_buttons():
    for i in range(3):
        for j in range(3):
            buttons["button{0}".format(str(i)+str(j))] = tk.Button(
                text="",
                name="button" + str(i) + str(j),
                font=100
            )
            buttons["button{0}".format(str(i)+str(j))] ["command"] = lambda row=i, col=j: handle_click(row, col)
            buttons["button{0}".format(str(i)+str(j))] .grid(row=i, column=j, sticky="nsew") 

def main():
    restartButton = tk.Button(
        text="Start the game",
        command=lambda:resetGame() and restartButton.destroy(),
        font=50
    )
    restartButton.grid(row=2, column=1, sticky="we")
 
main()
window.mainloop()