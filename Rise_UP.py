import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import math as mm
import random



def ellipse(rx,ry,segmrnts,xc,yc):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(segmrnts):
        angle = 2 * mm.pi * i / segmrnts
        x = xc + rx * mm.cos(angle)
        y = yc + ry * mm.sin(angle)
        glVertex2f(x,y)
    glEnd() 

def Ballon_Triangle(x1,y1,x2,y2,x3,y3):  
    glBegin(GL_TRIANGLES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()

def Circle1(radius,Xc,Yc):  
    glBegin(GL_LINE_LOOP)
    for i in range(100):
        angle = 2 * mm.pi * i / 100
        x= Xc + radius * mm.cos(angle)
        y= Yc + radius * mm.sin(angle)
        glVertex2f(x,y)
    glEnd()
    
def Circle2(radius,Xc,Yc):  
    glBegin(GL_TRIANGLE_FAN)
    for i in range(100):
        angle = 2 * mm.pi * i / 100
        x= Xc + radius * mm.cos(angle)
        y= Yc + radius * mm.sin(angle)
        glVertex2f(x,y)
    glEnd()

def protector(x,y):
    glColor3f(249/255,255/255,255/255)
    r = 0.04
    while r > 0.035:
        Circle1(r,x,y)
        r -= 0.001 
        
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA) 
    glColor4f(1,1,1,0.4)
    Circle2(0.035,x,y) 

def Line(x1,y1,x2,y2): 
    glBegin(GL_LINES)
    glVertex3f(x1,y1,0)
    glVertex3f(x2,y2,0)
    glEnd()

def Balloon(y):
    glColor3f(1,1,1)
    ellipse(0.1/2 ,0.15/2 , 400 , 0 ,  +y)
    Ballon_Triangle( -0.1/6  ,-(0.15/2) -0.01 +y , 0 , -(0.15/2)+0.01 +y, 0.1/6 , -(0.15/2) -0.01  +y)
    Line( 0 , -(0.15/2)-0.01 +y  ,  0  , -(0.15/2)-0.01 -0.15 +y  )
    
def Rectangle(x1,y1,x2,y2,x3,y3,x4,y4):
    glBegin(GL_QUADS)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glVertex2f(x4,y4)    
    glEnd()

def DuckBalloon(x,y):
    #back ellipse
    glColor3f(1,1,1)
    ellipse(0.1/2+0.005 ,0.15/2+0.005 , 400 , 0 +x ,  +y)
    #front ellipse
    glColor3f(251/255,226/255,110/255)
    Ballon_Triangle( -0.1/6 +x  ,-(0.15/2) -0.01 +y , 0 +x, -(0.15/2)+0.01 +y, 0.1/6+x , -(0.15/2) -0.01  +y)
    ellipse(0.1/2 ,0.15/2 , 400 , 0 +x ,  +y)
    #mouse
    glColor3f(251/255,135/255,84/255)
    ellipse(0.02,0.01,360, x , -0.02 +y)
    #cheeks
    glColor3f(255/255,152/255,154/255)
    Circle2(0.008,0.035+x,-0.01 +y)
    Circle2(0.008,-0.035+x,-0.01 +y)
    #eyes
    glColor3f(135/255,82/255,48/255)
    Circle2(0.01,-0.02+x,0.02+y)
    Circle2(0.01,0.02+x,0.02+y)
    #eyebrows
    glColor3f(136/255,87/255,57/255)
    Lshift_x=0.016
    Lshift_y=0.0035
    Rshift_x=-0.016
    Rshift_y=0.0035
    Rectangle(-0.02+x +Lshift_x, 0.02 +y+Lshift_y, -0.04+x+Lshift_x ,0.035+y+Lshift_y , -0.045+x +Lshift_x,0.03+y+Lshift_y , -0.024+x +Lshift_x,0.015+y+Lshift_y)
    Rectangle( 0.02+x +Rshift_x, 0.02 +y+Rshift_y,  0.04+x+Rshift_x ,0.035+y+Rshift_y ,  0.045+x +Rshift_x,0.03+y+Rshift_y ,  0.024+x +Rshift_x,0.015+y+Rshift_y)
    glColor3f(1,1,1)
    Line( 0+x , -(0.15/2)-0.01 +y  ,  0 +x , -(0.15/2)-0.01 -0.15 +y  )

