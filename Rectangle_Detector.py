import cv2
import numpy as np

def findRectangles(img):
    rectangles = []
    height = img.shape[0]
    width = img.shape[1]
    visited = np.zeros((height, width), dtype=bool)

    #iterate over each pixel in the grayscale image
    for y in range(height):
        for x in range(width):
            
            if not visited[y, x] and img[y, x] > 0: #not visited and not background
                rectangle = explorePixels(img, visited, x, y) #a rectangle detected so go and explore that new filled rectangle
                rectangles.append(rectangle)

    return rectangles

#explore the rectangle starting from given pixel values because a new rectangel is detected
def explorePixels(img, visited, x, y):
    height = img.shape[0]
    width = img.shape[1]
    intensity = img[y, x]
    rectangle = {'x': x, 'y': y, 'w': 0, 'h': 0}

    stack = [(x, y)] #store pixels in stack since suitable use 
    while stack:
        currX, currY = stack.pop() 
        visited[currY, currX] = True


        rectangle['x'] = min(rectangle['x'], currX) #top left corner x val
        rectangle['y'] = min(rectangle['y'], currY) #top left corner y val
        rectangle['w'] = max(rectangle['w'], currX - rectangle['x'] + 1) #width
        rectangle['h'] = max(rectangle['h'], currY - rectangle['y'] + 1) #height 

        #explore neighbor pixels of the current pixel in order to understand if the rectangle continues or is it done or are there any others
        for diffX, diffY in [(1, 0), (-1, 0), (0, 1), (0, -1)]: #neighbors are always between these bounds so add these numbers iteratively
            updateX = currX + diffX
            updateY = currY + diffY
            
            #check if neighbor pixels is in image, unvisited, and have the same intensity bc a full rectangle needs to satisfy these
            if 0 <= updateX < width and 0 <= updateY < height and not visited[updateY, updateX] and img[updateY, updateX] == intensity:
                stack.append((updateX, updateY))
                visited[updateY, updateX] = True #mark the neighbor pixels as visited too
                
    return rectangle

def drawLine(img, rectangles):
    for rectangle in rectangles:
        x, y, w, h = rectangle['x'], rectangle['y'], rectangle['w'], rectangle['h']
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

def locateRectangles(img_path, output_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) 
    rectangles = findRectangles(img)  
    detected = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    drawLine(detected, rectangles)
    cv2.imshow('Rectangles Detected', detected)
    cv2.imwrite(output_path, detected)
    cv2.waitKey(0)


input_img_path = 'image.png'
output_img_path = 'generated_image.png'
locateRectangles(input_img_path, output_img_path)  
