import random



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


# test = card(3,3)
# test.test()
# print(test.stack(1))
# print(str(test))