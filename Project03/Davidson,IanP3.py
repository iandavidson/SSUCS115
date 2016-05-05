'''
Assignment: Project 3
Author: Ian Davidson
Description: Lets user enter name of file(.gif) to be placed in the graphic window. Gives selections of
what should be done to image. After user picks an option, text display turns to processing. Operation is done
to image, shown, then asked what the file should be saved as.
'''
from graphics import*
import sys
import time

string1 = 'a. Invert the colors'
string2 = 'b. Switch the RGB channels'
string3 = 'c. Increase the contrast'
button_string_list = [string1, string2, string3]


def draw_button(win, txtCenter, txt, chosen):
    '''
    Draw a button with text, and return the button (as a Rectangle).
    Parameters:
    * win = window to draw the button in
    * txtCenter = coordinates of button center (as a point)
    * txt = text to draw in button
    * chosen = Boolean for if the button was clicked
    '''
    button = Rectangle(Point(txtCenter.getX() - len(txt) * 5,
                             txtCenter.getY() - 15),
                       Point(txtCenter.getX() + len(txt) * 5,
                             txtCenter.getY() + 15))
    button.setFill('DarkGray')
    button.draw(win)

    if chosen:
        buttontxt = Text(txtCenter, "Processing...")
    else:
        buttontxt = Text(txtCenter, txt)
    buttontxt.setSize(20)
    buttontxt.draw(win)
    return button


def wait_for_button(win, button_list):
    '''
    Waits for the user to click the button

    Parameters: win, the list of buttons (as a rectangle)
    Returns: nothing

    '''
    button_lr = []
    button_ul = []
    # Infinite loop - will break out of it by
    # returning if the user clicks the button
    for i in range(3):
        button_ul.append(button_list[i].getP1()) # button upper left
        button_lr.append(button_list[i].getP2()) # button lower right

    while True:
        mousept = win.getMouse()
        for i in range(3):
            if button_ul[i].getX() < mousept.getX() < button_lr[i].getX() and \
               button_ul[i].getY() < mousept.getY() < button_lr[i].getY():
                return i


def normalize(val, minval, maxval):
    '''

    Parameter val: Input value to normalize
    Parameter minval: Minimum value
    Parameter maxval: Maximum value

    Returns the normalized value after checking for out of bounds error.
    '''
    norm = 255*(val - minval)/(maxval-minval)
    if (norm < 0):
        norm = 0
    elif (norm > 255):
        norm = 255
    return norm


def transform(image, clicked_idx):
    '''
    passes image and function that does transformation
    iterates through each pixel 2d nested for loop. calls transformer function depending on button clicked
    returns new image object
    '''


    for i in range(image.getWidth()):
        for j in range(image.getHeight()):
            rgb = image.getPixel(i,j)
            if clicked_idx == 0:
                rgb = invert_pixel_color(rgb)
            elif clicked_idx == 1:
                rgb = switch_rgb_channels(rgb)
            elif clicked_idx == 2:
                rgb = increase_the_contrast(rgb)
            rgb = color_rgb(rgb[0], rgb[1], rgb[2])
            image.setPixel(i, j, rgb)
    return image

def invert_pixel_color(rgb):
    '''
    parameter: single pixel's color list with values out of 255 for red, green, blue
    function inverts each color value using formula "new_value[i] = (255-rgb[i])
    function returns the new rgb list of colors for the pixel
    '''
    new_pix = rgb
    for i in range(3):
        new_pix[i] = (255- rgb[i])
    return new_pix

def switch_rgb_channels(rgb):
    '''
    parameter: single pixel's color list with values out of 255 for red, green, blue
    function switches values of RGB channels
    function returns the new rgb list of colors for the pixel]
    returns newly modified pixel
    '''
    new_pix = rgb
    new_pix[0] = rgb[2]
    for i in range(2):
        new_pix[i+1] = rgb[i]
    return  new_pix




def increase_the_contrast():
    '''
    parameter: single pixel's color list with valuesout of 255 for red, green, blue.
    function: take a single pixel and increases the contrast
    '''





def main():
    file_name = input("Name of image to be opened: ")
    try:
        img = Image(Point(0,0), file_name)
    except tk.TclError as e:
        print('not valid file/image, quitting program: ', e)
        sys.exit()
    w = img.getWidth()
    h = img.getHeight()
    if h is 0 or w is 0: #checks and sees if picture too high def
        print('not valid file/image, quitting program')
        sys.exit()
    dy = h/2
    dx = w/2
    buttonx = 2*w/3
    buttony = 2*h/3
    buttonxy = Point(buttonx,buttony)
    button2xy = Point(buttonx,buttony + 35)
    button3xy = Point(buttonx,buttony + 35*2)
    button_coor_list = [buttonxy, button2xy, button3xy]
    win = GraphWin("Click to continue...", w, h)
    img.draw(win)
    img.move(dx,dy)
    chosen = False
    click_point = win.getMouse() #waits for first click
    #draw buttons--saves to variables
    buttonlist = []
    for i in range(3):
        button = draw_button(win, button_coor_list[i],button_string_list[i], chosen)
        buttonlist.append(button)
    #check if/which click is inside which button
    clicked_idx = wait_for_button(win, buttonlist)

    chosen = True
    button_trans = draw_button(win, button_coor_list[clicked_idx], button_string_list[clicked_idx], chosen)
    # do transformation based off of iteration in for loop
    if clicked_idx == 2:
            #contrast find mins and maxes

            new_image = transform(img, clicked_idx)
            #dont know how to put new_image in graphics window
    #close window
    #adress for output file
    output_filename = input("Enter a output file, either .jpeg or .gif")
    img.save(output_filename)

    time.sleep(3)
main()
