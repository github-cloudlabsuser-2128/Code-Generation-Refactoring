# Programa para calcular la suma de una lista de números enteros ingresados por el usuario.
# Refactorizado para seguir buenas prácticas de programación.

MAX_ELEMENTS = 100

def calculate_sum(numbers):
   """Calcula la suma de una lista de números."""
   return sum(numbers)

def get_integer_input(prompt):
   """Solicita al usuario un número entero y valida la entrada."""
   while True:
      try:
         return int(input(prompt))
      except ValueError:
         print("Entrada inválida. Por favor, ingrese un número entero.")

def get_numbers_from_user(count):
   """Solicita al usuario una cantidad específica de números enteros."""
   numbers = []
   print(f"Ingrese {count} números enteros:")
   for i in range(count):
      number = get_integer_input(f"  Número {i + 1}: ")
      numbers.append(number)
   return numbers

def main():
   """Función principal del programa."""
   print("Programa para calcular la suma de números enteros.")
   while True:
      try:
         n = get_integer_input(f"Ingrese la cantidad de números a sumar (1-{MAX_ELEMENTS}): ")
         if 1 <= n <= MAX_ELEMENTS:
            break
         print(f"Por favor, ingrese un número entre 1 y {MAX_ELEMENTS}.")
      except KeyboardInterrupt:
         print("\nPrograma terminado por el usuario.")
         return

   numbers = get_numbers_from_user(n)
   total = calculate_sum(numbers)
   print(f"La suma de los números ingresados es: {total}")

if __name__ == "__main__":
   main()
