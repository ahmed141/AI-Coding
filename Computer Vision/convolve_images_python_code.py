import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from pylab import *

def compute_convolve2D(image, kernel, output):
  for y in range(image.shape[1]):
    #convolve our y or row record
        if y > image.shape[1] - kernel.shape[1]:
            break
        for x in range(image.shape[0]):
          #convolve our x or column record
          if x > image.shape[0] - kernel.shape[0]:
            break
          try:
            #compute the sum
            output[x, y] = (kernel * image[x: x + kernel.shape[0], y: y + kernel.shape[1]]).sum()
          except:
            break
  return output

Prewitt=np.array([[1, 1, 1],[0, 0, 0],[-1, -1, -1]])
pil_im = np.array(Image.open(img).convert('L'))
print(imshow(pil_im, cmap='gray'))
output_size_height = int((pil_im.shape[0]-Prewitt.shape[0]+2)/1+1)
output_size_widht = int((pil_im.shape[1]-Prewitt.shape[1]+2)/1+1)
output_matrix = np.zeros((output_size_height,output_size_widht))
# Convolve prewitt filter with the image
output_matrix = compute_convolve2D(pil_im,Prewitt,output_matrix)
img_nme = 'result_prewitt_filter.jpg'.format(img)
plt.imsave(img_nme,output_matrix, cmap='gray')
