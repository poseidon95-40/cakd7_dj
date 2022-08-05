from django.urls import path
from . import views

urlpatterns = [
  #  path('', views.PostList.as_view()), #클래스를 기반으로한 view의 경우에는 클래스명.as_view() 로 표현한다
  #  path('<int:pk>/', views.PostDetail.as_view()),
  #  path('', views.Index.as_view()),

    path('about_me/', views.about_me),
    path('', views.landing),
    path('landing', views.landing, name="landing"),
    ]