def draw_arc2(radius,segments,start_angle,end_angel,Xc,Yc):  
    glBegin(GL_TRIANGLE_FAN)
    for i in range(segments):
        angle = mm.radians( start_angle + (end_angel - start_angle) * i / segments )
        x = Xc + radius * mm.cos(angle)
        y = Yc + radius * mm.sin(angle)
        glVertex2f(x,y)
    glEnd()

def Diamond(radius,Xc,Yc): 
    glColor3f(222/255, 243/255, 249/255)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(4):
        angle = 2 * mm.pi * i / 4
        x= Xc + radius * mm.cos(angle)
        y= Yc + radius * mm.sin(angle)
        glVertex2f(x,y)
    glEnd()

def Poly_8(radius,Xc,Yc):  
    glBegin(GL_TRIANGLE_FAN)
    for i in range(8):
        angle = 2 * mm.pi * i / 8
        x= Xc + radius * mm.cos(angle)
        y= Yc + radius * mm.sin(angle)
        glVertex2f(x,y)
    glEnd()

def X_Shape(x, y, size):
    glBegin(GL_QUADS)
    glVertex2f(x-size/6, y-size)
    glVertex2f(x+size/6, y-size)
    glVertex2f(x+size/6, y+size)
    glVertex2f(x-size/6, y+size)
    glVertex2f(x-size, y-size/6)
    glVertex2f(x+size, y-size/6)
    glVertex2f(x+size, y+size/6)
    glVertex2f(x-size, y+size/6)

    glEnd()

def square(X1, Y1, size): 
    half = size / 2
    glBegin(GL_QUADS)
    glVertex2f(X1+half ,Y1+half)
    glVertex2f(X1+half ,Y1-half)
    glVertex2f(X1-half,Y1-half )
    glVertex2f(X1-half ,Y1+half )
    glEnd()    

def Screen_boundry(x1,y1,x2,y2):
    glBegin(GL_QUADS)
    glColor3f(0,0,0)
    glVertex2f(x1,y1)
    glVertex2f(x2,y1)
    glVertex2f(x2,y2)
    glVertex2f(x1,y2)
    glEnd()

def Triangle(x, y, size):
    glBegin(GL_TRIANGLES)
    glVertex2f(x , y - size)
    glVertex2f(x - size, y + size/2)
    glVertex2f(x + size, y + size/2)
    glEnd()

def Poly_6(radius,Xc,Yc): 
    glBegin(GL_TRIANGLE_FAN)
    for i in range(6):
        angle = 2 * mm.pi * i / 6
        x= Xc + radius * mm.cos(angle)
        y= Yc + radius * mm.sin(angle)
        glVertex2f(x,y)
    glEnd()

def Star(xc, yc):
    TriStar(0 +xc, 0.07  +yc     , -0.02 +xc ,  0+yc   ,0.02+xc , 0+yc  )
    #body
    TriStar(0 +xc, -0.06+0.03+yc ,-0.06 +xc  ,  0.02 +yc,0.06+xc,0.02+yc)
    #bottom
    TriStar(0.04+xc,-0.05+yc, 0+xc , -0.06+0.03+yc , 0.02+xc,0.02 +yc)
    TriStar(-0.04+xc,-0.05+yc, 0 +xc, -0.06+0.03+yc , -0.02+xc,0.02+yc )

def Pyramid(angle,size,x,y,z):
    glPushMatrix()
    glTranslatef(x, y+0.02, z)
    glRotatef(angle, 0,1, 0)
    half = size / 2
    glBegin(GL_TRIANGLES)
    #face1 le bra
    glColor3f(191/255, 191/255, 191/255)  
    glVertex3f(0, -size, 0)
    glVertex3f(-half, 0, -half)
    glVertex3f(half, 0, -half)
    #face2 right 
    glColor3f(1, 1, 1)  
    glVertex3f(0, -size, 0)
    glVertex3f(half, 0, -half)
    glVertex3f(half, 0, half)
    # Back face
    glColor3f(1, 1, 1)  
    glVertex3f(0, -size, 0)
    glVertex3f(half, 0, half)
    glVertex3f(-half, 0, half)
    # Left face
    glColor3f(191/255, 191/255,191/255)  
    glVertex3f(0, -size, 0)
    glVertex3f(-half, 0, half)
    glVertex3f(-half, 0, -half)
    glColor3f(222/255, 243/255, 249/255)
    glEnd()
    glPopMatrix()

