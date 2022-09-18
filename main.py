BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
import random  
import time

iniciar_trivia = True
intentos = 0

print (MAGENTA+"Bienvenido a mi trivia sobre Cultura General del Perú nivel intermedio"+RESET)
time.sleep(3)
print ("Pondremos a prueba tus conocimientos")
time.sleep(2)
nombre = input ("\nIngresa tu nombre: ")
time.sleep(1)
print (BLUE+"\n Hola,", nombre,", esta trivia consiste en 4 preguntas las cuales, excepto la primera, te quitaran puntos si eliges la respuesta incorrecta, pero aumentarán tu puntaje si no lo es. Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET)
time.sleep(5)

while iniciar_trivia == True:
  intentos += 1

  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar\n")
  puntaje = random.randint(0, 20)
  print (YELLOW+"Antes de empezar, este programa te regalará un puntaje incial que será escogido aleatoriamente del rango 0-20"+RESET)
  time.sleep(3)
  print (YELLOW+"Cruza los dedos para que te toque un numero alto"+RESET)
  time.sleep(3)
  print("tu puntaje incial se mostrará en la pantalla en...")
  time.sleep(2)
  for numero_carga in range(3, 0, -1):
      print(numero_carga)
      time.sleep(1)
  print("\nTu puntaje es:",puntaje,)

  time.sleep(1)
  print("\nLa trivia empezara en...")
  for numero_carga in range(3, 0, -1):
      print(numero_carga)
      time.sleep(1)
  time.sleep(1)

# Pregunta 1

  print (GREEN+"\n1)"+RESET,GREEN+"La Ley General de las Ochos Horas fue conseguida durante el gobierno del presidente\n"+RESET)
  time.sleep(3)
  print (BLACK+"a)"+RESET, WHITE+ "José Pardo"+RESET)
  time.sleep(2)
  print (BLACK+"b)"+RESET +RESET, WHITE+ "Guillermo Billinghurst"+RESET)
  time.sleep(1)
  print (BLACK+"c)"+RESET, WHITE+ "Augusto B. Leguía"+RESET)
  time.sleep(2)
  print (BLACK+"d)"+RESET, WHITE+ "Lopez de Romaña"+RESET)
  
  respuesta_1 = input(RED+"\nTu respuesta: "+RESET).lower()
  time.sleep(1)
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input (YELLOW+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
  if respuesta_1 == "a":
    puntaje += 10
    print ("Muy bien,", nombre,"!")
  else:
    print ("Incorrecto,", nombre,"!")
  
  time.sleep(1)
  print(nombre,",llevas", puntaje, "puntos")
  time.sleep(2)
  
  # Pregunta 2
  
  print (GREEN+"\n2) ¿Cuáles son los símbolos patrios del Perú?\n"+RESET)
  time.sleep(3)
  print (BLACK+"a)"+RESET, WHITE+ "Himno nacional del Perú"+RESET)
  time.sleep(1)
  print (BLACK+"b)"+RESET, WHITE+ "Escudo del Perú"+RESET)
  time.sleep(1)
  print (BLACK+"c)"+RESET, WHITE+ "Bandera del Perú"+RESET)
  time.sleep(1)
  print (BLACK+"d)"+RESET, WHITE+"Todas las anteriores"+RESET)
  time.sleep(1)
  
  respuesta_2 = input(RED+"\nTu respuesta: "+RESET).lower()
  time.sleep(1)
  
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  time.sleep(1)
  if respuesta_2 == "a":
    print ("Es correcto!", nombre,", sin embargo, el escudo y la bandera del Perú tambien lo son, por lo que la alternativa correcta era la d")
    puntaje = puntaje -5
  elif respuesta_2 == "b":
    print ("Es correcto!",nombre,",""sin embargo, el himno nacional y la bandera del Perú tambien lo son, por lo que la alternativa correcta era la d")
    puntaje = puntaje -5
  elif respuesta_2 == "c":
    print ("Es correcto!", nombre,", sin embargo, el himno nacional y el escudo del Perú tambien lo son, por lo que la alternativa correcta era la d")
    puntaje = puntaje -5
  else:
    time.sleep(2)
    puntaje += 5
    print ("Bravisimo", nombre,"!")
  time.sleep(3)
  print(RED+ nombre, "llevas", puntaje, "puntos"+RESET)
  time.sleep(2)
  
  # Pregunta 3
  
  print (GREEN+"\n3) ¿Quiénes fueron los precursores y próceres del Perú?\n"+RESET)
  time.sleep(3)
  print (BLACK+"a)"+RESET, WHITE+"Juan Pablo Vizcardo y Guzmán"+RESET)
  time.sleep(1)
  print (BLACK+"b)"+RESET, WHITE+ "Magaly Bastidas"+RESET)
  time.sleep(1)
  print (BLACK+"c)"+RESET, WHITE+"Felipe Guamán Poma de Ayala"+RESET)
  time.sleep(1)
  print (BLACK+"d)"+RESET, WHITE+"Alan Garcia"+RESET)
  time.sleep(1)
  
  respuesta_3 = input(RED+"\nTu respuesta: "+RESET).lower()
  time.sleep(1)
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ").lower()
  time.sleep(1)
  if respuesta_3 == "a":
    print ("¡Exclente! Puedes pasar a la siguiente pregunta")
    puntaje = puntaje +15
  elif respuesta_3 == "b":
    print ("Incorrecto! Ese nombre es inventado")
    puntaje = puntaje - 10
  elif respuesta_3 == "c":
    print ("Incorrecto! Huaman Poma fue un cronista")
    puntaje = puntaje - 10
  else:
    print ("Alan Garcia?! es totalmente INCORRECTO! Él solo fue presidente del Perú en el perido 1985-1990 y 2006-2011")
    puntaje = puntaje -20
  time.sleep(1)
  print(RED+ nombre, "llevas", puntaje, "puntos"+RESET)
  time.sleep(1)
  print(RED+"ADVERTENCIA!!!"+RESET)
  time.sleep(2)
  print ("La siguiente y última pregunta sumaría el doble del valor absoluto de tu puntaje actual si la respondes correctamente! asi que aprovéchalo, tómate tu tiempo y léela detenidamente")
  time.sleep(6)
  print("¿Estás listx?")
  time.sleep(1)
  print("Última pregunta en...")
  time.sleep(1)
  for numero_carga in range(5, 0, -1):
    print(numero_carga)
    time.sleep(1)
  
  # Pregunta 4
  print (GREEN+"\n4) ¿Qué poeta de la Colonia es considerado el precursor de la poesía satírica?\n"+RESET)
  time.sleep(3)
  print (BLACK+"a)"+RESET, WHITE+ "Pedro Peralta"+RESET)
  time.sleep(1)
  print (BLACK+"b)"+RESET, WHITE+ "Juan del Valle y Caviedes"+RESET)
  time.sleep(2)
  print (BLACK+"c)"+RESET, WHITE+"Concolorcorvo"+RESET)
  time.sleep(2)
  print(BLACK+"d)"+RESET,WHITE+"Amarilis"+RESET)
  time.sleep(2)
  
  print("\nNo hay limite de tiempo en esta trivia,", nombre,",respira profundo y elije la correcta")
  time.sleep(4)
  respuesta_4 = input(RED+"\nTu respuesta: "+RESET).lower()
  time.sleep(1)
  
  while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  time.sleep(1)
  if respuesta_4 == "b":
    time.sleep(1)
    print ("¡¡¡Exclente!!! tu puntaje definitivamente es un valor positivo!!!")
    puntaje = puntaje + abs(puntaje)*3
    time.sleep(2)
  elif respuesta_4 == "b":
    time.sleep(1)
    print ("Incorrecto!...")
    time.sleep(1)
    puntaje = puntaje - 15
  elif respuesta_4 == "c":
    time.sleep(1)
    print ("Incorrecto!...")
    time.sleep(1)
    puntaje = puntaje - 15
  else:
    print ("Incorrecto!...")
    time.sleep(1)
    puntaje = puntaje -15
  time.sleep(1)
  
  print (MAGENTA+"\n Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos"+RESET)
  time.sleep(2)
  
  print(YELLOW+"\n¿Deseas intentar la trivia nuevamente?"+RESET)
  time.sleep(2)
  repetir_trivia = input(WHITE+"ingresa 'si'y luego enter para repetir, o cualquier tecla y luego enter para finalizar:"+RESET).lower()
  time.sleep(4)
  if repetir_trivia != "si":
    time.sleep(2)
    print(GREEN+"\nEspero", nombre, "que te hayas divertido, hasta pronto!"+RESET)

    
    iniciar_trivia = False
