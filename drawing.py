'''
    This python file imports all the content of the pixart module and 
    consists of the main function that allows the code to run in order 
    and execute smoothly.
'''


from pixart import * # importing all the functions from the pixart module/file. 


# main function controls in what order the program will be executed. 
def main():
    turta = turtle.Turtle() # assigning the Turtle object to a variable called turta
    turta.up()
    turta.setposition(-250,200) # moving to this position so that our drawings and grid fit in the turtle canvas/window. 
    turta.down()
    turta.speed(0)

    # the while loop below gives the user a choice and acts based upon that choice. If an invalid choice is entered then it will ask the user for another choice. 
    while True:
        user_choice = input('Enter G if you want to draw a 20 x 20 black and red grid, enter F if you want to draw a shape from a file, or enter Q to exit the program: ')

        if user_choice.upper() == 'G':
            draw_grid(turta)
            input() # input statement so that the turtle window does not close immediately. 
            #break
        elif user_choice.upper() == 'F':

            try: # try-except to check if the filepath entered is valid. 
                draw_shape_from_file(turta)
                input()
                break
            
            except:
                print('File path not found. Please enter a valid file path: ')

        elif user_choice.upper() == 'Q':
            turtle.bye() # bye() closes the turtle window. 
            #break 
        
        else:
            print('Invalid choice!')
        

# calling the main function by writing its script. 
if __name__ == '__main__':
    main()