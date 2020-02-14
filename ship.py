#coding=utf-8
import pygame

class Ship():
	"""飞船类"""
	def __init__(self, screen):
		self.screen = screen
		"""导入飞船照片，最好选用bmp图"""
		self.image = pygame.image.load('images/ship.bmp')
		"""
		获取图片矩形属性值和screen的矩形属性值
		pygame处理元素以矩形等简单图形来处理，这样效率高
		玩家也不会察觉，图片是不规则图形
		"""
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		"""
		centerx,centery,x,y,top,bottom,left,right等
		确定飞船在screen上的水平和垂直位置
		(0,0)原点在左上方，(1200,800)在右下方，移动数值会增加
		"""
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		"""使飞船不断移动的标志位"""
		self.moving_right = False
		self.moving_left = False
		
		"""设置飞行速度"""
		self.ship_speed_factor = 1.5
		"""由于self.rect.centerx属性只能存储整数，利用self.center进行加减"""
		self.center = float(self.rect.centerx)
		
	def update(self):
		"""
		当key_down时，使标志位置true
		不断改变飞船水平位置
		当key_up时，使标志位置false
		不改变飞船位置了
		保证飞船不会飞到界面外面去，左右控制
		"""
		if self.moving_right and \
				self.rect.right < self.screen_rect.right:
			self.center += self.ship_speed_factor
		elif self.moving_left and self.rect.left > 0:
			self.center -= self.ship_speed_factor
			
		"""改变完位置后再存储到self.rect.centerx属性中"""	
		self.rect.centerx = self.center
		print("self.rect.centerx: " + str(self.rect.centerx))
		
	def blitme(self):
		"""绘制飞船"""
		self.screen.blit(self.image, self.rect)
		