def Arrow(angle,size,x,y,z):
    glPushMatrix()
    glTranslatef(x, y+0.02, z)
    glRotatef(angle, 0,1, 0)
    half = size / 2
    glBegin(GL_TRIANGLES) 
    #face1 le bra
    glColor3f(191/255, 191/255, 191/255)  
    glVertex3f(0, -size, 0)
    glVertex3f(-half/2, 0, -half/2)
    glVertex3f(half/2, -size*0.3, -half/2)
    #face2 right 
    glColor3f(1, 1, 1)  
    glVertex3f(0, -size, 0)
    glVertex3f(half/2, -size*0.3, -half/2)
    glVertex3f(half/2, 0, half/2)
    # Back face
    glColor3f(1, 1, 1)  
    glVertex3f(0, -size, 0)
    glVertex3f(half/2, 0, half/2)
    glVertex3f(-half/2, -size*0.3, half/2)
    # Left face
    glColor3f(191/255, 191/255,191/255)  
    glVertex3f(0, -size, 0)
    glVertex3f(-half/2, -size*0.3, half/2)
    glVertex3f(-half/2, 0, -half/2)
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.6, 0.6) 
    glVertex3f(-half/2, 0, -half/2)
    glVertex3f(half/2,-size*0.3, -half/2)
    glVertex3f(half/2, 0, half/2)
    glVertex3f(-half/2, -size*0.3, half/2)
    glColor3f(222/255, 243/255, 249/255)
    glEnd()
    glPopMatrix()

def TriStar(x1,y1,x2,y2,x3,y3):
    glBegin(GL_TRIANGLES)
    glColor3f(1,1,1)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()

def Mountain(x, y, size,width,r1,g1,b1,r2,g2,b2,r3,g3,b3):
    glBegin(GL_TRIANGLES)
    glColor3f(r1/255,g1/255,b1/255)
    glVertex2f(x - size - width, y - size)
    glColor3f(r2/255,g2/255,b2/255)
    glVertex2f(x , y + size)
    glColor3f(r3/255,g3/255,b3/255)
    glVertex2f(x + size + width, y - size)
    glEnd()

def Tree(x, y, size,width,r1,g1,b1,r2,g2,b2,r3,g3,b3):
    glBegin(GL_TRIANGLES)
    glColor3f(r1/255,g1/255,b1/255)
    glVertex2f(x - size - width, y - size)
    glColor3f(r2/255,g2/255,b2/255)
    glVertex2f(x , y + size)
    glColor3f(r3/255,g3/255,b3/255)
    glVertex2f(x + size + width, y - size)
    glEnd()

