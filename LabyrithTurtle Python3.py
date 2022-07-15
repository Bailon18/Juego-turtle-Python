from turtle import Turtle, Screen
import math
import turtle
import random
import os
from random import randint





#Movimientos 
def forward():
    yertle.undo()
    turtle_1.forward(40)
    boundary_check()
    
    #Hallando coordenadas de la tortuga y mostrando
    x = turtle_1.xcor()
    y = turtle_1.ycor()
    vx='a'
    vy=0
    
    if(x==(-145.0)):
        vx = 'a'
    elif(x==(-105.0)):
        vx = 'b'
    elif(x==(-65.0)):
        vx = 'c'
    elif(x==(-25.0)):
        vx = 'd'
    elif(x==(15.0)):
        vx = 'e'
    elif(x==(55.0)):
        vx = 'f'
    elif(x==(95.0)):
        vx = 'g'
    elif(x==(135.0)):
        vx = 'h'
    elif(x==(175.0)):
        vx = 'i'
    elif(x==(215.0)):
        vx = 'j'
    elif(x==(255.0)):
        vx = 'k'
    elif(x==(295.0)):
        vx = 'l'

        
    if(y==(-145.0)):
        vy = '0'
    elif(y==(-105.0)):
        vy = '1'
    elif(y==(-65.0)):
        vy = '2'
    elif(y==(-25.0)):
        vy = '3'
    elif(y==(15.0)):
        vy = '4'
    elif(y==(55.0)):
        vy = '5'
    elif(y==(95.0)):
        vy = '6'
    elif(y==(135.0)):
        vy = '7'
    elif(y==(175.0)):
        vy = '8'
    elif(y==(215.0)):
        vy = '9'
    elif(y==(255.0)):
        vy = '10'
    elif(y==(295.0)):
        vy = '11'

    yertle.write("Avanza"+" "+str(vx)+","+str(vy), font=FONT)
    #fin de hallar y mostrar coordenadas de tortuga


def right():
    turtle_1.right(90)
    yertle.undo()
    yertle.write("Derecha", font=FONT)
    



def left():
    turtle_1.left(90)
    yertle.undo()
    yertle.write("Izquierda", font=FONT)
 


def backward():
    turtle_1.backward(40)
    boundary_check()
    yertle.undo()
    yertle.write("Retrocede", font=FONT)
    #Hallando coordenadas de la tortuga y mostrando
    x = turtle_1.xcor()
    y = turtle_1.ycor()
    vx='a'
    vy=0
    
    if(x==(-145.0)):
        vx = 'a'
    elif(x==(-105.0)):
        vx = 'b'
    elif(x==(-65.0)):
        vx = 'c'
    elif(x==(-25.0)):
        vx = 'd'
    elif(x==(15.0)):
        vx = 'e'
    elif(x==(55.0)):
        vx = 'f'
    elif(x==(95.0)):
        vx = 'g'
    elif(x==(135.0)):
        vx = 'h'
    elif(x==(175.0)):
        vx = 'i'
    elif(x==(215.0)):
        vx = 'j'
    elif(x==(255.0)):
        vx = 'k'
    elif(x==(295.0)):
        vx = 'l'

        
    if(y==(-145.0)):
        vy = '0'
    elif(y==(-105.0)):
        vy = '1'
    elif(y==(-65.0)):
        vy = '2'
    elif(y==(-25.0)):
        vy = '3'
    elif(y==(15.0)):
        vy = '4'
    elif(y==(55.0)):
        vy = '5'
    elif(y==(95.0)):
        vy = '6'
    elif(y==(135.0)):
        vy = '7'
    elif(y==(175.0)):
        vy = '8'
    elif(y==(215.0)):
        vy = '9'
    elif(y==(255.0)):
        vy = '10'
    elif(y==(295.0)):
        vy = '11'

    yertle.write("Avanza"+" "+str(vx)+","+str(vy), font=FONT)
    #fin de hallar y mostrar coordenadas de tortuga


#impacto entre la tortuga y la meta
def iscollision(t1, t2):
    d = math.sqrt((t2.xcor() - t1.xcor()) ** 2 + (t2.ycor() - t1.ycor()) ** 2)
    return d < 20.0

def draw_wall(turtle, positions):
    turtle.penup()
    turtle.setposition(positions[0])
    turtle.pendown()
    for position in positions[1:]:
        turtle.setposition(position)


#opciones de ventana
screen = Screen()
screen.title("Proyecto FINAL")
screen.setup(900, 900)
screen.bgcolor('white')

screen.onkey(forward, "Up")
screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(backward, "Down")
screen.listen()

