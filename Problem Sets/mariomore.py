                                # Mario (more) 

"""
Create a program that prints the following shape with a user-inputted height: 

~/workspace/ $ mario.py
height: 5
    #  #
   ##  ##
  ###  ###
 ####  ####
#####  #####

Specification: 
    1. First prompt the user for the height of the pyramid 
    2. Generate the desired half-pyramids (with the help of print and one or more loops)
    3. Take care to align the bottom-left corner of your half-pyramid with the left-hand edge of your terminal window.
"""

# Code goes below here 
# get a height 
while True: 
    height = input(int("height: "))
    if height >= 0 and height <= 23:
        break

for line in range(height):
    # print spaces
    for a in range(1, height - line):
        print(" ", end = "")
    # print blocks
    for a in range(1, line + 3):
        print("#", end = "")
    print(" ", end = "")
    for a in range(1, line + 3):
        print("#", end = "")
        
    print() 