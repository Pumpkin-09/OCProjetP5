## Écrivez votre code ici !

def square(number):
    if isinstance(number, (int, float)):
        return number * number
    else:
        print("Le paramètre doit être un nombre !")
        return None

test = square(8)

print(test)
