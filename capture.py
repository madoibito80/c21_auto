# coding: utf-8

import win32gui
import PIL
from PIL import Image
from PIL import ImageGrab
import numpy
import math


def captureAll():
	hwnd = win32gui.FindWindow(None,"C21")
	rect = win32gui.GetWindowRect(hwnd)
	left = rect[0] + 3
	top = rect[1] + 26
	size = win32gui.GetClientRect(hwnd)
	cap = [left,top,left+size[2],top+size[3]]
	img = ImageGrab.grab(cap)

	return img

def getHP():
	img = captureAll()
	wc = img.size[0]/2
	hpbar = img.crop((wc-116,21,wc+55,22))
	hpbar = numpy.asarray(hpbar)
	hpbar = 1*(hpbar == numpy.array([40,40,40]))[0,:,0]
	hp = int((hpbar.shape[0] - numpy.sum(hpbar)) / hpbar.shape[0] * 100)
	return hp


def captureRadar():
	img = captureAll()
	(w,h) = img.size
	img = img.crop((w-177,h-249,w-12,h-111))
	return img


def getDirection():
	radar = captureRadar()
	radar = numpy.asarray(radar)
	mask = numpy.zeros(radar.shape)
	color = numpy.array([174,12,10])
	mask[:,:] = color
	radar = numpy.absolute(mask-radar)
	radar = radar[:,:,0] + radar[:,:,1] + radar[:,:,2]
	radar = 1 * (radar < 50)

	hc = radar.shape[0]/2
	wc = radar.shape[1]/2

	for x in range(radar.shape[1]):
		for y in range(radar.shape[0]):
			px = x - wc
			py = y - hc
			if( math.sqrt(px**2+py**2) > 68 )or( math.sqrt(px**2+py**2) < 48 ):
				radar[y,x] = 0

	radar = Image.fromarray(numpy.uint8(radar)*255)
	radar = radar.resize((int(radar.size[0]/2),int(radar.size[1]/2)),resample=PIL.Image.BILINEAR)
	radar = radar.resize((int(radar.size[0]*2),int(radar.size[1]*2)),resample=PIL.Image.BILINEAR)
	radar = numpy.asarray(radar)

	radar = 1 * (radar > 50)

	ax = 0.0
	ay = 0.0
	c = 0
	hc = radar.shape[0]/2
	wc = radar.shape[1]/2

	for x in range(radar.shape[1]):
		for y in range(radar.shape[0]):
			if radar[y,x] == 1:
				c = c + 1
				ax += x - wc
				ay += hc - y

	if c == 0:
		return False

	else:
		ax /= c
		ay /= c

		rad = math.atan2(ay,ax)
		deg = math.degrees(rad)
		return int(deg)





if __name__ == "__main__":
	img = captureAll()
	#img.save("./captureAll.png")

	print("HP: " + str(getHP()) + "%")
	print("N角度: " + str(getDirection()) + "度")


	