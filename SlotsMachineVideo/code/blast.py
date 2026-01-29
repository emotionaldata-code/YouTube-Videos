import hmac
import hashlib

# These are the variables from the previous problem
gameHash = "0c966bf667629ae816ae8f4d6e151e2a3e1f51855c5f430a091894054c11fcda4fe811ef39a3fc35a5f13fa6199f900d3181f85bc58c70089e57f2023f15ed57"
clientSeed = "00000000000000000008603e0639eefe0d4d9fb571768754786f127b4bf38998"

# Generate the seed using HMAC-SHA512
seed = hmac.new(
    clientSeed.encode(), gameHash.encode(), hashlib.sha512
).hexdigest()

# Extract the first 13 characters and convert to a number
number_hex = seed[:13]
number = int(number_hex, 16)

# Calculate the multiplier
multiplier = 98 / (1 - (number / (2**52)))

# Get the final result, ensuring it's at least 1.00
print(multiplier)
result = max(100, int(multiplier)) / 100

print(f"The multiplier is: {result}")