import cv2 as cv
from pathlib import Path
import matplotlib.pyplot as plt

def rgb_splitter(image, save_place):
    B, G, R = cv.split(image)

    Titles =["Original", "Red", "Green", "Blue"]
    images =[cv.cvtColor(image, cv.COLOR_BGR2RGB), cv.cvtColor(R, cv.COLOR_BGR2RGB), cv.cvtColor(G, cv.COLOR_BGR2RGB), cv.cvtColor(B, cv.COLOR_BGR2RGB)]
    count = 4

    fig1 = plt.gcf()

    for i in range(count):
        plt.subplot(2, 2, i + 1)
        plt.title(Titles[i])
        plt.imshow(images[i])
    
    plt.show()

    fig1.savefig(str(save_place), dpi=100)
    
    cv.destroyAllWindows()