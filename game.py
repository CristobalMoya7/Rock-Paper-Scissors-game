
# User choices, creamos constantes, son como variables pero NO SE PUEDEN MODIFICAR.
# Se escriben en MAYUSCULA para que todo el mundo lo sepa

PAPER = 0
ROCK = 1
SCISSORS = 2
QUIT = 3
INVALID_CHOICE = -1 # Para el error si pone algo que no debe poner en el input



def game_loop():
    """
    Arranca el bucle principal del juego
    """
    while True:
        # Leo la selección del usuario (piedra, papel, tijera o parar el juego)
        user_choice = read_user_choice()
        # Siempre y cuando no quiera parar
        if not is_exit(user_choice):
            # genero una jugada del ordenador
            comp_choice = generate_computer_choice()
            # evalúo la jugada
            result = evaluate_move(user_choice, comp_choice)
            # muestro el ganador en pantalla y vuelta al principio
            print_result(result)
        else:
            # el humano es un gallina: salgo
            break

def read_user_choice():
    """
    Lee la jugada del humano, que ademas de piedra, papel o tijera,
    podria ser la de salir del juego
    """

    user_choice = INVALID_CHOICE

    while True:
        print("Select one number: ")
        print(f"{PAPER}. Paper") # f"{LO QUE SEA} Evaluo lo que hay en las llaves y el valor lo meto dentro de la cadena. 
        print(f"{ROCK}. Rock") # PARA ENTENDERLO: Esto lee que {ROCK} esta definido como 1 e imprimira 1. Rock, ya que yo puse el . Rock
        print(f"{SCISSORS}. Scissors")
        print("---------------------")
        print(f"{QUIT}. Quit the game")
        user_choice = int(input("Enter your choise: ")) # Ponemos el int para hacer el numero entero

        if user_choice in range(PAPER, QUIT + 1): # Validamos lo que haya escrito, recorremos desde el PAPER (que es el 1), Hasta QUIT. El 1 es para asegurar que QUIT tambien se incluye ya que es el ultimo
            # Si esta dentro de esto es un valor aceptable
            break

        else:
            # Si esta dentro de esto es un valor NO aceptable
            user_choice = INVALID_CHOICE

    return user_choice

def is_exit(game_choice):
    """
    Predicado que determina si la jugada es la opcion de salir del juego
    """
    
    return True

def generate_computer_choice():
    """
    Genera una jugada del ordenador al azar y la devuelve
    """

    return None

def evaluate_move(user_choise, computer_choise):
    """
    Recibe dos jugadas, determina cual ha ganado y devuelve un mensaje con el resultado.
    Por ejemplo: recibe Papel y Piedra, y devuelve "Papel envuelve a Piedra" 
    """

    return None

def print_result(result):
    """
    Imprime en plan bonito el resultado
    No devuelve nada
    """

    return None

if __name__ == "__main__":
    # No me han importado, me llaman desde la linea de comandos: Arranco el juego!!!!
    game_loop()
else:
    # Quiere decir que me han importado: No hago nada. El else no hace falta.
    pass