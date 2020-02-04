#Blake Kim kimx5227
# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work and that none of
# it was obtained from any source other than material presented as part of the
# course.
from turtle import *
import tkinter.messagebox
import tkinter
import random
import math
import datetime

screenMinX = -500
screenMinY = -500
screenMaxX = 500
screenMaxY = 500

class Ghost(RawTurtle):
    def __init__(self,canvasobj,dx,dy,x,y,size):
        RawTurtle.__init__(self,canvasobj)
        self.penup()
        self.goto(x,y)
        self.__dx = dx
        self.__dy = dy
        self.__size = size
        if self.__size==3:
            self.shape("blueghost.gif")
        elif self.__size==2:
            self.shape("pinkghost.gif")

    def setDx(self,dx):
        self.__dx=dx

    def setDy(self,dy):
        self.__dy=dy

    def getDx(self):
        return self.__dx

    def getDy(self):
        return self.__dy

    #Moves the ghost from its current position to a new position
    def move(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        x = (self.__dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.__dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY

        self.goto(x,y)

    #returns the apprximate "radius" of the Ghost object
    def getRadius(self):
        return self.__size * 10 - 5

class LaserBeam(RawTurtle):
    def __init__(self,canvas,x,y,direction,dx,dy):
        super().__init__(canvas)
        self.penup()
        self.goto(x,y)
        self.setheading(direction)
        self.color("Green")
        self.lifespan=200
        self.__direction=direction
        self.__dx=math.cos(math.radians(direction))*2 + dx
        self.__dy=math.sin(math.radians(direction))*2 + dy
        self.shape("laser")

    def getDx(self):
        return self.__dx

    def getDy(self):
        return self.__dy

    def getLifespan(self):
        return self.lifespan

    def getRadius(self):
        return 4

    def moveLaser(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        speed=math.sqrt((self.__dx)**2 +(self.__dy)**2)

        self.__dx=speed*(math.cos(math.radians(self.__direction)))
        self.__dy=speed*(math.sin(math.radians(self.__direction)))

        x = (self.__dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.__dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY

        self.goto(x,y)
        self.lifespan-=1

class FlyingTurtle(RawTurtle):
    def __init__(self,canvasobj,dx,dy,x,y):
        RawTurtle.__init__(self,canvasobj)
        self.penup()
        self.color("purple")
        self.goto(x,y)
        self.__dx = dx
        self.__dy = dy
        self.shape("turtle")

    def move(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        x = (self.__dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.__dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY

        self.goto(x,y)

    def turboBoost(self):
        angle = self.heading()
        x = math.cos(math.radians(angle))
        y = math.sin(math.radians(angle))
        if x < 0:
            x = -x
        if y < 0:
            y = -y
        speed=math.sqrt((self.__dx)**2 +(self.__dy)**2)
        self.__dx = math.cos(math.radians(angle))*(speed+ x)
        self.__dy = math.sin(math.radians(angle))*(speed + y)

    def stopTurtle(self):
        angle = self.heading()
        self.__dx = 0
        self.__dy = 0

    def getRadius(self):
        return 2

    def setDx(self,dx):
        self.__dx=dx

    def setDy(self,dy):
        self.__dy=dy

    def getDx(self):
        return self.__dx

    def getDy(self):
        return self.__dy

def intersect(obj1,obj2):
    xcor_obj1 = obj1.xcor()
    ycor_obj1 = obj1.ycor()
    xcor_obj2 = obj2.xcor()
    ycor_obj2 = obj2.ycor()
    maxrad=obj1.getRadius()+obj2.getRadius()
    distance = math.sqrt((xcor_obj2-xcor_obj1)**2 + (ycor_obj2-ycor_obj1)**2)
    if distance > maxrad:
        return False
    else:
        return True

def main():

    # Start by creating a RawTurtle object for the window.
    firstwindow = tkinter.Tk()
    firstwindow.title("Turtle Saves the World!")
    canvas = ScrolledCanvas(firstwindow,600,600,600,600)
    canvas.pack(side = tkinter.LEFT)
    t = RawTurtle(canvas)

    screen = t.getscreen()
    screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
    screen.register_shape("blueghost.gif")
    screen.register_shape("pinkghost.gif")
    screen.register_shape("laser",((-2,-4),(-2,4),(2,4),(2,-4)))
    frame = tkinter.Frame(firstwindow)
    frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)
    scoreVal = tkinter.StringVar()
    scoreVal.set("0")
    scoreTitle = tkinter.Label(frame,text="Score")
    scoreTitle.pack()
    scoreFrame = tkinter.Frame(frame,height=2, bd=1, relief=tkinter.SUNKEN)
    scoreFrame.pack()
    score = tkinter.Label(scoreFrame,height=2,width=20,textvariable=scoreVal,fg="Yellow",bg="black")
    livesTitle = tkinter.Label(frame, text="Extra Lives Remaining")
    livesTitle.pack()
    livesFrame = tkinter.Frame(frame,height=30,width=60,relief=tkinter.SUNKEN)
    livesFrame.pack()
    livesCanvas = ScrolledCanvas(livesFrame,150,40,150,40)
    livesCanvas.pack()
    livesTurtle = RawTurtle(livesCanvas)
    livesTurtle.ht()
    livesScreen = livesTurtle.getscreen()
    life1 = FlyingTurtle(livesCanvas,0,0,-35,0)
    life2 = FlyingTurtle(livesCanvas,0,0,0,0)
    life3 = FlyingTurtle(livesCanvas,0,0,35,0)
    lives = [life1, life2, life3]
    score.pack()
    t.ht()

    screen.tracer(10)

    #Tiny Turtle!
    flyingturtle = FlyingTurtle(canvas,0,0,(screenMaxX-screenMinX)/2+screenMinX,(screenMaxY-screenMinY)/2 + screenMinY)

    #A list to keep track of all the ghosts
    ghosts = []

    #A list to keep track of all the lasers
    lasers = []

    #Create some ghosts and randomly place them around the screen
    for numofghosts in range(6):
        dx =random.random()*6  - 4
        dy =random.random()*6  - 4
        x = random.random() * (screenMaxX - screenMinX) + screenMinX
        y = random.random() * (screenMaxY - screenMinY) + screenMinY

        ghost = Ghost(canvas,dx,dy,x,y,3)

        ghosts.append(ghost)

    def play():
        #start counting time for the play function
        ##LEAVE THIS AT BEGINNING OF play()
        start = datetime.datetime.now()

        #Keeps track of dead lasers
        dead_lasers = []

        #Keeps track of dead ghosts
        dead_ghosts = []

        hit_ghosts = []

        if len(lives)==0:
            tkinter.messagebox.showinfo("You Lost...", "The Ghosts win...")
            return
        elif len(ghosts)==0:
            tkinter.messagebox.showinfo("You Win!!", "You saved the world!")
            return

        # Move the turtle
        flyingturtle.move()

        #Move the Lasers
        for each_laser in lasers:
            each_laser.moveLaser()

        #Move the ghosts
        for each_ghost in ghosts:
            each_ghost.move()

        for each_ghost in ghosts:
            if intersect(each_ghost,flyingturtle):
                lostlife = lives.pop()
                lostlife.hideturtle()
                ghosts.remove(each_ghost)
                hit_ghosts.append(each_ghost)
                each_ghost.goto(-screenMinX*2, -screenMinY*2)
                each_ghost.hideturtle()
                tkinter.messagebox.showwarning("Uh-oh", "You Lost a Life!")


        for each_laser in lasers:
            for each_ghost in ghosts:
                if intersect(each_laser,each_ghost):
                    lasers.remove(each_laser)
                    dead_lasers.append(each_laser)
                    each_laser.goto(-screenMinX*2, -screenMinY*2)
                    each_laser.hideturtle()
                    ghosts.remove(each_ghost)
                    dead_ghosts.append(each_ghost)
                    each_ghost.goto(-screenMinX*2, -screenMinY*2)
                    each_ghost.hideturtle()
                    temp=int(scoreVal.get())+20
                    scoreVal.set(str(temp))

        for each_laser in lasers:
            if each_laser.getLifespan()<0:
                lasers.remove(each_laser)
                dead_lasers.append(each_laser)
                each_laser.goto(-screenMinX*2, -screenMinY*2)
                each_laser.hideturtle()

        #stop counting time for the play function
        ##LEAVE THIS AT END OF ALL CODE IN play()
        end = datetime.datetime.now()
        duration = end - start

        millis = duration.microseconds / 1000.0

        # Set the timer to go off again
        screen.ontimer(play,int(10-millis))


    # Set the timer to go off the first time in 5 milliseconds
    screen.ontimer(play, 5)

    #Turn turtle 7 degrees to the left
    def turnLeft():
        flyingturtle.setheading(flyingturtle.heading()+7)

    #turboBoost turtle
    def forward():
        flyingturtle.turboBoost()

    def turnRight():
        flyingturtle.setheading(flyingturtle.heading()-7)

    #stop Turtle
    def stop():
        flyingturtle.stopTurtle()

    def fireLaser():
        direction = flyingturtle.heading()
        x=flyingturtle.xcor()
        y=flyingturtle.ycor()
        dx=flyingturtle.getDx()
        dy=flyingturtle.getDy()
        newlaser = LaserBeam(canvas,x,y,direction,dx,dy)
        lasers.append(newlaser)

    #Call functions above when pressing relevant keys
    screen.onkeypress(turnLeft,"Left")
    screen.onkeypress(forward,"Up")
    screen.onkeypress(stop, "Down")
    screen.onkeypress(turnRight,"Right")
    screen.onkeypress(fireLaser,"")

    screen.listen()
    tkinter.mainloop()

if __name__ == "__main__":
    main()
