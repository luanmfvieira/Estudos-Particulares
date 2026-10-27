## ls no terminal somente powershell ele é sempre melhor que o cmd porque aceita mais atalhos e comandos.

criando um ambiente virtual    ou seja, tudo o que você baixar instalar e criar ficará isolado nesse ambiente

python -m venv ll_env    ((ll é learning_log))

para mudar a pasta é o comando cd e o caminho


No PowerShell, o . é chamado de “dot sourcing”.
Ele serve pra executar um script no contexto atual
. ll_env/Scripts/activate


se o power shell bloquear, abra como adm e execute

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

toda vez que entrar em um projeto precisa lembrar de ativar o projeto virtual

cd C:\Users\Luan\Documents\GitHub\estudos_particulares\main\django\learning_log

para ficar no caminho certo

pip install Django

django-admin --version   (para ver a versão atual do seu django instalado)


para criar um projeto é 

django-admin startproject learning_log .     (o . é para organizar as pastas de uma forma boa)  (learning_log é o nome do projeto)


python manage.py startapp

em settings.py em apps instalados adicionei learning_logs para ele fazer parte do servidor


no campo models, consultar tudo o que esta abaixo do import 


class Topic(models.Model):   (criou um modelo de tabela)
    """Um assunto sobre o qual o usuário está aprendendo."""
    text = models.CharField(max_length=200)    (aqui para dentro dela colocar um texto ate 200 char)
    date_added = models.DateTimeField(auto_now_add=True)    (para ver a hora que a pessoa logou)

    def __str__(self):  (parar criar uma função)
        """Retorna uma representação em string do modelo."""
        return self.text  (self daqui e text la de cima)


digite no terminal 

python manage.py makemigrations learning_logs

para criar o model 0001_initial.py


python manage.py migrate










