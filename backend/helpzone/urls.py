from django.urls import path, include
from . import views


urlpatterns = [
    path("helpzone/create_question", views.create_question),
    path("helpzone/create_answer", views.create_answer),
    path("helpzone/math", views.math_list),
    path("helpzone/art", views.art_list),
    path("helpzone/history", views.history_list),
    path("helpzone/ethics", views.ethics_list),
    path("helpzone/science", views.science_list),
    path("helpzone/geography", views.geography_list),
    path("helpzone/languages", views.languages_list),
    path("helpzone/communication", views.communication_list),
    path("helpzone/<str:question_id>/update", views.update_questions),
    path("helpzone/<str:question_id>/delete", views.delete_questions),
    path("helpzone/<str:question_id>", views.detail_question),
    path("helpzone/answers/all_answers/<str:answer_id>", views.detail_answer),
    path("helpzone/answers/all_answers/<str:answer_id>/update", views.update_answer),
    path("helpzone/answers/all_answers", views.all_answer)
]
