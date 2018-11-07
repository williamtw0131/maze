roles = "This is a maze game.\nStarts at top-left where is marked S.\nMovement option: \nup, down, right, left, or quit\nThe 0 is the path, make sure you stay in there.\nThe exit is at the bottom-right."
waller = "You can't go through walls!!"
mover = "Movement invalid."
# define starting point
r = 0
c = 0
default = [r, c]


# define movement
def down():
     default[0] += 1

def up():
     default[0] -= 1

def right():
     default[1] += 1

def left():
     default[1] -= 1


# creat a path list so that I can check the valid move later
path_list = []

# print the way(for coding convenience, no need to type every time)
def pt():
     print("0", end = " ")


print(roles)
gaming = True

# print out the maze 
while gaming:

     # the maze is 10x10 big
     for r in range(10):
          for c in range(10):

               # starting point
               if (r == default[0] and c == default[1]):
                    print("S", end = " ")
                    # put the path in list
                    path_list.append([r, c])
               
               elif (r == 0 and (c < 4 or c == 8)):
                    pt()
                    # put the path in list for later usage
                    path_list.append([r, c])
     
               elif (r == 1 and (c ==2 or c == 8)):
                    pt()
                    path_list.append([r, c])
     
               elif (r == 2 and (c != 3 and c != 7)):
                    pt()
                    path_list.append([r, c])
     
               elif (r == 3 and (c != 1 and c != 5 and c != 9)):
                    pt()
                    path_list.append([r, c])
     
               elif (r == 4 and (c == 1 or c == 3 or c == 6)):
                    pt()
                    path_list.append([r, c])
     
               elif (r == 5 and (c != 1 and c != 4)):
                    pt()
                    path_list.append([r, c])
     
               elif (r == 6 and (c == 3 or c == 5 or c == 8)):
                    pt()
                    path_list.append([r, c])

               elif (r == 7 and ((c > 2 and c < 7) or c == 8)):
                    pt()
                    path_list.append([r, c])

               elif (r == 8 and (c == 4 or c == 8 or c == 9)):
                    pt()
                    path_list.append([r, c])

               elif (r == 9 and c == 9):
                    pt()
                    path_list.append([r, c])
     
               else:
                    # except those (row, column) are all walls 
                    print("X", end = " ")
                    
          # for every 10 columns done drawing jump to next row
          print()
     
     # prompt user for movement or quit
     move = input("Where to go?")


     if move == "quit":
          break
     
     elif move == "down":
          # call movement function to move
          down()
          # and check for valid move
          # check if it is inside the maze
          if (default[0] > 9):
               up()
               print(mover)
          #check if it is inside the path
          elif (default not in path_list):
               up()
               print(waller)
               
     elif move == "up":
          up()
          if (default[0] < 0):
               down()
               print(mover)
          elif (default not in path_list):
               down()
               print(waller)
               
     elif move == "right":
          right()
          if (default[1] > 9):
               left()
               print(mover)
          elif (default not in path_list):
               left()
               print(waller)
               
     elif move == "left":
          left()
          if (default[1] < 0):
               right()
               print(mover)
          elif (default not in path_list):
               right()
               print(waller)
               
     else:
          print("not an option")

     # when reaching the end(9, 9)
     if (default[0] == 9 and default[1] == 9):
          print("Congratunation!!!\nYou reach the end!!!")
          gaming = False
     
