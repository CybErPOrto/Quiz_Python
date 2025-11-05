# Quizz interactif en Python
quizz = {
 "question": "Quelle est la capitale de la France ?",
 "options": ["Berlin", "Madrid", "Paris", "Rome"],
 "answer": "Paris"
}
def run_quiz(quiz):
    print(quiz["question"])
    for i, option in enumerate(quiz["options"], 1):
        print(f"{i}. {option}")

    user_answer = input("Votre réponse (entrez le numéro correspondant) : ")
    try:
        user_choice = quiz["options"][int(user_answer) - 1]
        if user_choice == quiz["answer"]:
            print("Bien joué epervier ! 🎉")
        else:
            print(f"Perdu 🤣. La bonne réponse est : {quiz['answer']}")

    except (IndexError, ValueError):
        print("N'oublie pas, la bonne réponse est toujours dans les options !")

if __name__ == "__main__":
    run_quiz(quizz)

quizz1 = {
 "question": "Ou habite Vincent ?",
 "options": ["Marseille", "Bordeaux", "Paris", "Lille"],
 "answer": "Paris"
}
def run_quiz(quiz):
    print(quiz["question"])
    for i, option in enumerate(quiz["options"], 1):
        print(f"{i}. {option}")
    user_answer = input("Entre ta réponse (entrez le numéro correspondant) : ")
    try:
        user_choice = quiz["options"][int(user_answer) - 1]
        if user_choice == quiz["answer"]:
            print("Bien joué epervier !😎 🎉")
        else:
            print(f"Perdu 🤣. La bonne réponse est : {quiz['answer']}")
    except (IndexError, ValueError):
        print("Perdu 😒. réessaye à nouveau.")
if __name__ == "__main__":
    run_quiz(quizz1)

    quizz2 = {
 "question": "Ou ce situe le plus beau Mac Do du monde ?",
 "options": ["Paris", "Bulgarie", "Belgique", "Portugal"],
 "answer": "Portugal"
}
def run_quiz(quiz):
    print(quiz["question"])
    for i, option in enumerate(quiz["options"], 1):
        print(f"{i}. {option}")
    user_answer = input("Entre ta réponse (entrez le numéro correspondant) : ")
    try:
        user_choice = quiz["options"][int(user_answer) - 1]
        if user_choice == quiz["answer"]:
            print("🎇 Bien joué epervier !Tu as le droit à un Mac Do ce soir !🍔🍟 😎 🎉")
            
        else:
            print(f"❌Perdu 🤣. Pas de Mac Do ce Soir 🤣😁: {quiz['answer']}")
    except (IndexError, ValueError):
        print("⚠️ Réponse pas valide. Essaie à nouveau avec un numéro entre 1 et 4.")

if __name__ == "__main__":
    run_quiz(quizz2)