def InitialSkyAndLand(y,r,g,b):
    half_The_hight = 6 * 0.5  
    glColor3f(92/255, 193/255, 223/255)
    glBegin(GL_QUADS)
    glVertex2f(-1, y  -1.2)
    glVertex2f( 1, y  -1.2)
    glVertex2f( 1, y + half_The_hight)
    glVertex2f(-1, y + half_The_hight)    
    glEnd()
    #cloudes
    segmentes = 100

    factor =0.7
    glColor3f(r + factor * (1 - r),g + factor * (1 - g),b + factor * (1 - b))
    draw_arc2(0.5, segmentes,0,180,-0.84 ,y+half_The_hight+0.05)
    draw_arc2(0.3, segmentes,0,180,-0.4 ,y+half_The_hight+0.08)
    ellipse(0.5,0.2,segmentes,0,y+half_The_hight+0.1)
    draw_arc2(0.3, segmentes,0,180,0.4 ,y+half_The_hight+0.08)
    draw_arc2(0.5, segmentes,0,180,0.84,y+half_The_hight+0.05)
    
    factor =0.7
    glColor3f(r + factor * (1 - r),g + factor * (1 - g),b + factor * (1 - b))
    #draw_arc2(0.3, segmentes,0,180,-1 ,y+half_The_hight  -0.1-0.1)
    draw_arc2(0.5, segmentes,0,180,-0.84 ,y+half_The_hight+0.05 -0.1-0.1)
    draw_arc2(0.3, segmentes,0,180,-0.4 ,y+half_The_hight+0.08 -0.1-0.1)
    ellipse(0.5,0.2,segmentes,0,y+half_The_hight+0.1 -0.1-0.1)
    draw_arc2(0.3, segmentes,0,180,0.4 ,y+half_The_hight+0.08 -0.1-0.1)
    draw_arc2(0.5, segmentes,0,180,0.84,y+half_The_hight+0.05 -0.1-0.1)

    factor =0.5
    glColor3f(r + factor * (1 - r),g + factor * (1 - g),b + factor * (1 - b))
    #draw_arc2(0.2, segmentes,0,180,-1 ,y+half_The_hight-0.2-0.1)
    draw_arc2(0.5, segmentes,0,180,-0.84 ,y+half_The_hight+0.05-0.2-0.1)
    draw_arc2(0.3, segmentes,0,180,-0.4 ,y+half_The_hight+0.08 -0.2-0.1)
    ellipse(0.5,0.2,segmentes,0,y+half_The_hight+0.1 -0.2-0.1)
    draw_arc2(0.3, segmentes,0,180,0.4 ,y+half_The_hight+0.08 -0.2-0.1)
    draw_arc2(0.5, segmentes,0,180,0.84,y+half_The_hight+0.05 -0.2-0.1)

    factor =0.3
    glColor3f(r + factor * (1 - r),g + factor * (1 - g),b + factor * (1 - b))
    #draw_arc2(0.2, segmentes,0,180,-1 ,y+half_The_hight-0.3-0.1)
    draw_arc2(0.5, segmentes,0,180,-0.84 ,y+half_The_hight+0.05-0.3-0.1)
    draw_arc2(0.3, segmentes,0,180,-0.4 ,y+half_The_hight+0.08-0.3-0.1)
    ellipse(0.5,0.2,segmentes,0,y+half_The_hight+0.1 -0.3-0.1)
    draw_arc2(0.3, segmentes,0,180,0.4 ,y+half_The_hight+0.08 -0.3-0.1)
    draw_arc2(0.5, segmentes,0,180,0.84,y+half_The_hight+0.05 -0.3-0.1)

    factor =0
    glColor3f(r + factor * (1 - r),g + factor * (1 - g),b + factor * (1 - b))
    #draw_arc2(0.2, segmentes,0,180,-1 ,y+half_The_hight-0.4-0.1)
    draw_arc2(0.5, segmentes,0,180,-0.84 ,y+half_The_hight+0.05-0.4-0.1)
    draw_arc2(0.3, segmentes,0,180,-0.4 ,y+half_The_hight+0.08-0.4-0.1)
    ellipse(0.5,0.2,segmentes,0,y+half_The_hight+0.1 -0.4-0.1)
    draw_arc2(0.3, segmentes,0,180,0.4 ,y+half_The_hight+0.08 -0.4-0.1)
    draw_arc2(0.5, segmentes,0,180,0.84,y+half_The_hight+0.05 -0.4-0.1)

    #land
    glColor3f(220/255, 255/255, 199/255)
    glBegin(GL_QUADS)
    glVertex2f(-1, y -1.2)
    glVertex2f( 1, y -1.2)
    glVertex2f( 1, y + -0.8)
    glVertex2f(-1, y + -0.8)  
    glEnd()
    #front
    glColor3f(125/255, 204/255, 182/255)
    draw_arc2(0.28,360,0,180,-0.6,-1.2+y)
    draw_arc2(0.2,360,0,180,-0.4,-1.2+y)
    draw_arc2(0.25,360,0,180,-0.1,-1.2+y)
    draw_arc2(0.2,360,0,180,0.2,-1.2+y)
    draw_arc2(0.1,360,0,180,0.4,-1.2+y)
    draw_arc2(0.05,360,0,180,0.5,-1.2+y)
    #back
    
    glColor3f(122/255, 185/255, 165/255)
    #right
    draw_arc2(0.1,360,0,180,0.5,-1.2+y)
    draw_arc2(0.2,360,0,180,0.7,-1.2+y)
    #left
    draw_arc2(0.15,360,0,180,-0.7,-1.2+y)
    draw_arc2(0.15,360,0,180,-0.7,-1.2+y)
    draw_arc2(0.1,360,0,180,-0.5,-1.2+y)

def initialBackground(y):
    InitialSkyAndLand(y,92/255, 193/255, 223/255)
    #mount2
    Mountain(0.2, -0.68 +y, 0.12,0.1, 165,192,201 , 172,176,185 , 165,192,201)
    #mount3
    Mountain(-0.25, -0.64+y, 0.16,0.05, 162,174,188 , 163,179,195 , 162,174,188)
    #mount4
    Mountain(-0.55, -0.59+y, 0.21,0 ,199,208,215 , 167,174,190 , 143,160,176)
    #mont1
    Mountain(0.5, -0.62+y, 0.18,0.1, 199,208,215 , 199,208,213 , 199,207,210)
    #trees
    #small right
    Tree(0.55, -0.75+y , 0.06 ,  -0.07 , 128,187,172, 128,187,172, 128,187,172 )
    Tree(0.5 , -0.75 +y , 0.06 , -0.07 , 128,187,172, 128,187,172, 128,187,172 )
    #big right
    Tree(0.4,-0.8+y ,0.1,-0.08 , 125,204,180, 125,204,180, 125,204,180 )
    #big Left
    Tree(-0.35,-0.82+y ,0.15,-0.12 , 125,204,182, 125,204,182, 125,204,182 )
    Tree(-0.68,-0.86+y ,0.15,-0.12 , 119,192,172, 119,192,172, 119,192,172 )
    #lower Trees
    Tree(0.6,-1+y ,0.25,-0.2 , 106,175,144, 106,175,144, 106,175,144 )
    Tree(0.45,-1.1+y ,0.13,-0.1 , 106,175,146, 106,175,146, 106,175,146 )

