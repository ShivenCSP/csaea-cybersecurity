# Hashing: one way function. Same input --> same output. 

import hashlib

password = "Kilyan.Dictator@2345?"

data = password.encode("utf-8")
digest = hashlib.md5(data).hexdigest()

print(f"Pasword: {password}")
print(f"Hash: {digest}", "\n")

#compareing hashed passwords

diff_pass = ["Crevical.Buck@576?", "PessiBoi_21", "Ronaldih978!", "NewJugular(234)", "PikeStick987%"]

for p in diff_pass:
    data = p.encode("utf-8")
    digest = hashlib.md5(data).hexdigest()

    print(f"Pasword: {p}")
    print(f"Hash: {digest}", "\n")

