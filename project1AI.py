#Cristian Cedeno
#N01369950

import pygame
from shapely.geometry import Polygon, LineString
from queue import PriorityQueue
import math

pygame.init()

white = (255,255,255)
black = (0,0,0,)

red = (255,0,0)
green=(0,255,0)
blue=(0,0,255)


gameDisplay = pygame.display.set_mode((1000,500))
gameDisplay.fill(white)

dot = pygame.PixelArray(gameDisplay)



start= pygame.draw.circle(gameDisplay, green, (75, 400), 10)

sOne = pygame.draw.polygon(gameDisplay, blue, ((200, 350),(200, 450), (450,450),(450, 350)), 3)
sTwo = pygame.draw.polygon(gameDisplay, blue, ((120, 130), (150, 245), (275, 275),(300, 120),(200, 5)), 3)
sThree = pygame.draw.polygon(gameDisplay, blue, ((300, 300), (400, 300), (350, 100)), 3)
sFour = pygame.draw.polygon(gameDisplay, blue, ((425, 30), (400, 175), (575, 100), (550, 25)), 3)
sFive = pygame.draw.polygon(gameDisplay, blue, ((545, 260), (520, 400), (625, 375)), 3)
sSix = pygame.draw.polygon(gameDisplay, blue, ((600, 40),(600, 290), (750, 290), (750, 40)), 3)
sSeven = pygame.draw.polygon(gameDisplay, blue, ((640, 375), (640, 440), (700, 475), (755,440), (755,375), (700,320)), 3)
sEight = pygame.draw.polygon(gameDisplay, blue, ((775, 75),(810, 350), (885, 75), (830,20)), 3)

pygame.draw.circle(gameDisplay, red, (925, 75), 10)



pList = []

pList.append(Polygon([(200, 350),(200, 450), (450,450),(450, 350)]))
pList.append(Polygon([(120, 130), (150, 245), (275, 275),(300, 120),(200, 5)]))
pList.append(Polygon([(300, 300), (400, 300), (350, 100)]))
pList.append(Polygon([(425, 30), (400, 175), (575, 100), (550, 25)]))
pList.append(Polygon([(545, 260), (520, 400), (625, 375)]))
pList.append(Polygon([(600, 40),(600, 290), (750, 290), (750, 40)]))
pList.append(Polygon([(640, 375), (640, 440), (700, 475), (755,440), (755,375), (700,320)]))
pList.append(Polygon([(775, 75),(810, 350), (885, 75), (830,20)]))

vertexList = []


class Graph:
	
	matrixTable = []

	def __init__(self, nodes, matSize):
		self.nodes = nodes
		self.matSize = matSize

		for x in range(matSize):
			self.matrixTable.append([])
			for y in range(matSize):
				self.matrixTable[x].append(0)

	def printMatrixTable(self):

		for m in self.matrixTable:
			print(m)

	def addEdge(self, s, e):
		self.matrixTable[s][e] = 1
		self.matrixTable[e][s] = 1


class Vertex:
    

    def __init__(self, x, y):
        self.childs = []
        self.x = x
        self.y = y


    def cord(self):
    	return str(self.x) + "," + str(self.y)

    def printVertex(self):
    	print(str(self.x) + "," + str(self.y))

    def addChild(self, c):
    	self.childs.append(c)

    def getchilds(self):
    	return self.childs

    def setfn(self, f):
    	self.fn = f

    def getfn(self):
    	return self.fn


       


start = Vertex(75, 400)
vertexList.append(start)

vertexList.append(Vertex(200, 350))
vertexList.append(Vertex(200,450))
vertexList.append(Vertex(450,450))
vertexList.append(Vertex(450,350))


vertexList.append(Vertex (120, 130))
vertexList.append(Vertex (150, 245))
vertexList.append(Vertex (275, 275))
vertexList.append(Vertex (300, 120))
vertexList.append(Vertex (200, 5))


vertexList.append(Vertex (300, 300))
vertexList.append(Vertex (400, 300))
vertexList.append(Vertex (350, 100))

