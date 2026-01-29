import hmac
import hashlib

# Valori di esempio
client_seed = "g62NtsuzGQmQ3e4r"
server_seed = "5fed58b716b988d33b054fb7fecf8783132c33d8ec14d6d19098f5fbf56205b28329a5d14d0429e63fa08ec17c0efe25ef6b71634e241a0483dcc14365130b3e"
nonce = 1

hash_to_expose = hashlib.sha256(server_seed.encode()).hexdigest()

# esposto c6076ecb3452d4012a2ff9d8101a7e35c39d7b0b38e5a6c1597013ad6c2a78c1
            
print(f"""
dato il server seed -> {server_seed}
questo è l'hash che dovevano esporre precedentemente {hash_to_expose}
""")

# 1. Calcolo dell'HMAC SHA-512 come seed, usando la chiave server_seed
# Il messaggio è client_seed + "," + nonce
message = f"{client_seed},{nonce}"
seed = hmac.new(
    server_seed.encode(),           # chiave
    message.encode(),               # messaggio
    hashlib.sha512                  # algoritmo
).hexdigest()                       # risultato in formato esadecimale

# 2. Inizializzazione
offset = 0
numbers = []

# 3. Genera 10 numeri univoci tra 1 e 42
for _ in range(10):
    # Calcola il massimo numero valido: floor(256 / 42) * 42 - 1 = 252 - 1 = 251
    max_number = (256 // 42) * 42 - 1
    print(max_number)
    while True:
        # Prendi due caratteri esadecimali (1 byte = 2 hex char = 8 bit)
        hex_byte = seed[offset:offset+2]
        number = int(hex_byte, 16)  # converte l'esadecimale in decimale
        offset += 2

        # Se il numero è maggiore di 251 o già usato (dopo modulo +1), riprova
        result = number % 42 + 1
        if number <= max_number and result not in numbers:
            break

    numbers.append(result)

# 4. Stampa il risultato
print(sorted(numbers))
