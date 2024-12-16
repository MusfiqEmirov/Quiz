# python quiz layihesi
bu bir imtaham ve sual cavab ucub teleberle bagli imtaham prosesidir

# layinin izahi
Layihe Quiz ve Question adli classlarla yaradilib

# MIT License

Copyright 2024 python.az

muellif huquqlaari pzulmadan awagidaki sertler altinda bu layiheni goturmek kopyalamaga ve derc elemeye icaze verilir

mullefi huquqlari layihenini butun nuscelerinde gosterilmelidir

# layihe ucun telebler
fayl islemeyi ucun sadece random kitabxanasi yuklemek yeter

## xususiyetler
- * her sual random olaraq secilir
- * her suala aid bir nece cavab var
- * her cavab yoxlanilir ve ona aid xal verilir
- * testin sonda neticesi gosterilir

### Qurasdirma ve ise salma haqqinda

- * python 3.12 versiya istifade olunub
- * istifade ucun class_quiz.py faylini ise salin
- * ``` bash
python class_quiz.py

### kod sturkturu
# <!--   SUALLAR,CAVAB VARIANTLARTI LSIT DAXILINDE,VE DOGRU OLAN CAVAB
<!-- class Question:
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

result_list = [q1, q2, q3, q4, q5] -->

## elaqe
- * Repository URL: https://github.com/MusfiqEmirov/Quiz








