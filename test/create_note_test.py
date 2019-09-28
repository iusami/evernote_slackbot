# coding:utf-8
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types

# ノートブック一覧の取得（1）
client = EvernoteClient(token='S=s1:U=955e9:E=17341675250:C=16be9b625c8:P=1cd:A=en-devtoken:V=2:H=e37cfedf34e6261a3d472c318c70fad4')
note_store = client.get_note_store()
notebooks = note_store.listNotebooks()
print('Number of notebooks: %d' % len(notebooks))

for notebook in notebooks:
    print('Notebook name: ' + notebook.name)
    if notebook.name == 'My First Notebook':

        # ノートインスタンスを生成する（4）
        note = Types.Note()
        note.title = 'Hello, Evernote'
        note.content = '<?xml version="1.0" encoding="UTF-8"?>'
        note.content += '<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
        note.content += '<en-note>New note!!!</en-note>'
        note.tagNames = ['test']
        # ノート作成先のノートブックのGUIDを指定する（5）
        note.notebookGuid = notebook.guid
        # ノートを作成する（6）
        note_store.createNote(note)

        print('A note was created!')