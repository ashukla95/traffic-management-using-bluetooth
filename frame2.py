import pygame, sys
from pygame.locals import *



#initialising pygame and setting frame value

pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()



# set up the window
DISPLAYSURF = pygame.display.set_mode((1000, 700), 0, 32)
pygame.display.set_caption('Traffic Regulations using Bluetooth and Messaging')






#Setting color values

white = (255, 255, 255)
red = (255,0,0)
blac = (255,0,0)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)
aqua = (0,255,255)
fuchsia = (255,0,255)
gray = (128,128,128)
maroon = (128,0,0)
navyblue = (0,0,128)
olive  = (128,128,0)
purple = (128,0,128)
silver = (192,192,192)
teal = (0,128,128)
yellow = (255,255,0)


#setting delay counter value and other coundition values
i =0
m = 0

#setting co-ordinates for various figures
x = 50
y = 250
x1 = 50
y1 = 170
x3 = 0
y3 = 200

direction = 'right'




#start of animation
#P
fontObj = pygame.font.Font('freesansbold.ttf', 20)
textSurfaceObj = fontObj.render('P', True, white, silver )
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (500, 350)

#60kmph
fontObj = pygame.font.Font('freesansbold.ttf', 20)
textSurfaceObj1 = fontObj.render('60 KMPH', True, white, black )
textRectObj1 = textSurfaceObj.get_rect()
textRectObj1.center = (375, 40)

#30kmph
fontObj = pygame.font.Font('freesansbold.ttf', 20)
textSurfaceObj2 = fontObj.render('30 KMPH', True, white, black )
textRectObj2 = textSurfaceObj.get_rect()
textRectObj2.center = (820, 225)

#50kmph
fontObj = pygame.font.Font('freesansbold.ttf', 20)
textSurfaceObj3 = fontObj.render('50 KMPH', True, white, black )
textRectObj3 = textSurfaceObj.get_rect()
textRectObj3.center = (750, 425)


#DISPLAYSURF.blit(textSurfaceObj, textRectObj)
#DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
#DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
#DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)





