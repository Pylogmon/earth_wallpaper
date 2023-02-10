from matrix_client.client import MatrixClient
import os

server = os.getenv('SERVER')
username = os.getenv('USERNAME')
passwd = os.getenv('PASSWD')
roomid = os.getenv('ROOMID')
message = os.getenv('MESSAGE')

client = MatrixClient(server)

# Existing user
token = client.login(username=username, password=passwd)
room = client.join_room(roomid)
room.send_text(message)