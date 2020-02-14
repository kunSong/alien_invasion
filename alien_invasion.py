#coding=utf-8
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	"""初始化背景，设置正常工作"""
	pygame.init()
	"""重构代码，将屏幕设置重构到settings模块中"""
	ai_settings = Settings()
	"""
	screen是一个surface
	surface是屏幕一部分用于显示元素，每个元素都是一个surface
	display.set_mode用于设置窗口大小，实参是元组
	"""
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	"""在循环前实例化对象，以免重复创建"""
	ship = Ship(screen)
	"""设置窗口标题"""
	pygame.display.set_caption("Alien Invasion")
	
	"""进入while循环后一直处于循环执行状态"""
	while True:
		"""监听鼠标和键盘事件，重构代码到game_functions模块中"""
		gf.check_event(ship)
		"""更新屏幕元素"""
		gf.update_screen(ai_settings, screen, ship)
		
run_game()
