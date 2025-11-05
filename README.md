#Def. du Quizz sous forme de dictionnaire
   quizz = {
    "question": "Quelle est la capitale de la France ?",
    "options": ["Berlin", "Madrid", "Paris", "Rome"],
     "answer": "Paris"
      }

#Fonction pour exécuter le quizz
def run_quiz(quiz):

#Affichage de la question
    print(quiz["question"])

#Affichage des options avec des numéros
    for i, option in enumerate(quiz["options"], 1):
        print(f"{i}. {option}")

#Demande de réponse à l'utilisateur
      user_answer = input("Votre réponse (entrez le numéro correspondant) : ")
      try:

#Affichage de la réponse de l'utilisateur
        user_choice = quiz["options"][int(user_answer) - 1]
        if user_choice == quiz["answer"]:
            print("Bien joué epervier ! 🎉")
         else:
            print(f"Perdu 🤣. La bonne réponse est : {quiz['answer']}")

#Affichage d'un message d'encouragement
        except (IndexError, ValueError):
        print("N'oublie pas, la bonne réponse est toujours dans les options !")
        
#Point d'entrée du programme
      if __name__ == "__main__":
       run_quiz(quizz)


