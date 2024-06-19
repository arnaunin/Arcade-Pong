import turtle
import random
import math

### -----VENTANA-----
# --Creamos la ventana--
wn = turtle.Screen()
wn.title("Juego arcade Pong")
wn.bgcolor("black")
wn.setup(width=600, height=800)

### -----CLASE PELOTA-----
# --Clase que crea la pelota--
class Pelota:
    def __init__(self):
        self.pelota = turtle.Turtle()
        self.pelota.color("white")
        self.pelota.shape("circle")
        self.pelota.penup()
        self.pelota.goto(0,0)
        self.dx = 0
        self.dy = 0
    
    # --Metodo para llevar la pelta al centro--
    def pelota_al_centro(self):
        self.pelota.hideturtle()
        self.pelota.goto(0,0)
        self.pelota.showturtle()
        self.dx = 0
        self.dy = 0
        
    # --Metodo para iniciar el movimiento de la pelota--
    def iniciar_movimiento(self):
        if self.dx == 0 and self.dy == 0:
            # La pelota saldrá cada vez en una dirección diferente
            self.velocidad = 8  # Magnitud fija de la velocidad
            # Ajustando el rango del ángulo para que la dirección sea más vertical
            angulo = random.uniform(math.pi/4, 3*math.pi/4)  # Hacia arriba
            angulo = random.choice([angulo, math.pi + angulo])  # Elegir entre hacia arriba o hacia abajo
            
            self.dx = self.velocidad * math.cos(angulo)  # Componente x de la velocidad
            self.dy = self.velocidad * math.sin(angulo)  # Componente y de la velocidad

    # --Metodo para mover la pelota--
    def mover(self):
        self.pelota.setx(self.pelota.xcor() + self.dx)
        self.pelota.sety(self.pelota.ycor() + self.dy)

    # --Metodo para hacer revotar la pelota contra las plataformas--
    def revotar_y(self):
        self.dy *= -1

    # --Metodo para hacer revotar la pelota contra las paredes--
    def revotar_x(self):
        self.dx *= -1

### -----CLASE PLATAFORMA-----
# --Clase de la plataforma con la que juega cada jugador--
class Plataforma:
    def __init__(self, posicion):
        self.cuerpo = turtle.Turtle() # Creamos la variable
        self.cuerpo.speed(0)
        self.cuerpo.shape("square") # Definimos la forma
        self.cuerpo.color("white") # Deefinimos el color
        self.cuerpo.shapesize(stretch_wid=0.2, stretch_len=4) # Definimos el tamaño
        self.cuerpo.penup() # Hace que no deje rastro del movimiento
        self.cuerpo.goto(0, posicion) #Establece la posición de la plataforma

    # --Metodo para mover hacia la izquiera--
    def izquierda(self):
        x = self.cuerpo.xcor()
        if x > -237:
            x = self.cuerpo.setx(x - 10)

    # --Metodo para mover hacia la derecha--
    def derecha(self):
        x = self.cuerpo.xcor()
        if x < 230:
            x = self.cuerpo.setx(x + 10)

### -----CLASE MARCADOR-----
class Marcador:
    def __init__(self):
        self.puntos_jugador1 = 0
        self.puntos_jugador2 = 0

        self.cuerpo_jugador1 = turtle.Turtle()
        self.cuerpo_jugador1.speed(0)
        self.cuerpo_jugador1.color("white")
        self.cuerpo_jugador1.penup()
        self.cuerpo_jugador1.hideturtle()
        self.cuerpo_jugador1.goto(0, 200)

        self.cuerpo_jugador2 = turtle.Turtle()
        self.cuerpo_jugador2.speed(0)
        self.cuerpo_jugador2.color("white")
        self.cuerpo_jugador2.penup()
        self.cuerpo_jugador2.hideturtle()
        self.cuerpo_jugador2.goto(0, -200)

        self.actualizar()

    def actualizar(self):
        self.cuerpo_jugador1.clear()
        self.cuerpo_jugador1.write(f"Jugador 1: {self.puntos_jugador2}", align="center", font=("Courier", 24, "normal"))

        self.cuerpo_jugador2.clear()
        self.cuerpo_jugador2.write(f"Jugador 2: {self.puntos_jugador1}", align="center", font=("Courier", 24, "normal"))

    def punto_para_jugador1(self):
        self.puntos_jugador1 += 1
        self.actualizar()

    def punto_para_jugador2(self):
        self.puntos_jugador2 += 1
        self.actualizar()

