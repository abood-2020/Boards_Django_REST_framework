from django.urls import path
from . import views 
urlpatterns = [
    path('',views.BoardList.as_view() , name='home'),
    path('boards/<int:board_id>/',views.BoardTopics.as_view() , name='board_topics'),
    path('board_detail/<int:board_id>/',views.BoardDetails.as_view() , name='board_detail')
]