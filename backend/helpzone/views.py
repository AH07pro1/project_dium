from django.shortcuts import render
from rest_framework import generics
from .models import Question, Answer
from .serializer import QuestionSerializer, AnswerSerializer

# ADD PERMISSIONS TO ALL VIEWS
# (("Mathematics", "M"), ("History", "H"), ("Ethics", "E"), ("Science", "S"), ("Geography", "G"), ("Languages", "L"), ("Art", "A"), ("Communication/personal_help", "C")

# Create your views here.
class CreateQuestion(generics.CreateAPIView):
    """Create questions instances"""
    queryset = Question
    serializer_class = QuestionSerializer

create_question = CreateQuestion.as_view()

class CreateAnswer(generics.CreateAPIView):
    """Create answer instances"""
    queryset = Answer
    serializer_class = AnswerSerializer

create_answer = CreateAnswer.as_view()

class MathList(generics.ListAPIView):
    """All questions instances that have the math category"""
    queryset = Question.objects.filter(subject = "Mathematics")
    serializer_class = QuestionSerializer

math_list = MathList.as_view()

class HistoryList(generics.ListAPIView):
    """All questions instances that have the history category"""
    queryset = Question.objects.filter(subject = "History")
    serializer_class = QuestionSerializer

history_list = HistoryList.as_view()

class EthicsList(generics.ListAPIView):
    """All questions instances that have the ethics category"""
    queryset = Question.objects.filter(subject = "Ethics")
    serializer_class = QuestionSerializer

ethics_list = EthicsList.as_view()


class ScienceList(generics.ListAPIView):
    """All questions instances that have the science category"""
    queryset = Question.objects.filter(subject = "Science")
    serializer_class = QuestionSerializer

science_list = ScienceList.as_view()

class GeographyList(generics.ListAPIView):
    """All questions instances that have the geography category"""
    queryset = Question.objects.filter(subject = "Geography")
    serializer_class = QuestionSerializer

geography_list = GeographyList.as_view()

class LanguagesList(generics.ListAPIView):
    """All questions instances that have the math category"""
    queryset = Question.objects.filter(subject = "Languages")
    serializer_class = QuestionSerializer

languages_list = LanguagesList.as_view()

class ArtList(generics.ListAPIView):
    """All questions instances that have the math category"""
    queryset = Question.objects.filter(subject = "Art")
    serializer_class = QuestionSerializer

art_list = ArtList.as_view()

class CommunicationList(generics.ListAPIView):
    """All questions instances that have the math category"""
    queryset = Question.objects.filter(subject = "Communication/personal_help")
    serializer_class = QuestionSerializer

communication_list = CommunicationList.as_view()


class UpdateQuestions(generics.UpdateAPIView):
    """Update the value of the questions instances"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = "question_id"
    lookup_url_kwarg = "question_id"

update_questions = UpdateQuestions.as_view()

class DeleteQuestions(generics.DestroyAPIView):
    """Update the value of the questions instances"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = "question_id"
    lookup_url_kwarg = "question_id"

delete_questions = DeleteQuestions.as_view()

class DetailQuestion(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = "question_id"
    lookup_url_kwarg = "question_id"

detail_question = DetailQuestion.as_view()

class DetailAnswer(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    lookup_field = "answer_id"
    lookup_url_kwarg = "answer_id"

detail_answer = DetailAnswer.as_view()


class AllAnswer(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

all_answer = AllAnswer.as_view()


