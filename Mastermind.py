import simpleguitk as simplegui
import random
import time

WIDTH = 500 
HEIGHT = 900

OFF_TOP = 50
OFF_BOTTOM = HEIGHT - 50
BOARD_WIDTH = 425
BOARD_START = [WIDTH/2, OFF_TOP]
BOARD_END = [WIDTH/2, OFF_BOTTOM]
SIDE_LINE_START = [BOARD_START[0] + ((BOARD_WIDTH/2) - 100), OFF_TOP]
SIDE_LINE_END = [BOARD_START[0] + ((BOARD_WIDTH/2) - 100), (OFF_BOTTOM - 100)]
GUESS_LINE_START = [BOARD_START[0] + (BOARD_WIDTH/2), (OFF_BOTTOM - 100)]
GUESS_LINE_END = [BOARD_START[0] - (BOARD_WIDTH/2), (OFF_BOTTOM - 100)]
row_space = 70
row_space = 70
first_row_start = [(BOARD_START[0] + (BOARD_WIDTH/2)) , (OFF_TOP + row_space)] 
first_row_end = [(BOARD_START[0] - (BOARD_WIDTH/2))  , (OFF_TOP + row_space)]
#circles
guess_circ_radius = 25
circle1 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + ((row_space/2) + 5), OFF_TOP + (row_space/2)]
circle2 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*3), OFF_TOP + (row_space/2)]
circle3 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*5), OFF_TOP + (row_space/2)]
circle4 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*7), OFF_TOP + (row_space/2)]

#Guess lists
current_guess = [0,0,0,0]
guess_color = ['','','','']
answer = [0,0,0,0]
answer_color = ['','','','']
blacks = 0
whites = 0

#Colors
WHITE = 1
BLUE = 2
RED = 3
ORANGE = 4

#Other stuff
row_number = 11
ans_circ_radius = 10

r1c1, r1c2, r1c3, r1c4, r2c1, r2c2, r2c3, r2c4, r3c1, r3c2, r3c3, r3c4 = 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver'
r4c1, r4c2, r4c3, r4c4, r5c1, r5c2, r5c3, r5c4, r6c1, r6c2, r6c3, r6c4 = 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver'
r7c1, r7c2, r7c3, r7c4, r8c1, r8c2, r8c3, r8c4, r9c1, r9c2, r9c3, r9c4 = 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver'
r10c1, r10c2, r10c3, r10c4, r11c1, r11c2, r11c3, r11c4 = 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver'

circle1_1 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*1), OFF_TOP + (row_space/2)]
circle2_1 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*3), OFF_TOP + (row_space/2)]
circle3_1 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*5), OFF_TOP + (row_space/2)]
circle4_1 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*7), OFF_TOP + (row_space/2)]

circle1_2 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*1), (OFF_TOP + (row_space/2) + 70)]
circle2_2 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*3), (OFF_TOP + (row_space/2) + 70)]
circle3_2 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*5), (OFF_TOP + (row_space/2) + 70)]
circle4_2 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*7), (OFF_TOP + (row_space/2) + 70)]

circle1_3 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*1), (OFF_TOP + (row_space/2) + 70 *2)]
circle2_3 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*3), (OFF_TOP + (row_space/2) + 70 *2)]
circle3_3 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*5), (OFF_TOP + (row_space/2) + 70 *2)]
circle4_3 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*7), (OFF_TOP + (row_space/2) + 70 *2)]

circle1_4 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*1), (OFF_TOP + (row_space/2) + 70 *3)]
circle2_4 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*3), (OFF_TOP + (row_space/2) + 70 *3)]
circle3_4 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*5), (OFF_TOP + (row_space/2) + 70 *3)]
circle4_4 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*7), (OFF_TOP + (row_space/2) + 70 *3)]

circle1_5 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*1), (OFF_TOP + (row_space/2) + 70 *4)]
circle2_5 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*3), (OFF_TOP + (row_space/2) + 70 *4)]
circle3_5 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*5), (OFF_TOP + (row_space/2) + 70 *4)]
circle4_5 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*7), (OFF_TOP + (row_space/2) + 70 *4)]

circle1_6 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*1), (OFF_TOP + (row_space/2) + 70 *5)]
circle2_6 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*3), (OFF_TOP + (row_space/2) + 70 *5)]
circle3_6 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*5), (OFF_TOP + (row_space/2) + 70 *5)]
circle4_6 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*7), (OFF_TOP + (row_space/2) + 70 *5)]

circle1_7 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*1), (OFF_TOP + (row_space/2) + 70 *6)]
circle2_7 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*3), (OFF_TOP + (row_space/2) + 70 *6)]
circle3_7 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*5), (OFF_TOP + (row_space/2) + 70 *6)]
circle4_7 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*7), (OFF_TOP + (row_space/2) + 70 *6)]

circle1_8 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*1), (OFF_TOP + (row_space/2) + 70 *7)]
circle2_8 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*3), (OFF_TOP + (row_space/2) + 70 *7)]
circle3_8 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*5), (OFF_TOP + (row_space/2) + 70 *7)]
circle4_8 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*7), (OFF_TOP + (row_space/2) + 70 *7)]

circle1_9 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*1), (OFF_TOP + (row_space/2) + 70 *8)]
circle2_9 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*3), (OFF_TOP + (row_space/2) + 70 *8)]
circle3_9 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*5), (OFF_TOP + (row_space/2) + 70 *8)]
circle4_9 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*7), (OFF_TOP + (row_space/2) + 70 *8)]

circle1_10 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*1), (OFF_TOP + (row_space/2) + 70 *9)]
circle2_10 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*3), (OFF_TOP + (row_space/2) + 70 *9)]
circle3_10 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*5), (OFF_TOP + (row_space/2) + 70 *9)]
circle4_10 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*7), (OFF_TOP + (row_space/2) + 70 *9)]

circle1_11 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*1), (OFF_TOP + (row_space/2) + 70 *10)]
circle2_11 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*3), (OFF_TOP + (row_space/2) + 70 *10)]
circle3_11 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*5), (OFF_TOP + (row_space/2) + 70 *10)]
circle4_11 = [(BOARD_START[0] - (BOARD_WIDTH/2)) + (((row_space/2) + 5)*7), (OFF_TOP + (row_space/2) + 70 *10)]

