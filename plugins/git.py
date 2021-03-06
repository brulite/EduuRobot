import requests
from config import bot

def git(msg):
    if msg.get('text'):
        if msg['text'].startswith('/git ') or msg['text'].startswith('!git '):
            text = msg['text'][5:]
            res = requests.get('https://api.github.com/users/' + text).json()
            if not res.get('login'):
                return bot.sendMessage(msg['chat']['id'], 'Usuário "{}" não encontrado.'.format(text),
                                       reply_to_message_id=msg['message_id'])
            else:
                bot.sendMessage(msg['chat']['id'], '''*Nome:* `{}`
*Login:* `{}`
*Localização:* `{}`
*Tipo:* `{}`
*Bio:* `{}`'''.format(res['name'], res['login'],
                       res['location'], res['type'],
                       res['bio']), 'Markdown',
                                reply_to_message_id=msg['message_id'])
            return True
