import cv2
import glob
import os
import re

def load_images_from_folder(folder):
	images = os.listdir(folder)
	images = sorted(images, key=lambda x: (int(re.sub('\D','',x)),x))
	return images

folder = '/media/luis/TOSHIBA EXT/VIAS Y TRANSITO/2_AV_REG_CL_80_SUR/PM/IMG'
images = load_images_from_folder(folder)

# Define the video codec
img_size = (1536,864) # Video resolution
fps  = 10 #Frames per second
fourcc = cv2.VideoWriter_fourcc(*'x264')
video = cv2.VideoWriter('output.avi',fourcc,fps,img_size)

for i in images:
	img = cv2.imread(folder + '/' + i)
	if img is not None:
		video.write(img)

video.release()