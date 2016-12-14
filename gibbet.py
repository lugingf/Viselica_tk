# coding: utf-8

import turtle
import random

x = random.randint(1,100)

print('X =', x)

def gotoxy(x,y):
	'''
	перемещение курсора
	'''
	
	turtle.penup()  #поднять графический карандаш
	turtle.goto(x, y)
	turtle.pendown()  #опустить графический карандаш
	
def draw_line(from_x, from_y, to_x, to_y):
	gotoxy(from_x, from_y)
	turtle.goto(to_x, to_y)
	
def draw_gibbet(step):
	if step == 1:
		draw_line(-160, -100, -160, 80) #вертикальный столб
	elif step== 2:
		draw_line(-160, 80, -40, 80)
	elif step== 3:
		draw_line(-160, 40, -120, 80)
	elif step== 4:
		draw_line(-100, 80, -100, 30)
	elif step== 5:
		gotoxy(-100, -10)
		turtle.circle(20)  #голова
	elif step== 6:
		draw_line(-100, -10, -100, -50) #туловище
	elif step== 7:
		draw_line(-100, -20, -120, -30)  #рука левая
	elif step== 8:
		draw_line(-100, -20, -80, -30)  #рука правая
	elif step== 9:
		draw_line(-100, -50, -120, -60)  # нога левая
	elif step== 10:
		draw_line(-100, -50, -80, -60)  # нога правая
	else:
		pass

def erase():
	turtle.begin_poly()
	turtle.end_poly()
	
turtle.color('blue')
turtle.speed(0)

try_count = 0

while True:	
	'''	answer = turtle.textinput('Играть дальше', 'Y/N')
	if answer == 'N':
		sys.exit()'''
	
	gotoxy(-200, 250)	
	turtle.write('Загадал число от 1 до 100\nПопробуй угадать', font=('Arial', 16, 'normal'))
	
	number = turtle.numinput('Введите число', 'Число')

	
	if number == x:
		gotoxy(150, 250)
		turtle.color('green')
		turtle.write('Вы угадали', font=('Arial', 16, 'normal'))
		break
	elif number == -13:
		break
	else:
		gotoxy(250, 200 - try_count * 20)
		if number < x:
			turtle.write('Надо больше', font=('Arial', 16, 'normal'))
		else:
			turtle.write('Надо меньше', font=('Arial', 16, 'normal'))
		try_count += 1
		draw_gibbet(try_count)
		
		if try_count == 10:
			turtle.color('red')
			gotoxy(-150, 100)
			turtle.write('Вы проиграли', font=('Arial', 16, 'normal'))
			break
	

	
input()