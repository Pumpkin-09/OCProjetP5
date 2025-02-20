def calculate_average(numbers):  # Fonction calculate_average
    i = 0
    average = 0.0
    for number in numbers:
        average += number
        i += 1
    return average / i
 
# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
