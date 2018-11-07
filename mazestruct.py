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




# creat a maze

# print the way
def pt():
     print("0", end = " ")


# r means row
# c means column
for r in range(10):
     for c in range(10):
          
          if (r == default[0] and c == default[1]):
               print("a", end = " ")
               
          elif (r == 0 and (c < 4 or c == 8)):
               pt()

          elif (r == 1 and (c ==2 or c == 8)):
               pt()

          elif (r == 2 and (c != 3 and c != 7)):
               pt()

          elif (r == 3 and (c != 1 and c != 5 and c != 9)):
               pt()

          elif (r == 4 and (c == 1 or c == 3 or c == 6)):
               pt()

          elif (r == 5 and (c != 1 and c != 4)):
               pt()

          elif (r == 6 and (c == 3 or c == 5 or c == 8)):
               pt()

          elif (r == 7 and ((c > 2 and c < 7) or c == 8)):
               pt()

          elif (r == 8 and (c == 4 or c == 8 or c == 9)):
               pt()

          elif (r == 9 and (c == 4 or c == 9)):
               pt()

          else:
               # except those (row, column) are walls 
               print("X", end = " ")
               
     print()
          