row1 = [circle1_1, circle2_1, circle3_1, circle4_1]
row2 = [circle1_2, circle2_2, circle3_2, circle4_2]
row3 = [circle1_3, circle2_3, circle3_3, circle4_3]
row4 = [circle1_4, circle2_4, circle3_4, circle4_4]
row5 = [circle1_5, circle2_5, circle3_5, circle4_5]
row6 = [circle1_6, circle2_6, circle3_6, circle4_6]
row7 = [circle1_7, circle2_7, circle3_7, circle4_7]
row8 = [circle1_8, circle2_8, circle3_8, circle4_8]
row9 = [circle1_9, circle2_9, circle3_9, circle4_9]
row10 = [circle1_10, circle2_10, circle3_10, circle4_10]
row11 = [circle1_11, circle2_11, circle3_11, circle4_11]

"""row_ans = [[0,0,0,0], ['gray', 'gray', 'gray', 'gray'], ['gray', 'gray', 'gray', 'gray'], ['gray', 'gray', 'gray', 'gray'], 
          ['gray', 'gray', 'gray', 'gray'], ['gray', 'gray', 'gray', 'gray'], ['gray', 'gray', 'gray', 'gray'],
          ['gray', 'gray', 'gray', 'gray'], ['gray', 'gray', 'gray', 'gray'], ['gray', 'gray', 'gray', 'gray'], 
          ['gray', 'gray', 'gray', 'gray']]""" 

r10d1, r10d2, r10d3, r10d4, r9d1, r9d2, r9d3, r9d4, r8d1, r8d2, r8d3, r8d4 = 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray'
r7d1, r7d2, r7d3, r7d4, r6d1, r6d2, r6d3, r6d4, r5d1, r5d2, r5d3, r5d4 = 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray'
r4d1, r4d2, r4d3, r4d4, r3d1, r3d2, r3d3, r3d4, r2d1, r2d2, r2d3, r2d4 = 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray' 
r1d1, r1d2, r1d3, r1d4 = 'gray', 'gray', 'gray', 'gray'

thisrow = [0,0,0,0]

num1, num2, num3, num4, g1, g2, g3, g4 = 0,0,0,0,0,0,0,0


        
def makeans():
    create_answer()
    
def reset():
    global answer, answer_color, current_guess, blacks, whites, row_number
    global r1c1, r1c2, r1c3, r1c4, r2c1, r2c2, r2c3, r2c4, r3c1, r3c2, r3c3, r3c4, r4c1, r4c2, r4c3, r4c4
    global r5c1, r5c2, r5c3, r5c4, r6c1, r6c2, r6c3, r6c4, r7c1, r7c2, r7c3, r7c4, r8c1, r8c2, r8c3, r8c4 
    global r9c1, r9c2, r9c3, r9c4, r10c1, r10c2, r10c3, r10c4, r11c1, r11c2, r11c3, r11c4
    global r10d1, r10d2, r10d3, r10d4, r9d1, r9d2, r9d3, r9d4, r8d1, r8d2, r8d3, r8d4, r7d1, r7d2, r7d3, r7d4
    global r6d1, r6d2, r6d3, r6d4, r5d1, r5d2, r5d3, r5d4, r4d1, r4d2, r4d3, r4d4, r3d1, r3d2, r3d3, r3d4
    global r2d1, r2d2, r2d3, r2d4, r1d1, r1d2, r1d3, r1d4
    makeans()
    blacks = 0
    whites = 0
    r1c1, r1c2, r1c3, r1c4, r2c1, r2c2, r2c3, r2c4, r3c1, r3c2, r3c3, r3c4 = 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver'
    r4c1, r4c2, r4c3, r4c4, r5c1, r5c2, r5c3, r5c4, r6c1, r6c2, r6c3, r6c4 = 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver'
    r7c1, r7c2, r7c3, r7c4, r8c1, r8c2, r8c3, r8c4, r9c1, r9c2, r9c3, r9c4 = 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver'
    r10c1, r10c2, r10c3, r10c4, r11c1, r11c2, r11c3, r11c4 = 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver'
    r10d1, r10d2, r10d3, r10d4, r9d1, r9d2, r9d3, r9d4, r8d1, r8d2, r8d3, r8d4 = 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray'
    r7d1, r7d2, r7d3, r7d4, r6d1, r6d2, r6d3, r6d4, r5d1, r5d2, r5d3, r5d4 = 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray'
    r4d1, r4d2, r4d3, r4d4, r3d1, r3d2, r3d3, r3d4, r2d1, r2d2, r2d3, r2d4 = 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray' 
    r1d1, r1d2, r1d3, r1d4 = 'gray', 'gray', 'gray', 'gray'
    row_number = 11   
def create_answer():
    global answer, answer_color
    global num1, num2, num3, num4
    #Create an answer with numbers
    #answer = random.sample(xrange(1,5), 4)
    num1 = random.randint (1, 4)
    num2 = random.randint (1, 4)
    num3 = random.randint (1, 4)
    num4 = random.randint (1, 4)
    
    answer = [num1, num2, num3, num4]
    
    #Create an answer with colors
    for x in range (0, 4):
        if answer[x] == 1:
            answer_color[x] = 'white'
        elif answer[x] == 2:
            answer_color[x] = 'blue'
        elif answer[x] == 3:
            answer_color[x] = 'red'
        elif answer[x] == 4:
            answer_color[x] = 'orange'
    
    #print (answer)
    print (answer_color)   
def create_guess():
    #change current answer to colors so that you can easily move it to the next row
    global current_guess, guess_color, g1, g2, g3, g4

    for x in range (0, 4):
        if current_guess[x] == 1:
            guess_color[x] = 'white'
        elif current_guess[x] == 2:
            guess_color[x] = 'blue'
        elif current_guess[x] == 3:
            guess_color[x] = 'red'
        elif current_guess[x] == 4:
            guess_color[x] = 'orange'
         
    #print (guess_color)      
