# coding: utf-8

import pyautogui
import time
import hakusai_room
import sys

import capture

def subDashAttack():

	pyautogui.keyDown('f')
	pyautogui.keyUp('f')

	for i in range(15):
		pyautogui.keyDown('s')
		pyautogui.keyUp('s')
		pyautogui.keyDown('s')
		time.sleep(0.4)
		mouse_pos = pyautogui.position()
		pyautogui.mouseDown(mouse_pos[0],mouse_pos[1],button='right')
		pyautogui.mouseUp(mouse_pos[0],mouse_pos[1],button='right')
		pyautogui.keyUp('s')
		time.sleep(0.6)



def hakusaiAttack():

	pyautogui.keyDown('s')
	pyautogui.keyUp('s')
	pyautogui.keyDown('s')
	time.sleep(0.4)
	pyautogui.keyUp('s')
	
	pyautogui.keyDown('f')
	pyautogui.keyUp('f')

	for i in range(2):
		mouse_pos = pyautogui.position()
		pyautogui.mouseDown(mouse_pos[0],mouse_pos[1],button='left')
		time.sleep(14)
		pyautogui.mouseUp(mouse_pos[0],mouse_pos[1],button='left')



	pyautogui.keyDown('f12')
	pyautogui.keyUp('f12')
	for i in range(10):
		pyautogui.keyDown('tab')
		pyautogui.keyUp('tab')
		time.sleep(0.2)

	pyautogui.keyDown('w')
	time.sleep(1)
	pyautogui.keyUp('w')

	pyautogui.keyDown('f12')
	pyautogui.keyUp('f12')
	for i in range(10):
		pyautogui.keyDown('tab')
		pyautogui.keyUp('tab')
		time.sleep(0.2)


	pyautogui.keyDown('s')
	time.sleep(2)
	pyautogui.keyUp('s')








def waitHakusai():

	print("再沸きまでの時間")

	last_hp = capture.getHP()

	while(1):
		rem_time = hakusai_room.getHakusaiRemainingTime()
		sys.stdout.write('\r' + rem_time)
		sys.stdout.flush()
		if rem_time == '00:00':
			hakusaiAttack()

		if capture.getHP() < last_hp and (rem_time[0:1] != '00'):
			mouse_pos = pyautogui.position()
			pyautogui.mouseDown(mouse_pos[0],mouse_pos[1],button='left')
			time.sleep(14)
			pyautogui.mouseUp(mouse_pos[0],mouse_pos[1],button='left')
			
			moveSafePos()

		if capture.getHP() < 50:
			pyautogui.keyDown('f1')
			pyautogui.keyUp('f1')

		last_hp = capture.getHP()

		time.sleep(0.5)

waitHakusai()