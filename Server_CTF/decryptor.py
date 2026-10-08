def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Large primes p and q
p = 100000000000031
q = 100000000000061

# Calculate n and phi(n)
n = p * q
phi = (p - 1) * (q - 1)

# Public exponent
e = 65537  # Common choice for e

# Check if e and phi are coprime
if gcd(e, phi) != 1:
    print(f"e = {e} is not coprime with phi(n) = {phi}.")
    # Choose a new value for e if necessary (not done in this example)
    e = 65537

# Calculate private exponent d (modular inverse of e modulo phi)
d = pow(e, -1, phi)

print("Public Key (n, e):", (n, e))
print("Private Key (n, d):", (n, d))

# Message to encrypt (must be < n)
mesaj = 154

# Encrypt the message
ct = pow(mesaj, e, n)
print("Encrypted Message:", ct)

# Decrypt the message
mesdec = pow(ct, d, n)

# Since the message is an integer, we print it directly
print("Decrypted Message:", mesdec)

# Check if the decrypted message matches the original message
if mesdec == mesaj:
    print("Decryption successful! The decrypted message matches the original.")
else:
    print("Decryption failed! The decrypted message does not match the original.")
