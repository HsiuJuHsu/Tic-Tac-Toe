"tic tac toe"

def main():
    intro()
    player = players_turn()
    winner(player)

def players_turn():
    data = {'1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}
    ANS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player = 'X'
    ans = '0'
    change_grid(data, ans, player)
    while grid_available(data, ANS):
        ans = input("Player " + player + ": Enter the position of the grid (1~9): ")
        ans = check_valid(ans, ANS, data)
        change_grid(data, ans, player)
        if someone_wins(data):
            return player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    player = 0
    return player

def winner(player):
    if player != 0:
        print("")
        print("Player " + player + " wins! :)")
    else:
        print("")
        print("Game over! Nobody wins :(")

def someone_wins(data):
    for i in range(3):
        #3 marks in a row
        A = str(1 + 3*i)
        B = str(2 + 3*i)
        C = str(3 + 3*i)
        if (data[A] == data[B]) and (data[B] == data[C]):
            return True
        #3 marks in a column
        a = str(1 + i)
        b = str(4 + i)
        c = str(7 + i)
        if (data[a] == data[b]) and (data[b] == data[c]):
            return True
    #3 marks in a diagonal
    if (data['1'] == data['5']) and (data['5'] == data['9']):
        return True
    if (data['3'] == data['5']) and (data['5'] == data['7']):
        return True
    return False

def grid_available(data, ANS):
    value = []
    for key in data:
        value.append(data[key])
    for i in range(len(ANS)):
        if ANS[i] in value:
            return True
    return False

def check_valid(ans, ANS, data):
    while True:
        if ans not in ANS:
            ans = input("Invalid position! Try again: ")
        elif data[ans] == 'O' or data[ans] == 'X':
            ans = input("Occupied position! Try again: ")
        else:
            return ans

def change_grid(data, ans, player):
    if ans != '0':
        data[ans] = player
    print("")
    print("Current grid:")
    print('|'+data['7']+'|'+data['8']+'|'+data['9']+'|')
    print('|'+data['4']+'|'+data['5']+'|'+data['6']+'|')
    print('|'+data['1']+'|'+data['2']+'|'+data['3']+'|')

def intro():
    input("Welcome to the game 'Tic Tac Toe'!")
    print("")
    print("The game is played on a grid of 3 squares by 3 squares.")
    print("Two players take turns mark a single square of this grid: one is 'X', and the other is 'O'.")
    print("The first player who gets 3 of the marks in a row wins!")
    input("Press enter to get started :D")

if __name__ == '__main__':
    main()
