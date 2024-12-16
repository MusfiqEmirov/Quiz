import random
 # vereceyimiz suallar ve cavablarin aldigi classi yaratmag
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
# cavablari yoxlamagcun
    def check_answer(self,answer):

        if answer not in self.choices:
            raise ValueError("xetali melumat")
        return self.answer == answer

q1 = Question("en yaxwi proqramlawdirma dili hansidir?", ["python", "java", "c#", "c++","php"], "python")        
q2 = Question("en mehsur proqramlawdirma dili hansidir?", ["c++", "c#", "php", "python", "java"], "python")        
q3 = Question("en cox qazandiran proqramlawdirma dili hansidir?", ["java", "python", "c#","php", "c++"], "python")        
q4 = Question("en cox sade yazilim olan proqramlawdirma dili hansidir?", ["php","java", "python", "c#", "c++"], "python")        
q5 = Question("en maragli ve suretli proqramlawdirma dili hansidir?", ["java", "python", "php", "c#", "c++"], "python")        

result_list = [q1, q2, q3, q4, q5]

class Quiz:
    def __init__(self,question):
        self.question = random.sample(question,len(question))# random.sample suallari random gotursun.suffle class daxilinde iwlmeir
        self.quiz_index = 0
        self.score = 0

    # hansi suali vereceyimiz indexle teyin edirik
    def get_question(self):
        return self.question[self.quiz_index]

    #suali sual_x daxil edib ve bunu method halina getirib
    def display_question(self):
        sual_x = self.get_question()
        
        print(f"Suallar {self.quiz_index  + 1} : {sual_x.text}")
        # sullarla bir yerde


        for x,q in enumerate(sual_x.choices):
            print(f"{x + 1}-{q}" )

        answer = input("cavab:")
        # eger cavab truedise pointi bir bir artir
        if sual_x.check_answer(answer):
            self.score += 1
            print("TEBRIKLER:DOGRU CAVAB")
        else:
            print("CAVAB DOGRU DEYIL")
        # ve tekrardan diger suala kec
        self.quiz_index += 1
        self.load_question()
        
    def load_question(self):
 
        # eger sual sayi indexe beraberdirse sual bitmiwdir ve pointi
        if len(self.question) == self.quiz_index:
            self.display_score()
        # eger sual sayi indexe beraber deyilse sual vermeye davam ele
        else:
            self.display_proqress()
            self.display_question()   

    # eger suaalar bitibse neticeler gosteren method
    def display_score(self):

        print("TEST NETICELERINIZ".center(100,"-"))
        point = 100 / len(self.question)
        total_point = self.score * point
        print(f"Umumi {len(self.question)} sualin {self.score} ededini bildiniz")
        print("Qazandiginiz Point:",total_point)

    # umumi suali ve hansi suallarda oldugunu gosterir
    def display_proqress(self):
        total_question = len(self.question)
        question_number = self.quiz_index + 1

        print(f"Umumi {total_question} sualin {question_number}-ci sualindasiniz".center(100,"-"))


quiz = Quiz(result_list)
quiz.load_question()  


# melumatlandiri ve kocurulmeli menbe Udemy