def enter():
    global r1c1, r1c2, r1c3, r1c4, r2c1, r2c2, r2c3, r2c4, r3c1, r3c2, r3c3, r3c4, r4c1, r4c2, r4c3, r4c4
    global r5c1, r5c2, r5c3, r5c4, r6c1, r6c2, r6c3, r6c4, r7c1, r7c2, r7c3, r7c4, r8c1, r8c2, r8c3, r8c4 
    global r9c1, r9c2, r9c3, r9c4, r10c1, r10c2, r10c3, r10c4, r11c1, r11c2, r11c3, r11c4
    global guess_color, current_guess, row_number, blacks, whites, thisrow
    global r10d1, r10d2, r10d3, r10d4, r9d1, r9d2, r9d3, r9d4, r8d1, r8d2, r8d3, r8d4, r7d1, r7d2, r7d3, r7d4
    global r6d1, r6d2, r6d3, r6d4, r5d1, r5d2, r5d3, r5d4, r4d1, r4d2, r4d3, r4d4, r3d1, r3d2, r3d3, r3d4
    global r2d1, r2d2, r2d3, r2d4, r1d1, r1d2, r1d3, r1d4
        
    compare()
    
    row_number -= 1
    
    if row_number == 10:
        r10c1 = guess_color[0]
        r10c2 = guess_color[1]
        r10c3 = guess_color[2]
        r10c4 = guess_color[3]
        r11c1, r11c2, r11c3, r11c4 = 'silver', 'silver', 'silver', 'silver'
        
        #print ("There are : ", blacks , "black dots")
        picnum = random.sample(range (1, 5), 4)
        while blacks >= 1:
            #print ("Blacks picnum: ",picnum)
            for x in range (0,blacks):
                print (picnum[x])
                if picnum[x] == 1:
                    r10d1 = 'black'
                    blacks -= 1
                elif picnum[x] == 2:
                    r10d2 = 'black'
                    blacks -= 1
                elif picnum[x] == 3:
                    r10d3 = 'black'
                    blacks -= 1
                elif picnum[x] == 4:
                    r10d4 = 'black'
                    blacks -= 1
                
                
        picnum = random.sample(range (1, 5), 4)
        while whites >= 1:
            #print ("whites picnum: ", picnum)
            for x in range (0, whites):
                if picnum[x] == 1 and r10d1 == 'gray':
                    r10d1 = 'white'
                    whites -= 1
                elif picnum[x] == 2 and r10d2 == 'gray':
                    r10d2 = 'white'
                    whites -= 1
                elif picnum[x] == 3 and r10d3 == 'gray':
                    r10d3 = 'white'
                    whites -= 1
                elif picnum[x] == 4 and r10d4 == 'gray':
                    r10d4 = 'white'
                    whites -= 1
                else:
                    picnum = random.sample(range (1, 5), 4)
                    continue        
    elif row_number == 9:
        r9c1 = guess_color[0]
        r9c2 = guess_color[1]
        r9c3 = guess_color[2]
        r9c4 = guess_color[3]
        r11c1, r11c2, r11c3, r11c4 = 'silver', 'silver', 'silver', 'silver'
        
        picnum = random.sample(range (1, 5), 4)
        while blacks >= 1:
            for x in range (0,blacks):
                if picnum[x] == 1:
                    r9d1 = 'black'
                    blacks -= 1
                elif picnum[x] == 2:
                    r9d2 = 'black'
                    blacks -= 1
                elif picnum[x] == 3:
                    r9d3 = 'black'
                    blacks -= 1
                elif picnum[x] == 4:
                    r9d4 = 'black'
                    blacks -= 1
                
                
        picnum = random.sample(range (1, 5), 4)
        while whites >= 1:
            for x in range (0, whites):
                if picnum[x] == 1 and r9d1 == 'gray':
                    r9d1 = 'white'
                    whites -= 1
                elif picnum[x] == 2 and r9d2 == 'gray':
                    r9d2 = 'white'
                    whites -= 1
                elif picnum[x] == 3 and r9d3 == 'gray':
                    r9d3 = 'white'
                    whites -= 1
                elif picnum[x] == 4 and r9d4 == 'gray':
                    r9d4 = 'white'
                    whites -= 1
                else:
                    picnum = random.sample(range (1, 5), 4)
                    continue   
    elif row_number == 8:
        r8c1 = guess_color[0]
        r8c2 = guess_color[1]
        r8c3 = guess_color[2]
        r8c4 = guess_color[3]
        r11c1, r11c2, r11c3, r11c4 = 'silver', 'silver', 'silver', 'silver'
        
        picnum = random.sample(range (1, 5), 4)
        while blacks >= 1:
            for x in range (0,blacks):
                if picnum[x] == 1:
                    r8d1 = 'black'
                    blacks -= 1
                elif picnum[x] == 2:
                    r8d2 = 'black'
                    blacks -= 1
                elif picnum[x] == 3:
                    r8d3 = 'black'
                    blacks -= 1
                elif picnum[x] == 4:
                    r8d4 = 'black'
                    blacks -= 1
                
                
        picnum = random.sample(range (1, 5), 4)
        while whites >= 1:
            for x in range (0, whites):
                if picnum[x] == 1 and r8d1 == 'gray':
                    r8d1 = 'white'
                    whites -= 1
                elif picnum[x] == 2 and r8d2 == 'gray':
                    r8d2 = 'white'
                    whites -= 1
                elif picnum[x] == 3 and r8d3 == 'gray':
                    r8d3 = 'white'
                    whites -= 1
                elif picnum[x] == 4 and r8d4 == 'gray':
                    r8d4 = 'white'
                    whites -= 1
                else:
                    picnum = random.sample(range (1, 5), 4)
                    continue
    elif row_number == 7:
        r7c1 = guess_color[0]
        r7c2 = guess_color[1]
        r7c3 = guess_color[2]
        r7c4 = guess_color[3]
        r11c1, r11c2, r11c3, r11c4 = 'silver', 'silver', 'silver', 'silver'  
        
        picnum = random.sample(range (1, 5), 4)
        while blacks >= 1:
            for x in range (0,blacks):
                if picnum[x] == 1:
                    r7d1 = 'black'
                    blacks -= 1
                elif picnum[x] == 2:
                    r7d2 = 'black'
                    blacks -= 1
                elif picnum[x] == 3:
                    r7d3 = 'black'
                    blacks -= 1
                elif picnum[x] == 4:
                    r7d4 = 'black'
                    blacks -= 1
                
                
        picnum = random.sample(range (1, 5), 4)
        while whites >= 1:
            for x in range (0, whites):
                if picnum[x] == 1 and r7d1 == 'gray':
                    r7d1 = 'white'
                    whites -= 1
                elif picnum[x] == 2 and r7d2 == 'gray':
                    r7d2 = 'white'
                    whites -= 1
                elif picnum[x] == 3 and r7d3 == 'gray':
                    r7d3 = 'white'
                    whites -= 1
                elif picnum[x] == 4 and r7d4 == 'gray':
                    r7d4 = 'white'
                    whites -= 1
                else:
                    picnum = random.sample(range (1, 5), 4)
                    continue
    elif row_number == 6:
        r6c1 = guess_color[0]
        r6c2 = guess_color[1]
        r6c3 = guess_color[2]
        r6c4 = guess_color[3]
        r11c1, r11c2, r11c3, r11c4 = 'silver', 'silver', 'silver', 'silver'  
        
        picnum = random.sample(range (1, 5), 4)
        while blacks >= 1:
            for x in range (0,blacks):
                if picnum[x] == 1:
                    r6d1 = 'black'
                    blacks -= 1
                elif picnum[x] == 2:
                    r6d2 = 'black'
                    blacks -= 1
                elif picnum[x] == 3:
                    r6d3 = 'black'
                    blacks -= 1
                elif picnum[x] == 4:
                    r6d4 = 'black'
                    blacks -= 1
                
                
        picnum = random.sample(range (1, 5), 4)
        while whites >= 1:
            for x in range (0, whites):
                if picnum[x] == 1 and r6d1 == 'gray':
                    r6d1 = 'white'
                    whites -= 1
                elif picnum[x] == 2 and r6d2 == 'gray':
                    r6d2 = 'white'
                    whites -= 1
                elif picnum[x] == 3 and r6d3 == 'gray':
                    r6d3 = 'white'
                    whites -= 1
                elif picnum[x] == 4 and r6d4 == 'gray':
                    r6d4 = 'white'
                    whites -= 1
                else:
                    picnum = random.sample(range (1, 5), 4)
                    continue
    elif row_number == 5:
        r5c1 = guess_color[0]
        r5c2 = guess_color[1]
        r5c3 = guess_color[2]
        r5c4 = guess_color[3]
        r11c1, r11c2, r11c3, r11c4 = 'silver', 'silver', 'silver', 'silver'  
        
        picnum = random.sample(range (1, 5), 4)
        while blacks >= 1:
            for x in range (0,blacks):
                if picnum[x] == 1:
                    r5d1 = 'black'
                    blacks -= 1
                elif picnum[x] == 2:
                    r5d2 = 'black'
                    blacks -= 1
                elif picnum[x] == 3:
                    r5d3 = 'black'
                    blacks -= 1
                elif picnum[x] == 4:
                    r5d4 = 'black'
                    blacks -= 1
                
                
        picnum = random.sample(range (1, 5), 4)
        while whites >= 1:
            for x in range (0, whites):
                if picnum[x] == 1 and r5d1 == 'gray':
                    r5d1 = 'white'
                    whites -= 1
                elif picnum[x] == 2 and r5d2 == 'gray':
                    r5d2 = 'white'
                    whites -= 1
                elif picnum[x] == 3 and r5d3 == 'gray':
                    r5d3 = 'white'
                    whites -= 1
                elif picnum[x] == 4 and r5d4 == 'gray':
                    r5d4 = 'white'
                    whites -= 1
                else:
                    picnum = random.sample(range (1, 5), 4)
                    continue
    elif row_number == 4:
        r4c1 = guess_color[0]
        r4c2 = guess_color[1]
        r4c3 = guess_color[2]
        r4c4 = guess_color[3]
        r11c1, r11c2, r11c3, r11c4 = 'silver', 'silver', 'silver', 'silver' 
        
        picnum = random.sample(range (1, 5), 4)
        while blacks >= 1:
            for x in range (0,blacks):
                if picnum[x] == 1:
                    r4d1 = 'black'
                    blacks -= 1
                elif picnum[x] == 2:
                    r4d2 = 'black'
                    blacks -= 1
                elif picnum[x] == 3:
                    r4d3 = 'black'
                    blacks -= 1
                elif picnum[x] == 4:
                    r4d4 = 'black'
                    blacks -= 1
                
                
        picnum = random.sample(range (1, 5), 4)
        while whites >= 1:
            for x in range (0, whites):
                if picnum[x] == 1 and r4d1 == 'gray':
                    r4d1 = 'white'
                    whites -= 1
                elif picnum[x] == 2 and r4d2 == 'gray':
                    r4d2 = 'white'
                    whites -= 1
                elif picnum[x] == 3 and r4d3 == 'gray':
                    r4d3 = 'white'
                    whites -= 1
                elif picnum[x] == 4 and r4d4 == 'gray':
                    r4d4 = 'white'
                    whites -= 1
                else:
                    picnum = random.sample(range (1, 5), 4)
                    continue
    elif row_number == 3:
        r3c1 = guess_color[0]
        r3c2 = guess_color[1]
        r3c3 = guess_color[2]
        r3c4 = guess_color[3]
        r11c1, r11c2, r11c3, r11c4 = 'silver', 'silver', 'silver', 'silver' 
        
        picnum = random.sample(range (1, 5), 4)
        while blacks >= 1:
            for x in range (0,blacks):
                if picnum[x] == 1:
                    r3d1 = 'black'
                    blacks -= 1
                elif picnum[x] == 2:
                    r3d2 = 'black'
                    blacks -= 1
                elif picnum[x] == 3:
                    r3d3 = 'black'
                    blacks -= 1
                elif picnum[x] == 4:
                    r3d4 = 'black'
                    blacks -= 1
                
                
        picnum = random.sample(range (1, 5), 4)
        while whites >= 1:
            for x in range (0, whites):
                if picnum[x] == 1 and r3d1 == 'gray':
                    r3d1 = 'white'
                    whites -= 1
                elif picnum[x] == 2 and r3d2 == 'gray':
                    r3d2 = 'white'
                    whites -= 1
                elif picnum[x] == 3 and r3d3 == 'gray':
                    r3d3 = 'white'
                    whites -= 1
                elif picnum[x] == 4 and r3d4 == 'gray':
                    r3d4 = 'white'
                    whites -= 1
                else:
                    picnum = random.sample(range (1, 5), 4)
                    continue
    elif row_number == 2:
        r2c1 = guess_color[0]
        r2c2 = guess_color[1]
        r2c3 = guess_color[2]
        r2c4 = guess_color[3]
        r11c1, r11c2, r11c3, r11c4 = 'silver', 'silver', 'silver', 'silver'  
        
        picnum = random.sample(range (1, 5), 4)
        while blacks >= 1:
            for x in range (0,blacks):
                if picnum[x] == 1:
                    r2d1 = 'black'
                    blacks -= 1
                elif picnum[x] == 2:
                    r2d2 = 'black'
                    blacks -= 1
                elif picnum[x] == 3:
                    r2d3 = 'black'
                    blacks -= 1
                elif picnum[x] == 4:
                    r2d4 = 'black'
                    blacks -= 1
                
                
        picnum = random.sample(range (1, 5), 4)
        while whites >= 1:
            for x in range (0, whites):
                if picnum[x] == 1 and r2d1 == 'gray':
                    r2d1 = 'white'
                    whites -= 1
                elif picnum[x] == 2 and r2d2 == 'gray':
                    r2d2 = 'white'
                    whites -= 1
                elif picnum[x] == 3 and r2d3 == 'gray':
                    r2d3 = 'white'
                    whites -= 1
                elif picnum[x] == 4 and r2d4 == 'gray':
                    r2d4 = 'white'
                    whites -= 1
                else:
                    picnum = random.sample(range (1, 5), 4)
                    continue
    elif row_number == 1:
        r1c1 = guess_color[0]
        r1c2 = guess_color[1]
        r1c3 = guess_color[2]
        r1c4 = guess_color[3]
        r11c1, r11c2, r11c3, r11c4 = 'silver', 'silver', 'silver', 'silver'
        
        picnum = random.sample(range (1, 5), 4)
        while blacks >= 1:
            for x in range (0,blacks):
                if picnum[x] == 1:
                    r1d1 = 'black'
                    blacks -= 1
                elif picnum[x] == 2:
                    r1d2 = 'black'
                    blacks -= 1
                elif picnum[x] == 3:
                    r1d3 = 'black'
                    blacks -= 1
                elif picnum[x] == 4:
                    r1d4 = 'black'
                    blacks -= 1
                
                
        picnum = random.sample(range (1, 5), 4)
        while whites >= 1:
            for x in range (0, whites):
                if picnum[x] == 1 and r1d1 == 'gray':
                    r1d1 = 'white'
                    whites -= 1
                elif picnum[x] == 2 and r1d2 == 'gray':
                    r1d2 = 'white'
                    whites -= 1
                elif picnum[x] == 3 and r1d3 == 'gray':
                    r1d3 = 'white'
                    whites -= 1
                elif picnum[x] == 4 and r1d4 == 'gray':
                    r1d4 = 'white'
                    whites -= 1
                else:
                    picnum = random.sample(range (1, 5), 4)
                    continue
    #I may have to put these statements in each if statement?
    correct()
    if blacks != 4:
        blacks = 0
        whites = 0
   
    
   
    
