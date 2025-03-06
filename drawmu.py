#import the cmpt120image module
import pyhelperfunctions as a

#check if the photo has white in it
def iswhitecolour(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    if r < 255 and g < 255 and b < 255:
        return False
    else:
        return True

#definition the recolour function
#recolour good copy
def recolour(img, colour):
    HEIGHT = len(img)
    WIDTH = len(img[0])
    photo = a.getBlackImage(HEIGHT, WIDTH)
    for row in range(HEIGHT):
        for col in range(WIDTH):
            pixelinsideloop = img[row][col]
            if iswhitecolour(pixelinsideloop)== False:
                photo[row][col] = colour
            else:
                photo[row][col] = [255,255,255]
    return(photo)



#mirror good copy
appleimg = a.getImage("images/apples.png")
def mirror(img):
    HEIGHT = len(img)
    WIDTH = len(img[0])
    blankphoto = a.getBlackImage(HEIGHT,WIDTH)
    for row in range(HEIGHT):
        for col in range(WIDTH):
            blankphoto[row][col]= img[row][-col-1]
    return(blankphoto)


#minify good copy
def minify(img):
    HEIGHT = len(img)
    WIDTH = len(img[0])
    emptyphoto = a.getBlackImage(HEIGHT//2,WIDTH//2)
    for row in range(0,HEIGHT,2):
        for col in range(0,WIDTH,2):
            p1 = img[row][col]
            p2 = img[row][col+1]
            p3 = img[row+1][col]
            p4 = img[row+1][col+1]
            averagered = (p1[0] + p2[0] + p3[0] + p4[0]) //4
            averageblue = (p1[1] + p2[1] + p3[1] + p4[1]) //4
            averagegreen = (p1[2] + p2[2] + p3[2] + p4[2]) //4
            listcolour = [averagered, averageblue, averagegreen]
            emptyphoto[row//2][col//2] = listcolour
    return emptyphoto



#test recolour
appleimg = a.getImage("images/apples.png")
a.showImage(appleimg)
appleimg = recolour(appleimg, [255, 0, 0])
a.showImage(appleimg)

#test mirror
appleimg = mirror(appleimg)
a.showImage(appleimg)

#test minify
appleimg = minify(appleimg)
a.showImage(appleimg)

