# --Creamos las dos plataformas con sus posiciones correctas--
plataforma_a = Plataforma(350)
plataforma_b = Plataforma(-350)

# --Vinculamos los metodos de movimiento de las plataformas a las teclas del teclado--
wn.listen()
wn.onkeypress(plataforma_a.izquierda, "a")  # Mueve la plataforma A hacia la izquierda con la tecla "a"
wn.onkeypress(plataforma_a.derecha, "d")    # Mueve la plataforma A hacia la derecha con la tecla "d"
wn.onkeypress(plataforma_b.izquierda, "Left")  # Mueve la plataforma B hacia la izquierda con la flecha izquierda
wn.onkeypress(plataforma_b.derecha, "Right")   # Mueve la plataforma B hacia la derecha con la flecha derecha


# --Dibujamos la linea en medio de la pantalla--
linea = turtle.Turtle()
linea.color("white")
linea.hideturtle() # Escondemos la tortuga
linea.penup()
linea.goto(-300,0) # Posicionamos la tortuga en un lado de la pantalla para empezar a dibujar la línea
# Dibujamos la línea del medio discontinua
for i in range(60):
    linea.pendown()
    linea.forward(5)
    linea.penup()
    linea.forward(5)

# Dibujamos el circulo central
circulo = turtle.Turtle()
circulo.color("white")
circulo.hideturtle()
circulo.penup()
circulo.goto(0,-100)
circulo.pendown()
circulo.circle(100)

# Creamos la variable de la pelota con la que vamos a jugar
pelota = Pelota()

# Creamos la variable marcador
marcador = Marcador()

# Cuando se presione la tecla de espacio la pelota comenzara a moverse
wn.listen()
wn.onkeypress(pelota.iniciar_movimiento, "space")

### -----MOVIMIENTO DE LA PELOTA-----
# Bucle que se ejecutara mientras la pelota este en movimiento
jugando = True

while jugando:
    pelota.mover() # Movemos la pelota

    # Caso en que la pelota rebota contra la plataforma superior (plataforma_a)
    if (330 <= pelota.pelota.ycor() <= 340) and \
        (pelota.pelota.xcor() > plataforma_a.cuerpo.xcor() - 60) and \
        (pelota.pelota.xcor() < plataforma_a.cuerpo.xcor() + 60):
        pelota.revotar_y()

    # Caso en que la pelota rebota contra la plataforma inferior (plataforma_b)
    if (-330 >= pelota.pelota.ycor() >= -340) and \
        (pelota.pelota.xcor() > plataforma_b.cuerpo.xcor() - 60) and \
        (pelota.pelota.xcor() < plataforma_b.cuerpo.xcor() + 60):
        pelota.revotar_y()

    # Caso en que la pelota revota contra una pared
    elif pelota.pelota.xcor() <= -285 or pelota.pelota.xcor() >= 280:
        pelota.revotar_x()

    # Caso en que el jugador b hace un punto
    if pelota.pelota.ycor() <= -400:
        pelota.pelota_al_centro()
        jugando = True
        pelota.iniciar_movimiento
        marcador.punto_para_jugador2()
    
    # Caso en que el jugadoor a hace punto
    if pelota.pelota.ycor() >= 400:
        jugando = False
        pelota.pelota_al_centro()
        jugando = True
        pelota.iniciar_movimiento
        marcador.punto_para_jugador1()

# --Para que la ventana no se cierre inmediatamente después de mover la tortuga--
turtle.done()