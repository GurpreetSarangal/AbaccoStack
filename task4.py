from operator import truediv
import task3
import re


def main():
    no_of_colors = int(input("select number of colors(2-5): "))
    depth = int(input("select depth(2-4): "))
    if not(2 <= no_of_colors <= 5 ):
        print("input a valid range of colors")
        return 
    elif not(2 <= depth <= 4):
        print("input a valid depth")
        return
    else:
        
        game = task3.AbaccoStack(no_of_colors, depth)
        start = True
        while start:
            game.show(True)
            print("Enter your move(s) [Q for quit and R to reset]: ")
            moves = input()
            moves = re.split(" ", moves)
            if len(moves) > 5:
                print("Max 5 moves at once")
                continue
            for move in moves:
                if move == "Q":
                    start = False
                    
                    return
                game.moveBead(move)
            if game.isSolved():
                print("Woalah!! you won")
                return
        
replay = 'Y'
while replay=="y" or replay=="Y":
    main()
    print("Do want to replay?(Y/n): ", end='')
    replay = input()

print("Thanks for playing AbaccoStack")