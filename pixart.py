'''
    This program asks the user if they want to draw a 20 x 20 black and red grid or if they want to 
    import a file a draw pixel art based on the contents of the file. Whatever the user chooses, the 
    program executes depending on it. 

    Heer's repository: https://github.com/HeerKGit/h-first-repository
    Nastassaya's respository: https://github.com/Nastassya1719/NRepository1
    Lamis's repository: https://github.com/lamis6579/turtle.py

    Group 2. Heer, Nastassya, Lamis
'''


import turtle # importing the turtle module.

def get_color(char):

    '''First function: this function uses if statements to return the color based on the character provided. 
    If any input other than the valid ones is given, the program returns None. '''

    if char == '0':
        return 'black'
    elif char == '1':
        return 'white'
    elif char == '2':
        return 'red'
    elif char == '3':
        return 'yellow'
    elif char == '4':
        return 'orange'
    elif char =='5':
        return 'green'
    elif char == '6':
        return 'yellowgreen'
    elif char == '7':
        return 'sienna'
    elif char == '8':
        return 'tan'
    elif char == '9':
        return 'gray'
    elif char == 'A':
        return 'darkgray'
    else:
        return None


# Second function: the function below simply is to draw a colored pixel.
def draw_color_pixel(color_string, turta):


    count = 0 # initialising count to 0 as we will use it in a while loop. 

    turta.begin_fill()
    turta.fillcolor(color_string) # filling in the pixel the color the user chose. 

    while count < 4: # this is just drawing a single pixel.

        turta.forward(20)
        turta.left(90)
        count += 1

    turta.end_fill()


# Third function: this funtion retrieves the color from the get_color function and then passes that value into the draw_color_pixel function and calls it. 
def draw_pixel(color_string, turta):
    color = get_color(color_string) # calling the get_color function and passing the number/letter of the color name and storing it in the color var.
    draw_color_pixel(color, turta) # calling draw_color_pixel with the color retrieved. 


# Fourth function: draws a single row of colored pixels based on the color string provided. 
def draw_line_from_string(color_string, turta):

    for char in color_string: # goes through each character in the color string
        if get_color(char) == None: # checks if passing the character into the get_color function returns None. If it does, False is returned and the program stops. 
            return False # False is returned if the value is None/is incorrect so the program stops drawing the row of pixels. 
        
        char.split() # if False isn't returned then we split the string so we can access each character
        draw_pixel(char, turta) # calling the draw_pixel function to draw a pixel and passing the character. 
        turta.forward(20) # we keep moving forward 20 so that the pixel doesn't draw over itself and actually moves forward to draw the next one. 
    
    return True # true is returned once the process of drawing the row is successful. 
 

"""
The code below is the requirement before we import files to draw the picture. This code would not work
if we want to import files as we do not need a user input for color_strings since we are getting them directly 
from the text file. 

def draw_shape_from_string(turta):

        while True:
            color_string = input('Enter color string: ')
            num_pixels_in_row = len(color_string) # calculating the number of pixels in the row. 
            draw_line_from_string(color_string, turta)
            
            # the following lines of code allow the turtle to move back to the start of each row so it can move on to drawing the next row. 

            turta.left(180)
            turta.forward(num_pixels_in_row * 20) 
            turta.left(90)
            
            turta.forward(20)
            turta.left(90)

"""


# Fifth function: draws a row with the provided color_string and moves back to the start point to draw new row.                
def draw_shape_from_string(color_string, turta):

        num_pixels_in_row = len(color_string) # calculating the number of pixels in the row. 
        draw_line_from_string(color_string, turta)
        
        # the following lines of code allow the turtle to move back to the start of each row so it can move on to drawing the next row. 

        turta.left(180)
        turta.forward(num_pixels_in_row * 20) 
        turta.left(90)
        turta.forward(20)
        turta.left(90)


def draw_grid(turta):
    
    '''
        Fifth function: function for drawing a black and red checker board. 
        The for loop below makes sure that the grid's rows are alternating colors of black and red. It 
        fills all the pixels in the odd number of rows starting with black and ending with red, 
        and even rows as starting with red and ending with black.
    '''

    red_end_black = '20202020202020202020' # variable with the first pixel in the row as red and last pixel as black. 
    black_end_red = '02020202020202020202' # variable with the first pixel in the row as black and last pixel as red. 

    for x in range(20):

        if x % 2 == 0: # creating a for loop and then using the mod operator to check if x is even, so it fills the even rows staring with red and ending with black. 
            draw_line_from_string(red_end_black, turta) 

        else:
            draw_line_from_string(black_end_red, turta) # otherwise it starts with black and ends with red. 

        # the code below is the same code for draw_shape_from_string but since we were asked to use draw_line_from_string I had to write it again. 

        turta.left(180)
        turta.forward(20 * 20) # moves back to the start point so it can start drawing the next row. 
        turta.left(90)

        # the if statement below ensures the the turtle doesn't go to its position to begin a new row after the drawing has been completed. 
        if x < 19:
            turta.forward(20)
            turta.left(90)


def draw_shape_from_file(turta):

    '''
        Last function: this function is to prompt the user for a file input 
        and retrive color_strings from that file and then draw 
        the image based on the color strings.
    '''

    file = input('Enter file path: ') 

    with open(file, 'r') as f:
        for (line) in f: # iterating through each line in the file. 
            color_string = line.strip() # strip function to remove any trailing whitespaces incase there are any. 
            draw_shape_from_string(color_string, turta) # calling the sraw_shape_from_string and passing in each color_string from the file. 
