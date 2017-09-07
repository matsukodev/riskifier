# riskifier/urls.py
from django.conf.urls import url
from django.conf.urls.static import static
from riskifier import views

urlpatterns = [
    url(r'^home/$', views.ViewPageHome.as_view()),
    url(r'^start/$', views.ViewPageStart.as_view()),
    url(r'^questionnaire/$', views.ViewPageQuestionnaire.as_view()),
    url(r'^result/$', views.ViewPageResult.as_view()),
    url(r'^formular/$', views.ViewPageFormular.as_view()),
    url(r'^emo/$', views.ViewPageEmo.as_view()),

    # default
    url(r'^$', views.ViewPageHome.as_view()),
]