# borde del juego
border = Turtle(visible=False)
border.penup()
border.pensize(10)
border.pencolor('black')
border.setposition(-450, -450)
border.pendown()
border.speed("fastest")

for _ in range(4):
    border.forward(900)
    border.left(90)























Tess=turtle.Turtle()
Tess.pensize(1)
Tess.speed(10)
w=40

def mysquare(who,thecolor,size):
    who.pendown()
    who.pencolor(thecolor)
    who.fillcolor(thecolor)
    who.begin_fill()
    who.setheading(0)
    for i in range(4):
        who.forward(size)
        who.left(90)
    who.end_fill()
    
#haciendo el grafico del laberinto
for i in range(12):
  for j in range(12):


#      print(i,j)
        #primera columna 
      if (i==0) and (j==6):
          scolor='blue'
          #segunda columna
      elif (i==1) and (j==6):
          scolor='blue'
      elif (i==1) and (j==4):
          scolor='blue'
      elif (i==1) and (j==3):
          scolor='blue'
      elif (i==1) and (j==2):
          scolor='blue'

          #tercera columna
      elif (i==2) and (j==6):
          scolor='blue'
      elif (i==2) and (j==4):
          scolor='blue'
      elif (i==2) and (j==2):
          scolor='blue'
      elif (i==2) and (j==7):
          scolor='blue'
      elif (i==2) and (j==8):
          scolor='blue'
      elif (i==2) and (j==9):
          scolor='blue'  
      elif (i==2) and (j==10):
          scolor='blue'

          

      elif (i==3) and (j==2):
          scolor='blue'
      elif (i==3) and (j==4):
          scolor='blue'
          scolor='blue'
      elif (i==3) and (j==9):
          scolor='blue'
      elif (i==3) and (j==6):
          scolor='blue'  


          
      elif (i==4) and (j==9):
          scolor='blue'
      elif (i==4) and (j==8):
          scolor='blue'
      elif (i==4) and (j==7):
          scolor='blue'
      elif (i==4) and (j==6):
          scolor='blue'
      elif (i==4) and (j==5):
          scolor='blue'
      elif (i==4) and (j==4):
          scolor='blue'        
      elif (i==4) and (j==2):
          scolor='blue'

          
   

      elif (i==5) and (j==2):
          scolor='blue'
      elif (i==5) and (j==4):
          scolor='blue'




      elif (i==6) and (j==2):
          scolor='blue'
      elif (i==6) and (j==4):
          scolor='blue'
          

      elif (i==7) and (j==9):
          scolor='blue'
      elif (i==7) and (j==8):
          scolor='blue'
      elif (i==7) and (j==7):
          scolor='blue'
      elif (i==7) and (j==6):
          scolor='blue'  
      elif (i==7) and (j==5):
          scolor='blue'
      elif (i==7) and (j==4):
          scolor='blue'
      elif (i==7) and (j==2):
          scolor='blue'
      elif (i==7) and (j==3):
          scolor='blue'

          

      elif (i==8) and (j==6):
          scolor='blue'


      elif (i==9) and (j==6):
          scolor='blue'
      elif (i==9) and (j==7):
          scolor='blue'
      elif (i==9) and (j==8):
          scolor='blue'



      elif (i==10) and (j==8):
          scolor='blue'


      elif (i==11) and (j==8):
          scolor='blue'

          
          
      else:
          scolor='red'
      Tess.penup()
      Tess.goto((i-4)*w,(j-4)*w)
      mysquare(Tess,scolor,w)


      
      letras = 'abcdefghijklmn'
      FONTE = 10
      FONTA = ("Ariel", FONTE, "normal")
      turtle.color("white")
      turtle.setpos((i*40)-120, (j*40)-150)
      turtle.write(str(letras[i])+","+str(j), align="right", font=FONTA)
  print("Juego python")    
   









	
 
	# solicituamos una opción al usuario

# end goal
goal = Turtle(shape='circle')
goal.color('gold')
goal.penup()
goal.setposition(305, 175)

turtle_1 = Turtle(shape='turtle')
turtle_1.color('black')
turtle_1.penup()
turtle_1.setposition(-145, 95)


trap = Turtle(shape='square')
trap.color('orange')
trap.penup()
trap.setposition(130, 175)


trap_1 = Turtle(shape='square')
trap_1.color('orange')
trap_1.penup()
trap_1.setposition(-65, 255)

trap_2 = Turtle(shape='square')
trap_2.color('orange')
trap_2.penup()
trap_2.setposition(-20, 95)

trap_3 = Turtle(shape='square')
trap_3.color('orange')
trap_3.penup()
trap_3.setposition(100, 25)

