# estamos importando o método path, que é o responsável 
# por criar a url que acionará a view HomeView
from django.urls import path
from medicSearch.views.HomeView import home_view


# O primeiro parâmetro é a string que corresponde ao caminho 
# da url. O segundo corresponde ao método view que estamos 
# chamando, em nosso caso, o home_view , que está dentro da 
# view HomeView.py
urlpatterns = [
    path("", home_view),
]