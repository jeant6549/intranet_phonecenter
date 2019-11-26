from django.urls import path

from calls import views

app_name = 'calls'
urlpatterns = [

    path('new_call/', views.new_call, name="new_call"),
    path('list_calls/', views.list_calls, name="list_calls"),
    path('update_call/<int:call_id>/', views.update_call, name="update_call"),
    path('delete_call/<int:call_id>/', views.delete_call, name="delete_call"),
    path('list_calls_client/<int:user_id>/', views.list_calls_client, name="list_calls_client"),
    path('update_call_client/<int:call_id>/', views.update_call_client, name="update_call_client"),
    path('new_call_client/', views.new_call_client, name="new_call_client"),
    path('list_calls_non_att/', views.list_calls_non_att, name="list_calls_non_att"),
    path('update_teammember/<int:call_id>', views.update_teammember, name="update_teammember"),

] 