def red():
    global current_guess
    global r1c1, r1c2, r1c3, r1c4, r2c1, r2c2, r2c3, r2c4, r3c1, r3c2, r3c3, r3c4, r4c1, r4c2, r4c3, r4c4
    global r5c1, r5c2, r5c3, r5c4, r6c1, r6c2, r6c3, r6c4, r7c1, r7c2, r7c3, r7c4, r8c1, r8c2, r8c3, r8c4 
    global r9c1, r9c2, r9c3, r9c4, r10c1, r10c2, r10c3, r10c4, r11c1, r11c2, r11c3, r11c4
    global g1, g2, g3, g4
    
    if r11c1 == 'silver' and r11c2 == 'silver' and r11c3 == 'silver'and r11c4 == 'silver':
        r11c1 = 'red'  
        current_guess[0] = 3
        g1 = 3
    elif r11c1 != 'silver'and r11c2 == 'silver' and r11c3 == 'silver'and r11c4 == 'silver':
        r11c2 = 'red'
        current_guess[1] = 3
        g2 = 3
    elif r11c1 != 'silver' and r11c2 != 'silver'and r11c3 == 'silver'and r11c4 == 'silver':
        r11c3 = 'red'
        current_guess[2] = 3
        g3 = 3
    else:
        r11c4 = 'red'
        current_guess[3] = 3
        g4 = 3
        print (current_guess)
        #compare()
        create_guess()
