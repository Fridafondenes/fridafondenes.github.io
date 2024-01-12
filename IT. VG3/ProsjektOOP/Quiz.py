class Quiz: 
    def __init__ (slef, name):
        self.name = name
        self.questions = []
    
    def add_questions(self, questions):
        self.questions.append(questions)

    def start_quiz(self, user)