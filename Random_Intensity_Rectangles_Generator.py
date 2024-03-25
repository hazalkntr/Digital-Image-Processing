# a Python program to generate an image with randomly
# placed filled rectangles. this work is to understand intensity values and opencv library
# also this work may be used for future projects to implement new learnings. 
    
import random
from PIL import Image, ImageDraw

# generate the intensity value between 100 and 255
def generate_random_intensity():
    return random.randint(100, 255)

# generate random rectangle parameters within specified constraints as sizings
def generate_random_rectangle():
    x0 = random.randint(0, 511 - 10)  # x coordinate of top-left corner
    y0 = random.randint(0, 511 - 10)  # y coordinate of top-left corner
    width = random.randint(10, 200)    # width 
    height = random.randint(10, 200)   # height 

    # calculate coordinates of bottom-right corner based on top-left corner and dimensions
    x1 = x0 + width
    y1 = y0 + height

    return x0, y0, x1, y1



# draw a rectangle on the image with a specified intensity
def draw_rectangle(image, intensity, rectangle):
    draw = ImageDraw.Draw(image)
    draw.rectangle(rectangle, fill=intensity)

# generate the image with randomly placed rectangles
def generate_image(num_rectangles):
    image = Image.new("L", (512, 512), color=0) # grayscale mode, 512x512 image, black background

    # generate rectangles sequentially
    for _ in range(num_rectangles):
        intensity = generate_random_intensity()
        rectangle = generate_random_rectangle()
        draw_rectangle(image, intensity, rectangle)

    return image

# main program
if __name__ == "__main__":
    num_rectangles = 5 # number of filled rectangles
    generated_image = generate_image(num_rectangles)
    generated_image.show()
