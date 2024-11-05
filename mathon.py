import pygame
import random 
pygame.init()

screen = pygame.display.set_mode((720,720))

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()
		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
			action  = False
		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))
		return action
		
class Math:
    def __init__(self):
        self.num = None
        self.ans = None
        self.p1 = None
        self.p2 = None
        self.p3 = None
        self.p4 = None
        self.op_list = None
        self.level = 1
        self.dlevel = 1
       
    def generate_question(self):
        self.dlevel += 1
        if self.dlevel % 10 == 0:
        	self.level += 1
        dif = self.level*10
        a = random.randint(1,dif)
        b = random.randint(1,dif)
        oq=["+","-","*"]
        oa=random.choice(oq)
        if oa == "+" :
        	self.num = f"{a} + {b}"
        	self.ans = a+b
        if oa == "-" :
        	self.num = f"{a} - {b}"
        	self.ans = a-b
        if oa == "*" :
        	self.num = f"{a} X {b}"
        	self.ans = a*b
        os = [self.ans - 10, self.ans + 20, self.ans - 3, self.ans]
        self.p1 = random.choice(os)
        os.remove(self.p1)
        self.p2 = random.choice(os)
        os.remove(self.p2)
        self.p3 = random.choice(os)
        os.remove(self.p3)
        self.p4 = random.choice(os)
        os.remove(self.p4)
        self.op_list= [self.p1,self.p2,self.p3,self.p4,self.ans]
        return self.num

    def render_question(self, screen, font1):
        op1 = font1.render(f"{self.p1}", False, (255, 255, 255))
        screen.blit(op1, (100, 710))
        op2 = font1.render(f"{self.p2}", False, (255, 255, 255))
        screen.blit(op2, (100, 910))
        op3 = font1.render(f"{self.p3}", False, (255, 255, 255))
        screen.blit(op3, (480, 710))
        op4 = font1.render(f"{self.p4}", False, (255, 255, 255))
        screen.blit(op4, (480, 910))
        Level = font1.render(f"Level : {self.level}",False,(255,255,255))
        screen.blit(Level,(130,170))
        self.op_list=[self.p1,self.p2,self.p3,self.p4,self.ans]
     
        return self.op_list
        
def Heart (A = 400,B = 400):
	heart = pygame.Surface((80,80),pygame.SRCALPHA)
	heart.fill((255,0,0,255))
	heart= pygame.transform.rotate(heart,45)
	screen.blit(heart,(A,B))
	pygame.draw.circle(screen,(255,0,0),(A+25,B +25),40)
	pygame.draw.circle(screen,(255,0,0),(A + 87,B + 25),40)
	

#fonts
font = pygame.font.Font("freesansbold.ttf",160)
font1 = pygame.font.Font("freesansbold.ttf",110)
font2 = pygame.font.Font("freesansbold.ttf",50)
font3 = pygame.font.Font("freesansbold.ttf",150)
font4 = pygame.font.Font("freesansbold.ttf",50)

#buttons png
but_j = pygame.Surface((250,100),pygame.SRCALPHA)
but_j.fill((255,0,0,0))

but_J = pygame.Surface((50,50),pygame.SRCALPHA)
but_J.fill((255,0,0,0))

but_0 = Button(290, 1100, but_J, 3)

but_1 = Button(10, 700, but_j, 1.3)

but_2 = Button(10, 900, but_j, 1.3)

but_3 = Button(380, 700, but_j, 1.3)

but_4 = Button(380, 900, but_j, 1.3)



bar = pygame.Surface((1120,145))
bar.fill((173,198,255))

#transparent background 
surf = pygame.Surface((900,1700),pygame.SRCALPHA)
surf.fill((0,0,0,200))


point =0
Math1 = Math()
num = Math1.generate_question()
op_list = Math1.render_question(screen,font1)

health = 3

optionA =False
optionB =False
optionC =False
optionD =False
game_active = False
tiks = pygame.time.get_ticks()


while True :

	screen.fill((16,19,24))
	
	if op_list[4] == op_list[0]: optionA =True
	if op_list[4] == op_list[1]: optionB =True
	if op_list[4] == op_list[2]: optionC =True
	if op_list[4] == op_list[3]: optionD =True
	
	if but_1.draw(screen) and game_active:
		num = Math1.generate_question()
		op_list = Math1.render_question(screen,font1)
		outline1 =10
		if optionA:
			if game_active:
				point += 1
		else :
			if game_active:
				health -= 1
			
	if but_2.draw(screen)and game_active:
		num = Math1.generate_question()
		op_list = Math1.render_question(screen,font1)
		if optionB:
			if game_active:
				point += 1
		else :
			if game_active:
				health -= 1
			
	if but_3.draw(screen)and game_active:
		num = Math1.generate_question()
		op_list = Math1.render_question(screen,font1)
		if optionC :
			if game_active:
				point += 1
		else :
			if game_active:
				health -= 1
			
	if but_4.draw(screen)and game_active:
		num = Math1.generate_question()
		op_list = Math1.render_question(screen,font1)
		if optionD:
			if game_active:
				point += 1
		else :
			if game_active:
				health -= 1
			
	optionA =False
	optionB =False
	optionC =False
	optionD =False
	pygame.draw.rect(screen,(173,198,255),(10,700,320,130),0,50)
	pygame.draw.rect(screen,(173,198,255),(10,900,320,130),0,50)
	pygame.draw.rect(screen,(173,198,255),(380,700,320,130),0,50)
	pygame.draw.rect(screen,(173,198,255),(380,900,320,130),0,50)	
	if health == 0 :
		game_active = False
		health = 3

	
	
# question bars
	screen.blit(bar,(-200,370))
	
	#harts
	if health >= 1:
		Heart(100,1150)
	if health >= 2:
		Heart(300,1150)
	if health == 3:
		Heart(500,1150)
	
	#options
	text = font.render(f"{num}",False,(255,255,255))
	screen.blit(text,(70,370))
	
	score = font1.render(f"Point : {point}",False,(255,255,255))
	screen.blit(score,(120,30))
	
	
	Math1.render_question(screen,font1)
	
	if game_active == False and point ==0 :
		screen.blit(surf, (0,0))
		game = font3.render("Mathon",False,(255,255,255))
		screen.blit(game,(80,310))
		game = font4.render("Power by Janak",False,(255,255,255))
		screen.blit(game,(150,450))
		pygame.draw.circle(screen,(255,255,255),(370,1170),70,10)
		if but_0.draw(screen):
			game_active = True
			health = 3
			point = 0
			Math1.level = 1
			
	if game_active == False and point >= 1:
		screen.blit(surf, (0,0))
		game = font1.render("Game Over",False,(255,255,255))
		screen.blit(game,(50,400))
		start_t = font1.render("start",False,(255,255,255))
		pygame.draw.rect(screen,(255,255,255),(290,1100,150,150),10,254)
		screen.blit(start_t,(230,1000))
		screen.blit(score,(100,530))
		if but_0.draw(screen):
			game_active = True
			health = 3
			point = 0
			Math1.level = 1
	
		
	pygame.display.update()