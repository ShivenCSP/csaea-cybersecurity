import hashlib
import os

plaintext_pass = "monkey101?"
password = plaintext_pass.encode("utf-8")

hash_a = hashlib.sha256(password).hexdigest()
hash_b = hashlib.sha256(password).hexdigest()

print("\n No salt:")
print(f"User A: {hash_a}")
print(f"User B: {hash_b}")

# add salt

salt_a = os.urandom(16)
salt_b = os.urandom(16)

print("\n Just salt:")
print(f"User A salt: {salt_a}")
print(f"User B salt: {salt_b}")

salthash_a = hashlib.sha256(salt_a + password).hexdigest()
salthash_b = hashlib.sha256(salt_b + password).hexdigest()

print("\n With salt:")
print(f"User A hash + salt: {salthash_a}")
print(f"User B hash + salt: {salthash_b}")

