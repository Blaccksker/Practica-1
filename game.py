import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "armaggedon", "desarrollo", "iteracion", "desafio",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_attempts = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# pregunto al usuario que dificultad quiere que tenga el juego
dificultad = input("""ELIJA LA DIFICULTAD: 
        1-Facil
        2-Medio
        3-Dificil
        """)

#Evaluo si la opcion ingresada es correcta
while dificultad not in ["1","2","3"]:
    print('dificultad no valida, ingrese otra opcion')
    dificultad = input("""ELIJA LA DIFICULTAD: 
        1-Facil
        2-Medio
        3-Dificil
        """)
        
#Procedo dependiendo la dificultad
match dificultad:
    case "1":
     print('Has elegido la dicultad (Facil), Ahora si la palabra contiene vocales estas se mostraran')
     word_displayed = "".join(letter if letter in 'aeiou' else "_" for letter in secret_word)
    case "2":
     print('Has elegido la dificultad(Medio), se mostrara la primera y ultima letra de la palabra')
     word_displayed = secret_word[0] + "_" * (len(secret_word)-2) + secret_word[-1]
    case "3": 
     print('Has elegido la dificultad (Dificil), no se mostrara completamente nada')
     word_displayed = "_" * len(secret_word)
         
#Muestro la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

failures = 0
while failures < max_attempts:
     
     #contador de errores
     print(f' ERRORES: {failures}')
     
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()
     
     # Verifico si se escribio alguna letra
     if not letter:
         print('No se ingreso ninguna letra, por favor ingrese una.')
         continue
     
     # Verificar si la letra ya ha sido adivinada
     if letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         failures += 1
         continue
         
     # Verificar si la letra está en la palabra secreta, si esta la agrega a las letras adivinadas.
     if letter in secret_word:
         print("¡Bien hecho! La letra está en la palabra.")
         guessed_letters.append(letter)
     else:
         print("Lo siento, la letra no está en la palabra.")
         failures += 1
         
     # Mostrar la palabra parcialmente adivinada
     if dificultad == "1":
         word_displayed = "".join([letter if letter in guessed_letters or letter in "aeiou" else "-" for letter in secret_word])
     elif dificultad == "2":
         word_displayed = secret_word[0] + "".join([letter if letter in guessed_letters else "_" for letter in secret_word[1:-1]]) + secret_word[-1]
     else:
         word_displayed = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
     
     print(f"Palabra: {word_displayed}")
     
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
         break
     
#Si el numero de fallos es igual al maximo 
if failures == max_attempts:
     print(f"¡Oh no! Has tenido {max_attempts} fallos.")
     print(f"La palabra secreta era: {secret_word}")