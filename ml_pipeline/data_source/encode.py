import base64

f = open("data_reader.py", "rb")
encoded = base64.b64encode(f.read())
open("data_reader.bin", "wb").write(encoded)
