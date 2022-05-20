from django.urls import path

from Board.views import CreateBoardView, ListBoardsView, CreateTaskView, ListTaskView

urlpatterns=[
    path('create-board/',CreateBoardView.as_view(),name='createboard'),
    path('list-boards/', ListBoardsView.as_view(),name='listboard'),
    path('create-tasks/', CreateTaskView.as_view(),name='createtask'),
    path('list-tasks/<int:id>/', ListTaskView.as_view(),name='listtask'),
]