from django.urls import path

from calls import views

app_name = 'calls'
urlpatterns = [

    path('new_call/', views.new_call, name="new_call"),
    path('list_calls/', views.list_calls, name="list_calls"),
    path('update_call/<int:call_id>/', views.update_call, name="update_call"),
    path('delete_call/<int:call_id>/', views.delete_call, name="delete_call"),

] 