'''
--  PENDULUM CLASS
--  IMPLEMENTS THE PENDULUM PHYSICS 
'''

#IMPORTING LIBRARIES
import turtle
import math

GRAVITY=20
DAMPING = .9999
FPS=50



class Pendulum:
    def __init__(self,wn,start_pos:turtle.Vec2D,bob_radius=10,rope_len=100,angle=math.pi/4) -> None:
        '''
            INPUT:
                wn (TURTLE.SCREEN): THE WINDOW 
                start_pos(tutle.vec2d): START POSITION OF THE PENDULUM ROPE (origin point)
                bob_radius(INT): RADIUS OF THE BOB(CIRCLE)
                rope_len (INT) : LENGTH OF THE PENDULUM ROPE
        '''
        self.wn= wn
        self.start_pos = start_pos
        self.bob_radius = bob_radius
        self.rope_len= rope_len

        #initial angle (if angle is negative then bob moves clock wise)
        # THE ANGLE , THE ROPE MAKES WITH THE Y AXIS
        self.angle = angle


        #position of bob wrt rope origin = bob pos - rop_pos
        # the y_cor of bob_pos is negative because the bob is under the origin point 
        self.bob_pos = turtle.Vec2D(self.rope_len*math.sin(self.angle),-self.rope_len*math.cos(self.angle))
        #getting the bob positon wrt rope origin
        self.bob_pos +=self.start_pos

        #THE BOB AND ROPE OBJECT
        self.bob = self.create_shape(['white','#0fafdb'],self.bob_pos,'circle')
        self.rope = self.create_shape(['white','white'],self.start_pos,'line')

        #ANGULAR VELOCITY OF BOB
        self.angular_vel=0

        #TO SHOW THE ANGLE
        self.pen= turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.penup()
        self.pen.goto(300,200)
        
        


    def create_shape(self,color:list,pos:turtle.Vec2D,shape:str) -> turtle.Turtle:
        '''
            input:
                color list(srt): color of the object and border
                pos (turtle.vec2d): position of the turtle
                shape (str): what shape(circle or line)

            output:
                return a turtle object
        '''
        t= turtle.Turtle()
        t.speed(0)
        t.penup()
  
        #CREATING A LINE
        if shape == 'line':
            t.hideturtle()
            t.goto(pos)
            t.pendown()
            t.pensize(5)
            t.pencolor(color[0])
            t.goto(self.bob_pos)
            t.penup()


        #CREATING CIRCLE
        elif shape == 'circle':    
            t.shape(shape)
            t.shapesize(3,3,3)
            t.color(color[0],color[1])
            t.goto(pos)
       


        return t

    def update(self):
        #UPDATES THE POSITION OF BOB AND ROPE

        #ANGULAR ACCELERATION = -g*sin(angle)/rope_len
        angular_acc= -GRAVITY*math.sin(self.angle)/(self.rope_len)
        # ANGULAR VELOCITY -= ANGLULAR ACCELERATION , BEACUSE VELOCITY DECREASE AS ACCELERATION INCREASES AND VICE VERSA
        self.angular_vel -= angular_acc

        # DECREASE THE ANGLE BY THE AMOUNT OF VELOCITY ANGLE -= ANGULAR VELOCITY
        self.angle -= self.angular_vel/(FPS)
        #CALCULATE NEW BOB POS BASED ON THE NEW ANGLE 
        self.bob_pos = turtle.Vec2D(self.rope_len*math.sin(self.angle),-self.rope_len*math.cos(self.angle))
        self.bob_pos +=self.start_pos

        self.rope.clear()
        self.rope.goto(self.start_pos)
        self.rope.pendown()
        #POSITION BOB AND ROPE AT THEIR NEW POSITION 
        self.bob.goto(self.bob_pos)
        self.rope.goto(self.bob_pos)
        self.rope.penup()

        #DAMP THE ANGLULAR VELOCITY
        self.angular_vel *= DAMPING

        self.show()


    def show(self):
        #SHOW THE ANGLE , THAT THE ROPE MAKES WITH THE Y AXIS
        self.pen.clear()
        self.pen.pendown()
        self.pen.color('white')
        self.pen.write('angle: {}'.format(math.degrees(self.angle)),align='center',font=("Roboto",30,'bold'))

        





    









