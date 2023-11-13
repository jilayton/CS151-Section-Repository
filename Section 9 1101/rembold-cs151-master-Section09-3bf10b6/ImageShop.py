
"""
This program is the starter file for the ImageShop application, which
implements the "Load" and "Flip Vertical" buttons.

It is being used here as the base for Problems 1 and 2 of Section 09
"""

from filechooser import choose_input_file
from pgl import GWindow, GImage, GRect
from button import GButton

# Constants

GWINDOW_WIDTH = 900
GWINDOW_HEIGHT = 500
BUTTON_WIDTH = 125
BUTTON_HEIGHT = 20
BUTTON_MARGIN = 10
BUTTON_BACKGROUND = "#CCCCCC"

# Derived constants

BUTTON_AREA_WIDTH = 2 * BUTTON_MARGIN + BUTTON_WIDTH
IMAGE_AREA_WIDTH = GWINDOW_WIDTH - BUTTON_AREA_WIDTH

# The image_shop application

def image_shop():
    def add_button(label, action):
        """
        Adds a button to the region on the left side of the window
        label is the text that will be displayed on the button and
        action is the callback function that will be run when the
        button is clicked.
        """
        x = BUTTON_MARGIN
        y = gw.next_button_y
        button = GButton(label, action)
        button.set_size(BUTTON_WIDTH, BUTTON_HEIGHT)
        gw.add(button, x, y)
        gw.next_button_y += BUTTON_HEIGHT + BUTTON_MARGIN

    def set_image(image):
        """
        Sets image as the current image after removing the old one.
        """
        if gw.current_image is not None:
            gw.remove(gw.current_image)
        gw.current_image = image
        x = BUTTON_AREA_WIDTH + (IMAGE_AREA_WIDTH - image.get_width()) / 2
        y = (gw.get_height() - image.get_height()) / 2
        gw.add(image, x, y)

    def load_button_action():
        """Callback function for the Load button"""
        filename = choose_input_file()
        if filename != "":
            set_image(GImage(filename))

    def flip_vertical_action():
        """Callback function for the Flip Vertical button"""
        if gw.current_image is not None:
            set_image(flip_vertical(gw.current_image))
            
    def red_eye_correction_action():
        """Callback function for the Red Eye Correction button"""
        if gw.current_image is not None:
            set_image(red_eye_correction(gw.current_image))

    def double_image_action():
        """Callback function for the Double Image button"""
        if gw.current_image is not None:
            set_image(double_image(gw.current_image))
        
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    button_area = GRect(0, 0, BUTTON_AREA_WIDTH, GWINDOW_HEIGHT)    
    button_area.set_filled(True)
    button_area.set_color(BUTTON_BACKGROUND)
    gw.add(button_area)
    gw.next_button_y = BUTTON_MARGIN
    gw.current_image = None
    add_button("Load", load_button_action)
    add_button("Flip Vertical", flip_vertical_action)
    add_button("Red Eye Correction", red_eye_correction_action)
    add_button("Double Image", double_image_action)

# Creates a new GImage from the original one by flipping it vertically.

def flip_vertical(image):
    array = image.get_pixel_array()
    return GImage(array[::-1])

def red_eye_correction(image):
    array = image.get_pixel_array()
    for i in range(len(array)):
        for j in range(len(array[i])):
            current_pixel = array[i][j]
            pix_red = image.get_red(current_pixel)
            pix_green = image.get_green(current_pixel)
            pix_blue = image.get_blue(current_pixel)
            max_gb = 0
            new_red = 0
            new_pixel = 0
            if pix_red > 2*pix_green and pix_red > 2*pix_blue:
                if pix_green >= pix_blue:
                    max_gb = pix_green
                else:
                    max_gb = pix_blue
                new_red = max_gb
                new_pixel = image.create_rgb_pixel(new_red, pix_green, pix_blue)
                array[i][j] = new_pixel
    return GImage(array)        

def double_image(image):
    array = image.get_pixel_array()
    array_h = len(array)
    array_w = len(array[0])
    #new_array = list( (2 * array_h) * f"{list((2 * array_w) * ' ')}" )
    new_array = [[0 for i in range(array_w*2)] for j in range(array_h*2)]
    for i in range(len(array)):
        for j in range(len(array[i])):
            og_current_pixel = array[i][j]
            new_i = i*2
            new_j = j*2
            new_array[new_i][new_j] = og_current_pixel
            new_array[new_i][new_j+1] = og_current_pixel
            new_array[new_i+1][new_j] = og_current_pixel
            new_array[new_i+1][new_j+1] = og_current_pixel
    return GImage(new_array) 
            
                    

                    
    
                
                
    

# Startup code

if __name__ == "__main__":
    image_shop()
