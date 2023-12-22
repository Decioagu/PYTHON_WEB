# Enviando E-mails SMTP com Python (aula 302 e 303)
import os
import pathlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

# pip install python-dotenv
from dotenv import load_dotenv  # type: ignore

'''
    A função load_dotenv() é uma parte da biblioteca Python python-dotenv, 
    que é usada para carregar variáveis de ambiente de um arquivo externo .env
'''
load_dotenv()

# Caminho arquivo HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula.html'

# Dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', 'FALHA DE CONEXÃO') # arquivo .env (1º argumento, falha)
destinatario = remetente

# Configurações SMTP
smtp_server = os.getenv('EMAIL_SERVER', '')
smtp_port = os.getenv('EMAIL_PORT', '')
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto (aula.html)
with open(CAMINHO_HTML, 'r') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Helena') # substituir palavras em um texto padrão

# Transformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente # 'decioagu@gmail.com'
mime_multipart['to'] = destinatario # 'mara.sueli.santana@gmail.com'
mime_multipart['subject'] = 'Este é o assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com  sucesso!')