while True: # the main game loop

	while (x1<250 ):
	
		DISPLAYSURF.fill(black)

		# construction of border for road

		pygame.draw.line(DISPLAYSURF,white,[0,160],[250,160],2)
		pygame.draw.line(DISPLAYSURF,white,[0,540],[250,540],2)
		pygame.draw.line(DISPLAYSURF,white,[250,160],[250,0],2)	
		pygame.draw.line(DISPLAYSURF,white,[250,540],[250,700],2)
		pygame.draw.line(DISPLAYSURF,white,[750,160],[750,0],2)	
		pygame.draw.line(DISPLAYSURF,white,[750,540],[750,700],2)
		pygame.draw.line(DISPLAYSURF,white,[750,160],[1000,160],2)
		pygame.draw.line(DISPLAYSURF,white,[750,540],[1000,540],2)
		pygame.draw.rect(DISPLAYSURF,yellow,(0,0,250,160))
		pygame.draw.rect(DISPLAYSURF,yellow,(0,540,250,160))
		pygame.draw.rect(DISPLAYSURF,yellow,(750,0,250,160))
		pygame.draw.rect(DISPLAYSURF,yellow,(750,540,250,160))


		#construction of slant lines for building and foothpath representation 
		#top left corner
		#front slash
		pygame.draw.line(DISPLAYSURF,red,[230,160],[250,140],2)
		pygame.draw.line(DISPLAYSURF,red,[210,160],[250,120],2)
		pygame.draw.line(DISPLAYSURF,red,[190,160],[250,100],2)
		pygame.draw.line(DISPLAYSURF,red,[170,160],[250,80],2)
		pygame.draw.line(DISPLAYSURF,red,[150,160],[250,60],2)
		pygame.draw.line(DISPLAYSURF,red,[130,160],[250,40],2)
		pygame.draw.line(DISPLAYSURF,red,[110,160],[250,20],2)
		pygame.draw.line(DISPLAYSURF,red,[90,160],[250,0],2)
		pygame.draw.line(DISPLAYSURF,red,[70,160],[230,0],2)
		pygame.draw.line(DISPLAYSURF,red,[50,160],[210,0],2)
		pygame.draw.line(DISPLAYSURF,red,[30,160],[190,0],2)
		pygame.draw.line(DISPLAYSURF,red,[10,160],[170,0],2)
		pygame.draw.line(DISPLAYSURF,red,[0,140],[150,0],2)
		pygame.draw.line(DISPLAYSURF,red,[0,120],[130,0],2)
		pygame.draw.line(DISPLAYSURF,red,[0,100],[110,0],2)
		pygame.draw.line(DISPLAYSURF,red,[0,80],[90,0],2)
		pygame.draw.line(DISPLAYSURF,red,[0,60],[70,0],2)
		pygame.draw.line(DISPLAYSURF,red,[0,40],[50,0],2)
		pygame.draw.line(DISPLAYSURF,red,[0,20],[30,0],2)
		pygame.draw.line(DISPLAYSURF,red,[0,0],[10,0],2)

		#back slash
		pygame.draw.line(DISPLAYSURF,red,[0,140],[20,160],2)
		pygame.draw.line(DISPLAYSURF,red,[0,120],[40,160],2)
		pygame.draw.line(DISPLAYSURF,red,[0,100],[60,160],2)
		pygame.draw.line(DISPLAYSURF,red,[0,80],[80,160],2)
		pygame.draw.line(DISPLAYSURF,red,[0,60],[100,160],2)
		pygame.draw.line(DISPLAYSURF,red,[0,40],[120,160],2)
		pygame.draw.line(DISPLAYSURF,red,[0,20],[140,160],2)
		pygame.draw.line(DISPLAYSURF,red,[0,0],[160,160],2)
		pygame.draw.line(DISPLAYSURF,red,[20,0],[180,160],2)
		pygame.draw.line(DISPLAYSURF,red,[40,0],[200,160],2)
		pygame.draw.line(DISPLAYSURF,red,[60,0],[220,160],2)
		pygame.draw.line(DISPLAYSURF,red,[80,0],[240,160],2)
		pygame.draw.line(DISPLAYSURF,red,[100,0],[250,140],2)
		pygame.draw.line(DISPLAYSURF,red,[120,0],[250,120],2)
		pygame.draw.line(DISPLAYSURF,red,[140,0],[250,100],2)
		pygame.draw.line(DISPLAYSURF,red,[160,0],[250,80],2)
		pygame.draw.line(DISPLAYSURF,red,[180,0],[250,60],2)
		pygame.draw.line(DISPLAYSURF,red,[200,0],[250,40],2)
		pygame.draw.line(DISPLAYSURF,red,[220,0],[250,20],2)
		pygame.draw.line(DISPLAYSURF,red,[240,0],[250,0],2)
		#bottom-right corner construction
		#front slash
		pygame.draw.line(DISPLAYSURF,red,[230,700],[250,680],2)
		pygame.draw.line(DISPLAYSURF,red,[210,700],[250,660],2)
		pygame.draw.line(DISPLAYSURF,red,[190,700],[250,640],2)
		pygame.draw.line(DISPLAYSURF,red,[170,700],[250,620],2)
		pygame.draw.line(DISPLAYSURF,red,[150,700],[250,600],2)
		pygame.draw.line(DISPLAYSURF,red,[130,700],[250,580],2)
		pygame.draw.line(DISPLAYSURF,red,[110,700],[250,560],2)
		pygame.draw.line(DISPLAYSURF,red,[90,700],[250,540],2)
		pygame.draw.line(DISPLAYSURF,red,[70,700],[230,540],2)
		pygame.draw.line(DISPLAYSURF,red,[50,700],[210,540],2)
		pygame.draw.line(DISPLAYSURF,red,[30,700],[190,540],2)
		pygame.draw.line(DISPLAYSURF,red,[10,700],[170,540],2)
		pygame.draw.line(DISPLAYSURF,red,[0,680],[150,540],2)
		pygame.draw.line(DISPLAYSURF,red,[0,660],[130,540],2)
		pygame.draw.line(DISPLAYSURF,red,[0,640],[110,540],2)
		pygame.draw.line(DISPLAYSURF,red,[0,620],[90,540],2)
		pygame.draw.line(DISPLAYSURF,red,[0,600],[70,540],2)
		pygame.draw.line(DISPLAYSURF,red,[0,580],[50,540],2)
		pygame.draw.line(DISPLAYSURF,red,[0,560],[30,540],2)
		pygame.draw.line(DISPLAYSURF,red,[0,540],[10,540],2)
		#back SLash

		pygame.draw.line(DISPLAYSURF,red,[0,680],[20,700],2)
		pygame.draw.line(DISPLAYSURF,red,[0,660],[40,700],2)
		pygame.draw.line(DISPLAYSURF,red,[0,640],[60,700],2)
		pygame.draw.line(DISPLAYSURF,red,[0,620],[80,700],2)
		pygame.draw.line(DISPLAYSURF,red,[0,600],[100,700],2)
		pygame.draw.line(DISPLAYSURF,red,[0,580],[120,700],2)
		pygame.draw.line(DISPLAYSURF,red,[0,560],[140,700],2)
		pygame.draw.line(DISPLAYSURF,red,[0,540],[160,700],2)

		pygame.draw.line(DISPLAYSURF,red,[20,540],[180,700],2)
		pygame.draw.line(DISPLAYSURF,red,[40,540],[200,700],2)
		pygame.draw.line(DISPLAYSURF,red,[60,540],[220,700],2)
		pygame.draw.line(DISPLAYSURF,red,[80,540],[240,700],2)

		pygame.draw.line(DISPLAYSURF,red,[100,540],[250,680],2)
		pygame.draw.line(DISPLAYSURF,red,[120,540],[250,660],2)
		pygame.draw.line(DISPLAYSURF,red,[140,540],[250,640],2)
		pygame.draw.line(DISPLAYSURF,red,[160,540],[250,620],2)
		pygame.draw.line(DISPLAYSURF,red,[180,540],[250,600],2)
		pygame.draw.line(DISPLAYSURF,red,[200,540],[250,580],2)
		pygame.draw.line(DISPLAYSURF,red,[220,540],[250,560],2)
		pygame.draw.line(DISPLAYSURF,red,[240,540],[250,540],2)
		pygame.draw.line(DISPLAYSURF,red,[250,540],[250,540],2)




		#pygame.draw.line(DISPLAYSURF,red,[,],[,],2)




		#bottom-right corner
		pygame.draw.line(DISPLAYSURF,red,[970,700],[1000,680],2)
		pygame.draw.line(DISPLAYSURF,red,[950,700],[1000,660],2)
		pygame.draw.line(DISPLAYSURF,red,[930,700],[1000,640],2)
		pygame.draw.line(DISPLAYSURF,red,[910,700],[1000,620],2)
		pygame.draw.line(DISPLAYSURF,red,[890,700],[1000,600],2)
		pygame.draw.line(DISPLAYSURF,red,[870,700],[1000,580],2)
		pygame.draw.line(DISPLAYSURF,red,[850,700],[1000,560],2)
		pygame.draw.line(DISPLAYSURF,red,[830,700],[1000,540],2)

		pygame.draw.line(DISPLAYSURF,red,[810,700],[980,540],2)
		pygame.draw.line(DISPLAYSURF,red,[790,700],[960,540],2)
		pygame.draw.line(DISPLAYSURF,red,[770,700],[940,540],2)
		pygame.draw.line(DISPLAYSURF,red,[750,700],[920,540],2)

		pygame.draw.line(DISPLAYSURF,red,[750,680],[900,540],2)
		pygame.draw.line(DISPLAYSURF,red,[750,660],[880,540],2)
		pygame.draw.line(DISPLAYSURF,red,[750,640],[860,540],2)
		pygame.draw.line(DISPLAYSURF,red,[750,620],[840,540],2)
		pygame.draw.line(DISPLAYSURF,red,[750,600],[820,540],2)
		pygame.draw.line(DISPLAYSURF,red,[750,580],[800,540],2)
		pygame.draw.line(DISPLAYSURF,red,[750,560],[780,540],2)
		pygame.draw.line(DISPLAYSURF,red,[750,540],[760,540],2)


		pygame.draw.line(DISPLAYSURF,red,[750,680],[770,700],2)
		pygame.draw.line(DISPLAYSURF,red,[750,660],[790,700],2)
		pygame.draw.line(DISPLAYSURF,red,[750,640],[810,700],2)
		pygame.draw.line(DISPLAYSURF,red,[750,620],[830,700],2)
		pygame.draw.line(DISPLAYSURF,red,[750,600],[850,700],2)
		pygame.draw.line(DISPLAYSURF,red,[750,580],[870,700],2)
		pygame.draw.line(DISPLAYSURF,red,[750,560],[890,700],2)
		pygame.draw.line(DISPLAYSURF,red,[750,540],[910,700],2)

		pygame.draw.line(DISPLAYSURF,red,[770,540],[930,700],2)
		pygame.draw.line(DISPLAYSURF,red,[790,540],[950,700],2)
		pygame.draw.line(DISPLAYSURF,red,[810,540],[970,700],2)
		pygame.draw.line(DISPLAYSURF,red,[830,540],[990,700],2)

		pygame.draw.line(DISPLAYSURF,red,[850,540],[1000,680],2)
		pygame.draw.line(DISPLAYSURF,red,[870,540],[1000,660],2)
		pygame.draw.line(DISPLAYSURF,red,[890,540],[1000,640],2)
		pygame.draw.line(DISPLAYSURF,red,[910,540],[1000,620],2)
		pygame.draw.line(DISPLAYSURF,red,[930,540],[1000,600],2)
		pygame.draw.line(DISPLAYSURF,red,[950,540],[1000,580],2)
		pygame.draw.line(DISPLAYSURF,red,[970,540],[1000,560],2)
		pygame.draw.line(DISPLAYSURF,red,[990,540],[1000,540],2)

		# top - right

		#pygame.draw.line(DISPLAYSURF,red,[,],[,],2)
		pygame.draw.line(DISPLAYSURF,red,[970,160],[1000,140],2)
		pygame.draw.line(DISPLAYSURF,red,[950,160],[1000,120],2)
		pygame.draw.line(DISPLAYSURF,red,[930,160],[1000,100],2)
		pygame.draw.line(DISPLAYSURF,red,[910,160],[1000,80],2)
		pygame.draw.line(DISPLAYSURF,red,[890,160],[1000,60],2)
		pygame.draw.line(DISPLAYSURF,red,[870,160],[1000,40],2)
		pygame.draw.line(DISPLAYSURF,red,[850,160],[1000,20],2)
		pygame.draw.line(DISPLAYSURF,red,[830,160],[1000,0],2)

		pygame.draw.line(DISPLAYSURF,red,[810,160],[980,0],2)
		pygame.draw.line(DISPLAYSURF,red,[790,160],[960,0],2)
		pygame.draw.line(DISPLAYSURF,red,[770,160],[940,0],2)
		pygame.draw.line(DISPLAYSURF,red,[750,160],[920,0],2)

		pygame.draw.line(DISPLAYSURF,red,[750,140],[900,0],2)
		pygame.draw.line(DISPLAYSURF,red,[750,120],[880,0],2)
		pygame.draw.line(DISPLAYSURF,red,[750,100],[860,0],2)
		pygame.draw.line(DISPLAYSURF,red,[750,80],[840,0],2)
		pygame.draw.line(DISPLAYSURF,red,[750,60],[820,0],2)
		pygame.draw.line(DISPLAYSURF,red,[750,40],[800,0],2)
		pygame.draw.line(DISPLAYSURF,red,[750,20],[780,0],2)
		pygame.draw.line(DISPLAYSURF,red,[750,00],[760,0],2)

		pygame.draw.line(DISPLAYSURF,red,[750,140],[770,160],2)
		pygame.draw.line(DISPLAYSURF,red,[750,120],[790,160],2)
		pygame.draw.line(DISPLAYSURF,red,[750,100],[810,160],2)
		pygame.draw.line(DISPLAYSURF,red,[750,80],[830,160],2)
		pygame.draw.line(DISPLAYSURF,red,[750,60],[850,160],2)
		pygame.draw.line(DISPLAYSURF,red,[750,40],[870,160],2)
		pygame.draw.line(DISPLAYSURF,red,[750,20],[890,160],2)
		pygame.draw.line(DISPLAYSURF,red,[750,0],[910,160],2)

		pygame.draw.line(DISPLAYSURF,red,[770,0],[930,160],2)
		pygame.draw.line(DISPLAYSURF,red,[790,0],[950,160],2)
		pygame.draw.line(DISPLAYSURF,red,[810,0],[970,160],2)
		pygame.draw.line(DISPLAYSURF,red,[830,0],[990,160],2)

		pygame.draw.line(DISPLAYSURF,red,[850,0],[1000,140],2)
		pygame.draw.line(DISPLAYSURF,red,[870,0],[1000,120],2)
		pygame.draw.line(DISPLAYSURF,red,[890,0],[1000,100],2)
		pygame.draw.line(DISPLAYSURF,red,[910,0],[1000,80],2)
		pygame.draw.line(DISPLAYSURF,red,[930,0],[1000,60],2)
		pygame.draw.line(DISPLAYSURF,red,[950,0],[1000,40],2)
		pygame.draw.line(DISPLAYSURF,red,[970,0],[1000,20],2)
		pygame.draw.line(DISPLAYSURF,red,[990,0],[1000,0],2)

		#zebra crossing
		#up-down

		pygame.draw.line(DISPLAYSURF,white,[200,180],[240,180],12)
		pygame.draw.line(DISPLAYSURF,white,[200,200],[240,200],12)
		pygame.draw.line(DISPLAYSURF,white,[200,220],[240,220],12)
		pygame.draw.line(DISPLAYSURF,white,[200,240],[240,240],12)
		pygame.draw.line(DISPLAYSURF,white,[200,260],[240,260],12)
		pygame.draw.line(DISPLAYSURF,white,[200,280],[240,280],12)
		pygame.draw.line(DISPLAYSURF,white,[200,300],[240,300],12)
		pygame.draw.line(DISPLAYSURF,white,[200,320],[240,320],12)
		pygame.draw.line(DISPLAYSURF,white,[200,340],[240,340],12)
		pygame.draw.line(DISPLAYSURF,white,[200,360],[240,360],12)
		pygame.draw.line(DISPLAYSURF,white,[200,380],[240,380],12)
		pygame.draw.line(DISPLAYSURF,white,[200,400],[240,400],12)
		pygame.draw.line(DISPLAYSURF,white,[200,420],[240,420],12)
		pygame.draw.line(DISPLAYSURF,white,[200,440],[240,440],12)
		pygame.draw.line(DISPLAYSURF,white,[200,460],[240,460],12)
		pygame.draw.line(DISPLAYSURF,white,[200,480],[240,480],12)
		pygame.draw.line(DISPLAYSURF,white,[200,500],[240,500],12)
		pygame.draw.line(DISPLAYSURF,white,[200,520],[240,520],12)
		#pygame.draw.line(DISPLAYSURF,white,[200,160],[200,540],4)
		#pygame.draw.line(DISPLAYSURF,white,[240,160],[240,540],4)


		#left-right : bottom
		pygame.draw.line(DISPLAYSURF,white,[730,550],[730,590],12)
		pygame.draw.line(DISPLAYSURF,white,[710,550],[710,590],12)
		pygame.draw.line(DISPLAYSURF,white,[690,550],[690,590],12)
		pygame.draw.line(DISPLAYSURF,white,[670,550],[670,590],12)
		pygame.draw.line(DISPLAYSURF,white,[650,550],[650,590],12)
		pygame.draw.line(DISPLAYSURF,white,[630,550],[630,590],12)
		pygame.draw.line(DISPLAYSURF,white,[610,550],[610,590],12)
		pygame.draw.line(DISPLAYSURF,white,[590,550],[590,590],12)
		pygame.draw.line(DISPLAYSURF,white,[570,550],[570,590],12)
		pygame.draw.line(DISPLAYSURF,white,[550,550],[550,590],12)
		pygame.draw.line(DISPLAYSURF,white,[530,550],[530,590],12)
		pygame.draw.line(DISPLAYSURF,white,[510,550],[510,590],12)
		pygame.draw.line(DISPLAYSURF,white,[490,550],[490,590],12)
		pygame.draw.line(DISPLAYSURF,white,[470,550],[470,590],12)
		pygame.draw.line(DISPLAYSURF,white,[450,550],[450,590],12)
		pygame.draw.line(DISPLAYSURF,white,[430,550],[430,590],12)
		pygame.draw.line(DISPLAYSURF,white,[410,550],[410,590],12)
		pygame.draw.line(DISPLAYSURF,white,[390,550],[390,590],12)
		pygame.draw.line(DISPLAYSURF,white,[370,550],[370,590],12)
		pygame.draw.line(DISPLAYSURF,white,[350,550],[350,590],12)
		pygame.draw.line(DISPLAYSURF,white,[330,550],[330,590],12)
		pygame.draw.line(DISPLAYSURF,white,[310,550],[310,590],12)
		pygame.draw.line(DISPLAYSURF,white,[290,550],[290,590],12)
		pygame.draw.line(DISPLAYSURF,white,[270,550],[270,590],12)
		#bottom-top 
		pygame.draw.line(DISPLAYSURF,white,[760,520],[800,520],12)
		pygame.draw.line(DISPLAYSURF,white,[760,500],[800,500],12)
		pygame.draw.line(DISPLAYSURF,white,[760,480],[800,480],12)
		pygame.draw.line(DISPLAYSURF,white,[760,460],[800,460],12)
		pygame.draw.line(DISPLAYSURF,white,[760,440],[800,440],12)
		pygame.draw.line(DISPLAYSURF,white,[760,420],[800,420],12)
		pygame.draw.line(DISPLAYSURF,white,[760,400],[800,400],12)
		pygame.draw.line(DISPLAYSURF,white,[760,380],[800,380],12)
		pygame.draw.line(DISPLAYSURF,white,[760,360],[800,360],12)
		pygame.draw.line(DISPLAYSURF,white,[760,340],[800,340],12)
		pygame.draw.line(DISPLAYSURF,white,[760,320],[800,320],12)
		pygame.draw.line(DISPLAYSURF,white,[760,300],[800,300],12)
		pygame.draw.line(DISPLAYSURF,white,[760,280],[800,280],12)
		pygame.draw.line(DISPLAYSURF,white,[760,260],[800,260],12)
		pygame.draw.line(DISPLAYSURF,white,[760,240],[800,240],12)
		pygame.draw.line(DISPLAYSURF,white,[760,220],[800,220],12)
		pygame.draw.line(DISPLAYSURF,white,[760,200],[800,200],12)
		pygame.draw.line(DISPLAYSURF,white,[760,180],[800,180],12)
		#right-left
		pygame.draw.line(DISPLAYSURF,white,[730,150],[730,110],12)
		pygame.draw.line(DISPLAYSURF,white,[710,150],[710,110],12)
		pygame.draw.line(DISPLAYSURF,white,[690,150],[690,110],12)
		pygame.draw.line(DISPLAYSURF,white,[670,150],[670,110],12)
		pygame.draw.line(DISPLAYSURF,white,[650,150],[650,110],12)
		pygame.draw.line(DISPLAYSURF,white,[630,150],[630,110],12)
		pygame.draw.line(DISPLAYSURF,white,[610,150],[610,110],12)
		pygame.draw.line(DISPLAYSURF,white,[590,150],[590,110],12)
		pygame.draw.line(DISPLAYSURF,white,[570,150],[570,110],12)
		pygame.draw.line(DISPLAYSURF,white,[550,150],[550,110],12)
		pygame.draw.line(DISPLAYSURF,white,[530,150],[530,110],12)
		pygame.draw.line(DISPLAYSURF,white,[510,150],[510,110],12)
		pygame.draw.line(DISPLAYSURF,white,[490,150],[490,110],12)
		pygame.draw.line(DISPLAYSURF,white,[470,150],[470,110],12)
		pygame.draw.line(DISPLAYSURF,white,[450,150],[450,110],12)
		pygame.draw.line(DISPLAYSURF,white,[430,150],[430,110],12)
		pygame.draw.line(DISPLAYSURF,white,[410,150],[410,110],12)
		pygame.draw.line(DISPLAYSURF,white,[390,150],[390,110],12)
		pygame.draw.line(DISPLAYSURF,white,[370,150],[370,110],12)
		pygame.draw.line(DISPLAYSURF,white,[350,150],[350,110],12)
		pygame.draw.line(DISPLAYSURF,white,[330,150],[330,110],12)
		pygame.draw.line(DISPLAYSURF,white,[310,150],[310,110],12)
		pygame.draw.line(DISPLAYSURF,white,[290,150],[290,110],12)
		pygame.draw.line(DISPLAYSURF,white,[270,150],[270,110],12)







		#construction of road divider -> x-axis

		pygame.draw.line(DISPLAYSURF,white,[0,350],[20,350],2)
		pygame.draw.line(DISPLAYSURF,white,[30,350],[50,350],2)
		pygame.draw.line(DISPLAYSURF,white,[60,350],[80,350],2)
		pygame.draw.line(DISPLAYSURF,white,[90,350],[110,350],2)
		pygame.draw.line(DISPLAYSURF,white,[120,350],[140,350],2)
		pygame.draw.line(DISPLAYSURF,white,[150,350],[170,350],2)
		pygame.draw.line(DISPLAYSURF,white,[180,350],[200,350],2)
		pygame.draw.line(DISPLAYSURF,white,[210,350],[230,350],2)
		pygame.draw.line(DISPLAYSURF,white,[240,350],[260,350],2)
		pygame.draw.line(DISPLAYSURF,white,[270,350],[290,350],2)
		pygame.draw.line(DISPLAYSURF,white,[300,350],[320,350],2)
		pygame.draw.line(DISPLAYSURF,white,[330,350],[350,350],2)
		pygame.draw.line(DISPLAYSURF,white,[360,350],[380,350],2)
		pygame.draw.line(DISPLAYSURF,white,[390,350],[410,350],2)
		pygame.draw.line(DISPLAYSURF,white,[420,350],[440,350],2)
		pygame.draw.line(DISPLAYSURF,white,[450,350],[470,350],2)
		pygame.draw.line(DISPLAYSURF,white,[480,350],[500,350],2)
		pygame.draw.line(DISPLAYSURF,white,[510,350],[530,350],2)
		pygame.draw.line(DISPLAYSURF,white,[540,350],[560,350],2)
		pygame.draw.line(DISPLAYSURF,white,[570,350],[590,350],2)
		pygame.draw.line(DISPLAYSURF,white,[600,350],[620,350],2)
		pygame.draw.line(DISPLAYSURF,white,[630,350],[650,350],2)
		pygame.draw.line(DISPLAYSURF,white,[660,350],[680,350],2)
		pygame.draw.line(DISPLAYSURF,white,[690,350],[710,350],2)
		pygame.draw.line(DISPLAYSURF,white,[720,350],[740,350],2)
		pygame.draw.line(DISPLAYSURF,white,[750,350],[770,350],2)
		pygame.draw.line(DISPLAYSURF,white,[780,350],[800,350],2)
		pygame.draw.line(DISPLAYSURF,white,[810,350],[830,350],2)
		pygame.draw.line(DISPLAYSURF,white,[840,350],[860,350],2)
		pygame.draw.line(DISPLAYSURF,white,[870,350],[890,350],2)
		pygame.draw.line(DISPLAYSURF,white,[900,350],[920,350],2)
		pygame.draw.line(DISPLAYSURF,white,[930,350],[950,350],2)
		pygame.draw.line(DISPLAYSURF,white,[960,350],[980,350],2)



		# road divider  --> y-axis

		pygame.draw.line(DISPLAYSURF,white,[500,0],[500,20],2)
		pygame.draw.line(DISPLAYSURF,white,[500,30],[500,50],2)
		pygame.draw.line(DISPLAYSURF,white,[500,60],[500,80],2)
		pygame.draw.line(DISPLAYSURF,white,[500,90],[500,110],2)
		pygame.draw.line(DISPLAYSURF,white,[500,120],[500,140],2)
		pygame.draw.line(DISPLAYSURF,white,[500,150],[500,170],2)
		pygame.draw.line(DISPLAYSURF,white,[500,180],[500,200],2)
		pygame.draw.line(DISPLAYSURF,white,[500,210],[500,230],2)
		pygame.draw.line(DISPLAYSURF,white,[500,240],[500,260],2)
		pygame.draw.line(DISPLAYSURF,white,[500,270],[500,290],2)
		pygame.draw.line(DISPLAYSURF,white,[500,300],[500,320],2)
		pygame.draw.line(DISPLAYSURF,white,[500,330],[500,350],2)
		pygame.draw.line(DISPLAYSURF,white,[500,360],[500,380],2)
		pygame.draw.line(DISPLAYSURF,white,[500,390],[500,410],2)
		pygame.draw.line(DISPLAYSURF,white,[500,420],[500,440],2)
		pygame.draw.line(DISPLAYSURF,white,[500,450],[500,470],2)
		pygame.draw.line(DISPLAYSURF,white,[500,480],[500,500],2)
		pygame.draw.line(DISPLAYSURF,white,[500,510],[500,530],2)
		pygame.draw.line(DISPLAYSURF,white,[500,540],[500,560],2)
		pygame.draw.line(DISPLAYSURF,white,[500,570],[500,590],2)
		pygame.draw.line(DISPLAYSURF,white,[500,600],[500,620],2)
		pygame.draw.line(DISPLAYSURF,white,[500,630],[500,650],2)
		pygame.draw.line(DISPLAYSURF,white,[500,660],[500,680],2)
		pygame.draw.circle(DISPLAYSURF,silver,(500,350),40)
		DISPLAYSURF.blit(textSurfaceObj, textRectObj)
		DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
		DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
		#DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)




		#signal line construction on 3 lanes:

		pygame.draw.line(DISPLAYSURF,green,[250,160],[250,350],4)
		pygame.draw.line(DISPLAYSURF,red,[500,160],[750,160],4)
		pygame.draw.line(DISPLAYSURF,red,[250,540],[500,540],4)
		pygame.draw.line(DISPLAYSURF,red,[750,540],[750,350],4)

		#circular sensor representation
		pygame.draw.circle(DISPLAYSURF,green,(190,160),10)
		pygame.draw.circle(DISPLAYSURF,green,(190,350),10)
		pygame.draw.circle(DISPLAYSURF,red,(500,600),10)
		pygame.draw.circle(DISPLAYSURF,red,(250,600),10)
		pygame.draw.circle(DISPLAYSURF,red,(750,105),10)
		pygame.draw.circle(DISPLAYSURF,red,(500,105),10)
		pygame.draw.circle(DISPLAYSURF,red,(810,350),10)
		pygame.draw.circle(DISPLAYSURF,red,(810,540),10)

		pygame.draw.line(DISPLAYSURF,green,[190,160],[190,350])
		pygame.draw.line(DISPLAYSURF,red,[810,350],[810,540])
		pygame.draw.line(DISPLAYSURF,red,[750,105],[500,105])
		pygame.draw.line(DISPLAYSURF,red,[500,600],[250,600])

		




		#static car on rest of the lanes
		# bottom-left lane
		pygame.draw.rect(DISPLAYSURF,aqua,(257,610,40,40))
		pygame.draw.rect(DISPLAYSURF,fuchsia,(257,660,40,40))
		pygame.draw.rect(DISPLAYSURF,purple,(320,610,40,40))
		pygame.draw.rect(DISPLAYSURF,olive,(320,660,30,30))
		pygame.draw.rect(DISPLAYSURF,teal,(380,660,40,40))
		pygame.draw.rect(DISPLAYSURF,yellow,(380,660,40,40))
		pygame.draw.rect(DISPLAYSURF,silver,(380,610,20,20))
		pygame.draw.rect(DISPLAYSURF,maroon,(430,610,10,70))

		#top-right lane

		pygame.draw.rect(DISPLAYSURF,yellow,(530,40,40,40))
		pygame.draw.rect(DISPLAYSURF,teal,(610,40,40,40))
		pygame.draw.rect(DISPLAYSURF,aqua,(670,00,60,90))
		pygame.draw.rect(DISPLAYSURF,gray,(610,10,20,20))
		pygame.draw.rect(DISPLAYSURF,yellow,(580,50,20,20))
		#pygame.draw.rect(DISPLAYSURF,red,(320,660,40,40),2)






		# car drive on lane 1 --> moving cars
		pygame.draw.rect(DISPLAYSURF,green,(x,y,80,40))
		pygame.draw.rect(DISPLAYSURF,fuchsia,(x1,y1,20,20))
		pygame.draw.rect(DISPLAYSURF,aqua,(x3,y3,50,30),2)
		pygame.draw.circle(DISPLAYSURF,green,(190,160),10)
		#pygame.draw.line(DISPLAYSURF,green,[250,160],[250,350],4)
		pygame.draw.circle(DISPLAYSURF,green,(190,350),10)



		#delay loop counter
		for i in range (0,1000000):
			continue
		for i in range (0,1000000):
			continue
		for i in range (0,1000000):
			continue

		#increaments
		x = x +4
		x1 = x1 +3
		x3 = x3+9
		
		if x1 == 248:
			DISPLAYSURF.fill(black)

			# construction of border for road

			pygame.draw.line(DISPLAYSURF,white,[0,160],[250,160],2)
			pygame.draw.line(DISPLAYSURF,white,[0,540],[250,540],2)
			pygame.draw.line(DISPLAYSURF,white,[250,160],[250,0],2)	
			pygame.draw.line(DISPLAYSURF,white,[250,540],[250,700],2)
			pygame.draw.line(DISPLAYSURF,white,[750,160],[750,0],2)	
			pygame.draw.line(DISPLAYSURF,white,[750,540],[750,700],2)
			pygame.draw.line(DISPLAYSURF,white,[750,160],[1000,160],2)
			pygame.draw.line(DISPLAYSURF,white,[750,540],[1000,540],2)
			pygame.draw.rect(DISPLAYSURF,yellow,(0,0,250,160))
			pygame.draw.rect(DISPLAYSURF,yellow,(0,540,250,160))
			pygame.draw.rect(DISPLAYSURF,yellow,(750,0,250,160))
			pygame.draw.rect(DISPLAYSURF,yellow,(750,540,250,160))

			#construction of slant lines for building and foothpath representation 
			#top left corner
			#front slash
			pygame.draw.line(DISPLAYSURF,red,[230,160],[250,140],2)
			pygame.draw.line(DISPLAYSURF,red,[210,160],[250,120],2)
			pygame.draw.line(DISPLAYSURF,red,[190,160],[250,100],2)
			pygame.draw.line(DISPLAYSURF,red,[170,160],[250,80],2)
			pygame.draw.line(DISPLAYSURF,red,[150,160],[250,60],2)
			pygame.draw.line(DISPLAYSURF,red,[130,160],[250,40],2)
			pygame.draw.line(DISPLAYSURF,red,[110,160],[250,20],2)
			pygame.draw.line(DISPLAYSURF,red,[90,160],[250,0],2)
			pygame.draw.line(DISPLAYSURF,red,[70,160],[230,0],2)
			pygame.draw.line(DISPLAYSURF,red,[50,160],[210,0],2)
			pygame.draw.line(DISPLAYSURF,red,[30,160],[190,0],2)
			pygame.draw.line(DISPLAYSURF,red,[10,160],[170,0],2)
			pygame.draw.line(DISPLAYSURF,red,[0,140],[150,0],2)
			pygame.draw.line(DISPLAYSURF,red,[0,120],[130,0],2)
			pygame.draw.line(DISPLAYSURF,red,[0,100],[110,0],2)
			pygame.draw.line(DISPLAYSURF,red,[0,80],[90,0],2)
			pygame.draw.line(DISPLAYSURF,red,[0,60],[70,0],2)
			pygame.draw.line(DISPLAYSURF,red,[0,40],[50,0],2)
			pygame.draw.line(DISPLAYSURF,red,[0,20],[30,0],2)
			pygame.draw.line(DISPLAYSURF,red,[0,0],[10,0],2)

			#back slash
			pygame.draw.line(DISPLAYSURF,red,[0,140],[20,160],2)
			pygame.draw.line(DISPLAYSURF,red,[0,120],[40,160],2)
			pygame.draw.line(DISPLAYSURF,red,[0,100],[60,160],2)
			pygame.draw.line(DISPLAYSURF,red,[0,80],[80,160],2)
			pygame.draw.line(DISPLAYSURF,red,[0,60],[100,160],2)
			pygame.draw.line(DISPLAYSURF,red,[0,40],[120,160],2)
			pygame.draw.line(DISPLAYSURF,red,[0,20],[140,160],2)
			pygame.draw.line(DISPLAYSURF,red,[0,0],[160,160],2)
			pygame.draw.line(DISPLAYSURF,red,[20,0],[180,160],2)
			pygame.draw.line(DISPLAYSURF,red,[40,0],[200,160],2)
			pygame.draw.line(DISPLAYSURF,red,[60,0],[220,160],2)
			pygame.draw.line(DISPLAYSURF,red,[80,0],[240,160],2)
			pygame.draw.line(DISPLAYSURF,red,[100,0],[250,140],2)
			pygame.draw.line(DISPLAYSURF,red,[120,0],[250,120],2)
			pygame.draw.line(DISPLAYSURF,red,[140,0],[250,100],2)
			pygame.draw.line(DISPLAYSURF,red,[160,0],[250,80],2)
			pygame.draw.line(DISPLAYSURF,red,[180,0],[250,60],2)
			pygame.draw.line(DISPLAYSURF,red,[200,0],[250,40],2)
			pygame.draw.line(DISPLAYSURF,red,[220,0],[250,20],2)
			pygame.draw.line(DISPLAYSURF,red,[240,0],[250,0],2)
			#bottom-right corner construction
			#front slash
			pygame.draw.line(DISPLAYSURF,red,[230,700],[250,680],2)
			pygame.draw.line(DISPLAYSURF,red,[210,700],[250,660],2)
			pygame.draw.line(DISPLAYSURF,red,[190,700],[250,640],2)
			pygame.draw.line(DISPLAYSURF,red,[170,700],[250,620],2)
			pygame.draw.line(DISPLAYSURF,red,[150,700],[250,600],2)
			pygame.draw.line(DISPLAYSURF,red,[130,700],[250,580],2)
			pygame.draw.line(DISPLAYSURF,red,[110,700],[250,560],2)
			pygame.draw.line(DISPLAYSURF,red,[90,700],[250,540],2)
			pygame.draw.line(DISPLAYSURF,red,[70,700],[230,540],2)
			pygame.draw.line(DISPLAYSURF,red,[50,700],[210,540],2)
			pygame.draw.line(DISPLAYSURF,red,[30,700],[190,540],2)
			pygame.draw.line(DISPLAYSURF,red,[10,700],[170,540],2)
			pygame.draw.line(DISPLAYSURF,red,[0,680],[150,540],2)
			pygame.draw.line(DISPLAYSURF,red,[0,660],[130,540],2)
			pygame.draw.line(DISPLAYSURF,red,[0,640],[110,540],2)
			pygame.draw.line(DISPLAYSURF,red,[0,620],[90,540],2)
			pygame.draw.line(DISPLAYSURF,red,[0,600],[70,540],2)
			pygame.draw.line(DISPLAYSURF,red,[0,580],[50,540],2)
			pygame.draw.line(DISPLAYSURF,red,[0,560],[30,540],2)
			pygame.draw.line(DISPLAYSURF,red,[0,540],[10,540],2)
			#back SLash

			pygame.draw.line(DISPLAYSURF,red,[0,680],[20,700],2)
			pygame.draw.line(DISPLAYSURF,red,[0,660],[40,700],2)
			pygame.draw.line(DISPLAYSURF,red,[0,640],[60,700],2)
			pygame.draw.line(DISPLAYSURF,red,[0,620],[80,700],2)
			pygame.draw.line(DISPLAYSURF,red,[0,600],[100,700],2)
			pygame.draw.line(DISPLAYSURF,red,[0,580],[120,700],2)
			pygame.draw.line(DISPLAYSURF,red,[0,560],[140,700],2)
			pygame.draw.line(DISPLAYSURF,red,[0,540],[160,700],2)

			pygame.draw.line(DISPLAYSURF,red,[20,540],[180,700],2)
			pygame.draw.line(DISPLAYSURF,red,[40,540],[200,700],2)
			pygame.draw.line(DISPLAYSURF,red,[60,540],[220,700],2)
			pygame.draw.line(DISPLAYSURF,red,[80,540],[240,700],2)

			pygame.draw.line(DISPLAYSURF,red,[100,540],[250,680],2)
			pygame.draw.line(DISPLAYSURF,red,[120,540],[250,660],2)
			pygame.draw.line(DISPLAYSURF,red,[140,540],[250,640],2)
			pygame.draw.line(DISPLAYSURF,red,[160,540],[250,620],2)
			pygame.draw.line(DISPLAYSURF,red,[180,540],[250,600],2)
			pygame.draw.line(DISPLAYSURF,red,[200,540],[250,580],2)
			pygame.draw.line(DISPLAYSURF,red,[220,540],[250,560],2)
			pygame.draw.line(DISPLAYSURF,red,[240,540],[250,540],2)
			pygame.draw.line(DISPLAYSURF,red,[250,540],[250,540],2)




			#pygame.draw.line(DISPLAYSURF,red,[,],[,],2)




			#bottom-right corner
			pygame.draw.line(DISPLAYSURF,red,[970,700],[1000,680],2)
			pygame.draw.line(DISPLAYSURF,red,[950,700],[1000,660],2)
			pygame.draw.line(DISPLAYSURF,red,[930,700],[1000,640],2)
			pygame.draw.line(DISPLAYSURF,red,[910,700],[1000,620],2)
			pygame.draw.line(DISPLAYSURF,red,[890,700],[1000,600],2)
			pygame.draw.line(DISPLAYSURF,red,[870,700],[1000,580],2)
			pygame.draw.line(DISPLAYSURF,red,[850,700],[1000,560],2)
			pygame.draw.line(DISPLAYSURF,red,[830,700],[1000,540],2)

			pygame.draw.line(DISPLAYSURF,red,[810,700],[980,540],2)
			pygame.draw.line(DISPLAYSURF,red,[790,700],[960,540],2)
			pygame.draw.line(DISPLAYSURF,red,[770,700],[940,540],2)
			pygame.draw.line(DISPLAYSURF,red,[750,700],[920,540],2)

			pygame.draw.line(DISPLAYSURF,red,[750,680],[900,540],2)
			pygame.draw.line(DISPLAYSURF,red,[750,660],[880,540],2)
			pygame.draw.line(DISPLAYSURF,red,[750,640],[860,540],2)
			pygame.draw.line(DISPLAYSURF,red,[750,620],[840,540],2)
			pygame.draw.line(DISPLAYSURF,red,[750,600],[820,540],2)
			pygame.draw.line(DISPLAYSURF,red,[750,580],[800,540],2)
			pygame.draw.line(DISPLAYSURF,red,[750,560],[780,540],2)
			pygame.draw.line(DISPLAYSURF,red,[750,540],[760,540],2)


			pygame.draw.line(DISPLAYSURF,red,[750,680],[770,700],2)
			pygame.draw.line(DISPLAYSURF,red,[750,660],[790,700],2)
			pygame.draw.line(DISPLAYSURF,red,[750,640],[810,700],2)
			pygame.draw.line(DISPLAYSURF,red,[750,620],[830,700],2)
			pygame.draw.line(DISPLAYSURF,red,[750,600],[850,700],2)
			pygame.draw.line(DISPLAYSURF,red,[750,580],[870,700],2)
			pygame.draw.line(DISPLAYSURF,red,[750,560],[890,700],2)
			pygame.draw.line(DISPLAYSURF,red,[750,540],[910,700],2)

			pygame.draw.line(DISPLAYSURF,red,[770,540],[930,700],2)
			pygame.draw.line(DISPLAYSURF,red,[790,540],[950,700],2)
			pygame.draw.line(DISPLAYSURF,red,[810,540],[970,700],2)
			pygame.draw.line(DISPLAYSURF,red,[830,540],[990,700],2)

			pygame.draw.line(DISPLAYSURF,red,[850,540],[1000,680],2)
			pygame.draw.line(DISPLAYSURF,red,[870,540],[1000,660],2)
			pygame.draw.line(DISPLAYSURF,red,[890,540],[1000,640],2)
			pygame.draw.line(DISPLAYSURF,red,[910,540],[1000,620],2)
			pygame.draw.line(DISPLAYSURF,red,[930,540],[1000,600],2)
			pygame.draw.line(DISPLAYSURF,red,[950,540],[1000,580],2)
			pygame.draw.line(DISPLAYSURF,red,[970,540],[1000,560],2)
			pygame.draw.line(DISPLAYSURF,red,[990,540],[1000,540],2)

			# top - right

			#pygame.draw.line(DISPLAYSURF,red,[,],[,],2)
			pygame.draw.line(DISPLAYSURF,red,[970,160],[1000,140],2)
			pygame.draw.line(DISPLAYSURF,red,[950,160],[1000,120],2)
			pygame.draw.line(DISPLAYSURF,red,[930,160],[1000,100],2)
			pygame.draw.line(DISPLAYSURF,red,[910,160],[1000,80],2)
			pygame.draw.line(DISPLAYSURF,red,[890,160],[1000,60],2)
			pygame.draw.line(DISPLAYSURF,red,[870,160],[1000,40],2)
			pygame.draw.line(DISPLAYSURF,red,[850,160],[1000,20],2)
			pygame.draw.line(DISPLAYSURF,red,[830,160],[1000,0],2)

			pygame.draw.line(DISPLAYSURF,red,[810,160],[980,0],2)
			pygame.draw.line(DISPLAYSURF,red,[790,160],[960,0],2)
			pygame.draw.line(DISPLAYSURF,red,[770,160],[940,0],2)
			pygame.draw.line(DISPLAYSURF,red,[750,160],[920,0],2)

			pygame.draw.line(DISPLAYSURF,red,[750,140],[900,0],2)
			pygame.draw.line(DISPLAYSURF,red,[750,120],[880,0],2)
			pygame.draw.line(DISPLAYSURF,red,[750,100],[860,0],2)
			pygame.draw.line(DISPLAYSURF,red,[750,80],[840,0],2)
			pygame.draw.line(DISPLAYSURF,red,[750,60],[820,0],2)
			pygame.draw.line(DISPLAYSURF,red,[750,40],[800,0],2)
			pygame.draw.line(DISPLAYSURF,red,[750,20],[780,0],2)
			pygame.draw.line(DISPLAYSURF,red,[750,00],[760,0],2)

			pygame.draw.line(DISPLAYSURF,red,[750,140],[770,160],2)
			pygame.draw.line(DISPLAYSURF,red,[750,120],[790,160],2)
			pygame.draw.line(DISPLAYSURF,red,[750,100],[810,160],2)
			pygame.draw.line(DISPLAYSURF,red,[750,80],[830,160],2)
			pygame.draw.line(DISPLAYSURF,red,[750,60],[850,160],2)
			pygame.draw.line(DISPLAYSURF,red,[750,40],[870,160],2)
			pygame.draw.line(DISPLAYSURF,red,[750,20],[890,160],2)
			pygame.draw.line(DISPLAYSURF,red,[750,0],[910,160],2)

			pygame.draw.line(DISPLAYSURF,red,[770,0],[930,160],2)
			pygame.draw.line(DISPLAYSURF,red,[790,0],[950,160],2)
			pygame.draw.line(DISPLAYSURF,red,[810,0],[970,160],2)
			pygame.draw.line(DISPLAYSURF,red,[830,0],[990,160],2)

			pygame.draw.line(DISPLAYSURF,red,[850,0],[1000,140],2)
			pygame.draw.line(DISPLAYSURF,red,[870,0],[1000,120],2)
			pygame.draw.line(DISPLAYSURF,red,[890,0],[1000,100],2)
			pygame.draw.line(DISPLAYSURF,red,[910,0],[1000,80],2)
			pygame.draw.line(DISPLAYSURF,red,[930,0],[1000,60],2)
			pygame.draw.line(DISPLAYSURF,red,[950,0],[1000,40],2)
			pygame.draw.line(DISPLAYSURF,red,[970,0],[1000,20],2)
			pygame.draw.line(DISPLAYSURF,red,[990,0],[1000,0],2)

			#zebra crossing
			#up-down

			pygame.draw.line(DISPLAYSURF,white,[200,180],[240,180],12)
			pygame.draw.line(DISPLAYSURF,white,[200,200],[240,200],12)
			pygame.draw.line(DISPLAYSURF,white,[200,220],[240,220],12)
			pygame.draw.line(DISPLAYSURF,white,[200,240],[240,240],12)
			pygame.draw.line(DISPLAYSURF,white,[200,260],[240,260],12)
			pygame.draw.line(DISPLAYSURF,white,[200,280],[240,280],12)
			pygame.draw.line(DISPLAYSURF,white,[200,300],[240,300],12)
			pygame.draw.line(DISPLAYSURF,white,[200,320],[240,320],12)
			pygame.draw.line(DISPLAYSURF,white,[200,340],[240,340],12)
			pygame.draw.line(DISPLAYSURF,white,[200,360],[240,360],12)
			pygame.draw.line(DISPLAYSURF,white,[200,380],[240,380],12)
			pygame.draw.line(DISPLAYSURF,white,[200,400],[240,400],12)
			pygame.draw.line(DISPLAYSURF,white,[200,420],[240,420],12)
			pygame.draw.line(DISPLAYSURF,white,[200,440],[240,440],12)
			pygame.draw.line(DISPLAYSURF,white,[200,460],[240,460],12)
			pygame.draw.line(DISPLAYSURF,white,[200,480],[240,480],12)
			pygame.draw.line(DISPLAYSURF,white,[200,500],[240,500],12)
			pygame.draw.line(DISPLAYSURF,white,[200,520],[240,520],12)
			#pygame.draw.line(DISPLAYSURF,white,[200,160],[200,540],4)
			#pygame.draw.line(DISPLAYSURF,white,[240,160],[240,540],4)


			#left-right : bottom
			pygame.draw.line(DISPLAYSURF,white,[730,550],[730,590],12)
			pygame.draw.line(DISPLAYSURF,white,[710,550],[710,590],12)
			pygame.draw.line(DISPLAYSURF,white,[690,550],[690,590],12)
			pygame.draw.line(DISPLAYSURF,white,[670,550],[670,590],12)
			pygame.draw.line(DISPLAYSURF,white,[650,550],[650,590],12)
			pygame.draw.line(DISPLAYSURF,white,[630,550],[630,590],12)
			pygame.draw.line(DISPLAYSURF,white,[610,550],[610,590],12)
			pygame.draw.line(DISPLAYSURF,white,[590,550],[590,590],12)
			pygame.draw.line(DISPLAYSURF,white,[570,550],[570,590],12)
			pygame.draw.line(DISPLAYSURF,white,[550,550],[550,590],12)
			pygame.draw.line(DISPLAYSURF,white,[530,550],[530,590],12)
			pygame.draw.line(DISPLAYSURF,white,[510,550],[510,590],12)
			pygame.draw.line(DISPLAYSURF,white,[490,550],[490,590],12)
			pygame.draw.line(DISPLAYSURF,white,[470,550],[470,590],12)
			pygame.draw.line(DISPLAYSURF,white,[450,550],[450,590],12)
			pygame.draw.line(DISPLAYSURF,white,[430,550],[430,590],12)
			pygame.draw.line(DISPLAYSURF,white,[410,550],[410,590],12)
			pygame.draw.line(DISPLAYSURF,white,[390,550],[390,590],12)
			pygame.draw.line(DISPLAYSURF,white,[370,550],[370,590],12)
			pygame.draw.line(DISPLAYSURF,white,[350,550],[350,590],12)
			pygame.draw.line(DISPLAYSURF,white,[330,550],[330,590],12)
			pygame.draw.line(DISPLAYSURF,white,[310,550],[310,590],12)
			pygame.draw.line(DISPLAYSURF,white,[290,550],[290,590],12)
			pygame.draw.line(DISPLAYSURF,white,[270,550],[270,590],12)
			#bottom-top 
			pygame.draw.line(DISPLAYSURF,white,[760,520],[800,520],12)
			pygame.draw.line(DISPLAYSURF,white,[760,500],[800,500],12)
			pygame.draw.line(DISPLAYSURF,white,[760,480],[800,480],12)
			pygame.draw.line(DISPLAYSURF,white,[760,460],[800,460],12)
			pygame.draw.line(DISPLAYSURF,white,[760,440],[800,440],12)
			pygame.draw.line(DISPLAYSURF,white,[760,420],[800,420],12)
			pygame.draw.line(DISPLAYSURF,white,[760,400],[800,400],12)
			pygame.draw.line(DISPLAYSURF,white,[760,380],[800,380],12)
			pygame.draw.line(DISPLAYSURF,white,[760,360],[800,360],12)
			pygame.draw.line(DISPLAYSURF,white,[760,340],[800,340],12)
			pygame.draw.line(DISPLAYSURF,white,[760,320],[800,320],12)
			pygame.draw.line(DISPLAYSURF,white,[760,300],[800,300],12)
			pygame.draw.line(DISPLAYSURF,white,[760,280],[800,280],12)
			pygame.draw.line(DISPLAYSURF,white,[760,260],[800,260],12)
			pygame.draw.line(DISPLAYSURF,white,[760,240],[800,240],12)
			pygame.draw.line(DISPLAYSURF,white,[760,220],[800,220],12)
			pygame.draw.line(DISPLAYSURF,white,[760,200],[800,200],12)
			pygame.draw.line(DISPLAYSURF,white,[760,180],[800,180],12)
			#right-left
			pygame.draw.line(DISPLAYSURF,white,[730,150],[730,110],12)
			pygame.draw.line(DISPLAYSURF,white,[710,150],[710,110],12)
			pygame.draw.line(DISPLAYSURF,white,[690,150],[690,110],12)
			pygame.draw.line(DISPLAYSURF,white,[670,150],[670,110],12)
			pygame.draw.line(DISPLAYSURF,white,[650,150],[650,110],12)
			pygame.draw.line(DISPLAYSURF,white,[630,150],[630,110],12)
			pygame.draw.line(DISPLAYSURF,white,[610,150],[610,110],12)
			pygame.draw.line(DISPLAYSURF,white,[590,150],[590,110],12)
			pygame.draw.line(DISPLAYSURF,white,[570,150],[570,110],12)
			pygame.draw.line(DISPLAYSURF,white,[550,150],[550,110],12)
			pygame.draw.line(DISPLAYSURF,white,[530,150],[530,110],12)
			pygame.draw.line(DISPLAYSURF,white,[510,150],[510,110],12)
			pygame.draw.line(DISPLAYSURF,white,[490,150],[490,110],12)
			pygame.draw.line(DISPLAYSURF,white,[470,150],[470,110],12)
			pygame.draw.line(DISPLAYSURF,white,[450,150],[450,110],12)
			pygame.draw.line(DISPLAYSURF,white,[430,150],[430,110],12)
			pygame.draw.line(DISPLAYSURF,white,[410,150],[410,110],12)
			pygame.draw.line(DISPLAYSURF,white,[390,150],[390,110],12)
			pygame.draw.line(DISPLAYSURF,white,[370,150],[370,110],12)
			pygame.draw.line(DISPLAYSURF,white,[350,150],[350,110],12)
			pygame.draw.line(DISPLAYSURF,white,[330,150],[330,110],12)
			pygame.draw.line(DISPLAYSURF,white,[310,150],[310,110],12)
			pygame.draw.line(DISPLAYSURF,white,[290,150],[290,110],12)
			pygame.draw.line(DISPLAYSURF,white,[270,150],[270,110],12)

			#construction of road divider -> x-axis
			pygame.draw.line(DISPLAYSURF,white,[0,350],[20,350],2)
			pygame.draw.line(DISPLAYSURF,white,[30,350],[50,350],2)
			pygame.draw.line(DISPLAYSURF,white,[60,350],[80,350],2)
			pygame.draw.line(DISPLAYSURF,white,[90,350],[110,350],2)
			pygame.draw.line(DISPLAYSURF,white,[120,350],[140,350],2)
			pygame.draw.line(DISPLAYSURF,white,[150,350],[170,350],2)
			pygame.draw.line(DISPLAYSURF,white,[180,350],[200,350],2)
			pygame.draw.line(DISPLAYSURF,white,[210,350],[230,350],2)
			pygame.draw.line(DISPLAYSURF,white,[240,350],[260,350],2)
			pygame.draw.line(DISPLAYSURF,white,[270,350],[290,350],2)
			pygame.draw.line(DISPLAYSURF,white,[300,350],[320,350],2)
			pygame.draw.line(DISPLAYSURF,white,[330,350],[350,350],2)
			pygame.draw.line(DISPLAYSURF,white,[360,350],[380,350],2)
			pygame.draw.line(DISPLAYSURF,white,[390,350],[410,350],2)
			pygame.draw.line(DISPLAYSURF,white,[420,350],[440,350],2)
			pygame.draw.line(DISPLAYSURF,white,[450,350],[470,350],2)
			pygame.draw.line(DISPLAYSURF,white,[480,350],[500,350],2)
			pygame.draw.line(DISPLAYSURF,white,[510,350],[530,350],2)
			pygame.draw.line(DISPLAYSURF,white,[540,350],[560,350],2)
			pygame.draw.line(DISPLAYSURF,white,[570,350],[590,350],2)
			pygame.draw.line(DISPLAYSURF,white,[600,350],[620,350],2)
			pygame.draw.line(DISPLAYSURF,white,[630,350],[650,350],2)
			pygame.draw.line(DISPLAYSURF,white,[660,350],[680,350],2)
			pygame.draw.line(DISPLAYSURF,white,[690,350],[710,350],2)
			pygame.draw.line(DISPLAYSURF,white,[720,350],[740,350],2)
			pygame.draw.line(DISPLAYSURF,white,[750,350],[770,350],2)
			pygame.draw.line(DISPLAYSURF,white,[780,350],[800,350],2)
			pygame.draw.line(DISPLAYSURF,white,[810,350],[830,350],2)
			pygame.draw.line(DISPLAYSURF,white,[840,350],[860,350],2)
			pygame.draw.line(DISPLAYSURF,white,[870,350],[890,350],2)
			pygame.draw.line(DISPLAYSURF,white,[900,350],[920,350],2)
			pygame.draw.line(DISPLAYSURF,white,[930,350],[950,350],2)
			pygame.draw.line(DISPLAYSURF,white,[960,350],[980,350],2)


			# road divider  --> y-axis
			pygame.draw.line(DISPLAYSURF,white,[500,0],[500,20],2)
			pygame.draw.line(DISPLAYSURF,white,[500,30],[500,50],2)
			pygame.draw.line(DISPLAYSURF,white,[500,60],[500,80],2)
			pygame.draw.line(DISPLAYSURF,white,[500,90],[500,110],2)
			pygame.draw.line(DISPLAYSURF,white,[500,120],[500,140],2)
			pygame.draw.line(DISPLAYSURF,white,[500,150],[500,170],2)
			pygame.draw.line(DISPLAYSURF,white,[500,180],[500,200],2)
			pygame.draw.line(DISPLAYSURF,white,[500,210],[500,230],2)
			pygame.draw.line(DISPLAYSURF,white,[500,240],[500,260],2)
			pygame.draw.line(DISPLAYSURF,white,[500,270],[500,290],2)
			pygame.draw.line(DISPLAYSURF,white,[500,300],[500,320],2)
			pygame.draw.line(DISPLAYSURF,white,[500,330],[500,350],2)
			pygame.draw.line(DISPLAYSURF,white,[500,360],[500,380],2)
			pygame.draw.line(DISPLAYSURF,white,[500,390],[500,410],2)
			pygame.draw.line(DISPLAYSURF,white,[500,420],[500,440],2)
			pygame.draw.line(DISPLAYSURF,white,[500,450],[500,470],2)
			pygame.draw.line(DISPLAYSURF,white,[500,480],[500,500],2)
			pygame.draw.line(DISPLAYSURF,white,[500,510],[500,530],2)
			pygame.draw.line(DISPLAYSURF,white,[500,540],[500,560],2)
			pygame.draw.line(DISPLAYSURF,white,[500,570],[500,590],2)
			pygame.draw.line(DISPLAYSURF,white,[500,600],[500,620],2)
			pygame.draw.line(DISPLAYSURF,white,[500,630],[500,650],2)
			pygame.draw.line(DISPLAYSURF,white,[500,660],[500,680],2)
			pygame.draw.circle(DISPLAYSURF,silver,(500,350),40)
			DISPLAYSURF.blit(textSurfaceObj, textRectObj)
			DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
			DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
			#DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)





			#signal line construction on 3 lanes:

			pygame.draw.line(DISPLAYSURF,green,[250,160],[250,350],4)
			pygame.draw.line(DISPLAYSURF,red,[500,160],[750,160],4)
			pygame.draw.line(DISPLAYSURF,red,[250,540],[500,540],4)
			pygame.draw.line(DISPLAYSURF,red,[750,540],[750,350],4)

			#circular sensor representation
			pygame.draw.circle(DISPLAYSURF,green,(190,160),10)
			pygame.draw.circle(DISPLAYSURF,green,(190,350),10)
			pygame.draw.circle(DISPLAYSURF,red,(500,600),10)
			pygame.draw.circle(DISPLAYSURF,red,(250,600),10)
			pygame.draw.circle(DISPLAYSURF,red,(750,105),10)
			pygame.draw.circle(DISPLAYSURF,red,(500,105),10)
			pygame.draw.circle(DISPLAYSURF,red,(810,350),10)
			pygame.draw.circle(DISPLAYSURF,red,(810,540),10)

			pygame.draw.line(DISPLAYSURF,green,[190,160],[190,350])
			pygame.draw.line(DISPLAYSURF,red,[810,350],[810,540])
			pygame.draw.line(DISPLAYSURF,red,[750,105],[500,105])
			pygame.draw.line(DISPLAYSURF,red,[500,600],[250,600])






			#static car on rest of the lanes
			# bottom-left lane
			pygame.draw.rect(DISPLAYSURF,aqua,(257,610,40,40))
			pygame.draw.rect(DISPLAYSURF,fuchsia,(257,660,40,40))
			pygame.draw.rect(DISPLAYSURF,purple,(320,610,40,40))
			pygame.draw.rect(DISPLAYSURF,olive,(320,660,30,30))
			pygame.draw.rect(DISPLAYSURF,teal,(380,660,40,40))
			pygame.draw.rect(DISPLAYSURF,yellow,(380,660,40,40))
			pygame.draw.rect(DISPLAYSURF,silver,(380,610,20,20))
			pygame.draw.rect(DISPLAYSURF,maroon,(430,610,10,70))

			#top-right lane
			pygame.draw.rect(DISPLAYSURF,yellow,(530,40,40,40))
			pygame.draw.rect(DISPLAYSURF,teal,(610,40,40,40))
			pygame.draw.rect(DISPLAYSURF,aqua,(670,00,60,90))
			pygame.draw.rect(DISPLAYSURF,gray,(610,10,20,20))
			pygame.draw.rect(DISPLAYSURF,yellow,(580,50,20,20))
			#pygame.draw.rect(DISPLAYSURF,red,(320,660,40,40),2)

			pygame.draw.rect(DISPLAYSURF,green,(x,y,80,40))
			pygame.draw.rect(DISPLAYSURF,fuchsia,(260,180,20,20))
			pygame.draw.line(DISPLAYSURF,aqua,[660,240],[681,280],2)
			pygame.draw.line(DISPLAYSURF,aqua,[681,280],[655,298],2)
			pygame.draw.line(DISPLAYSURF,aqua,[655,298],[635,258],2)
			pygame.draw.line(DISPLAYSURF,aqua,[635,258],[660,240],2)
			pygame.draw.circle(DISPLAYSURF,green,(190,160),10)
			#pygame.draw.line(DISPLAYSURF,green,[250,160],[250,350],4)
			pygame.draw.circle(DISPLAYSURF,green,(190,350),10)

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
			fpsClock.tick(FPS)

			x1 = 260


		if x1 == 260 :

			
			x1 =270
			x3 = 665
			y1 = 180
			y3 = 258
			x4 = 257
			x5 =257
			x6 =320
			x7 =320
			x8 = 380
			x9 =380
			x10 =380
			x11 =430

			y4 =610	
			y5 =660
			y6 =610
			y7 =660
			y8 =660
			y9 =660
			y10 =610
			y11 =610
			while y3 <700:




				DISPLAYSURF.fill(black)

				# construction of border for road

				pygame.draw.line(DISPLAYSURF,white,[0,160],[250,160],2)
				pygame.draw.line(DISPLAYSURF,white,[0,540],[250,540],2)
				pygame.draw.line(DISPLAYSURF,white,[250,160],[250,0],2)	
				pygame.draw.line(DISPLAYSURF,white,[250,540],[250,700],2)
				pygame.draw.line(DISPLAYSURF,white,[750,160],[750,0],2)	
				pygame.draw.line(DISPLAYSURF,white,[750,540],[750,700],2)
				pygame.draw.line(DISPLAYSURF,white,[750,160],[1000,160],2)
				pygame.draw.line(DISPLAYSURF,white,[750,540],[1000,540],2)
				pygame.draw.rect(DISPLAYSURF,yellow,(0,0,250,160))
				pygame.draw.rect(DISPLAYSURF,yellow,(0,540,250,160))
				pygame.draw.rect(DISPLAYSURF,yellow,(750,0,250,160))
				pygame.draw.rect(DISPLAYSURF,yellow,(750,540,250,160))


				#construction of slant lines for building and foothpath representation 
				#top left corner
				#front slash
				pygame.draw.line(DISPLAYSURF,red,[230,160],[250,140],2)
				pygame.draw.line(DISPLAYSURF,red,[210,160],[250,120],2)
				pygame.draw.line(DISPLAYSURF,red,[190,160],[250,100],2)
				pygame.draw.line(DISPLAYSURF,red,[170,160],[250,80],2)
				pygame.draw.line(DISPLAYSURF,red,[150,160],[250,60],2)
				pygame.draw.line(DISPLAYSURF,red,[130,160],[250,40],2)
				pygame.draw.line(DISPLAYSURF,red,[110,160],[250,20],2)
				pygame.draw.line(DISPLAYSURF,red,[90,160],[250,0],2)
				pygame.draw.line(DISPLAYSURF,red,[70,160],[230,0],2)
				pygame.draw.line(DISPLAYSURF,red,[50,160],[210,0],2)
				pygame.draw.line(DISPLAYSURF,red,[30,160],[190,0],2)
				pygame.draw.line(DISPLAYSURF,red,[10,160],[170,0],2)
				pygame.draw.line(DISPLAYSURF,red,[0,140],[150,0],2)
				pygame.draw.line(DISPLAYSURF,red,[0,120],[130,0],2)
				pygame.draw.line(DISPLAYSURF,red,[0,100],[110,0],2)
				pygame.draw.line(DISPLAYSURF,red,[0,80],[90,0],2)
				pygame.draw.line(DISPLAYSURF,red,[0,60],[70,0],2)
				pygame.draw.line(DISPLAYSURF,red,[0,40],[50,0],2)
				pygame.draw.line(DISPLAYSURF,red,[0,20],[30,0],2)
				pygame.draw.line(DISPLAYSURF,red,[0,0],[10,0],2)

				#back slash
				pygame.draw.line(DISPLAYSURF,red,[0,140],[20,160],2)
				pygame.draw.line(DISPLAYSURF,red,[0,120],[40,160],2)
				pygame.draw.line(DISPLAYSURF,red,[0,100],[60,160],2)
				pygame.draw.line(DISPLAYSURF,red,[0,80],[80,160],2)
				pygame.draw.line(DISPLAYSURF,red,[0,60],[100,160],2)
				pygame.draw.line(DISPLAYSURF,red,[0,40],[120,160],2)
				pygame.draw.line(DISPLAYSURF,red,[0,20],[140,160],2)
				pygame.draw.line(DISPLAYSURF,red,[0,0],[160,160],2)
				pygame.draw.line(DISPLAYSURF,red,[20,0],[180,160],2)
				pygame.draw.line(DISPLAYSURF,red,[40,0],[200,160],2)
				pygame.draw.line(DISPLAYSURF,red,[60,0],[220,160],2)
				pygame.draw.line(DISPLAYSURF,red,[80,0],[240,160],2)
				pygame.draw.line(DISPLAYSURF,red,[100,0],[250,140],2)
				pygame.draw.line(DISPLAYSURF,red,[120,0],[250,120],2)
				pygame.draw.line(DISPLAYSURF,red,[140,0],[250,100],2)
				pygame.draw.line(DISPLAYSURF,red,[160,0],[250,80],2)
				pygame.draw.line(DISPLAYSURF,red,[180,0],[250,60],2)
				pygame.draw.line(DISPLAYSURF,red,[200,0],[250,40],2)
				pygame.draw.line(DISPLAYSURF,red,[220,0],[250,20],2)
				pygame.draw.line(DISPLAYSURF,red,[240,0],[250,0],2)
				#bottom-right corner construction
				#front slash
				pygame.draw.line(DISPLAYSURF,red,[230,700],[250,680],2)
				pygame.draw.line(DISPLAYSURF,red,[210,700],[250,660],2)
				pygame.draw.line(DISPLAYSURF,red,[190,700],[250,640],2)
				pygame.draw.line(DISPLAYSURF,red,[170,700],[250,620],2)
				pygame.draw.line(DISPLAYSURF,red,[150,700],[250,600],2)
				pygame.draw.line(DISPLAYSURF,red,[130,700],[250,580],2)
				pygame.draw.line(DISPLAYSURF,red,[110,700],[250,560],2)
				pygame.draw.line(DISPLAYSURF,red,[90,700],[250,540],2)
				pygame.draw.line(DISPLAYSURF,red,[70,700],[230,540],2)
				pygame.draw.line(DISPLAYSURF,red,[50,700],[210,540],2)
				pygame.draw.line(DISPLAYSURF,red,[30,700],[190,540],2)
				pygame.draw.line(DISPLAYSURF,red,[10,700],[170,540],2)
				pygame.draw.line(DISPLAYSURF,red,[0,680],[150,540],2)
				pygame.draw.line(DISPLAYSURF,red,[0,660],[130,540],2)
				pygame.draw.line(DISPLAYSURF,red,[0,640],[110,540],2)
				pygame.draw.line(DISPLAYSURF,red,[0,620],[90,540],2)
				pygame.draw.line(DISPLAYSURF,red,[0,600],[70,540],2)
				pygame.draw.line(DISPLAYSURF,red,[0,580],[50,540],2)
				pygame.draw.line(DISPLAYSURF,red,[0,560],[30,540],2)
				pygame.draw.line(DISPLAYSURF,red,[0,540],[10,540],2)
				#back SLash

				pygame.draw.line(DISPLAYSURF,red,[0,680],[20,700],2)
				pygame.draw.line(DISPLAYSURF,red,[0,660],[40,700],2)
				pygame.draw.line(DISPLAYSURF,red,[0,640],[60,700],2)
				pygame.draw.line(DISPLAYSURF,red,[0,620],[80,700],2)
				pygame.draw.line(DISPLAYSURF,red,[0,600],[100,700],2)
				pygame.draw.line(DISPLAYSURF,red,[0,580],[120,700],2)
				pygame.draw.line(DISPLAYSURF,red,[0,560],[140,700],2)
				pygame.draw.line(DISPLAYSURF,red,[0,540],[160,700],2)

				pygame.draw.line(DISPLAYSURF,red,[20,540],[180,700],2)
				pygame.draw.line(DISPLAYSURF,red,[40,540],[200,700],2)
				pygame.draw.line(DISPLAYSURF,red,[60,540],[220,700],2)
				pygame.draw.line(DISPLAYSURF,red,[80,540],[240,700],2)

				pygame.draw.line(DISPLAYSURF,red,[100,540],[250,680],2)
				pygame.draw.line(DISPLAYSURF,red,[120,540],[250,660],2)
				pygame.draw.line(DISPLAYSURF,red,[140,540],[250,640],2)
				pygame.draw.line(DISPLAYSURF,red,[160,540],[250,620],2)
				pygame.draw.line(DISPLAYSURF,red,[180,540],[250,600],2)
				pygame.draw.line(DISPLAYSURF,red,[200,540],[250,580],2)
				pygame.draw.line(DISPLAYSURF,red,[220,540],[250,560],2)
				pygame.draw.line(DISPLAYSURF,red,[240,540],[250,540],2)
				pygame.draw.line(DISPLAYSURF,red,[250,540],[250,540],2)




				#pygame.draw.line(DISPLAYSURF,red,[,],[,],2)




				#bottom-right corner
				pygame.draw.line(DISPLAYSURF,red,[970,700],[1000,680],2)
				pygame.draw.line(DISPLAYSURF,red,[950,700],[1000,660],2)
				pygame.draw.line(DISPLAYSURF,red,[930,700],[1000,640],2)
				pygame.draw.line(DISPLAYSURF,red,[910,700],[1000,620],2)
				pygame.draw.line(DISPLAYSURF,red,[890,700],[1000,600],2)
				pygame.draw.line(DISPLAYSURF,red,[870,700],[1000,580],2)
				pygame.draw.line(DISPLAYSURF,red,[850,700],[1000,560],2)
				pygame.draw.line(DISPLAYSURF,red,[830,700],[1000,540],2)

				pygame.draw.line(DISPLAYSURF,red,[810,700],[980,540],2)
				pygame.draw.line(DISPLAYSURF,red,[790,700],[960,540],2)
				pygame.draw.line(DISPLAYSURF,red,[770,700],[940,540],2)
				pygame.draw.line(DISPLAYSURF,red,[750,700],[920,540],2)

				pygame.draw.line(DISPLAYSURF,red,[750,680],[900,540],2)
				pygame.draw.line(DISPLAYSURF,red,[750,660],[880,540],2)
				pygame.draw.line(DISPLAYSURF,red,[750,640],[860,540],2)
				pygame.draw.line(DISPLAYSURF,red,[750,620],[840,540],2)
				pygame.draw.line(DISPLAYSURF,red,[750,600],[820,540],2)
				pygame.draw.line(DISPLAYSURF,red,[750,580],[800,540],2)
				pygame.draw.line(DISPLAYSURF,red,[750,560],[780,540],2)
				pygame.draw.line(DISPLAYSURF,red,[750,540],[760,540],2)


				pygame.draw.line(DISPLAYSURF,red,[750,680],[770,700],2)
				pygame.draw.line(DISPLAYSURF,red,[750,660],[790,700],2)
				pygame.draw.line(DISPLAYSURF,red,[750,640],[810,700],2)
				pygame.draw.line(DISPLAYSURF,red,[750,620],[830,700],2)
				pygame.draw.line(DISPLAYSURF,red,[750,600],[850,700],2)
				pygame.draw.line(DISPLAYSURF,red,[750,580],[870,700],2)
				pygame.draw.line(DISPLAYSURF,red,[750,560],[890,700],2)
				pygame.draw.line(DISPLAYSURF,red,[750,540],[910,700],2)

				pygame.draw.line(DISPLAYSURF,red,[770,540],[930,700],2)
				pygame.draw.line(DISPLAYSURF,red,[790,540],[950,700],2)
				pygame.draw.line(DISPLAYSURF,red,[810,540],[970,700],2)
				pygame.draw.line(DISPLAYSURF,red,[830,540],[990,700],2)

				pygame.draw.line(DISPLAYSURF,red,[850,540],[1000,680],2)
				pygame.draw.line(DISPLAYSURF,red,[870,540],[1000,660],2)
				pygame.draw.line(DISPLAYSURF,red,[890,540],[1000,640],2)
				pygame.draw.line(DISPLAYSURF,red,[910,540],[1000,620],2)
				pygame.draw.line(DISPLAYSURF,red,[930,540],[1000,600],2)
				pygame.draw.line(DISPLAYSURF,red,[950,540],[1000,580],2)
				pygame.draw.line(DISPLAYSURF,red,[970,540],[1000,560],2)
				pygame.draw.line(DISPLAYSURF,red,[990,540],[1000,540],2)

				# top - right

				#pygame.draw.line(DISPLAYSURF,red,[,],[,],2)
				pygame.draw.line(DISPLAYSURF,red,[970,160],[1000,140],2)
				pygame.draw.line(DISPLAYSURF,red,[950,160],[1000,120],2)
				pygame.draw.line(DISPLAYSURF,red,[930,160],[1000,100],2)
				pygame.draw.line(DISPLAYSURF,red,[910,160],[1000,80],2)
				pygame.draw.line(DISPLAYSURF,red,[890,160],[1000,60],2)
				pygame.draw.line(DISPLAYSURF,red,[870,160],[1000,40],2)
				pygame.draw.line(DISPLAYSURF,red,[850,160],[1000,20],2)
				pygame.draw.line(DISPLAYSURF,red,[830,160],[1000,0],2)

				pygame.draw.line(DISPLAYSURF,red,[810,160],[980,0],2)
				pygame.draw.line(DISPLAYSURF,red,[790,160],[960,0],2)
				pygame.draw.line(DISPLAYSURF,red,[770,160],[940,0],2)
				pygame.draw.line(DISPLAYSURF,red,[750,160],[920,0],2)

				pygame.draw.line(DISPLAYSURF,red,[750,140],[900,0],2)
				pygame.draw.line(DISPLAYSURF,red,[750,120],[880,0],2)
				pygame.draw.line(DISPLAYSURF,red,[750,100],[860,0],2)
				pygame.draw.line(DISPLAYSURF,red,[750,80],[840,0],2)
				pygame.draw.line(DISPLAYSURF,red,[750,60],[820,0],2)
				pygame.draw.line(DISPLAYSURF,red,[750,40],[800,0],2)
				pygame.draw.line(DISPLAYSURF,red,[750,20],[780,0],2)
				pygame.draw.line(DISPLAYSURF,red,[750,00],[760,0],2)

				pygame.draw.line(DISPLAYSURF,red,[750,140],[770,160],2)
				pygame.draw.line(DISPLAYSURF,red,[750,120],[790,160],2)
				pygame.draw.line(DISPLAYSURF,red,[750,100],[810,160],2)
				pygame.draw.line(DISPLAYSURF,red,[750,80],[830,160],2)
				pygame.draw.line(DISPLAYSURF,red,[750,60],[850,160],2)
				pygame.draw.line(DISPLAYSURF,red,[750,40],[870,160],2)
				pygame.draw.line(DISPLAYSURF,red,[750,20],[890,160],2)
				pygame.draw.line(DISPLAYSURF,red,[750,0],[910,160],2)

				pygame.draw.line(DISPLAYSURF,red,[770,0],[930,160],2)
				pygame.draw.line(DISPLAYSURF,red,[790,0],[950,160],2)
				pygame.draw.line(DISPLAYSURF,red,[810,0],[970,160],2)
				pygame.draw.line(DISPLAYSURF,red,[830,0],[990,160],2)

				pygame.draw.line(DISPLAYSURF,red,[850,0],[1000,140],2)
				pygame.draw.line(DISPLAYSURF,red,[870,0],[1000,120],2)
				pygame.draw.line(DISPLAYSURF,red,[890,0],[1000,100],2)
				pygame.draw.line(DISPLAYSURF,red,[910,0],[1000,80],2)
				pygame.draw.line(DISPLAYSURF,red,[930,0],[1000,60],2)
				pygame.draw.line(DISPLAYSURF,red,[950,0],[1000,40],2)
				pygame.draw.line(DISPLAYSURF,red,[970,0],[1000,20],2)
				pygame.draw.line(DISPLAYSURF,red,[990,0],[1000,0],2)

				#zebra crossing
				#up-down

				pygame.draw.line(DISPLAYSURF,white,[200,180],[240,180],12)
				pygame.draw.line(DISPLAYSURF,white,[200,200],[240,200],12)
				pygame.draw.line(DISPLAYSURF,white,[200,220],[240,220],12)
				pygame.draw.line(DISPLAYSURF,white,[200,240],[240,240],12)
				pygame.draw.line(DISPLAYSURF,white,[200,260],[240,260],12)
				pygame.draw.line(DISPLAYSURF,white,[200,280],[240,280],12)
				pygame.draw.line(DISPLAYSURF,white,[200,300],[240,300],12)
				pygame.draw.line(DISPLAYSURF,white,[200,320],[240,320],12)
				pygame.draw.line(DISPLAYSURF,white,[200,340],[240,340],12)
				pygame.draw.line(DISPLAYSURF,white,[200,360],[240,360],12)
				pygame.draw.line(DISPLAYSURF,white,[200,380],[240,380],12)
				pygame.draw.line(DISPLAYSURF,white,[200,400],[240,400],12)
				pygame.draw.line(DISPLAYSURF,white,[200,420],[240,420],12)
				pygame.draw.line(DISPLAYSURF,white,[200,440],[240,440],12)
				pygame.draw.line(DISPLAYSURF,white,[200,460],[240,460],12)
				pygame.draw.line(DISPLAYSURF,white,[200,480],[240,480],12)
				pygame.draw.line(DISPLAYSURF,white,[200,500],[240,500],12)
				pygame.draw.line(DISPLAYSURF,white,[200,520],[240,520],12)
				#pygame.draw.line(DISPLAYSURF,white,[200,160],[200,540],4)
				#pygame.draw.line(DISPLAYSURF,white,[240,160],[240,540],4)


				#left-right : bottom
				pygame.draw.line(DISPLAYSURF,white,[730,550],[730,590],12)
				pygame.draw.line(DISPLAYSURF,white,[710,550],[710,590],12)
				pygame.draw.line(DISPLAYSURF,white,[690,550],[690,590],12)
				pygame.draw.line(DISPLAYSURF,white,[670,550],[670,590],12)
				pygame.draw.line(DISPLAYSURF,white,[650,550],[650,590],12)
				pygame.draw.line(DISPLAYSURF,white,[630,550],[630,590],12)
				pygame.draw.line(DISPLAYSURF,white,[610,550],[610,590],12)
				pygame.draw.line(DISPLAYSURF,white,[590,550],[590,590],12)
				pygame.draw.line(DISPLAYSURF,white,[570,550],[570,590],12)
				pygame.draw.line(DISPLAYSURF,white,[550,550],[550,590],12)
				pygame.draw.line(DISPLAYSURF,white,[530,550],[530,590],12)
				pygame.draw.line(DISPLAYSURF,white,[510,550],[510,590],12)
				pygame.draw.line(DISPLAYSURF,white,[490,550],[490,590],12)
				pygame.draw.line(DISPLAYSURF,white,[470,550],[470,590],12)
				pygame.draw.line(DISPLAYSURF,white,[450,550],[450,590],12)
				pygame.draw.line(DISPLAYSURF,white,[430,550],[430,590],12)
				pygame.draw.line(DISPLAYSURF,white,[410,550],[410,590],12)
				pygame.draw.line(DISPLAYSURF,white,[390,550],[390,590],12)
				pygame.draw.line(DISPLAYSURF,white,[370,550],[370,590],12)
				pygame.draw.line(DISPLAYSURF,white,[350,550],[350,590],12)
				pygame.draw.line(DISPLAYSURF,white,[330,550],[330,590],12)
				pygame.draw.line(DISPLAYSURF,white,[310,550],[310,590],12)
				pygame.draw.line(DISPLAYSURF,white,[290,550],[290,590],12)
				pygame.draw.line(DISPLAYSURF,white,[270,550],[270,590],12)
				#bottom-top 
				pygame.draw.line(DISPLAYSURF,white,[760,520],[800,520],12)
				pygame.draw.line(DISPLAYSURF,white,[760,500],[800,500],12)
				pygame.draw.line(DISPLAYSURF,white,[760,480],[800,480],12)
				pygame.draw.line(DISPLAYSURF,white,[760,460],[800,460],12)
				pygame.draw.line(DISPLAYSURF,white,[760,440],[800,440],12)
				pygame.draw.line(DISPLAYSURF,white,[760,420],[800,420],12)
				pygame.draw.line(DISPLAYSURF,white,[760,400],[800,400],12)
				pygame.draw.line(DISPLAYSURF,white,[760,380],[800,380],12)
				pygame.draw.line(DISPLAYSURF,white,[760,360],[800,360],12)
				pygame.draw.line(DISPLAYSURF,white,[760,340],[800,340],12)
				pygame.draw.line(DISPLAYSURF,white,[760,320],[800,320],12)
				pygame.draw.line(DISPLAYSURF,white,[760,300],[800,300],12)
				pygame.draw.line(DISPLAYSURF,white,[760,280],[800,280],12)
				pygame.draw.line(DISPLAYSURF,white,[760,260],[800,260],12)
				pygame.draw.line(DISPLAYSURF,white,[760,240],[800,240],12)
				pygame.draw.line(DISPLAYSURF,white,[760,220],[800,220],12)
				pygame.draw.line(DISPLAYSURF,white,[760,200],[800,200],12)
				pygame.draw.line(DISPLAYSURF,white,[760,180],[800,180],12)
				#right-left
				pygame.draw.line(DISPLAYSURF,white,[730,150],[730,110],12)
				pygame.draw.line(DISPLAYSURF,white,[710,150],[710,110],12)
				pygame.draw.line(DISPLAYSURF,white,[690,150],[690,110],12)
				pygame.draw.line(DISPLAYSURF,white,[670,150],[670,110],12)
				pygame.draw.line(DISPLAYSURF,white,[650,150],[650,110],12)
				pygame.draw.line(DISPLAYSURF,white,[630,150],[630,110],12)
				pygame.draw.line(DISPLAYSURF,white,[610,150],[610,110],12)
				pygame.draw.line(DISPLAYSURF,white,[590,150],[590,110],12)
				pygame.draw.line(DISPLAYSURF,white,[570,150],[570,110],12)
				pygame.draw.line(DISPLAYSURF,white,[550,150],[550,110],12)
				pygame.draw.line(DISPLAYSURF,white,[530,150],[530,110],12)
				pygame.draw.line(DISPLAYSURF,white,[510,150],[510,110],12)
				pygame.draw.line(DISPLAYSURF,white,[490,150],[490,110],12)
				pygame.draw.line(DISPLAYSURF,white,[470,150],[470,110],12)
				pygame.draw.line(DISPLAYSURF,white,[450,150],[450,110],12)
				pygame.draw.line(DISPLAYSURF,white,[430,150],[430,110],12)
				pygame.draw.line(DISPLAYSURF,white,[410,150],[410,110],12)
				pygame.draw.line(DISPLAYSURF,white,[390,150],[390,110],12)
				pygame.draw.line(DISPLAYSURF,white,[370,150],[370,110],12)
				pygame.draw.line(DISPLAYSURF,white,[350,150],[350,110],12)
				pygame.draw.line(DISPLAYSURF,white,[330,150],[330,110],12)
				pygame.draw.line(DISPLAYSURF,white,[310,150],[310,110],12)
				pygame.draw.line(DISPLAYSURF,white,[290,150],[290,110],12)
				pygame.draw.line(DISPLAYSURF,white,[270,150],[270,110],12)

				#construction of road divider -> x-axis

				pygame.draw.line(DISPLAYSURF,white,[0,350],[20,350],2)
				pygame.draw.line(DISPLAYSURF,white,[30,350],[50,350],2)
				pygame.draw.line(DISPLAYSURF,white,[60,350],[80,350],2)
				pygame.draw.line(DISPLAYSURF,white,[90,350],[110,350],2)
				pygame.draw.line(DISPLAYSURF,white,[120,350],[140,350],2)
				pygame.draw.line(DISPLAYSURF,white,[150,350],[170,350],2)
				pygame.draw.line(DISPLAYSURF,white,[180,350],[200,350],2)
				pygame.draw.line(DISPLAYSURF,white,[210,350],[230,350],2)
				pygame.draw.line(DISPLAYSURF,white,[240,350],[260,350],2)
				pygame.draw.line(DISPLAYSURF,white,[270,350],[290,350],2)
				pygame.draw.line(DISPLAYSURF,white,[300,350],[320,350],2)
				pygame.draw.line(DISPLAYSURF,white,[330,350],[350,350],2)
				pygame.draw.line(DISPLAYSURF,white,[360,350],[380,350],2)
				pygame.draw.line(DISPLAYSURF,white,[390,350],[410,350],2)
				pygame.draw.line(DISPLAYSURF,white,[420,350],[440,350],2)
				pygame.draw.line(DISPLAYSURF,white,[450,350],[470,350],2)
				pygame.draw.line(DISPLAYSURF,white,[480,350],[500,350],2)
				pygame.draw.line(DISPLAYSURF,white,[510,350],[530,350],2)
				pygame.draw.line(DISPLAYSURF,white,[540,350],[560,350],2)
				pygame.draw.line(DISPLAYSURF,white,[570,350],[590,350],2)
				pygame.draw.line(DISPLAYSURF,white,[600,350],[620,350],2)
				pygame.draw.line(DISPLAYSURF,white,[630,350],[650,350],2)
				pygame.draw.line(DISPLAYSURF,white,[660,350],[680,350],2)
				pygame.draw.line(DISPLAYSURF,white,[690,350],[710,350],2)
				pygame.draw.line(DISPLAYSURF,white,[720,350],[740,350],2)
				pygame.draw.line(DISPLAYSURF,white,[750,350],[770,350],2)
				pygame.draw.line(DISPLAYSURF,white,[780,350],[800,350],2)
				pygame.draw.line(DISPLAYSURF,white,[810,350],[830,350],2)
				pygame.draw.line(DISPLAYSURF,white,[840,350],[860,350],2)
				pygame.draw.line(DISPLAYSURF,white,[870,350],[890,350],2)
				pygame.draw.line(DISPLAYSURF,white,[900,350],[920,350],2)
				pygame.draw.line(DISPLAYSURF,white,[930,350],[950,350],2)
				pygame.draw.line(DISPLAYSURF,white,[960,350],[980,350],2)



				# road divider  --> y-axis

				pygame.draw.line(DISPLAYSURF,white,[500,0],[500,20],2)
				pygame.draw.line(DISPLAYSURF,white,[500,30],[500,50],2)
				pygame.draw.line(DISPLAYSURF,white,[500,60],[500,80],2)
				pygame.draw.line(DISPLAYSURF,white,[500,90],[500,110],2)
				pygame.draw.line(DISPLAYSURF,white,[500,120],[500,140],2)
				pygame.draw.line(DISPLAYSURF,white,[500,150],[500,170],2)
				pygame.draw.line(DISPLAYSURF,white,[500,180],[500,200],2)
				pygame.draw.line(DISPLAYSURF,white,[500,210],[500,230],2)
				pygame.draw.line(DISPLAYSURF,white,[500,240],[500,260],2)
				pygame.draw.line(DISPLAYSURF,white,[500,270],[500,290],2)
				pygame.draw.line(DISPLAYSURF,white,[500,300],[500,320],2)
				pygame.draw.line(DISPLAYSURF,white,[500,330],[500,350],2)
				pygame.draw.line(DISPLAYSURF,white,[500,360],[500,380],2)
				pygame.draw.line(DISPLAYSURF,white,[500,390],[500,410],2)
				pygame.draw.line(DISPLAYSURF,white,[500,420],[500,440],2)
				pygame.draw.line(DISPLAYSURF,white,[500,450],[500,470],2)
				pygame.draw.line(DISPLAYSURF,white,[500,480],[500,500],2)
				pygame.draw.line(DISPLAYSURF,white,[500,510],[500,530],2)
				pygame.draw.line(DISPLAYSURF,white,[500,540],[500,560],2)
				pygame.draw.line(DISPLAYSURF,white,[500,570],[500,590],2)
				pygame.draw.line(DISPLAYSURF,white,[500,600],[500,620],2)
				pygame.draw.line(DISPLAYSURF,white,[500,630],[500,650],2)
				pygame.draw.line(DISPLAYSURF,white,[500,660],[500,680],2)
				pygame.draw.circle(DISPLAYSURF,silver,(500,350),40)
				DISPLAYSURF.blit(textSurfaceObj, textRectObj)
				DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
				DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
				#DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)



				#signal line construction on 3 lanes:

				pygame.draw.line(DISPLAYSURF,red,[250,160],[250,350],4)
				pygame.draw.line(DISPLAYSURF,red,[500,160],[750,160],4)
				pygame.draw.line(DISPLAYSURF,green,[250,540],[500,540],4)
				pygame.draw.line(DISPLAYSURF,red,[750,540],[750,350],4)

				#circular sensor representation
				pygame.draw.circle(DISPLAYSURF,red,(190,160),10)
				pygame.draw.circle(DISPLAYSURF,red,(190,350),10)
				pygame.draw.circle(DISPLAYSURF,green,(500,600),10)
				pygame.draw.circle(DISPLAYSURF,green,(250,600),10)
				pygame.draw.circle(DISPLAYSURF,red,(750,105),10)
				pygame.draw.circle(DISPLAYSURF,red,(500,105),10)
				pygame.draw.circle(DISPLAYSURF,red,(810,350),10)
				pygame.draw.circle(DISPLAYSURF,red,(810,540),10)

				pygame.draw.line(DISPLAYSURF,red,[190,160],[190,350])
				pygame.draw.line(DISPLAYSURF,red,[810,350],[810,540])
				pygame.draw.line(DISPLAYSURF,red,[750,105],[500,105])
				pygame.draw.line(DISPLAYSURF,green,[500,600],[250,600])




				#static car on rest of the lanes
				# bottom-left lane
				
				#top-right lane

				pygame.draw.rect(DISPLAYSURF,yellow,(530,40,40,40))
				pygame.draw.rect(DISPLAYSURF,teal,(610,40,40,40))
				pygame.draw.rect(DISPLAYSURF,aqua,(670,00,60,90))
				pygame.draw.rect(DISPLAYSURF,gray,(610,10,20,20))
				pygame.draw.rect(DISPLAYSURF,yellow,(580,50,20,20))
				#pygame.draw.rect(DISPLAYSURF,red,(320,660,40,40),2)


				


				pygame.draw.rect(DISPLAYSURF,green,(x,y,80,40))
				pygame.draw.rect(DISPLAYSURF,fuchsia,(x1,y1,20,20))
				pygame.draw.rect(DISPLAYSURF,aqua,(x3,y3,30,50),2)
				pygame.draw.rect(DISPLAYSURF,aqua,(x4,y4,40,40))
				pygame.draw.rect(DISPLAYSURF,fuchsia,(x5,y5,40,40))
				pygame.draw.rect(DISPLAYSURF,purple,(x6,y5,40,40))
				#pygame.draw.rect(DISPLAYSURF,olive,(x7,y7,30,30))
				#pygame.draw.rect(DISPLAYSURF,teal,(x8,y8,40,40))
				pygame.draw.rect(DISPLAYSURF,yellow,(x9,y9,40,40))
				pygame.draw.rect(DISPLAYSURF,silver,(x10,y10,20,20))
				pygame.draw.rect(DISPLAYSURF,maroon,(x11,y11,10,70))
				pygame.draw.line(DISPLAYSURF,green,[250,540],[500,540],4)




				#delay loop counter
				for i in range (0,1000000):
					continue
				for i in range (0,1000000):
					continue
				for i in range (0,1000000):
					continue
				x = x +4
				 
				y3 = y3 +3
				y1 = y1 -4
				y4 = y4-3
				y5 = y5 -2
				y6 = y6-2
				y7 = y7 -2
				y8 = y8 -3
				y9 = y9-4
				y10 = y10-6
				y11 = y11-5
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
				pygame.display.update()
				fpsClock.tick(FPS)
				m = 1
		#new frame starts: main bluetooth explaination frame.
		if m == 1:
			a1 =120
			b1 =150
			a2 =50
			b2 =150
			a3 =00
			b3 =270
			a4 =0
			b4 =0
			i =0	

			while a1 < 520:
				DISPLAYSURF.fill(black)
				# construction of border for road

				pygame.draw.line(DISPLAYSURF,white,[0,100],[600,100],2)
				pygame.draw.line(DISPLAYSURF,white,[0,600],[600,600],2)
				pygame.draw.line(DISPLAYSURF,white,[600,100],[600,0],2)	
				pygame.draw.line(DISPLAYSURF,white,[600,600],[600,700],2)
				pygame.draw.rect(DISPLAYSURF,gray,(0,0,600,100))
				pygame.draw.rect(DISPLAYSURF,gray,(0,600,600,100))

				#construction of building and foothpath
				#top block
				pygame.draw.line(DISPLAYSURF,blac,[30,0],[30,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[60,0],[60,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[90,0],[90,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[120,0],[120,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[150,0],[150,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[180,0],[180,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[210,0],[210,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[240,0],[240,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[270,0],[270,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[300,0],[300,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[330,0],[330,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[360,0],[360,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[390,0],[390,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[420,0],[420,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[450,0],[450,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[480,0],[480,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[510,0],[510,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[540,0],[540,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[570,0],[570,100],2)
				pygame.draw.line(DISPLAYSURF,blac,[0,20],[600,20],2)
				pygame.draw.line(DISPLAYSURF,blac,[0,40],[600,40],2)
				pygame.draw.line(DISPLAYSURF,blac,[0,60],[600,60],2)
				pygame.draw.line(DISPLAYSURF,blac,[0,80],[600,80],2)
				#pygame.draw.line(DISPLAYSURF,black,[0,],[600,],2)

				#bottom block
				#pygame.draw.line(DISPLAYSURF,black,[,],[,],2)
				pygame.draw.line(DISPLAYSURF,blac,[30,600],[30,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[60,600],[60,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[90,600],[90,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[120,600],[120,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[150,600],[150,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[180,600],[180,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[210,600],[210,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[240,600],[240,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[270,600],[270,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[300,600],[300,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[330,600],[330,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[360,600],[360,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[390,600],[390,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[420,600],[420,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[450,600],[450,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[480,600],[480,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[510,600],[510,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[540,600],[540,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[570,600],[570,700],2)
				pygame.draw.line(DISPLAYSURF,blac,[0,620],[600,620],2)
				pygame.draw.line(DISPLAYSURF,blac,[0,640],[600,640],2)
				pygame.draw.line(DISPLAYSURF,blac,[0,660],[600,660],2)
				pygame.draw.line(DISPLAYSURF,blac,[0,680],[600,680],2)
				#pygame.draw.line(DISPLAYSURF,black,[0,],[600,],2)



				#construction of zebra crossing

				pygame.draw.line(DISPLAYSURF,white,[550,120],[590,120],12)
				pygame.draw.line(DISPLAYSURF,white,[550,140],[590,140],12)
				pygame.draw.line(DISPLAYSURF,white,[550,160],[590,160],12)
				pygame.draw.line(DISPLAYSURF,white,[550,180],[590,180],12)
				pygame.draw.line(DISPLAYSURF,white,[550,200],[590,200],12)
				pygame.draw.line(DISPLAYSURF,white,[550,220],[590,220],12)
				pygame.draw.line(DISPLAYSURF,white,[550,240],[590,240],12)
				pygame.draw.line(DISPLAYSURF,white,[550,260],[590,260],12)
				pygame.draw.line(DISPLAYSURF,white,[550,280],[590,280],12)
				pygame.draw.line(DISPLAYSURF,white,[550,300],[590,300],12)
				pygame.draw.line(DISPLAYSURF,white,[550,320],[590,320],12)
				pygame.draw.line(DISPLAYSURF,white,[550,340],[590,340],12)
				pygame.draw.line(DISPLAYSURF,white,[550,360],[590,360],12)
				pygame.draw.line(DISPLAYSURF,white,[550,380],[590,380],12)
				pygame.draw.line(DISPLAYSURF,white,[550,400],[590,400],12)
				pygame.draw.line(DISPLAYSURF,white,[550,420],[590,420],12)
				pygame.draw.line(DISPLAYSURF,white,[550,440],[590,440],12)
				pygame.draw.line(DISPLAYSURF,white,[550,460],[590,460],12)
				pygame.draw.line(DISPLAYSURF,white,[550,480],[590,480],12)
				pygame.draw.line(DISPLAYSURF,white,[550,500],[590,500],12)
				pygame.draw.line(DISPLAYSURF,white,[550,520],[590,520],12)
				pygame.draw.line(DISPLAYSURF,white,[550,540],[590,540],12)
				pygame.draw.line(DISPLAYSURF,white,[550,560],[590,560],12)
				pygame.draw.line(DISPLAYSURF,white,[550,580],[590,580],12)
			
				#construction of road divider -> x-axis

				pygame.draw.line(DISPLAYSURF,white,[0,350],[20,350],2)
				pygame.draw.line(DISPLAYSURF,white,[30,350],[50,350],2)
				pygame.draw.line(DISPLAYSURF,white,[60,350],[80,350],2)
				pygame.draw.line(DISPLAYSURF,white,[90,350],[110,350],2)
				pygame.draw.line(DISPLAYSURF,white,[120,350],[140,350],2)
				pygame.draw.line(DISPLAYSURF,white,[150,350],[170,350],2)
				pygame.draw.line(DISPLAYSURF,white,[180,350],[200,350],2)
				pygame.draw.line(DISPLAYSURF,white,[210,350],[230,350],2)
				pygame.draw.line(DISPLAYSURF,white,[240,350],[260,350],2)
				pygame.draw.line(DISPLAYSURF,white,[270,350],[290,350],2)
				pygame.draw.line(DISPLAYSURF,white,[300,350],[320,350],2)
				pygame.draw.line(DISPLAYSURF,white,[330,350],[350,350],2)
				pygame.draw.line(DISPLAYSURF,white,[360,350],[380,350],2)
				pygame.draw.line(DISPLAYSURF,white,[390,350],[410,350],2)
				pygame.draw.line(DISPLAYSURF,white,[420,350],[440,350],2)
				pygame.draw.line(DISPLAYSURF,white,[450,350],[470,350],2)
				pygame.draw.line(DISPLAYSURF,white,[480,350],[500,350],2)
				pygame.draw.line(DISPLAYSURF,white,[510,350],[530,350],2)
				pygame.draw.line(DISPLAYSURF,white,[540,350],[560,350],2)
				pygame.draw.line(DISPLAYSURF,white,[570,350],[590,350],2)
				pygame.draw.line(DISPLAYSURF,white,[600,350],[620,350],2)
				pygame.draw.line(DISPLAYSURF,white,[630,350],[650,350],2)
				pygame.draw.line(DISPLAYSURF,white,[660,350],[680,350],2)
				pygame.draw.line(DISPLAYSURF,white,[690,350],[710,350],2)
				pygame.draw.line(DISPLAYSURF,white,[720,350],[740,350],2)
				pygame.draw.line(DISPLAYSURF,white,[750,350],[770,350],2)
				pygame.draw.line(DISPLAYSURF,white,[780,350],[800,350],2)
				pygame.draw.line(DISPLAYSURF,white,[810,350],[830,350],2)
				pygame.draw.line(DISPLAYSURF,white,[840,350],[860,350],2)
				pygame.draw.line(DISPLAYSURF,white,[870,350],[890,350],2)
				pygame.draw.line(DISPLAYSURF,white,[900,350],[920,350],2)
				pygame.draw.line(DISPLAYSURF,white,[930,350],[950,350],2)
				pygame.draw.line(DISPLAYSURF,white,[960,350],[980,350],2)
				#DISPLAYSURF.blit(textSurfaceObj, textRectObj)
				#DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
				#DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
				DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)

				
				#construction of signal depicting line:
				pygame.draw.line(DISPLAYSURF,red,[600,100],[600,350],4)
				pygame.draw.circle(DISPLAYSURF,red,(545,100),10)
				pygame.draw.circle(DISPLAYSURF,red,(545,350),10)
				pygame.draw.line(DISPLAYSURF,red,[545,100],[545,350])

				#this ends the basic scenario of zoom road depiction
				''' this time our main road that was green in last frame is basically blocked and now our animation for illegal 					issues start'''

				
				pygame.draw.rect(DISPLAYSURF,yellow,(a1,b1,60,40))
				pygame.draw.rect(DISPLAYSURF,yellow,(a2,b2,40,30))
				pygame.draw.rect(DISPLAYSURF,yellow,(a3,b3,50,40))
				pygame.draw.line(DISPLAYSURF,red,[600,100],[600,350],4)

				a1 = a1 +2
				a2= a2 + 2
				a3= a3+4

				if a3 > 600:
					break
				'''
				if a1 == 519:
					DISPLAYSURF.fill(black)
					# construction of border for road
	
					pygame.draw.line(DISPLAYSURF,white,[0,100],[600,100],2)
					pygame.draw.line(DISPLAYSURF,white,[0,600],[600,600],2)
					pygame.draw.line(DISPLAYSURF,white,[600,100],[600,0],2)	
					pygame.draw.line(DISPLAYSURF,white,[600,600],[600,700],2)
				
					#construction of road divider -> x-axis
	
					pygame.draw.line(DISPLAYSURF,white,[0,350],[20,350],2)
					pygame.draw.line(DISPLAYSURF,white,[30,350],[50,350],2)
					pygame.draw.line(DISPLAYSURF,white,[60,350],[80,350],2)
					pygame.draw.line(DISPLAYSURF,white,[90,350],[110,350],2)
					pygame.draw.line(DISPLAYSURF,white,[120,350],[140,350],2)
					pygame.draw.line(DISPLAYSURF,white,[150,350],[170,350],2)
					pygame.draw.line(DISPLAYSURF,white,[180,350],[200,350],2)
					pygame.draw.line(DISPLAYSURF,white,[210,350],[230,350],2)
					pygame.draw.line(DISPLAYSURF,white,[240,350],[260,350],2)
					pygame.draw.line(DISPLAYSURF,white,[270,350],[290,350],2)
					pygame.draw.line(DISPLAYSURF,white,[300,350],[320,350],2)
					pygame.draw.line(DISPLAYSURF,white,[330,350],[350,350],2)
					pygame.draw.line(DISPLAYSURF,white,[360,350],[380,350],2)
					pygame.draw.line(DISPLAYSURF,white,[390,350],[410,350],2)
					pygame.draw.line(DISPLAYSURF,white,[420,350],[440,350],2)
					pygame.draw.line(DISPLAYSURF,white,[450,350],[470,350],2)
					pygame.draw.line(DISPLAYSURF,white,[480,350],[500,350],2)
					pygame.draw.line(DISPLAYSURF,white,[510,350],[530,350],2)
					pygame.draw.line(DISPLAYSURF,white,[540,350],[560,350],2)
					pygame.draw.line(DISPLAYSURF,white,[570,350],[590,350],2)
					pygame.draw.line(DISPLAYSURF,white,[600,350],[620,350],2)
					pygame.draw.line(DISPLAYSURF,white,[630,350],[650,350],2)
					pygame.draw.line(DISPLAYSURF,white,[660,350],[680,350],2)
					pygame.draw.line(DISPLAYSURF,white,[690,350],[710,350],2)
					pygame.draw.line(DISPLAYSURF,white,[720,350],[740,350],2)
					pygame.draw.line(DISPLAYSURF,white,[750,350],[770,350],2)
					pygame.draw.line(DISPLAYSURF,white,[780,350],[800,350],2)
					pygame.draw.line(DISPLAYSURF,white,[810,350],[830,350],2)
					pygame.draw.line(DISPLAYSURF,white,[840,350],[860,350],2)
					pygame.draw.line(DISPLAYSURF,white,[870,350],[890,350],2)
					pygame.draw.line(DISPLAYSURF,white,[900,350],[920,350],2)
					pygame.draw.line(DISPLAYSURF,white,[930,350],[950,350],2)
					pygame.draw.line(DISPLAYSURF,white,[960,350],[980,350],2)
					
					#construction of signal depicting line:
					pygame.draw.line(DISPLAYSURF,red,[600,100],[600,350],2)
	
					#this ends the basic scenario of zoom road depiction
					

				
					pygame.draw.rect(DISPLAYSURF,yellow,(a1,b1,60,40),2)
					pygame.draw.rect(DISPLAYSURF,yellow,(a2,b2,40,30),2)
					pygame.draw.rect(DISPLAYSURF,yellow,(a3,b3,50,40),2)
					a3 = a3 +2

					#final quit event
					for event in pygame.event.get():
						if event.type == QUIT:
							pygame.quit()
							sys.exit()
					pygame.display.update()
					fpsClock.tick(FPS)
					'''









				#this is the quit event for the 2nd zoom frame
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
				pygame.display.update()
				fpsClock.tick(FPS)


				

		






		#don't even touch this part of code.
			
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()
		fpsClock.tick(FPS)
	

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	fpsClock.tick(FPS)
	sys.exit()










