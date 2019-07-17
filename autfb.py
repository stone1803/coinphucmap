from fbchat import Client
from fbchat.models import *

client = Client("ledanghongphuc@gmail.com", "PhucMap")

print("Own id: {}".format(client.uid))

client.send(Message(text="Chao Phuc"), thread_id=100028593181497, thread_type=ThreadType.USER)

client.logout()