def BackGround(y, r, g, b,levelSize):
    half_The_hight = levelSize * 0.5  
    glColor3f(r, g, b)
    glBegin(GL_QUADS)
    glVertex2f(-1, y -half_The_hight)
    glVertex2f( 1, y -half_The_hight)
    glVertex2f( 1, y + half_The_hight)
    glVertex2f(-1, y + half_The_hight)    
    glEnd()
    segmentes = 100

    factor =0.7
    glColor3f(r + factor * (1 - r),g + factor * (1 - g),b + factor * (1 - b))
    draw_arc2(0.5, segmentes,0,180,-0.84 ,y+half_The_hight+0.05)
    draw_arc2(0.3, segmentes,0,180,-0.4 ,y+half_The_hight+0.08)
    ellipse(0.5,0.2,segmentes,0,y+half_The_hight+0.1)
    draw_arc2(0.3, segmentes,0,180,0.4 ,y+half_The_hight+0.08)
    draw_arc2(0.5, segmentes,0,180,0.84,y+half_The_hight+0.05)
    
    factor =0.7
    glColor3f(r + factor * (1 - r),g + factor * (1 - g),b + factor * (1 - b))
    #draw_arc2(0.3, segmentes,0,180,-1 ,y+half_The_hight  -0.1-0.1)
    draw_arc2(0.5, segmentes,0,180,-0.84 ,y+half_The_hight+0.05 -0.1-0.1)
    draw_arc2(0.3, segmentes,0,180,-0.4 ,y+half_The_hight+0.08 -0.1-0.1)
    ellipse(0.5,0.2,segmentes,0,y+half_The_hight+0.1 -0.1-0.1)
    draw_arc2(0.3, segmentes,0,180,0.4 ,y+half_The_hight+0.08 -0.1-0.1)
    draw_arc2(0.5, segmentes,0,180,0.84,y+half_The_hight+0.05 -0.1-0.1)

    factor =0.5
    glColor3f(r + factor * (1 - r),g + factor * (1 - g),b + factor * (1 - b))
    #draw_arc2(0.2, segmentes,0,180,-1 ,y+half_The_hight-0.2-0.1)
    draw_arc2(0.5, segmentes,0,180,-0.84 ,y+half_The_hight+0.05-0.2-0.1)
    draw_arc2(0.3, segmentes,0,180,-0.4 ,y+half_The_hight+0.08 -0.2-0.1)
    ellipse(0.5,0.2,segmentes,0,y+half_The_hight+0.1 -0.2-0.1)
    draw_arc2(0.3, segmentes,0,180,0.4 ,y+half_The_hight+0.08 -0.2-0.1)
    draw_arc2(0.5, segmentes,0,180,0.84,y+half_The_hight+0.05 -0.2-0.1)

    factor =0.3
    glColor3f(r + factor * (1 - r),g + factor * (1 - g),b + factor * (1 - b))
    #draw_arc2(0.2, segmentes,0,180,-1 ,y+half_The_hight-0.3-0.1)
    draw_arc2(0.5, segmentes,0,180,-0.84 ,y+half_The_hight+0.05-0.3-0.1)
    draw_arc2(0.3, segmentes,0,180,-0.4 ,y+half_The_hight+0.08-0.3-0.1)
    ellipse(0.5,0.2,segmentes,0,y+half_The_hight+0.1 -0.3-0.1)
    draw_arc2(0.3, segmentes,0,180,0.4 ,y+half_The_hight+0.08 -0.3-0.1)
    draw_arc2(0.5, segmentes,0,180,0.84,y+half_The_hight+0.05 -0.3-0.1)

    factor =0
    glColor3f(r + factor * (1 - r),g + factor * (1 - g),b + factor * (1 - b))
    #draw_arc2(0.2, segmentes,0,180,-1 ,y+half_The_hight-0.4-0.1)
    draw_arc2(0.5, segmentes,0,180,-0.84 ,y+half_The_hight+0.05-0.4-0.1)
    draw_arc2(0.3, segmentes,0,180,-0.4 ,y+half_The_hight+0.08-0.4-0.1)
    ellipse(0.5,0.2,segmentes,0,y+half_The_hight+0.1 -0.4-0.1)
    draw_arc2(0.3, segmentes,0,180,0.4 ,y+half_The_hight+0.08 -0.4-0.1)
    draw_arc2(0.5, segmentes,0,180,0.84,y+half_The_hight+0.05 -0.4-0.1)

