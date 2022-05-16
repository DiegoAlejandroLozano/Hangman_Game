from juego_del_ahorcado import Ahorcado

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
                ahorcado.dibujar_pantalla_ganadora()
                palabra_encontrada = True
            else:
                continue

#inicializando el programa
if __name__ == "__main__":
    main()
