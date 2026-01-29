import hmac
import hashlib

# Valori di esempio
server_seed = "21926bf6a0cdefb74eddfe18477f09125f6b8aa045c9762c3f5ea0167f61a7bbd0560d51ab2f7616090f5649b37bb0c185fc53c7584865a3050a7c3cb89cad9c"
hash_to_expose = hashlib.sha256(server_seed.encode()).hexdigest()

# esposto c6076ecb3452d4012a2ff9d8101a7e35c39d7b0b38e5a6c1597013ad6c2a78c1
            
print(f"""
dato il server seed -> {server_seed}
questo è l'hash che dovevano esporre precedentemente {hash_to_expose}
""")