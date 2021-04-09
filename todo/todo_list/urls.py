from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView\
    , TaskDetail, RegisterView, UserUpdateView, UserDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login", CustomLoginView.as_view(), name='login'),
    path("logout", LogoutView.as_view(next_page="login"), name='logout'),
    path("register", RegisterView.as_view(), name='register'),
    path("update-user", UserUpdateView.as_view(), name='update-user'),
    path("delete-user", UserDelete.as_view(), name='delete-user'),
    path("", TaskList.as_view(), name= "tasks"),
    path("task/<int:pk>", TaskDetail.as_view(), name="task"),
    path("task-create", TaskCreate.as_view(), name= "task-create"),
    path("task-update/<int:pk>", TaskUpdate.as_view(), name= "task-update"),
    path("task-delete/<int:pk>", TaskDelete.as_view(), name= "task-delete"),
]