def orange():
    global current_guess
    global r1c1, r1c2, r1c3, r1c4, r2c1, r2c2, r2c3, r2c4, r3c1, r3c2, r3c3, r3c4, r4c1, r4c2, r4c3, r4c4
    global r5c1, r5c2, r5c3, r5c4, r6c1, r6c2, r6c3, r6c4, r7c1, r7c2, r7c3, r7c4, r8c1, r8c2, r8c3, r8c4 
    global r9c1, r9c2, r9c3, r9c4, r10c1, r10c2, r10c3, r10c4, r11c1, r11c2, r11c3, r11c4, g1, g2, g3, g4
    
    if r11c1 == 'silver' and r11c2 == 'silver' and r11c3 == 'silver'and r11c4 == 'silver':
        r11c1 = 'orange' 
        current_guess[0] = 4
        g1 = 4
    elif r11c1 != 'silver'and r11c2 == 'silver' and r11c3 == 'silver'and r11c4 == 'silver':
        r11c2 = 'orange'
        current_guess[1] = 4
        g2 = 4
    elif r11c1 != 'silver' and r11c2 != 'silver'and r11c3 == 'silver'and r11c4 == 'silver':
        r11c3 = 'orange'
        current_guess[2] = 4
        g3 = 4
    else:
        r11c4 = 'orange'
        current_guess[3] = 4
        g4 = 4
        #print (current_guess)
        #compare()
        create_guess()
