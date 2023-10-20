# Importar biblioteca telebot
import telebot


# Registrar em variavel Chave de acesso ao Servidor bot 
key_api='5931977784:AAFntidN9TbsbbIyqfc_0QcQw1enNP_4hp4'


# Acessar Servidor Bot
bot = telebot.TeleBot(key_api)


# Escolha opção 1
@bot.message_handler(commands=['op1'])
# Exibir Cardápio
def op1(mensagem):
    cardapio = """
/xs Xis - Salada - é 15 conto
/xb Xis - Hamburgi - mais caro por conta do nome 20 conto
/xt Xis - Tudo - Ta passando fome ? 25 conto"""
    bot.send_message(mensagem.chat.id, cardapio)


# Escolha X - Salada
@bot.message_handler(['xs'])
# Confirmar recebimento do pedido
def xs(mensagem):
    bot.send_message(mensagem.chat.id, 'Seu X - Salada será enviado em ate 20 minutos')


# Escolha X - Hamburgi
@bot.message_handler(['xb'])
# Confirmar recebimento do pedido
def xb(mensagem):
    bot.send_message(mensagem.chat.id, 'Seu X - Hamburgi será enviado em ate 20 minutos')


# Escolha X - Tudo
@bot.message_handler(['xt'])
# Confirmar recebimento do pedido
def xt(mensagem):
    bot.send_message(mensagem.chat.id, 'Seu X - Tudo será enviado em ate 20 minutos')


# Escolha opção 2
@bot.message_handler(commands=['op2'])
# Enviar mensagem de resposta respectiva
def op2(mensagem):
    bot.send_message(mensagem.chat.id, 'Enviar reclamação para reclamanapqp@gmail.com ou ligue no numero (35) 9950-2888')


# Escolha opção 3
@bot.message_handler(commands=['op3'])
# Enviar Mensagem de cancelamento do pedido
def op3(mensagem):
    bot.send_message(mensagem.chat.id, 'Seu pedido foi cancelado com sucesso!')


# verificar se há alguma mensagem
def verificar(mensagem):
    return True


# Verificação Verdadeira
@bot.message_handler(func=verificar)


# Exibir menu principal
def responder(mensagem):
    texto = """
Escolha uma opção ou clique no item:
/op1 - Fazer um pedido
/op2 - Gerar uma reclamação
/op3 - Cancelar um pedido 
Qualquer resposta diferente das opções acima não irá funcionar"""
    bot.reply_to(mensagem,texto )


# Exibir mensagem de ativação do sistema
print('Rodando')


# Sistema em loop
bot.polling()