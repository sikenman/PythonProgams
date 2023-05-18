from NoughtandCrosses import *

#Tic-Tac-Toe game with 1 Player and Computer
def menu():
    menu = """Enter one of the following options:
    \t 1 - PLAY THE GAME
    \t q - END THE PROGRAM
    """
    print(menu)
    choice = input("1 or q: ")
    print("")
    return choice

def main():
    
    welcome()
    total_score = 0
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:',total_score)
        if choice == 'q':
            print('Thank you for playing the "Tic-tac-toe" game.')
            print('Good bye')
            return

# Program execution begins here
if __name__ == '__main__':
    main()
