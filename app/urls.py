from django.urls import path
from .views import(
    SignUpView,
    LoginView,
    PeopleView,
    SettingsView,
    DetailsView,
    TaskDetailView,
    TaskView
)

app_name = 'app'

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup-view'),
    path('login/',LoginView.as_view(),name='login-view'),
    path('detail/',DetailsView.as_view(),name='detail-view'),
    path('people/',PeopleView.as_view(),name='people-view'),
    path('settings/',SettingsView.as_view(),name='settings-view'),
    path('task/',TaskView.as_view(),name='task-view'),
    path('taskdetail/',TaskDetailView.as_view(),name='task-detail-view'),

]
