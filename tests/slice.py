from queryset_client import Client

client = Client("http://192.168.57.132:8888/message/v1/")

al = client.inbox.objects.all()
for i in al[0:8]:
    assert i

al = client.inbox_message_many.objects.all()
for i in al[0:10]:
    assert i