# coding:utf-8
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types

# Evernoteクライアントを初期化する（1）
client = EvernoteClient(token='S=s1:U=955e9:E=17341675250:C=16be9b625c8:P=1cd:A=en-devtoken:V=2:H=e37cfedf34e6261a3d472c318c70fad4')
note_store = client.get_note_store()
notebooks = note_store.listNotebooks()

# ノートブックインスタンスを生成する（2）
notebook = Types.Notebook()
notebook.name = 'My First Notebook'
# ノートブックを作成する（3）
created_notebook = note_store.createNotebook(notebook)

print('A notebook was created!')
