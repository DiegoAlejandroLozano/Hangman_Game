import os
import random
import mensajes

class Ahorcado:

    #Método encargado de iniciarlizar el objeto Ahorcado
    def __init__(self):        
        self.__titulo_juego = mensajes.TITULO_JUEGO
        self.__palabra_adivinar = self.__seleccionar_palabra_azar()
        self.__palabra_guiones = self.__inicializar_palabra_guiones()

    #Método encargado de contruir palabra con solo guiones
    def __inicializar_palabra_guiones(self):
        palabra = ""
        for i in self.__palabra_adivinar:
            palabra += "_"
        return palabra
    
    #Méotodo encargada de seleccionar una palabra al azar del archivo data.txt
    def __seleccionar_palabra_azar(self):
        palabra_azar = ""
        with open("data.txt", "r", encoding="utf-8") as f:
            lista_palabras = f.readlines()
            palabra_azar = random.choice(lista_palabras).rstrip()
        return palabra_azar    

    #Método encargado de ir contruyendo la palabra con las letras encontradas y guiones
    def construir_palabra(self, letra): 
        array_palabra_guiones = list(self.__palabra_guiones)       
        for i in range(0, len(self.__palabra_adivinar)):
            if letra == self.__palabra_adivinar[i]:
                array_palabra_guiones[i] = letra
        self.__palabra_guiones = "".join(array_palabra_guiones)

    #Método encargado de actualizar la pantalla del juego cuando se encuentra una letra
    def actualizar_pantallar(self):
        os.system("cls")
        print(self.__titulo_juego)
        print("Palabra oculta: %s" % self.__palabra_guiones)

    #Método encargado de verificar si el usuario ingreso una letra
    def verificar_letra(self, letra):
        letras_abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'á', 'é', 'í', 'ó', 'ú']
        if letra.lower() in letras_abc:
            return True
        else:
            return False   

    #Método encargado de validar si la letra está en la palabra
    def comprobar_letra_en_palabra(self, letra):
        if letra in self.__palabra_adivinar:
            """ self.__construir_palabra(letra)
            self.__actualizar_pantallar() """
            return True
        else:
            return False   

    #Método encargada de limpiar la pantalla cuando se inicia el juego
    def dibujar_pantalla_inicio(self):
        os.system("cls")
        print(self.__titulo_juego)
        matriz = ["_" for letra in self.__palabra_adivinar]
        print("Palabra oculta: %s" % "".join(matriz))

    #Método encargado de verificar si ya se adivinó la palabra
    def comparar_palabras(self):
        if self.__palabra_adivinar == self.__palabra_guiones:
            return True
        else:
            return False

#Función de inicio
def main():

    ahorcado = Ahorcado()
    ahorcado.dibujar_pantalla_inicio()
    palabra_encontrada = False

    while not palabra_encontrada:
        letra = input("Ingrese una letra: ")
        if not ahorcado.verificar_letra(letra) and not ahorcado.comprobar_letra_en_palabra(letra):
            continue
        else:
            ahorcado.construir_palabra(letra)
            ahorcado.actualizar_pantallar()
            if ahorcado.comparar_palabras():
                print("Palabra encontrada")
                palabra_encontrada = True
            else:
                continue

#inicializando el programa
if __name__ == "__main__":
    main()
