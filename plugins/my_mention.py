# coding: utf-8

from datetime import datetime
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

# coding:utf-8
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types

create_flag = 0
client = EvernoteClient(token='S=s1:U=955e9:E=17341675250:C=16be9b625c8:P=1cd:A=en-devtoken:V=2:H=e37cfedf34e6261a3d472c318c70fad4')
note_store = client.get_note_store()
notebooks = note_store.listNotebooks()


@respond_to(r'.+')
def post_to_evernote(message):
    text = message.body['text']
    #print(type(message.body['text']))
    #print(text.splitlines())
    text_splitted = text.splitlines()
    message.send('It is your post {}'.format("```" + message.body['text'] + "```"))
    for notebook in notebooks:
        if notebook.name == 'My First Notebook':
            # ノートインスタンスを生成する（4）
            note = Types.Note()
            note.title = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            note.content = '<?xml version="1.0" encoding="UTF-8"?>'
            note.content += '<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
            note.content += '<en-note>'
            note.content += '<p>'
            for i in text_splitted:
                note.content += '<br>'
                body = i
                if 'http' in i:
                    link = i.replace('<','').replace('>','')
                    body = '<a href="%s">%s</a>' % (link,link)
                if 'tel' in i:
                    tel = i.replace('<','').replace('>','').split('|')[0]
                    body = '<a href="%s">%s</a>' % (tel, tel.replace('tel:','TEL:'))
                note.content += body
                note.content += '</br>'
            note.content += '</p>'
            note.content += '</en-note>'
            #note.content += '<en-note>New note!!!</en-note>'
            note.tagNames = ['test']
            print(note)
            # ノート作成先のノートブックのGUIDを指定する（5）
            note.notebookGuid = notebook.guid
            # ノートを作成する（6）
            note_store.createNote(note)
            create_flag = 1
    if create_flag == 1:
        message.send('Note created succesfully!')
    else:
        message.send('I failed to post...')