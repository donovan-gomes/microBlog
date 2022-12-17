# Projeto microblog (arquivo de execução principal)
from app import app # Import da variavel de instancia do Flask
import os           # Import das variaveis de acesso do Sistema Operacional

# O método main faz com que o python identifique o arquivo de execução principal.

if __name__== 'main':
  port = int(os.getenv('PORT'), '5000') # Nesse momento, o método os.getenv resgata a váriavel de ambiente "PORT" e seta porta = 5000
  app.run(host='0.0.0.0', port = port)