from django.urls import path
from.import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('list/', views.index, name='index_list'), 
    path('list/new',views.new, name='new'),
]