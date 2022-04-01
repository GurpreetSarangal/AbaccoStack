from curses.ascii import isalpha, isdigit
import task1


class AbaccoStack(task1.card):
    def __init__(self, color, depth) -> None:
        task1.card.__init__(self, color, depth)
        self.top_row_length = color+2
        self.top_row = ['.' for x in range(0, color+2)]
        self.moves = 0
    
    def moveBead(self,move):
        if move == "R" or move == "r":
            print("your moves are reset")
            self.reset()
            return

        if len(move) < 2 or len(move) >2 or not isalpha(move[1]) or not isdigit(move[0]):
            print("please input a valid move")

            
        elif move[1] == 'u' or move[1] == 'U':
            if int(move[0]) == 0 or int(move[0]) == len(self.top_row)-1: 
                print("Invalid Move")
            elif self.__stackIsEmpty(int(move[0])) or self.__position_is_occupied(int(move[0])):
                print("either stack is empty or position is already occupied")
                print(self.__stackIsEmpty(int(move[0])),  self.__position_is_occupied(int(move[0])))
                # raise Exception("Invalid Move")
            else:
                self.__pop_from_stack( int(move[0]))
                self.moves += 1
               

        elif move[1] == 'd' or move[1] == 'D':
            if int(move[0]) == 0 or int(move[0]) == len(self.top_row)-1: 
                print("Invalid Move")
                # raise Exception("Invalid Move")
            if self.__stackIsFull( int(move[0])) or self.__bead_not_there( int(move[0])):
                print("either stack is full or bead is not there")
                # print(self.__stackIsFull( int(move[0])), self.__bead_not_there( int(move[0])))
                # raise Exception("Invalid Move")
            else:
                self.__push_into_stack( int(move[0]))
                self.moves += 1

        elif move[1] == 'r' or move[1] == 'R':
            if int(move[0]) == len(self.top_row)-1:
                print("can't move")
                # raise Exception("Invalid Move")
            elif self.__position_is_occupied(int(move[0])+1):
                # raise Exception("Invalid Move")
                print("bead already there invalid move")
                
            else:
                self.__move_right(int(move[0]))
                self.moves += 1
                pass
        elif move[1] == 'l' or move[1] == 'L':
            if int(move[0] == 0):
                print("can't  move")
                # raise Exception("Invalid Move")

            elif self.__position_is_occupied(int(move[0])-1):
                # raise Exception("Invalid Move")
                print("already there invalid move")
            else:
                self.__move_left(int(move[0]))
                self.moves += 1
                pass
        else:
            # raise Exception("Invalid Move")
            print("Invalid move")


    def __stackIsEmpty(self, stack_no):
        if self.unshuffled_beads_for_user[stack_no-1][self.depth-1] == '.':
        
            # print(self.unshuffled_beads_for_user[stack_no-1][0])
            return True
        else:
            # print(self.unshuffled_beads_for_user[stack_no-1][0])
            return False

    def __stackIsFull(self, stack_no):
        if self.unshuffled_beads_for_user[stack_no-1][0] == '.':
            # print(self.unshuffled_beads_for_user[stack_no-1][0])
            return False
        else:
            # print(self.unshuffled_beads_for_user[stack_no-1][0])
            return True
        
    def __position_is_occupied(self, position):
        if self.top_row[position] != '.':
            return True
        else:
            return False
        
    def __bead_not_there(self, position):
        if self.top_row[position] == '.':
            return True
        else: 
            return False

    def __pop_from_stack(self, stack_no):
        # removed = self.unshuffled_beads_for_user[stack_no-1][0]
        for i in range(len(self.unshuffled_beads_for_user[stack_no-1])):
            if self.unshuffled_beads_for_user[stack_no-1][i] != '.':
                removed = self.unshuffled_beads_for_user[stack_no-1][i]
                self.unshuffled_beads_for_user[stack_no-1][i] = '.'
                break

        self.top_row[stack_no] = removed
        
    def __push_into_stack(self, stack_no):
        removed = self.top_row[stack_no]
        self.top_row[stack_no] = '.'
        for i in range(len(self.unshuffled_beads_for_user[stack_no-1])):
            if self.unshuffled_beads_for_user[stack_no-1][i] != '.':
                self.unshuffled_beads_for_user[stack_no-1][i-1] = removed
                break
        else:
            last_index = len(self.unshuffled_beads_for_user[stack_no-1]) - 1
            self.unshuffled_beads_for_user[stack_no-1][last_index] = removed
        # self.unshuffled_beads_for_user[stack_no-1].insert(0, removed)
    
    def __move_right(self, position):
        self.top_row[position+1] = self.top_row[position]
        self.top_row[position] = '.'
    
    def __move_left(self, position):
        self.top_row[position-1] = self.top_row[position]
        self.top_row[position] = '.'
    
    def isSolved(self):
        for i in range(0, len(self.shuffled_beads[0])):
            for j in range(0, len(self.shuffled_beads)):
                if self.unshuffled_beads_for_user[j][i] != self.shuffled_beads[j][i]:
                    return False 
        return True

    def reset(self):
        for i in range(0, len(self.shuffled_beads[0])):
            for j in range(0, len(self.shuffled_beads)):
                self.unshuffled_beads_for_user[j][i] = self.unshuffled_init_beads[j][i]
        self.moves = 0
        self.top_row = ['.' for x in range(0, self.top_row_length)]

    def show(self, card=False):
        for i in range(len(self.top_row)):
            print(i,end=" ")
        print()
        for top_element in self.top_row:
            print(top_element, end=" ")
        print()
        self.test()
        if card:
            print("card")
            for i in range(0, len(self.shuffled_beads[0])):
                print("|",end="")
                for j in range(0, len(self.shuffled_beads)):
                    print(self.shuffled_beads[j][i],end=" ")
                print("|")
        print(self.moves, "moves")
        print("won = ", self.isSolved())
        
        

# tasks
# make the unshuffled list
# correct the pop operation
# 
# test = AbaccoStack(2,2)
# test.show(True)
# while True:
#     move = input("enter next move(1u) : ")
#     test.moveBead(move)
#     if test.isSolved():
#         print("woalah!! you won bro")
#         break

#     test.show(True)