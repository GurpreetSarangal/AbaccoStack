import random
from curses.ascii import isalpha, isdigit


# **********************************************************
# **********************************************************
# task 1
class card:
    def __init__(self, no_of_colors, depth):
        self.unshuffled_init_beads=[]
        self.no_of_colors = no_of_colors
        self.depth = depth
        # generate unshuffled_init_beads
        for i in range(0, no_of_colors):
            temp=[]
            for j in range(0, depth):
                temp.append(chr(65+i))
            temp = tuple(temp)
            self.unshuffled_init_beads.append(temp)
        # print(self.unshuffled_init_beads)
        self.unshuffled_beads_for_user = []
        to_be_shuffled = []
        for stack in self.unshuffled_init_beads:
            to_be_shuffled.append(list(stack))
            self.unshuffled_beads_for_user.append(list(stack))
        # self.unshuffled_init_beads = tuple(self.unshuffled_init_beads)
        # self.unshuffled_beads_for_user[0][0] = '---'
        # print(self.unshuffled_beads_for_user)
        # print(self.unshuffled_init_beads)


        self.shuffled_beads = self.__shuffle(to_be_shuffled)
        # print(self.unshuffled_init_beads)
        # print(self.unshuffled_beads_for_user)
        # print(self.shuffled_beads)
        

    def __shuffle(self, unshuffled_beads):
        temp_list1 = [x for x in range(0, self.no_of_colors)]
        temp_list2 = [x for x in range(0, self.depth)]

        # loop will also iterate for random range
        for i in range(0, random.randrange(3, self.depth + self.no_of_colors) ):
            # select random bead to swap
            # print(i)
            first_x = random.choice(temp_list1)  
            first_y = random.choice(temp_list2)
            # print(first_x,"  ",first_y)
            # select random bead to swap
            second_x = random.choice(temp_list1)  
            second_y = random.choice(temp_list2) 
            # print(second_x,"  ",second_y)

            # swap random shuffled_init_beads
            unshuffled_beads[second_x][second_y], unshuffled_beads[first_x][first_y] = unshuffled_beads[first_x][first_y], unshuffled_beads[second_x][second_y]
        return unshuffled_beads
            
    def test(self):
        
        for i in range(len(self.unshuffled_beads_for_user[0])):
            print("| ", end="")
            for j in range(0, len(self.unshuffled_beads_for_user)):
                print(self.unshuffled_beads_for_user[j][i], end=" ")
            print("|")
        
        print("+", end="")
        for i in range(len(self.unshuffled_beads_for_user)):
            print("--",end="")
        print("-+")

    

    def reset(self):
        # self.shuffled_beads = self.shuffled_init_beads
        pass

    def show(self):
        for i in range(len(self.unshuffled_init_beads[0])):
            print("| ", end="")
            for j in range(0, len(self.unshuffled_init_beads)):
                print(self.unshuffled_init_beads[j][i], end=" ")
            print("|")
        
        print("+", end="")
        for i in range(len(self.unshuffled_init_beads[0])):
            print("--",end="")
        print("+")

    def stack(self, number):
        return self.shuffled_beads[number-1]

    def __str__(self) -> str:
        response = ""
        for i in range(0, self.no_of_colors):
            response += '|'
            for j in range(0, self.depth):
                response += self.shuffled_beads[i][j]
            response += '|'
        return response

    def replace(self, filename, n):
        pass

# task 1 ends
# *************************************************************
# *************************************************************
# task 2 


class BStack:
    def __init__(self, max_capacity) -> None:
        self.max_capacity = max_capacity
        self.stack = []
    
    def push(self, item):
        if len(self.stack)>self.max_capacity:
            print("Stack is full")
        else:
            self.stack.append(item)
    
    def pop(self):
        if len(self.stack)==0:
            print("underflow")
            return
        else:
            return self.stack.pop()
    
    def isFull(self):
        return len(self.stack)>=self.max_capacity

    def peek(self):
        last_index = len(self.stack)-1
        return self.stack[last_index]

# task 2 ends
# **************************************************
# **************************************************
# task 3



class AbaccoStack(card):
    def __init__(self, color, depth) -> None:
        card.__init__(self, color, depth)
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
        
# task 3 ends
# ****************************************************
# ****************************************************