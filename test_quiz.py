import pytest
import random
from class_quiz import Question, Quiz

def test_check_answer_correct():
     q1 = Question("en yaxwi proqramlawdirma dili hansidir?", ["python", "java", "c#", "c++","php"], "python") 
     result = q1.check_answer("python")
     assert result == True  # eger cavab dogrudursa,yeni "pythondursa"  cavab true olsun bu test edildi!!!!


def test_check_answer_incorrect():
    q2 = Question("en yaxwi proqramlawdirma dili hansidir?", ["python", "java", "c#", "c++","php"], "python")
    result = q2.check_answer("java")
    assert result == False # eger cavab yalnisdirsa,yeni "yeni python deyilse bize false deyerini qaytarmalidir.bu test isledi!!!!"


def test_check_answer_not_result():
    q1 = Question("en yaxwi proqramlawdirma dili hansidir?", ["python", "java", "c#", "c++","php"], "python")
    
    with pytest.raises(ValueError):
        q1.check_answer("PHP") # eger cavab siyahida yoxdursa valueError qaytarmalidir

def test_get_question():
    q1 = Question("en yaxwi proqramlawdirma dili hansidir?", ["python", "java", "c#", "c++","php"], "python")
    q2 = Question("en mehsur proqramlawdirma dili hansidir?", ["c++", "c#", "php", "python", "java"], "python")
    quiz = Quiz([q1, q2])

    first_question = quiz.get_question() # get_question methodunun duzgun islemesini test elemek
    assert first_question.text == "en yaxwi proqramlawdirma dili hansidir?" or first_question.text == "en mehsur proqramlawdirma dili hansidir?"

def test_quiz_index():
    q1 = Question("en yaxwi proqramlawdirma dili hansidir?", ["python", "java", "c#", "c++","php"], "python")
    q2 = Question("en mehsur proqramlawdirma dili hansidir?", ["c++", "c#", "php", "python", "java"], "python")
    quiz = Quiz([q1, q2]) 

    first_question = quiz.get_question()
    assert quiz.quiz_index == 0 # ilk sualdan sonra index yeniden 0 olmalidir

    quiz.quiz_index += 1
    second_question = quiz.get_question()
    assert quiz.quiz_index == 1 # ikinci sualdan sonra index 1 olmaldir