def boundary_check():
    # boundary check
    if not -450 < turtle_1.xcor() < 450 or not -450 < turtle_1.ycor() < 450:
        turtle_1.right(180)

    if iscollision(turtle_1, goal):
        goal.hideturtle()
        turtle.undo()
        turtle.write("FIN DEL JUEGO", font=FONT)
            

    #colisiones con las trampas    
    if iscollision(turtle_1, trap):
        turtle_1.penup()
        turtle_1.setposition(-145, 95)
      
        
        
    if iscollision(turtle_1, trap_1):
        turtle_1.penup()
        turtle_1.setposition(-145, 95)

    if iscollision(turtle_1, trap_2):
        turtle_1.penup()
        turtle_1.setposition(-145, 95)
        
    if iscollision(turtle_1, trap_3):
        turtle_1.penup()
        turtle_1.setposition(-145, 95)

    # if iscollision(turtle, maze_1):
    #   turtle_1.right(180)
    # if iscollision(turtle, maze_2):
    #   turtle_1.right(180)
    # if iscollision(turtle, maze_3):
    #   turtle_1.right(180)


     





global FONTSIZE
global FONT

FONTSIZE= 15
FONT = ("Ariel", 15, "normal")

turtle = Turtle(visible=False)
turtle.penup()








yertle = Turtle()

yertle.penup()
yertle.home()










turtle.setpos(-210, FONTSIZE*2 - FONTSIZE/2)
turtle.write("1.Jugar", align="right", font=FONT)

turtle.setpos(-210, -FONTSIZE/2)
turtle.write("2.Solucion", align="right", font=FONT)

turtle.setpos(-210, -FONTSIZE*2 - FONTSIZE/2)
turtle.write("3.Instrucciones", align="right", font=FONT)

turtle.setpos(-340, -200)
turtle.write("Seleciona una opcion: ", font=FONT)



