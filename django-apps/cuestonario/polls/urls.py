from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='details'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('mapa/<int:total_score>', views.MapaView.as_view(), name='mapa'),
    path('mapa/add_location/', views.add_location, name='addlocation'),
    path('mapa/resultados', views.listaResultados , name="resultados"),
   
]
