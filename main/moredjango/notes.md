Tudo o que precisa saber é apenas manage, settings e urls

settings 

aonde vai configurar todo o seu projeto, banco de dados, apps, templates

urls

colocar as rotas e pontos de acessos



comandos ----


python magane.py runserver      #para dar run no server


em url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/')
]

(adicionado a variavel path('teste/') para quando inserida na ulr fazer algo)



agora

em url foi colocado

from django.http import HttpResponse

def teste_view(request):
    return HttpResponse("Essa é a rota de teste!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', teste_view)
]

importado o httpresponse, adicionado uma def chama teste_view con a função para dar return no site dizendo ("Essa é a rota de teste!")

apenas adicionado a variavel patch o teste_view

assim que der run e entrar em

http://127.0.0.1:8000/teste/

aparece na tela Essa é a rota de teste!

como não tem nenhuma rota configurada para a page inicial ela aparecer o error 404

so aparecia o normal do django antes pq ainda n tinha configurado nenhuma rota antes

criei o arquivo views.py para deixar configurado nele as defs e o que quero no site


quando utiliza from . import talcoisa ele importa tudo o que esta dentro da pasta do seu projeto em questão, assim você não precisa dar varios imports, apenas puxar a função dela


usar square cloud para serviço de hospedagem online

pesquisar flexbox

essa pasta projeto é um app, e é um app principal do projeto

executou python manage.py startapp tarefas
criou a pasta tarefas

adicionado 'tarefas' em installed apps em settings, como um novo app para usar precisa deixar registrado no framework.





