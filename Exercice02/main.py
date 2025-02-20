students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}


name = input("Entrez le nom de l'étudiant:")

if name in students:
     number_subjects = 0
     somme_subjects = 0.0
     print(f"Note de {name}:")
     for subjects, data in students[name].items():
          print(f"Nom de la matière: {subjects} - {data}")
          somme_subjects += 1
          number_subjects += data
     average = number_subjects / somme_subjects
     print(f"Moyenne de {name}: {average:.2f}")

else:
     print(f"L'étudiant {name} n'exsiste pas dans la liste.")
