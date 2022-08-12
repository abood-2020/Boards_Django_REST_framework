from django.urls import path
from . import views 
urlpatterns = [
    path('',views.BoardList.as_view() , name='boards_list'),
    path('boards/<int:board_id>/',views.BoardTopics.as_view() , name='board_topics')
]