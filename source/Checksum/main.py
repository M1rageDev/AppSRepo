import hashlib

original = input("Enter original SHA256 hash: ")
filename = input("Enter file name: ")

if hashlib.sha256(open(f'{filename}.exe','rb').read()).hexdigest() == original:
    print("Checksum integrity: True")
else:
    print("Checksum integrity: False")
