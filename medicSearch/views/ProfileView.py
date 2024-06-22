# retornará como resultado nossos dados 
# de perfil em uma tela html
from django.http import HttpResponse

# por enquanto exibe o id do usuário
def list_profile_view(request, id=None):
    if id is None and request.user.is_authenticated:
        id = request.user.id
        
    elif not request.user.is_authenticated:
        id = 0
    
    return HttpResponse('<h1>Usuário de id %s!</h1>' % id)
    
    