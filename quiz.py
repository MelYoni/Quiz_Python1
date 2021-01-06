from question import Question

question_prompts = [
"Quel est le doctype d'un document HTML5?\n(a) <!DOCTYPE html5>\n(b) <!DOCTYPE html>\n(c) <!DOCTYPE html PUBLIC\n\n",
"Quelle nouvelle balise de section permet de regrouper un contenu tangentiel au contenu principal du document ?\n(a) <section id='sidebar'>\n(b) <sidebar>\n(c) <aside>\n\n",
"Quel élément sépare la propriété de sa valeur ?\n(a) Le signe espace ( )\n(b) Le signe égal (=)\n(c) Le signe deux points (:)\n\n",
"Quelle URL dois-je créer pour ma version de site mobile ?\n(a) celle qui me plaît\n(b) monsite.mobi\n(c) iphone.monsite.com\n\n"
]

questions = [
    Question(question_prompts[0],"b"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"c"),
    Question(question_prompts[3],"a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Vous avez", score, "réponses sur", len(questions))

run_test(questions)