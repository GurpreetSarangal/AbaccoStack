# AbaccoStack

AbaccoStack is a game. You have a structure formed by three side by side stacks that are limited in size.  
Taking example of three stacks with depth of three. The structure is filled with nine beads, 3 As, 3 Bs, 3 Cs, representing 3 colors. Initially the structure looks like this:
```
0 1 2 3 4
. . . . .
  A B C
  A B C
  A B C
```
The structure always has 9 beads. The beads can move on position at a time to an empty position. An empty position is represented by a `'.'` here.  

For example from the initial configuration, one can pop a bead from the first stack and switch it with the top bead in the second stack in the following series of moves


```
0 1 2 3 4
. A . . .
  . B C
  A B C
  A B C
```
```
0 1 2 3 4
A . . . .
  . B C
  A B C
  A B C
```
```
0 1 2 3 4
A . B . .
  . . C
  A B C
  A B C
```
```
0 1 2 3 4
A B . . .
  . . C
  A B C
  A B C
```
```
0 1 2 3 4
A . . . .
  B . C
  A B C
  A B C
```

## Game Logic
The game consists of getting a random configuration card and doing the minimum numbers of moves to change the beads of the AbaccoStack to that given configuration.  
For example, if player gets the following card.
```
|A A C|
|B C A|
|C B B|
```
Player can only move beads one by one to get
```
From                to

0 1 2 3 4       0 1 2 3 4
. . . . .       . . . . .
  A B C           A A C
  A B C           B C A
  A B C           C B B
```

The is played by a user, not the computer. The computer would generate a random configuration card and the user would have to solve the game by indicating the move to do in order to change the configuration from the initial one to the one indicated on the card.  

### The moves
The moves are indicated by the following input pair `ij` where `i` is a digit and `j` a character like the following:  
- `1u` means stack 1 upward move
- `1d` means stack 1 downward move
- `2u` means stack 2 upward move
- `2d` means stack 2 downward move
- `3u` means stack 3 upward move 
- `3d` means stack 3 downward move
- `0r` means position 0 right move
- `1r` and `1l` means position 1 right move and left move respectively
- `2r` and `2l` means position 2 right move and left move respectively
- `3r` and `3l` means position 3 right move and left move respectively
- `4l` means position 4 left move

At most 5 moves can be executed at once. After completing the game, game congratulates you and asks for replay `Y/n` or quit `Q`  
`R` or `r` will reset the whole structure to initial configuration


## `AbaccoStack` Class
`AbaccoStack` class represents the structure. An instance of this class stores bounded stacks and a list representing the top row. The number of bounded stacks and their common depth is given as input to constructor of the class. The structure initializes the stacks to that each stack has only one and unique color (colors are represented by letters A,B,C, etc). The instance also stores the numbers of moves already done since the initialization. Initially it is 0.  
There is a method `moveBeads()` which changes the state of the AbaccoStack instance based on the valid moves indicating above. `move` is a string of two characters. It warns the user on invalid moves (Actually it should raise an exception but this terminates the execution so, I omitted that).
There is another method `isSolved()` which returns TRUE when if the state of the instance corresponds to the configuration card, otherwise FALSE. `card` is an instance of class `card`.  
The method `reset()` resets the property `moves` to zero and rearranges the stack to the initial position with each stack having its own beads
To display the state of AbaccoStack instance we have a method `show()` which takes an optional argument `card`. When the parameter `card` is present, the configuration car will also be displayed on the side of the AbaccoStack instance in addition to the number of moves already taken since the start, otherwise only the state of AbaccoStack is shown  
```             
0 1 2 3 4       
A . . C .          card
| . B . |         | A A C |
| A B C |         | B C A |
| A B C |         | C B B |
+-------+
34 moves
```
and without the card

```
0 1 2 3 4      
A . . B .       
| . . C |         
| A B C |         
| A B C |
+-------+
14 moves
```



## Future Plans 
We can add the number of minutes and seconds to solve the problem by getting the current time from the system when you start the game and display the card the fist time. Then the spent time is the new current time minus the start time. 