colors = [
    (239/255, 55/255, 79/255), 
    (234/255, 66/255, 48/255),
    (238/255, 120/255, 48/255),
    (202/255, 65/255, 0/255) ,
    (0/255, 40/255, 46/255),

    (120/255, 194/255, 62/255),
    (0/255, 146/255, 201/255),
    (234/255, 159/255, 48/255),
    (64/255, 194/255, 68/255),
    (77/255, 12/255, 73/255),
    (239/255, 216/255, 48/255),

    (0/255, 208/255, 160/255),
    (147/255, 163/255, 248/255),
    (64/255, 70/255, 64/255),
    (249/255, 195/255, 148/255),


]

def draw_text(text, x, y, font_size, color=(1, 1, 1)):
    font = pg.font.Font("BebasNeue-Regular.ttf", font_size)
    text_surface = font.render(text, True, color)
    text_data = pg.image.tostring(text_surface, "RGBA", True)
    glRasterPos2d(x, y)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
    if font is None:
        print("Font failed to load!")

def draw_photo(text_surface, x, y):
    text_data = pg.image.tostring(text_surface, "RGBA", True)
    glRasterPos2d(x, y)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
    
shapesOfEachLevel = {
    1: ['square'],
    2: ['circle'],
    3: ['X_Shape'],
    4: ['triangle'],
    5: ['poly_8','poly_6'],
    6: ['Arrow'],
    7: ['Diamond'],
    8: ['pyramid'],
    9: ['Star'],
    10: ['square', 'triangle','circle','poly_8','Diamond','X_Shape','pyramid','Arrow']
}