vertexList.append(Vertex (425, 30))
vertexList.append(Vertex (400, 175))
vertexList.append(Vertex (575, 100))
vertexList.append(Vertex (550, 25))

vertexList.append(Vertex (545, 260))
vertexList.append(Vertex (520, 400))
vertexList.append(Vertex (625, 375))


vertexList.append(Vertex (600, 40))
vertexList.append(Vertex (600, 290))
vertexList.append(Vertex (750, 290))
vertexList.append(Vertex (750,40))


vertexList.append(Vertex (640, 375))
vertexList.append(Vertex (640, 440))
vertexList.append(Vertex (700, 475))
vertexList.append(Vertex (755, 440))
vertexList.append(Vertex (755, 375))
vertexList.append(Vertex (700, 320))


vertexList.append(Vertex (775, 75))
vertexList.append(Vertex (810, 350))
vertexList.append(Vertex (885, 75))
vertexList.append(Vertex (830,20))

goal = Vertex (925, 75)
vertexList.append(goal)

def findHN(v):
	hn = math.sqrt((v.x - 925)**2 + (v.y - 75)**2)
	return hn

def findGN(v1, v2):
	gn = math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2)
	return gn

def findFN(v1, v2):
	fn = findGN(v1, v2) + findHN(v2)
	return fn

print("this is a test: ")



graph = Graph(vertexList, (len(vertexList ) ))


'''
for x in range(len(vertexList) ):
	for y in range(len(vertexList) ):
		if(x == y):
			continue

		line = LineString([(vertexList[x].x, vertexList[x].y), (vertexList[y].x, vertexList[y].y)])

		change = False
		for p in pList:


			if line.intersects(p) == False and line.touches(p) == True:

				change = True


			elif line.intersects(p) == True and line.touches(p) == True:
				print("TSSSSSSSSSSSST")
				change = True
			elif line.intersects(p) == True and line.touches(p) == False: 
				change = False 
				break
		if change:
			vertexList[x].addChild(vertexList[y])
			graph.addEdge(x, y)'''



def actions(x,vertexObject):
	for y in range(len(vertexList) ):
		if(x == y):
			continue

		line = LineString([(vertexObject.x, vertexObject.y), (vertexList[y].x, vertexList[y].y)])
	
		change = False
		for p in pList:


			if line.intersects(p) == False and line.touches(p) == True:
				change = True
			elif line.intersects(p) == True and line.touches(p) == True:
				change = True
			elif line.intersects(p) == True and line.touches(p) == False: 
				change = False 
				break
		if change:
			vertexObject.addChild(vertexList[y])
			graph.addEdge(x, y)
			
	return vertexObject.childs

for x in range(len(vertexList) ):
	actions(x,vertexList[x])

amount = 0

flag = True

op = []
cl = []

transfer = vertexList[0]

cl.append(transfer)



while(flag):
	for x in transfer.getchilds():
		x.setfn(findFN(transfer, x))
		#print(x.getfn())
	for x in transfer.getchilds():
		#print(str(len(op)))
		
		if amount ==  0:
			op.append(x) 
			print
			amount +=1
			continue

		if(x.getfn() <= op[len(op)-1].getfn()):
			op.append(x)
		else:
			op.insert(0, x)
			
		amount +=1


	

	
	transfer = op.pop()
	amount -= 1

	cl.append(transfer)

	if(transfer == goal):
		flag = False







start.setfn(findFN(start, goal))
thefn = start.getfn()
print(thefn)



poly = Polygon([(300, 300), (400, 300), (350, 100)])




print("number: " + str(len(vertexList)))


path = LineString([(300, 300), (400, 300)])
col = path.intersects(poly)

#coli = lTest.within(sOne)

colided = sOne.collidepoint(120, 130)
print(str(col))




graph.printMatrixTable();
'''

'''
pygame.display.update()
for p in range(len(cl)-1):
	pygame.time.wait(1000)
	pygame.draw.line(gameDisplay, green, (cl[p].x, cl[p].y), (cl[p+1].x, cl[p+1].y), 4)
	pygame.display.update()


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	
	pygame.display.update()








