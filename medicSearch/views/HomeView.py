# aqui estamos importando a classe HttpResponse para dentro do nosso arquivo HomeView.py
# desse modo poderemos usá-lo para retornar uma resposta para nosso client
from django.http import HttpResponse

# método que vamos disparar através da url / ou /home
# request é o parametro padraoa da view
def home_view(request):
    return HttpResponse('<h1>Olá Mundo</h1>', status=200)