from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()), #클래스를 기반으로한 view의 경우에는 클래스명.as_view() 로 표현한다
    path('<int:pk>/', views.PostDetail.as_view()),
  #  path('', views.Index.as_view()),
    path('search/<str:q>/', views.PostSearch.as_view()),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('delete_comment/<int:pk>/', views.delete_comment ),
    path('category/<str:slug>/', views.category_page), 
    path('<int:pk>/new_comment/', views.new_comment),
    path('tag/<str:slug>/', views.tag_page), 
    path('create_post/', views.PostCreate.as_view()), 
    path('update_post/<int:pk>/', views.PostUpdate.as_view()), 
    ]