def main():
    pg.init()
    display = (1000, 800)
    pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 1)
    pg.display.gl_set_attribute(pg.GL_MULTISAMPLESAMPLES, 4)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_MULTISAMPLE)
    s =1
    gluOrtho2D(-s, s, -s, s)
    glClearColor(0, 0, 0, 1)  
    # score=0
    
    while True:
        RestartImage=pg.image.load("reload.png")
        pg.mixer.pre_init(44100, -16, 2, 512)
        pop_sound = pg.mixer.Sound("pop.wav") 
        levelMusic = pg.mixer.music.load("Veaceslav Draganov - The Last Hero.mp3")
        pg.mixer.music.play(loops=-1, start=0.0)
        
        ###
        gravity = 0.3
        StandStillTimer =2
        TimeBetweenObjects = 0.4
        levelSize=12

        ###
        score=0
        current_level =1
        scroll_speed = 0.3

        ###
        FallingObjects = []       
        level1_incremented = False   
        FallingObjectsSpawnTimer = 0.0
        StartFalligTimer =StandStillTimer+10

        balloonX=0
        balloonY=-0.35
        balloonRx =0.1/2
        balloonRy=0.15/2
        balloonPop=False
        #popTimer= 0    
        #popDelay= 0 
        angle=0
       
        
        initialBackgroundCenter=0.2
        backGround_1_Center = 6.0
        randColor1 =random.choice(colors)
        backGround_1_color = randColor1
        backGround_2_Center = backGround_1_Center + levelSize
        randColor2 = random.choice(colors)
        while randColor1 == randColor2:
            randColor2 = random.choice(colors)
        backGround_2_color=randColor2
        

        clock = pg.time.Clock() 
        playing = True
        while playing:
            if not balloonPop:
                dt = clock.tick(60) / 1000.0 
            else:
                dt = clock.tick(60) / 1000.0 *0.3
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return    
                elif event.type == pg.MOUSEBUTTONDOWN and balloonPop :
                    playing = False
                    break


            FallingObjectsSpawnTimer += dt
            if StartFalligTimer > 0:
                StartFalligTimer -=dt

            if StartFalligTimer <=0:
                if FallingObjectsSpawnTimer >= TimeBetweenObjects:
                    FallingObjectsSpawnTimer = 0 
                    x = random.uniform(-0.4, 0.4)
                    y = 1.6
                    type = random.choice(shapesOfEachLevel[current_level])
                    FallObject = { 'x': x , 'y': y , 'type': type ,'horizontalSpeed': random.uniform(-0.02,0.02) ,'VerticalSpeed': 0.5  }
                    if type == 'square':
                        FallObject['size'] = random.uniform(0.05,0.1)
                        FallObject['radius'] =  FallObject['size']/2 
                    elif type == 'Diamond':
                        FallObject['Realradius']= random.uniform(0.01,0.05)
                        FallObject['radius'] = FallObject['Realradius']-0.25*FallObject['Realradius']
                    elif type in ['circle', 'poly_8','poly_6']:
                        FallObject['Realradius']= random.uniform(0.01,0.05)
                        FallObject['radius'] = FallObject['Realradius']-(0.1*FallObject['Realradius'])
                    elif type == 'X_Shape':
                        FallObject['size'] = random.uniform(0.04,0.08)
                        FallObject['radius'] = FallObject['size'] -0.01 
                    elif type =='triangle':
                        FallObject['size'] = random.uniform(0.01,0.05)
                        FallObject['radius'] = FallObject['size']/2
                    elif type == 'Star':
                        FallObject['radius'] = 0.04
                    elif type == 'pyramid':
                        FallObject['size'] = random.uniform(0.04,0.1)
                        FallObject['radius'] =FallObject['size']/2
                    elif type == 'Arrow':
                        FallObject['size'] = random.uniform(0.04,0.1)
                        FallObject['radius'] =FallObject['size']/3
  
                    FallingObjects.append(FallObject) 

            # Update obstacle positions
                for n in FallingObjects:
                    n['VerticalSpeed'] += gravity * dt
                    n['y'] -= n['VerticalSpeed'] * dt
                    n['x'] +=  n['horizontalSpeed'] *dt 
            # remove form list
            FallingObjects = [n for n in FallingObjects if -1.8 <= n['y'] <= 1.8   and 1.4 >= n['x'] >= -1.4]


            #collison 
            if not balloonPop:
                for obj in FallingObjects:
                    dx = obj['x'] - balloonX
                    dy = obj['y'] - balloonY
                    rx_eff = (balloonRx + obj['radius'])
                    ry_eff = (balloonRy + obj['radius'])

                    Decision_Parameter=mm.pow(ry_eff,2)*mm.pow(dx,2)+mm.pow(rx_eff,2)*mm.pow(dy,2)-mm.pow(rx_eff,2)*mm.pow(ry_eff,2)

                    if Decision_Parameter <=0 :
                        balloonPop = True
                        pg.mixer.music.stop()
                        pop_sound.play()
                        break
                
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            if StandStillTimer > 0:
                StandStillTimer -=dt

            if StandStillTimer <=  0:
                initialBackgroundCenter -= scroll_speed * dt
                backGround_1_Center -= scroll_speed * dt
                backGround_2_Center -= scroll_speed * dt
                
            #score
            if not balloonPop :
                score += scroll_speed  *dt *10
           
            if backGround_1_Center +(levelSize/2) -1 < -1 and not level1_incremented:
                if current_level < 10 :
                    current_level += 1
                    level1_incremented = True
                    if current_level ==10:
                        pg.mixer.music.load("AlexGrohl - Breath of Light.mp3")
                        pg.mixer.music.play(loops=-1)
              
            

            if backGround_1_Center + ((levelSize/2)+1) < -1.0:
                backGround_1_Center = backGround_2_Center + levelSize
                color_back1 =  random.choice(colors)
                backGround_1_color =  color_back1
            
            
            if  backGround_2_Center + ((levelSize/2)+1) < -1.0:
                backGround_2_Center = backGround_1_Center + levelSize
                color_back2 = random.choice(colors)
                while color_back1 == color_back2 :
                    color_back2 = random.choice(colors)
                backGround_2_color =  color_back2


            if backGround_1_Center + (levelSize/2)-1 >= -1:
                level1_incremented = False
            

            # 3l4an el cloudes tzhr .. mfi4 w7da ttrsm fo2 w7da t5feha
            if backGround_1_Center > backGround_2_Center:
                BackGround(backGround_1_Center, backGround_1_color[0], backGround_1_color[1], backGround_1_color[2],levelSize)
                BackGround(backGround_2_Center , backGround_2_color[0],backGround_2_color[1],backGround_2_color[2],levelSize)
            else:
                BackGround(backGround_2_Center, backGround_2_color[0],backGround_2_color[1],backGround_2_color[2],levelSize)
                BackGround(backGround_1_Center, backGround_1_color[0], backGround_1_color[1], backGround_1_color[2],levelSize)

            
            if initialBackgroundCenter > -levelSize:
                initialBackground(initialBackgroundCenter)#initialBackgroundCenter


            if not balloonPop:
                x, y = pg.mouse.get_pos()
                t=1
                Width, Hight = display
                
                prot_r = 0.035
                DistX, DistY = pg.mouse.get_rel()  # how far the mouse moved since last frame
                MotionX = (DistX / Width) * (2*t) 
                MotionY = (DistY / Hight) * (2*t) 


            glColor3f(222/255, 243/255, 249/255)
            for n in FallingObjects:    
                if n['type'] == 'square':
                    square(n['x'], n['y'],n['size'])
                    #Circle1(n['radius'] ,n['x'], n['y'])
                elif n['type'] == 'triangle':
                    Triangle(n['x'], n['y'],n['size'])
                    #Circle1(n['radius'] ,n['x'], n['y'])
                elif n['type'] == 'circle':
                    Circle2(n['Realradius'],n['x'], n['y'])
                elif n['type'] == 'Diamond':
                    Diamond(n['Realradius'],n['x'], n['y'])
                    #Circle1(n['radius'] ,n['x'], n['y'])
                elif n['type'] == 'poly_8':
                    Poly_8(n['Realradius'],n['x'], n['y'])
                    #Circle1(n['radius'] ,n['x'], n['y'])
                elif n['type'] == 'poly_6':
                    Poly_6(n['Realradius'],n['x'], n['y'])
                    #Circle1(n['radius'] ,n['x'], n['y'])
                elif n['type'] == 'X_Shape':
                    X_Shape(n['x'], n['y'],n['size'])
                    #Circle1(n['radius'] ,n['x'], n['y'])
                elif  n['type'] == 'Star':
                    Star(n['x'], n['y'])
                    #Circle1(n['radius'] ,n['x'], n['y'])
                elif n['type'] == 'pyramid':
                    glEnable(GL_DEPTH_TEST)
                    Pyramid(angle,n['size'],n['x'],n['y'],0)
                    glDisable(GL_DEPTH_TEST)
                    #Circle1(n['radius'] ,n['x'], n['y'])
                elif  n['type'] == 'Arrow':
                    glEnable(GL_DEPTH_TEST)
                    Arrow(angle,n['size'],n['x'],n['y'],0)
                    glDisable(GL_DEPTH_TEST)
                    #Circle1(n['radius'],n['x'],n['y'])
                
                
                angle+=1

               
                dx = n['x'] - MouseX
                dy = n['y'] - MouseY
                effective_r = prot_r + n['radius'] 
                fcirc = mm.pow(dx,2) + mm.pow(dy,2) - pow(effective_r,2)
                
                if fcirc <= 0: 
                    dist = mm.sqrt(mm.pow(dx,2) + mm.pow(dy,2))
                    distToPush = effective_r  - dist + 0.001
                    push_x = (dx / dist) * distToPush  
                    push_y = (dy / dist) * distToPush 
                    n['x'] += push_x
                    n['y'] += push_y
                    
                    power = 4
                    n['VerticalSpeed'] =MotionY * power 
                    n['horizontalSpeed'] += MotionX * power  
                

            if not balloonPop :
                Balloon(-0.35)
                DuckBalloon(0,-0.35)
                x, y = pg.mouse.get_pos()
                t=1
                Width, Hight = display
                MouseX =  (x / Width) * ( 2*t ) - t
                MouseY =  ( (Hight - y) / Hight ) * ( 2*t ) - t
                protector(MouseX, MouseY)
        
           
            
            draw_text(f"{int(score)}", -0.8, 0.81, 25)
            draw_text("_____", -0.8, 0.8, 30)
            draw_text(" SCORE", -0.8, 0.76, 20)

            #levels
            draw_text(f" {current_level} / 10", 0.7, 0.81, 25)
            draw_text("______", 0.7, 0.8, 30)
            draw_text("LEVEL", 0.72, 0.76, 20)
            

            Screen_boundry(-1.2,1.5,-0.85,-1.5)
            Screen_boundry(1.2,-1.5,0.85,1.5)

            if balloonPop:
                draw_photo(RestartImage, -0.05,0)
                draw_text("Restart", -0.05, -0.06, 20)
                draw_text("On Mouse Click", -0.1, -0.1, 20)
            
            pg.display.flip()
      
main()