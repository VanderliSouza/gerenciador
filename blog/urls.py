from django.urls import path

from blog import views
#from adiciona import views

urlpatterns = [
	#path(r'^$', 'agenda.views.lista', name='lista.html'),
    #path('', views.index, name='index'),
	path('lista.html', views.lista, name='lista.html'),
	#path('<int:ItemAgenda_id>/', views.adiciona, name='adiciona'),
	#path('adiciona.html', views.adiciona, name='adiciona.html'),
	
]