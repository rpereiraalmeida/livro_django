from django.urls import path
from medicSearch.views.ProfileView import list_profile_view

"""
Como podemos perceber, existem duas linhas de url chamando a
mesma view list_profile_view . Mas isso é possível? Sem dúvidas, é
possível e muito recomendável. O primeiro path chamará o método
list_profile_view e não passará um id . Isso não é um problema,
pois quando criamos esse método na view ProfileView.py nós
falamos para o Python que id poderia ser None . Veja como
escrevemos: def list_profile_view(request, id=None): , então caso
chamemos a url sem o parâmetro id , ele será None , mas não se
esqueça de que foi preciso colocar id como None . 
"""

urlpatterns = [
    path("", list_profile_view),
    path("<int:id>", list_profile_view, name='profile'),
]