#coding: utf8
from graphics_teclas_simultaneas import *
import time
import random
import math 
import datetime
janela = 1
win = GraphWin("test", 1280*janela,960*janela)
win.setCoords(0, 960, 1280, 0)
win.setBackground("silver")
win.ligar_Buffer()
import pygame 
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("musicas/10.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(10)

def menu_musica():
	global music
	escolha = Entry(Point(880,784),"10")
	escolha.draw(win)

	win.getMouse()
	musica = escolha.getText()

	if musica == "":
		musica = 14
	pygame.mixer.music.stop()
	pygame.mixer.music.load("musicas/"+str(musica)+".mp3")
	pygame.mixer.music.set_volume(0.3)
	pygame.mixer.music.play(10)
	escolha.undraw()
	music = False

#############
music = False
def menu():
	menu_fundo = Image(Point(640,480),"menuprincipal.png")
	menu_fundo.draw(win)
	xx = win.checkKey_Buffer()
	win.update()

	while "Return" not in xx:
		xx = win.checkKey_Buffer()
		win.update()
		
		if "c" in xx:
			creditos()
		if "s" in xx:
			win.close()
		if "t" in xx:
			win.close()
		if "n" in x:
			fundo_musicas = Image(Point(640,480),"menumusicas.png")
			fundo_musicas.draw(win)
			menu_musica()
			fundo_musicas.undraw()
	if music:
		pygame.mixer.music.stop()
		pygame.mixer.music.load("musicas/14.mp3")
		pygame.mixer.music.set_volume(0.3)
		pygame.mixer.music.play(10)
		menu_fundo.undraw()

def pause_game(x,pause):
	global time_pause
	global true
	global break_T
	if "p" in x or not pause :
		time_inicial_pause = datetime.datetime.now()
		x = win.checkKey_Buffer()
		win.update()
		pause_fundo = Image(Point(640,480),"pause_frame.png")
		pause_fundo.draw(win)
		pause = True

		
	
		while pause :
			x = win.checkKey_Buffer()
			win.update()
			if "c" in x:
				pause = False
			if "t" in x:
				true = False
				pause = False
				break_T = False
			if "s" in x:
				win.close()
			


		pause_fundo.undraw()
		time_final_pause = datetime.datetime.now()
		time_delta_pause = time_final_pause - time_inicial_pause 
		time_pause = time_pause + time_delta_pause
		


def marchas(Ve):
	M=1
	global G
	if Ve < 3:
		M = 2
		G = 1
	elif Ve < 7:
		M = 2.5
		G = 2
	elif Ve < 10:
		M = 2
		G = 3
	elif Ve < 13:
		M = 1.5
		G = 4
	elif Ve < 16:
		M = 1
		G = 5
	elif Ve < 20:
		M = 0.4
		G = 6
	
	return M

def control(x,Xcar):
	A = 0
	
	global car
	if 'Left' in x and Xcar > 450:
		car.move(-10,0)
		
	if 'Right' in x and Xcar < 825:
		car.move(10,0)
		
	if 'Up' not in x and V > 0 :
		A = -0.2
	if 'Down' not in x and V < 0 :
		A = 0.2
	if 'Up' in x:
		A = 0.6
	if "Down" in x:
		A = -1
	return A


def atrito(V,X):
	if (X < 470 or X >805) and V > 0:
		V = V-0.7
	return V





def gear(V,G,G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G11,G12,G13,G14,G15):
	q = (V/G)*10.0
	
	if q > 3:
		G1.setFill('red')
	else:
		G1.setFill('green')
	if q > 6:
		G2.setFill('red')
	else:
		G2.setFill('green')
	if q > 9:
		G3.setFill('red')
	else:
		G3.setFill('green')
	if q > 12:
		G4.setFill('red')
	else:
		G4.setFill('green')
	if q > 15:
		G5.setFill('red')
	else:
		G5.setFill('green')
	if q > 18:
		G6.setFill('red')
	else:
		G6.setFill('green')
	if q > 21:
		G7.setFill('red')
	else:
		G7.setFill('green')
	if q > 24:
		G8.setFill('red')
	else:
		G8.setFill('green')
	if q > 27:
		G9.setFill('red')
	else:
		G9.setFill('green')
	if q > 29:
		G10.setFill('red')
	else:
		G10.setFill('green')
	if q > 30:
		G11.setFill('red')
	else:
		G11.setFill('green')
	if q > 31:
		G12.setFill('red')
	else:
		G12.setFill('green')
	if q > 32:
		G13.setFill('red')
	else:
		G13.setFill('green')		
	if q > 33:
		G14.setFill('red')
	else:
		G14.setFill('green')
	if q > 34:
		G15.setFill('red')
	else:
		G15.setFill('green')



def colisao(car,Xcar,Ycar,enia,Xia,Yia):
	global limiteL
	global limiteR

	
	if (Ycar < Yia):
		Ycol = Yia-Ycar
		if (Ycol < 500)and(Ycol):
			if (Xcar <= Xia):
				Xcol = Xia-Xcar
				if (Xcol <= 130):
					car.move(-10,0)
					enia.move(15,0)
			if (Xcar > Xia):
				Xcol = Xcar-Xia
				if(Xcol <= 130):
					car.move(10,0)
					enia.move(-15,0)

	if (Ycar > Yia):
		Ycol = Ycar-Yia
		if (Ycol < 500):
			if (Xcar <= Xia):
				Xcol = Xia-Xcar
				if (Xcol <= 130):
					car.move(-10,0)
					enia.move(15,0)
			if (Xcar > Xia):
				Xcol = Xcar-Xia
				if(Xcol <= 130):
					car.move(10,0)
					enia.move(-15,0)
	
	

	if Xia < 450:
		limiteL += 3
	if limiteL > 10:
		limiteL = 10
	if limiteL > 0:
		enia.move(13,0)
		limiteL -= 1
	if Xia < 440:
		enia.move(7,0)

	if Xia > 820:
		limiteR += 3
	if limiteR > 10:
		limiteR = 10
	if limiteR > 0:
		enia.move(-13,0)
		limiteR -= 1
	if Xia > 800:
		enia.move(-7,0)







#####IA###IA###IA##IA###IA######################################################################
def marchasia(Via):
	Mia=1
	global Gia
	if Via < 3:
		Mia = 4
		Gia = 1
	elif Via < 7:
		Mia = 4
		Gia = 2
	elif Via < 10:
		Mia = 3
		Gia = 3
	elif Via < 13:
		Mia = 2.5
		Gia = 4
	elif Via < 16:
		Mia = 1
		Gia = 5
	elif Via < 20:
		Mia = 0.4
		Gia = 6

	return Mia




def controlia(enia,V,Via):
	Aia = 0
	Ycar = car.getAnchor().getY()
	Xcar = car.getAnchor().getX()
	Xia = enia.getAnchor().getX()
	Yia = enia.getAnchor().getY()

	
	if Yia > Ycar+130 and Yia < Ycar+250:
		if  Xia > Xcar and Xia < Xcar+100:
			if Xia > 840:
				enia.move(-10,0)
			else:
				enia.move(10,0)
		elif Xia <= Xcar and Xia > Xcar-100:
			if Xia < 425:
				enia.move(10,0)
			else:
				enia.move(-10,0)
	
	
	xia = random.randint(1,10)
	if xia == 1:
		xia = ['']
	else:
		xia = ['Up']
	

	if 'Up' in xia:
		Aia = 0.6
	
	Mia = marchasia(Via)
	
	if 'Up' in xia and Gia == 6:
		numia = random.randint(10,11)
		numia = numia/10
	else:
		numia = 0

	Via = Via + Aia*Mia - numia
	Via = atrito(Via,Xia)
	Via = abs(Via)
	if Via > 20:
		Via = 20
	if Via < -15:
		Via = -15

	enia.move(0,-Via+V )
	
	return Via

		
		
def vitoria(road,enia,car):
	 
	if road.getAnchor().getY() > 13950 and enia.getAnchor().getY() > car.getAnchor().getY():
		wintext = Image(Point(640,400),"vitoria.png")
		wintext2 = Image(Point(640,400),"espaco2.png")
		piscar(wintext, wintext2)
		
	elif road.getAnchor().getY() > 13950 and enia.getAnchor().getY() < car.getAnchor().getY():
		wintext = Image(Point(640,400),"derrota.png")
		wintext2 = Image(Point(640,400),"espaco2.png")
		piscar(wintext, wintext2)
	
		










def piscar(text1, text2):
	seletor = 0
	text2.draw(win)
	timex = datetime.datetime.now()
	xx = win.checkKey_Buffer()
	win.update()
	while ("space" not in xx):
	
		xx = win.checkKey_Buffer()
		win.update()
		timex2 = datetime.datetime.now()
		timeh = int(abs((timex2.microsecond - timex.microsecond)/100000))
	
		if (timeh == 5):
			timeh += 1
			if(seletor == 0):
				text1.draw(win)
				text2.undraw()
				seletor = 1
		
			else:
				text2.draw(win)
				text1.undraw()
				seletor = 0
			timex = datetime.datetime.now()	
				
		if 'Escape' in xx and 'Control_L' in xx:
			win.close()	
	if seletor == 0:
		text2.undraw()
	else:
		text1.undraw()
		
		
		
		
		
		
		
		

####################################_PRESS_SPACE_####################################


def inicial():
	winstart = Image(Point(640,480),"start.png")
	winstart.draw(win)
	press_space1 = Image(Point(640,910),"espaco1.png")
	press_space2 = Image(Point(640,910),"espaco2.png")
	
	piscar(press_space1, press_space2)
	
	winstart.undraw()
	press_space1.undraw()
	

def creditos():
	v=25
	pygame.mixer.music.load("musicas/03.mp3")
	pygame.mixer.music.set_volume(0.3)
	pygame.mixer.music.play(10)
	fundo = Image(Point(640,480),"creditos.png")
	fundo.draw(win)
	letras = Image(Point(640,2300),"creditos2.png")
	letras.draw(win)
	penna1 = Image(Point(230,700),"penna1.png")
	penna1.draw(win)
	cleo1 = Image(Point(1030,700),"cleo1.png")
	cleo1.draw(win)
	cleo2 = Image(Point(1030,700),"cleo2.png")
	penna2 = Image(Point(230,700),"penna2.png")
	seletor = False
	
	timex = datetime.datetime.now()
	xx = win.checkKey_Buffer()
	win.update()

	true_c = True
	while true_c:
	
		xx = win.checkKey_Buffer()
		win.update()
		if 'r' in xx:
			true_c = False
		if seletor:

			cleo2.undraw()
			penna2.undraw()
			cleo1.draw(win)
			penna1.draw(win)

			seletor = 0
		
		else:

			cleo1.undraw()
			penna1.undraw()
			penna2.draw(win)
			cleo2.draw(win)
			
			seletor = 1
		
		letras.move(0,-v)
				
		if 'Escape' in xx and 'Control_L' in xx:
			win.close()
		time.sleep(0.4)
		
	if seletor == 0:
		cleo1.undraw()
		penna1.undraw()
	else:
		cleo2.undraw()
		penna2.undraw()
	fundo.undraw()
	letras.undraw()
	pygame.mixer.music.stop()







#__________________________________________________________________________
def MakeGear():
	G1 = Rectangle(Point(1230,920),Point(1245,930))
	G1.draw(win)
	G1.setFill('green')
	G2 = Rectangle(Point(1230,910),Point(1245,920))
	G2.draw(win)
	G2.setFill('green')
	G3 = Rectangle(Point(1230,900),Point(1245,910))
	G3.draw(win)
	G3.setFill('green')
	G4 = Rectangle(Point(1230,890),Point(1245,900))
	G4.draw(win)
	G4.setFill('green')
	G5 = Rectangle(Point(1230,880),Point(1245,890))
	G5.draw(win)
	G5.setFill('green')
	G6 = Rectangle(Point(1230,870),Point(1245,880))
	G6.draw(win)
	G6.setFill('green')
	G7 = Rectangle(Point(1230,860),Point(1245,870))
	G7.draw(win)
	G7.setFill('green')
	G8 = Rectangle(Point(1230,850),Point(1245,860))
	G8.draw(win)
	G8.setFill('green')
	G9 = Rectangle(Point(1230,840),Point(1245,850))
	G9.draw(win)
	G9.setFill('green')
	G10 = Rectangle(Point(1230,830),Point(1245,840))
	G10.draw(win)
	G10.setFill('green')
	G11 = Rectangle(Point(1230,820),Point(1245,830))
	G11.draw(win)
	G11.setFill('green')
	G12 = Rectangle(Point(1230,810),Point(1245,820))
	G12.draw(win)
	G12.setFill('green')
	G13 = Rectangle(Point(1230,800),Point(1245,810))
	G13.draw(win)
	G13.setFill('green')
	G14 = Rectangle(Point(1230,790),Point(1245,800))
	G14.draw(win)
	G14.setFill('green')
	G15 = Rectangle(Point(1230,780),Point(1245,790))
	G15.draw(win)
	G15.setFill('green')
	return G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G11,G12,G13,G14,G15




def obstaculos(win):
	num_obstaculos = 1
	obstaculos_lista = []
	while num_obstaculos*1500 < 99000 :
		posicaoX_obstaculo = random.randint(430,850)
		posicaoY_obstaculo = random.randint(-500,500)- num_obstaculos*1500
		if (posicaoY_obstaculo < -27800 or posicaoY_obstaculo > -28200 ) or (posicaoY_obstaculo < 55800 or posicaoY_obstaculo > 56200) or (posicaoY_obstaculo < 83800 or posicaoY_obstaculo > 84200):
			obstaculo = Image(Point(posicaoX_obstaculo,posicaoY_obstaculo),"oleo.png")
			obstaculo.draw(win)
			obstaculos_lista.append(obstaculo)
			num_obstaculos += 1
	return obstaculos_lista
	
	
	
def move_obstaculos(V,Xcar,Ycar, obstaculos_lista):
	for elem in obstaculos_lista:
		Yelem = elem.getAnchor().getY()
		Xelem = elem.getAnchor().getX()
		if (Ycar < Yelem):
			Ycol = Yelem-Ycar
			if (Ycol < 300):
				if (Xcar <= Xelem):
					Xcol = Xelem-Xcar
					if (Xcol <= 90):
						V = V*0.85
				if (Xcar > Xelem):
					Xcol = Xcar-Xelem
					if(Xcol <= 90):
						V = V*0.85

		if (Ycar > Yelem):
			Ycol = Ycar-Yelem
			if (Ycol < 300):
				if (Xcar <= Xelem):
					Xcol = Xelem-Xcar
					if (Xcol <= 90):
						V = V*0.85
				if (Xcar > Xelem):
					Xcol = Xcar-Xelem
					if(Xcol <= 90):
						V = V*0.85
		elem.move(0,V)
	return V



def move_obstaculos_enia(V,Xia,Yia,enia, obstaculos_lista):
	for elem in obstaculos_lista:
		Yelem = elem.getAnchor().getY()
		Xelem = elem.getAnchor().getX()
		if (Yia < Yelem):
			Ycol = Yelem-Yia
			if (Ycol < 300):
				if (Xia <= Xelem):
					Xcol = Xelem-Xia
					if (Xcol <= 90):
						V = V*0.85
				if (Xia > Xelem):
					Xcol = Xia-Xelem
					if(Xcol <= 90):
						V = V*0.85

		if (Yia > Yelem):
			Ycol = Yia-Yelem
			if (Ycol < 300):
				if (Xia <= Xelem):
					Xcol = Xelem-Xia
					if (Xcol <= 90):
						V = V*0.85
				if (Xia > Xelem):
					Xcol = Xia-Xelem
					if(Xcol <= 90):
						V = V*0.85

		if (Yelem < Yia):
			Ycol = Yia-Yelem
			if (Ycol < 500)and(Ycol):
				if (Xelem <= Xia):
					Xcol = Xia-Xelem
					if (Xcol <= 130):
						enia.move(15,0)
				if (Xelem > Xia):
					Xcol = Xelem-Xia
					if(Xcol <= 130):
						enia.move(-15,0)
		if (Yelem > Yia):
			Ycol = Yelem-Yia
			if (Ycol < 500):
				if (Xelem <= Xia):
					Xcol = Xia-Xelem
					if (Xcol <= 130):
						enia.move(15,0)
				if (Xelem > Xia):
					Xcol = Xelem-Xia
					if(Xcol <= 130):
						enia.move(-15,0)




cronostart = 0
#######################GAME#######################GAME#######################
x = win.checkKey_Buffer()
win.update()


preto = Image(Point(640,480),"transicao.png")
furg = Image(Point(640,480),"furg.png")
c3 = Image(Point(640,480),"c3.png")
preto.draw(win)
time.sleep(0.5)
furg.draw(win)

time.sleep(0.5)
furg.undraw()

time.sleep(0.5)
c3.draw(win)

time.sleep(0.5)
c3.undraw()
time.sleep(0.5)
preto.undraw()



while True:
	############################################

	############################################
	inicial()
	win.update()
	menu()

	#######################_INICIO_#######################

	road = Image(Point(640,-13040),"road.png")
	road.draw(win)
	obstaculos_lista = obstaculos(win)
	background = Image(Point(640,road.getAnchor().getY()-14480),"background.png")
	background.draw(win)
	car = Image(Point(510,700),"interno.png")

	car.draw(win)
	#ia
	enia = Image(Point(770,700),"noivadomar.png")
	
	enia.draw(win)
	guarita = Image(Point(640,road.getAnchor().getY()+13565),"guarita.png")
	guarita.draw(win)
	nitro = Image(Point(1200,860),"nitro.png")
	nitro.draw(win)
	NN = 5
	nitro_num = Text(Point(1160,880),str(NN)+"x")
	nitro_num.setTextColor("white")
	nitro_num.setSize(18)
	nitro_num.draw(win)
	##############CRIACAO#DE#VARIAVEIS######################
	V=0
	N = 1

	G = 0
	nitro = True
	nitrotime = 0
	Via = 0
	limiteL = 0
	limiteR = 0
	minutes = 0
	laps = 1

	vel = Text(Point(1150,915),str(V*5)+" Km/h")
	vel.setTextColor("white")
	vel.setSize(25)
	vel.draw(win)

	speedia  =  Via
	rel =  Rectangle(Point(580,12),Point(700,47))
	rel.setFill("black")
	rel.draw(win)
	ti = "00:00"
	crono = Text(Point(640,30),str(ti))
	crono.setStyle("bold")
	crono.setSize(25)
	crono.setTextColor("black")
	crono.setOutline("white")
	crono.draw(win)
	laps_text = Text(Point(1195,30),"VOLTAS")
	laps_text.setStyle("bold")
	laps_text.setSize(20)
	laps_text.setTextColor("white")
	laps_text.draw(win)
	laps_text_num = Text(Point(1215,70),str(laps)+"/3")
	laps_text_num.setStyle("bold")
	laps_text_num.setSize(36)
	laps_text_num.setTextColor("white")
	laps_text_num.draw(win)
	

	G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G11,G12,G13,G14,G15 = MakeGear()
	#########################################################
	cronostart = 3
	cronostart_text = Text(Point(640,400),str(cronostart))
	cronostart_text.setTextColor("yellow")
	cronostart_text.setSize(36)
	cronostart_text.setStyle("bold")
	cronostart_text.draw(win)
	time.sleep(1)
	cronostart -= 1
	cronostart_text.setText(str(cronostart))
	time.sleep(1)
	cronostart -= 1
	cronostart_text.setText(str(cronostart))
	time.sleep(1)
	cronostart_text.undraw()
	go = Image(Point(640,400),"go.png")
	go.draw(win)
	
	
	
	
	cronostart_TRUE = True

	tistart = datetime.datetime.now()
	time_pause = tistart - tistart
	road_true = False
	true = True
	pause = True
	break_T = True
	while (laps < 3 or road.getAnchor().getY() < 13950) and break_T:
	


		x = win.checkKey_Buffer()
		win.update()
		Xcar = car.getAnchor().getX()
		Xia = enia.getAnchor().getX()
		Ycar = car.getAnchor().getY()
		Yia = enia.getAnchor().getY()
		

		#controle de velocidade:	
		M = marchas(V)
		A = control(x,Xcar)
		colisao(car,Xcar,Ycar,enia,Xia,Yia)
		if 'Down' in x:
			M = 1
			G = -2

		if 'Up' in x and G == 6:
			num = random.randint(10,11)
			num = num/10
		else:
			num = 0
	

		V = V + A*M - num
		if V > 20:
				V = 20
		if V <= 0:
			V = 0
	
		V = atrito(V, Xcar)


		
		
		########################################################

		if 'x' in x and nitro and NN > 0:
			nitro = False
			nitrotime = datetime.datetime.now()
			NN -= 1
			nitro_num.setText(str(NN)+"x")
		elif not nitro:
			tinow = datetime.datetime.now()
			nitrodelta = tinow - nitrotime

			if nitrodelta.seconds <= 5:
				N = 1.1
			else:
				N = 1
				nitro = True
		V = V*N
		vel.setText(str(int(V*5))+" Km/h")
	
		gear(V,G,G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G11,G12,G13,G14,G15)
		
		


	#########################################################################
		
		Xcar = car.getAnchor().getX()
		Xia = enia.getAnchor().getX()
		Ycar = car.getAnchor().getY()
		Yia = enia.getAnchor().getY()
		
		move_obstaculos_enia(V,Xia,Yia,enia, obstaculos_lista)
		
		V = move_obstaculos(V,Xcar,Ycar, obstaculos_lista)
		
		background.move(0,V)
		road.move(0,V)
		guarita.move(0,V)

		speedia = controlia(enia,V,speedia)
			
		if 'Escape' in x and 'Control_L' in x:
			time.sleep(0.3)
			x = win.checkKey_Buffer()
			win.update()
			break
	
		
		
		
#######################PAUSE########################################

		pause_game(x,pause)
		

#####################################################################
	
		tinow = datetime.datetime.now()
		delta_time = tinow - tistart
		delta_time_play = delta_time - time_pause
		
		if (delta_time_play).seconds > 60:
			minutes = int((delta_time_play).seconds/60)
			tistart = datetime.datetime.now()
		crono.setText(str((minutes)) + ":"+str((delta_time_play).seconds)+":"+str(int((delta_time_play).microseconds/10000)))

		
		if cronostart_TRUE and (tinow-tistart).seconds >= 2:
		
			go.undraw()
			cronostart_TRUE = False
		if background.getAnchor().getY() > 470 and laps <= 3 and true:
			road.move(0,(-28940))
			guarita.move(0,road.getAnchor().getY()+13565- guarita.getAnchor().getY())
			laps = laps + 1
			laps_text_num.setText(str(laps)+"/3")
			true = False
		elif background.getAnchor().getY()> 3000:
			true = True
			background.move(0,(road.getAnchor().getY()-background.getAnchor().getY()-14470))

	vitoria(road,enia,car)
	road.undraw()
	car.undraw()
	enia.undraw()
	guarita.undraw()
	background.undraw()




win.close()