def onclick_handler(x, y):
    turtle.undo()      
    if -400 < x < 100:
        if FONTSIZE < y < FONTSIZE*3:
            yertle.undo()             
            turtle.undo()      
            n=(randint(1, 6))#numero del dado
            d=(randint(1, 4))#posicion a donde ira
            if (d==1):
                r='izquierda'
            elif (d==2):
                r='derecha'
            elif (d==3):
                r='arriba'
            elif (d==4):
                r='abajo'

            turtle.setpos(-340, -200)
            turtle.write("El dado lanzo: " + str(n)+ "  |  Direcion es hacia: " + str(r), font=FONT)
            yertle.setpos(-340, -250)
            yertle.write("Inicio ", font=FONT)
        elif -FONTSIZE < y < FONTSIZE:
            turtle.undo()
            turtle.setpos(-340, -200)
            turtle.write("Solucion del laberinto", font=FONT)



                        #pintando solucion
            for i in range(12):
              for j in range(12):



            #      print(i,j)
                    #primera columna 
                  if (i+j)==0:
                      scolor='yellow'
                      #segunda columna
                  elif (i==1) and (j==0):
                      scolor='yellow'
                  elif (i==1) and (j==1):
                      scolor='yellow'
                  elif (i==1) and (j==2):
                      scolor='yellow'
                  elif (i==1) and (j==3):
                      scolor='yellow'
                  elif (i==1) and (j==4):
                      scolor='yellow'
                  elif (i==1) and (j==5):
                      scolor='yellow'
                  elif (i==1) and (j==6):
                      scolor='blue'
                  elif (i==1) and (j==7):
                      scolor='blue'
                  elif (i==1) and (j==8):
                      scolor='blue'
                  elif (i==1) and (j==9):
                      scolor='blue'
                  elif (i==1) and (j==10):
                      scolor='blue'

                      #tercera columna
                  elif (i==2) and (j==0):
                      scolor='blue'
                  elif (i==2) and (j==3):
                      scolor='blue'
                  elif (i==2) and (j==5):
                      scolor='yellow'
                  elif (i==2) and (j==10):
                      scolor='blue'

                      

                  elif (i==3) and (j==5):
                      scolor='yellow'
                  elif (i==3) and (j==2):
                      scolor='blue'
                  elif (i==3) and (j==1):
                      scolor='blue'
                  elif (i==3) and (j==0):
                      scolor='blue'
                  elif (i==3) and (j==3):
                      scolor='blue'
                      scolor='blue'
                  elif (i==3) and (j==10):
                      scolor='blue'

                      
                      
                  elif (i==4) and (j==0):
                      scolor='blue'
                  elif (i==4) and (j==5):
                      scolor='yellow'
                  elif (i==4) and (j==4):
                      scolor='yellow'
                  elif (i==4) and (j==6):
                      scolor='blue'
                  elif (i==4) and (j==10):
                      scolor='blue'
                      
               
                  elif (i==5) and (j==6):
                      scolor='blue'
                  elif (i==5) and (j==4):
                      scolor='yellow'
                  elif (i==5) and (j==3):
                      scolor='yellow'
                  elif (i==5) and (j==2):
                      scolor='yellow'
                  elif (i==5) and (j==10):
                      scolor='blue'


                      
                  elif (i==6) and (j==6):
                      scolor='blue'
                  elif (i==6) and (j==2):
                      scolor='yellow'
                  elif (i==6) and (j==1):
                      scolor='blue'
                  elif (i==6) and (j==0):
                      scolor='blue'
                  elif (i==6) and (j==4):
                      scolor='blue'
                  elif (i==6) and (j==10):
                      scolor='blue'
                  elif (i==6) and (j==7):
                      scolor='blue'
                  elif (i==6) and (j==8):
                      scolor='blue'
                  elif (i==6) and (j==9):
                      scolor='blue'


                      
                  elif (i==7) and (j==0):
                      scolor='blue'
                  elif (i==7) and (j==10):
                      scolor='blue'
                  elif (i==7) and (j==2):
                      scolor='yellow'
                  elif (i==7) and (j==4):
                      scolor='blue'

                      

                  elif (i==8) and (j==0):
                      scolor='yellow'
                  elif (i==8) and (j==1):
                      scolor='yellow'
                  elif (i==8) and (j==10):
                      scolor='blue'
                  elif (i==8) and (j==2):
                      scolor='yellow'
                  elif (i==8) and (j==4):
                      scolor='blue'
                      

                  elif (i==9) and (j==0):
                      scolor='yellow'
                  elif (i==9) and (j==10):
                      scolor='blue'
                  elif (i==9) and (j==4):
                      scolor='blue'
                  elif (i==9) and (j==5):
                      scolor='blue'
                  elif (i==9) and (j==6):
                      scolor='blue'
                  elif (i==9) and (j==7):
                      scolor='blue'          


                  elif (i==10) and (j==0):
                      scolor='yellow'
                  elif (i==10) and (j==10):
                      scolor='blue'


                  elif (i==11) and (j==1):
                      scolor='blue'
                  elif (i==11) and (j==10):
                      scolor='blue'
                  elif (i==11) and (j==2):
                      scolor='blue'
                  elif (i==11) and (j==3):
                      scolor='blue'
                  elif (i==11) and (j==4):
                      scolor='blue'
                  elif (i==11) and (j==5):
                      scolor='blue'
                  elif (i==11) and (j==6):
                      scolor='blue'
                  elif (i==11) and (j==7):
                      scolor='blue'
                  elif (i==11) and (j==8):
                      scolor='blue'
                  elif (i==11) and (j==9):
                      scolor='blue'
                  elif (i==11) and (j==0):
                      scolor='yellow'
                      
                      
                  else:
                      scolor='red'
                  Tess.penup()
                  Tess.goto((i-4)*w,(j-4)*w)
                  mysquare(Tess,scolor,w)

##                  letras = 'abcdefghijklmn'
##                  FONTSIZE = 10
##                  FONT = ("Ariel", FONTSIZE, "normal")
##                  turtle.color("white")
##                  turtle.setpos((i*40)-120, (j*40)-150)
##                  turtle.write(str(letras[i])+","+str(j), align="right", font=FONTS)
##              print("Juego python")    


                        #regresando a su estado




                                

                         # solicituamos una opción al usuario
                        
                        # end goal
                       
              goal.color('gold')
              goal.penup()
              goal.setposition(305, -145)

                        
              turtle_1.color('black')
              turtle_1.penup()
              turtle_1.setposition(-145, -145)


              trap.color('orange')
              trap.penup()
              trap.setposition(10, -145)


              trap_1.color('orange')
              trap_1.penup()
              trap_1.setposition(20, 100)


              trap_2.color('orange')
              trap_2.penup()
              trap_2.setposition(-100, 100)

              trap_3.color('orange')
              trap_3.penup()
              trap_3.setposition(100, -145)









              
        elif -FONTSIZE*3 < y < -FONTSIZE:
            turtle.undo()
            turtle.setpos(-340, -200)
            turtle.write("Para poder moverse debe girar la cabeza de la tortuga a la direccion", font=FONT)

         
##Llamando a las funciones            
screen = Screen()
screen.onscreenclick(onclick_handler)

screen.mainloop()
