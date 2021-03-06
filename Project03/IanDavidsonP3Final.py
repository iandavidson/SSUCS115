'''
Assignment: Project 3 Final Code
Author: Ian Davidson
Description: Lets user enter name of file(.gif) to be placed in the graphic window. Gives selections of
what should be done to image. After user picks an option, text display turns to processing. Operation is done
to image, shown, then asked what the name the file should be saved as.
'''
from graphics import*
import sys
import time
import random

string1 = 'a. Invert the colors'
string2 = 'b. Switch the RGB channels'
string3 = 'c. Increase the contrast'
button_string_list = [string1, string2, string3]


def draw_button(win, txtCenter, txt, chosen):
    """
    Draw a button with text, and return the button (as a Rectangle).
    Parameters:
    * win = window to draw the button in
    * txtCenter = coordinates of button center (as a point)
    * txt = text to draw in button
    * chosen = Boolean for if the button was clicked
    """
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
    """
    Waits for the user to click the button
    Parameters: win, the list of buttons (as a rectangle)
    Returns: nothing
    """
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
    """

    Parameter val: Input value to normalize
    Parameter minval: Minimum value
    Parameter maxval: Maximum value

    Returns the normalized value after checking for out of bounds error.
    """
    norm = 255*(val - minval)/(maxval-minval)


    #add in the +25 and -25?
    if (norm < 0):
        norm = 0
    elif (norm > 255):
        norm = 255
    return int(norm)


def transform(image, clicked_idx, min_max):
    """
    passes image and function that does transformation, min_max is a set of tuples used for changing contrast
    iterates through each pixel 2d nested for loop. calls specific transformer function depending on button clicked
    returns new image object
    """
    image.undraw()

    #for switch rgb to work properly the function needs to iterate through the pixels
    if clicked_idx == 1:
        image = switch_rgb_channels(image)

    #iterates through all pixels going col by col from left to right
    for i in range(image.getWidth()):
        for j in range(image.getHeight()):

            rgb = image.getPixel(i,j)

            #invert colors
            if clicked_idx == 0:

                rgb = invert_pixel_color(rgb)

            #for switch rgb to work properly the function needs to iterate through the pixels

            #contrast change
            elif clicked_idx == 2:
                for g in range(3):
                    rgb[g] = normalize(rgb[g], min_max[g][0] + 25, min_max[g][1] - 25 )

            #turn list to color object, set pixel
            rgb = color_rgb(rgb[0], rgb[1], rgb[2])
            image.setPixel(i, j, rgb)

    return image

def switch_rgb_channels(image):
    """
    parameter: image object is passed
    function switches same values of RGB channels for entire picture by iterating through pixels
    returns newly modified image
    """
    #using the values to be randomized
    list = ['red', 'green', 'blue']
    random.shuffle(list)


    for i in range(image.getWidth()):
        for j in range(image.getHeight()):

            rgb = image.getPixel(i,j)
            rgb = color_rgb(rgb[list.index('red')], rgb[list.index('green')], rgb[list.index('blue')])
            image.setPixel(i, j, rgb)

    return image



def invert_pixel_color(rgb):
    """
    parameter: single pixel's color list with values out of 255 for red, green, blue
    function inverts each color value using formula "new_value[i] = (255-rgb[i])
    function returns the new rgb list of colors for the pixel
    """
    new_pix = rgb
    for i in range(3):
        new_pix[i] = (255- rgb[i])
    return new_pix


def find_min_max(image):
    """
    parameter: takes an image
    function: iterates through pixels in an image to find the max and min values of colors rgb
    in image.
    returns tuple with all values in order Red, Green, Blue as lists of min and max values
    """

    max_list = [-1, -1, -1]
    min_list = [256, 256, 256]



    for x in range(image.getWidth()):
        for y in range(image.getHeight()):

            pix_rgb_list = image.getPixel(x, y)
            for i in range(3):

                #checking for max
                if pix_rgb_list[i] >= max_list[i]:
                    max_list[i] = pix_rgb_list[i]

                #cheking for min
                if pix_rgb_list[i] <= min_list[i]:
                    min_list[i] = pix_rgb_list[i]

    return ([min_list[0], max_list[0]], [min_list[1], max_list[1]], [min_list[2], max_list[2]])



def open_file(filename):
    """
    parameter: name of file taken from user
    function: opens image file from current directory, makes image
    object, checks for errors, if any found ends program
    return: the created image object is returned
    """
    try:
        img = Image(Point(0,0), filename)
    except tk.TclError as e:
        print('not valid file/image, quitting program: ', e)
        sys.exit()

    if img.getHeight() is 0 or img.getWidth() is 0: #checks and sees if picture too high def
        print('not valid file/image, quitting program')
        sys.exit()
    return img


def save_file(image):
    """
    parameter: string variable entered by user
    function: saves image file into current directory, checks for errors, if any found ends program
    """
    output_filename = input("Enter name for output file, followed by .gif: ")
    try:
        image.save(output_filename)
    except tk.TclError as e:
        print('error caused: ', e)
        sys.exit()


def main():

    file_name = input("Name of image to be opened: ")

    #function opens file and if catches an error exits
    img = open_file(file_name)



    w = img.getWidth()
    h = img.getHeight()
    dy = img.getHeight()/2
    dx = img.getWidth()/2
    buttonx = 2*w/3
    buttony = 2*h/3
    button_coor_list = [Point(buttonx,buttony), Point(buttonx,buttony + 35), Point(buttonx,buttony + 35*2)]
    win = GraphWin("Click to continue...", w, h)
    img.draw(win)
    img.move(dx,dy)
    chosen = False

    click_point = win.getMouse() #waits for first click


    #draw buttons--saves to variables, then appends to list
    buttonlist = []
    for i in range(3):
        button = draw_button(win, button_coor_list[i],button_string_list[i], chosen)
        buttonlist.append(button)
    #check if/which click is inside which button
    clicked_idx = wait_for_button(win, buttonlist)


    #sets "processing..." to text of clicked button
    chosen = True
    button_trans = draw_button(win, button_coor_list[clicked_idx], button_string_list[clicked_idx], chosen)

    # do transformation based off of iteration in for loop
    min_max = None
    if clicked_idx == 2:
        min_max = find_min_max(img)
            #contrast find mins and maxes

    new_image = transform(img, clicked_idx, min_max)
    new_image.draw(win)


    #waits for a click
    win.getMouse()

    #close window
    win.close()

    #saves file and catches error
    save_file(new_image)

main()