''' Graphics functions for Image Transformations project

    You can create your own versions of these functions and give
    them different names (in your own file), but DO NOT CHANGE THIS FILE.

    Functions include:
    - draw_button: draw and return a button
    - wait_for_button: wait until the user clicks the button, then return
    - normalize: Transform pixel value according to a range given by minimum and maximum value, then return it

    
    See the specific documentation for each function.

    Authors: Suzanne Rivoire and Gurman Gill '''

from graphics import *






def draw_button(win, txtCenter, txt, chosen):
    ''' 
    Draw a button with text, and return the button (as a Rectangle).
    Parameters:
    * win = window to draw the button in
    * txtCenter = coordinates of button center (as a point)
    * txt = text to draw in button
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