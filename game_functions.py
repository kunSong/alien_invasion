#coding=utf-8
import sys
import pygame

def check_event_keydown(event, ship):
	"""重构代码，当keydown，设置标志位位true，更改飞船位置"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
		
def check_event_keyup(event, ship):
	"""重构代码，当keyup，设置标志位位false，停止更改飞船位置"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_event(ship):
	"""监听键盘和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("Thank you for playing!")
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_event_keydown(event, ship)
		elif event.type == pygame.KEYUP:
			check_event_keyup(event, ship)
				
def update_screen(ai_settings, screen, ship):
	"""屏幕填充颜色"""
	screen.fill(ai_settings.bg_color)
	"""更新飞船移动当前位置"""
	ship.update()
	"""screen绘制飞船"""
	ship.blitme()
	"""
	每次循环执行，创建空屏幕，删除旧屏幕，
	使最新的元素和元素状态绘画在屏幕上，
	以此来展现元素位置的移动和变化
	"""
	pygame.display.flip()
