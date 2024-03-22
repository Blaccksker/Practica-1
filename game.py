import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_attempts = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

# variable que ira contando los errores del jugador para evaluar si llego al maximo perimitido(perder)
failures = 0

while failures < max_attempts:
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
     letters = []
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
         else:
             letters.append("_")
     word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")
     
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
         break
     
#Si el numero de fallos es igual al maximo 
if failures == max_attempts:
     print(f"¡Oh no! Has tenido {max_attempts} fallos.")
     print(f"La palabra secreta era: {secret_word}")