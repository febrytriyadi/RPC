# import xmlrpc bagian client
import xmlrpc.client
# buat stub proxy client
s = xmlrpc.client.ServerProxy('http://192.168.43.122:45678')

# buka file yang akan diupload
with open("file_diupload.txt",'rb') as handle:
    # baca file dan ubah menjadi biner dengan xmlrpc.client.Binary
    binarydata = xmlrpc.client.Binary(handle.read())
    s.file_upload(binarydata)