def white():
    global current_guess
    global r1c1, r1c2, r1c3, r1c4, r2c1, r2c2, r2c3, r2c4, r3c1, r3c2, r3c3, r3c4, r4c1, r4c2, r4c3, r4c4
    global r5c1, r5c2, r5c3, r5c4, r6c1, r6c2, r6c3, r6c4, r7c1, r7c2, r7c3, r7c4, r8c1, r8c2, r8c3, r8c4 
    global r9c1, r9c2, r9c3, r9c4, r10c1, r10c2, r10c3, r10c4, r11c1, r11c2, r11c3, r11c4, g1, g2, g3, g4
    
    if r11c1 == 'silver' and r11c2 == 'silver' and r11c3 == 'silver'and r11c4 == 'silver':
        r11c1 = 'white'  
        current_guess[0] = 1
        g1 = 1
    elif r11c1 != 'silver'and r11c2 == 'silver' and r11c3 == 'silver'and r11c4 == 'silver':
        r11c2 = 'white'
        current_guess[1] = 1
        g2 = 1
    elif r11c1 != 'silver' and r11c2 != 'silver'and r11c3 == 'silver'and r11c4 == 'silver':
        r11c3 = 'white'
        current_guess[2] = 1
        g3 = 1
    else:
        r11c4 = 'white'
        current_guess[3] = 1
        g4 = 1
        #print (current_guess)
        #compare() 
        create_guess()
def blue():
    global current_guess
    global r1c1, r1c2, r1c3, r1c4, r2c1, r2c2, r2c3, r2c4, r3c1, r3c2, r3c3, r3c4, r4c1, r4c2, r4c3, r4c4
    global r5c1, r5c2, r5c3, r5c4, r6c1, r6c2, r6c3, r6c4, r7c1, r7c2, r7c3, r7c4, r8c1, r8c2, r8c3, r8c4
    global r9c1, r9c2, r9c3, r9c4, r10c1, r10c2, r10c3, r10c4, r11c1, r11c2, r11c3, r11c4, g1, g2, g3, g4
    
    if r11c1 == 'silver' and r11c2 == 'silver' and r11c3 == 'silver'and r11c4 == 'silver':
        r11c1 = 'blue' 
        current_guess[0] = 2
        g1 = 2
    elif r11c1 != 'silver'and r11c2 == 'silver' and r11c3 == 'silver'and r11c4 == 'silver':
        r11c2 = 'blue'
        current_guess[1] = 2
        g2 = 2
    elif r11c1 != 'silver' and r11c2 != 'silver'and r11c3 == 'silver'and r11c4 == 'silver':
        r11c3 = 'blue'
        current_guess[2] = 2
        g3 = 2
    else:
        r11c4 = 'blue'
        current_guess[3] = 2
        g4 = 2
        #print (current_guess)
        #compare()
        create_guess()     
def compare():
    global answer, current_guess, blacks, whites
    global r10d1, r10d2, r10d3, r10d4, r9d1, r9d2, r9d3, r9d4, r8d1, r8d2, r8d3, r8d4, r7d1, r7d2, r7d3, r7d4
    global r6d1, r6d2, r6d3, r6d4, r5d1, r5d2, r5d3, r5d4, r4d1, r4d2, r4d3, r4d4, r3d1, r3d2, r3d3, r3d4
    global r2d1, r2d2, r2d3, r2d4, r1d1, r1d2, r1d3, r1d4
    global num1, num2, num3, num4, g1, g2, g3, g4

    holda = [num1, num2, num3, num4]
    holdg = [g1, g2, g3, g4]
    
    #print (holdg)
    for x in range (0, 4):
        #print (x)
        if answer[x] == current_guess[x]:
            blacks += 1
            holdg[x] = 0
            holda[x] = 0
            #print ("black goes to " + "The ", x+1 , "number")
        else:
            continue
    for x in range(len(holdg)):
        if holdg[x] in holda and holdg[x] != 0:
            whites += 1
            gindex = holda.index(holdg[x])
            holdg[x] = 0
            holda[gindex] = 0

    #print (blacks, whites)
def correct():
    global blacks
    if blacks == 4:
        return True
        print ('correct')
    
def incorrect():
    global blacks, row_number
    if row_number == 0 and blacks != 4:
        return True
