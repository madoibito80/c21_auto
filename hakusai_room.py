# coding: utf-8

import os
import datetime
import time
import sys
import pyautogui
import capture

def moveSafePos():
	
	deg = capture.getDirection()
	while(deg < 130 or deg > 140):
		if deg < 130:
			mouse_pos = pyautogui.position()
			pyautogui.moveTo(mouse_pos[0] + 50, mouse_pos[1])
		if deg > 140:
			mouse_pos = pyautogui.position()
			pyautogui.moveTo(mouse_pos[0] - 50, mouse_pos[1])

		deg = capture.getDirection()
		
	for i in range(2):
		pyautogui.keyDown('s')
		pyautogui.keyUp('s')
		pyautogui.keyDown('s')
		time.sleep(0.4)
		pyautogui.keyUp('s')


def getHakusaiRemainingTime():
	log_dir = "C:\\CyberStep\\C21\\chat"
	log_list = os.listdir(log_dir)
	log_list.sort()
	log_list.reverse()
	log_path = log_list[0]

	f = open(log_dir+"\\"+log_path,"r")

	for line in f:
		line = line.split("\t")
		if line[2] == "[INFO]" and "ハクサイガーを撃破した！" in line[3] :
			last_time = line[0] + " " + line[1]

	f.close()

	last_time = datetime.datetime.strptime(last_time,'%Y-%m-%d %H:%M:%S')
	interval_time = datetime.datetime.strptime("20:21",'%M:%S')

	now_time = datetime.datetime.today()
	rem_time = interval_time - (now_time - last_time)
	rem_time = rem_time.strftime('%M:%S')

	return rem_time



def countHakusai():
	log_dir = "C:\\CyberStep\\C21\\chat"
	log_list = os.listdir(log_dir)

	c = 0
	
	for log_path in log_list:
		f = open(log_dir+"\\"+log_path,"r")

		for line in f:
			line = line.split("\t")
			if line[2] == "[INFO]" and "ハクサイガーを撃破した！" in line[3] :
				c = c + 1

		f.close()

	return c




if __name__ == '__main__':
	count = countHakusai()
	print("これまでの撃破数: " + str(count) + "体")


	print("再沸きまでの時間")

	while(1):
		rem_time = getHakusaiRemainingTime()
		sys.stdout.write('\r' + rem_time)
		sys.stdout.flush()
		time.sleep(1)