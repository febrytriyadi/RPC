# import SimpleXMLRPCServer bagian server
from xmlrpc.server import SimpleXMLRPCServer


# buat fungsi bernama file_upload()
def file_upload(filedata):
    # buka file
    with open("hasil_upload.txt", 'wb') as handle:
        # convert from byte to binary IMPORTANT!
        data = filedata.data

        # tulis file tersebut
        handle.write(data)

        return True  # IMPORTANT


# must have return value
# else error messsage: "cannot marshal None unless allow_none is enabled"

# buat server
with SimpleXMLRPCServer(("192.168.43.122", 45678)) as a:
    a.register_introspection_functions()

    # tulis pesan server telah berjalan
    print("Listening on port 45678")

    # register fungsi
    a.register_function(file_upload)

    # jalankan server
    a.serve_forever()