def draw(canvas):
    global answer_color, row_number
    #print (row_number)
    canvas.draw_line(BOARD_START, BOARD_END, BOARD_WIDTH, 'maroon')
    canvas.draw_line(SIDE_LINE_START, SIDE_LINE_END, 2, "white")
    canvas.draw_line(GUESS_LINE_START, GUESS_LINE_END, 2, "white")
    #Draw separated rows between guesses
    rows_drawn = 0
    while rows_drawn < 10:
        canvas.draw_line([first_row_start[0], (first_row_start[1] + row_space*rows_drawn)], 
                         [first_row_end[0] , (first_row_end[1] + row_space*rows_drawn)], 2, 'white' )
        rows_drawn += 1
    
    #Draw Blank Circles
    canvas.draw_circle([row1[0][0], row1[0][1] + (0 * row_space) ], guess_circ_radius, 2, r1c1, r1c1)
    canvas.draw_circle([row1[1][0], row1[1][1] + (0 * row_space) ], guess_circ_radius, 2, r1c2, r1c2)
    canvas.draw_circle([row1[2][0], row1[2][1] + (0 * row_space) ], guess_circ_radius, 2, r1c3, r1c3)
    canvas.draw_circle([row1[3][0], row1[3][1] + (0 * row_space) ], guess_circ_radius, 2, r1c4, r1c4)
   
    canvas.draw_circle([row2[0][0], row2[0][1] + (0 * row_space) ], guess_circ_radius, 2, r2c1, r2c1)
    canvas.draw_circle([row2[1][0], row2[1][1] + (0 * row_space) ], guess_circ_radius, 2, r2c2, r2c2)
    canvas.draw_circle([row2[2][0], row2[2][1] + (0 * row_space) ], guess_circ_radius, 2, r2c3, r2c3)
    canvas.draw_circle([row2[3][0], row2[3][1] + (0 * row_space) ], guess_circ_radius, 2, r2c4, r2c4)
    
    canvas.draw_circle([row3[0][0], row3[0][1] + (0 * row_space) ], guess_circ_radius, 2, r3c1, r3c1)
    canvas.draw_circle([row3[1][0], row3[1][1] + (0 * row_space) ], guess_circ_radius, 2, r3c2, r3c2)
    canvas.draw_circle([row3[2][0], row3[2][1] + (0 * row_space) ], guess_circ_radius, 2, r3c3, r3c3)
    canvas.draw_circle([row3[3][0], row3[3][1] + (0 * row_space) ], guess_circ_radius, 2, r3c4, r3c4)
    
    canvas.draw_circle([row4[0][0], row4[0][1] + (0 * row_space) ], guess_circ_radius, 2, r4c1, r4c1)
    canvas.draw_circle([row4[1][0], row4[1][1] + (0 * row_space) ], guess_circ_radius, 2, r4c2, r4c2)
    canvas.draw_circle([row4[2][0], row4[2][1] + (0 * row_space) ], guess_circ_radius, 2, r4c3, r4c3)
    canvas.draw_circle([row4[3][0], row4[3][1] + (0 * row_space) ], guess_circ_radius, 2, r4c4, r4c4)
        
    canvas.draw_circle([row5[0][0], row5[0][1] + (0 * row_space) ], guess_circ_radius, 2, r5c1, r5c1)
    canvas.draw_circle([row5[1][0], row5[1][1] + (0 * row_space) ], guess_circ_radius, 2, r5c2, r5c2)
    canvas.draw_circle([row5[2][0], row5[2][1] + (0 * row_space) ], guess_circ_radius, 2, r5c3, r5c3)
    canvas.draw_circle([row5[3][0], row5[3][1] + (0 * row_space) ], guess_circ_radius, 2, r5c4, r5c4)   
    
    canvas.draw_circle([row6[0][0], row6[0][1] + (0 * row_space) ], guess_circ_radius, 2, r6c1, r6c1)
    canvas.draw_circle([row6[1][0], row6[1][1] + (0 * row_space) ], guess_circ_radius, 2, r6c2, r6c2)
    canvas.draw_circle([row6[2][0], row6[2][1] + (0 * row_space) ], guess_circ_radius, 2, r6c3, r6c3)
    canvas.draw_circle([row6[3][0], row6[3][1] + (0 * row_space) ], guess_circ_radius, 2, r6c4, r6c4)
    
    canvas.draw_circle([row7[0][0], row7[0][1] + (0 * row_space) ], guess_circ_radius, 2, r7c1, r7c1)
    canvas.draw_circle([row7[1][0], row7[1][1] + (0 * row_space) ], guess_circ_radius, 2, r7c2, r7c2)
    canvas.draw_circle([row7[2][0], row7[2][1] + (0 * row_space) ], guess_circ_radius, 2, r7c3, r7c3)
    canvas.draw_circle([row7[3][0], row7[3][1] + (0 * row_space) ], guess_circ_radius, 2, r7c4, r7c4)
    
    canvas.draw_circle([row8[0][0], row8[0][1] + (0 * row_space) ], guess_circ_radius, 2, r8c1, r8c1)
    canvas.draw_circle([row8[1][0], row8[1][1] + (0 * row_space) ], guess_circ_radius, 2, r8c2, r8c2)
    canvas.draw_circle([row8[2][0], row8[2][1] + (0 * row_space) ], guess_circ_radius, 2, r8c3, r8c3)
    canvas.draw_circle([row8[3][0], row8[3][1] + (0 * row_space) ], guess_circ_radius, 2, r8c4, r8c4)
    
    canvas.draw_circle([row9[0][0], row9[0][1] + (0 * row_space) ], guess_circ_radius, 2, r9c1, r9c1)
    canvas.draw_circle([row9[1][0], row9[1][1] + (0 * row_space) ], guess_circ_radius, 2, r9c2, r9c2)
    canvas.draw_circle([row9[2][0], row9[2][1] + (0 * row_space) ], guess_circ_radius, 2, r9c3, r9c3)
    canvas.draw_circle([row9[3][0], row9[3][1] + (0 * row_space) ], guess_circ_radius, 2, r9c4, r9c4)
    
    canvas.draw_circle([row10[0][0], row10[0][1] + (0 * row_space) ], guess_circ_radius, 2, r10c1, r10c1)
    canvas.draw_circle([row10[1][0], row10[1][1] + (0 * row_space) ], guess_circ_radius, 2, r10c2, r10c2)
    canvas.draw_circle([row10[2][0], row10[2][1] + (0 * row_space) ], guess_circ_radius, 2, r10c3, r10c3)
    canvas.draw_circle([row10[3][0], row10[3][1] + (0 * row_space) ], guess_circ_radius, 2, r10c4, r10c4)
    
    canvas.draw_circle([row11[0][0], row11[0][1] + (0 * row_space) ], guess_circ_radius, 2, r11c1, r11c1)
    canvas.draw_circle([row11[1][0], row11[1][1] + (0 * row_space) ], guess_circ_radius, 2, r11c2, r11c2)
    canvas.draw_circle([row11[2][0], row11[2][1] + (0 * row_space) ], guess_circ_radius, 2, r11c3, r11c3)
    canvas.draw_circle([row11[3][0], row11[3][1] + (0 * row_space) ], guess_circ_radius, 2, r11c4, r11c4)

    #Draw black and white dots
    if WIDTH == 1000:
        left_dotx = WIDTH - ((BOARD_WIDTH) - 105) #395
        right_dotx = WIDTH - ((BOARD_WIDTH) - 70)#430
    elif WIDTH == 500:
        left_dotx = 395
        right_dotx = 430
        
    topdotgap = 700
    bottomdotgap = 730
    
    topdoty = topdotgap - row_space
    bottomdoty = bottomdotgap - row_space
    
    
    canvas.draw_circle((left_dotx,700), ans_circ_radius, 2, r10d1, r10d1)
    canvas.draw_circle((left_dotx,730), ans_circ_radius, 2, r10d2, r10d2)
    canvas.draw_circle((right_dotx,700), ans_circ_radius, 2, r10d3, r10d3)
    canvas.draw_circle((right_dotx,730), ans_circ_radius, 2, r10d4, r10d4)
    
    canvas.draw_circle((left_dotx, topdoty), ans_circ_radius, 2, r9d1, r9d1)
    canvas.draw_circle((left_dotx,bottomdoty), ans_circ_radius, 2, r9d2, r9d2)
    canvas.draw_circle((right_dotx,topdoty), ans_circ_radius, 2, r9d3, r9d3)
    canvas.draw_circle((right_dotx, bottomdoty), ans_circ_radius, 2, r9d4, r9d4)
    
    canvas.draw_circle((left_dotx, bottomdotgap - row_space * 2), ans_circ_radius, 2, r8d1, r8d1)
    canvas.draw_circle((left_dotx,topdotgap - row_space * 2), ans_circ_radius, 2, r8d2, r8d2)
    canvas.draw_circle((right_dotx,bottomdotgap - row_space * 2), ans_circ_radius, 2, r8d3, r8d3)
    canvas.draw_circle((right_dotx, topdotgap - row_space * 2), ans_circ_radius, 2, r8d4, r8d4)
    
    canvas.draw_circle((left_dotx, bottomdotgap - row_space * 3), ans_circ_radius, 2, r7d1, r7d1)
    canvas.draw_circle((left_dotx,topdotgap - row_space * 3), ans_circ_radius, 2, r7d2, r7d2)
    canvas.draw_circle((right_dotx,bottomdotgap - row_space * 3), ans_circ_radius, 2, r7d3, r7d3)
    canvas.draw_circle((right_dotx, topdotgap - row_space * 3), ans_circ_radius, 2, r7d4, r7d4)
    
    canvas.draw_circle((left_dotx, bottomdotgap - row_space * 4), ans_circ_radius, 2, r6d1, r6d1)
    canvas.draw_circle((left_dotx,topdotgap - row_space * 4), ans_circ_radius, 2, r6d2, r6d2)
    canvas.draw_circle((right_dotx,bottomdotgap - row_space * 4), ans_circ_radius, 2, r6d3, r6d3)
    canvas.draw_circle((right_dotx, topdotgap - row_space * 4), ans_circ_radius, 2, r6d4, r6d4)
    
    canvas.draw_circle((left_dotx, bottomdotgap - row_space * 5), ans_circ_radius, 2, r5d1, r5d1)
    canvas.draw_circle((left_dotx,topdotgap - row_space * 5), ans_circ_radius, 2, r5d2, r5d2)
    canvas.draw_circle((right_dotx,bottomdotgap - row_space * 5), ans_circ_radius, 2, r5d3, r5d3)
    canvas.draw_circle((right_dotx, topdotgap - row_space * 5), ans_circ_radius, 2, r5d4, r5d4)
    
    canvas.draw_circle((left_dotx, bottomdotgap - row_space * 6), ans_circ_radius, 2, r4d1, r4d1)
    canvas.draw_circle((left_dotx,topdotgap - row_space * 6), ans_circ_radius, 2, r4d2, r4d2)
    canvas.draw_circle((right_dotx,bottomdotgap - row_space * 6), ans_circ_radius, 2, r4d3, r4d3)
    canvas.draw_circle((right_dotx, topdotgap - row_space * 6), ans_circ_radius, 2, r4d4, r4d4)
    
    canvas.draw_circle((left_dotx, bottomdotgap - row_space * 7), ans_circ_radius, 2, r3d1, r3d1)
    canvas.draw_circle((left_dotx,topdotgap - row_space * 7), ans_circ_radius, 2, r3d2, r3d2)
    canvas.draw_circle((right_dotx,bottomdotgap - row_space * 7), ans_circ_radius, 2, r3d3, r3d3)
    canvas.draw_circle((right_dotx, topdotgap - row_space * 7), ans_circ_radius, 2, r3d4, r3d4)
    
    canvas.draw_circle((left_dotx, bottomdotgap - row_space * 8), ans_circ_radius, 2, r2d1, r2d1)
    canvas.draw_circle((left_dotx,topdotgap - row_space * 8), ans_circ_radius, 2, r2d2, r2d2)
    canvas.draw_circle((right_dotx,bottomdotgap - row_space * 8), ans_circ_radius, 2, r2d3, r2d3)
    canvas.draw_circle((right_dotx, topdotgap - row_space * 8), ans_circ_radius, 2, r2d4, r2d4)
    
    canvas.draw_circle((left_dotx, bottomdotgap - row_space * 9), ans_circ_radius, 2, r1d1, r1d1)
    canvas.draw_circle((left_dotx,topdotgap - row_space * 9), ans_circ_radius, 2, r1d2, r1d2)
    canvas.draw_circle((right_dotx,bottomdotgap - row_space * 9), ans_circ_radius, 2, r1d3, r1d3)
    canvas.draw_circle((right_dotx, topdotgap - row_space * 9), ans_circ_radius, 2, r1d4, r1d4)     
    
    
    if correct():
        row_number = str(row_number)
        canvas.draw_line(BOARD_START, BOARD_END, BOARD_WIDTH, 'maroon')
        canvas.draw_text("YOU DID IT!" , (125, HEIGHT/2 - HEIGHT/4), 45, 'white')
        canvas.draw_text("The Code was: " , (125, HEIGHT/2 - HEIGHT/6), 45, 'white')
        
        
        canvas.draw_text("You got it in " + row_number + " guesses!" , (50, 450), 45, 'white')
        
    if incorrect():
        
        canvas.draw_line(BOARD_START, BOARD_END, BOARD_WIDTH, 'maroon')
        canvas.draw_text(("Incorrect, You did not guess the code.") , (15, HEIGHT/2 - HEIGHT/4), 30, 'white')
        canvas.draw_text(" The code was: ",  (175, HEIGHT/2 - HEIGHT /6), 30, 'white')
        
        canvas.draw_circle([row5[0][0]+ 50, row5[0][1] + (0 * row_space) ], guess_circ_radius + 5, 2, answer_color[0], answer_color[0])
        canvas.draw_circle([row5[1][0]+ 50, row5[1][1] + (0 * row_space) ], guess_circ_radius + 5, 2, answer_color[1], answer_color[1])
        canvas.draw_circle([row5[2][0]+ 50, row5[2][1] + (0 * row_space) ], guess_circ_radius + 5, 2, answer_color[2], answer_color[2])
        canvas.draw_circle([row5[3][0]+ 50, row5[3][1] + (0 * row_space) ], guess_circ_radius + 5, 2, answer_color[3], answer_color[3]) 
        
    
        
frame = simplegui.create_frame("Mastermind" , WIDTH, HEIGHT)
frame.set_canvas_background('maroon')
frame.set_draw_handler(draw)
frame.add_label ("Hello, welcome to mastermind. To begin, press start: ")
frame.add_label ("Once you have entered your guess, push enter to get results")
frame.add_label ("To restart a game, push start again.")
frame.add_button("START", reset, 150)
frame.add_label(" ")
frame.add_button("RED", red, 150)
frame.add_button("ORANGE", orange, 150)
frame.add_button("WHITE", white, 150)
frame.add_button("BLUE", blue, 150)
frame.add_label(" ")
frame.add_button("ENTER", enter, 150)
frame.start()
   


