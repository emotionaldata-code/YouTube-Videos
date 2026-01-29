import numpy as np
import hashlib
import hmac

e = 2**52
clientSeed = "0xbb6bbbec33700761b7816330b017d8291ec6a775c2b582aefc8bc75103f8f3ef"
game_hash = '1c1797292d6a5ac35f3fa97f4436a5418930441826c68fa045cec2beff6a21f0' 
serverSeed = "84351c2efd08c69ae4ae7b462207b813da40bdeaccb1350370338a0bd119710e"

def get_multiplayer(game_hash):

    h = hmac.new(str.encode(game_hash), clientSeed.encode(), hashlib.sha256).hexdigest()

    if (int(h, 16) % 33 == 0):
        return 1
    
    h = int(h[:13], 16)
    e = 2**52

    return (((100 * e - h) / (e-h)) // 1) / 100.0

def get_previous_game(hash_code):

    m = hashlib.sha256()
    m.update(hash_code.encode("utf-8"))

    return m.hexdigest()

results = []
count = 0

while game_hash != serverSeed:
    count += 1
    results.append(get_multiplayer(game_hash))
    game_hash = get_previous_game(game_hash)
    
results = np.array(results)
print(results)
multiplier = 1.99
(results <= multiplier).mean(), 1/33 + (32/33)*(.01 + .99*(1 - 1/multiplier))

multiplier = 1.05
((1/33) + (32/33)*(.01 + .99*(1 - 1/(multiplier-.01))))*-1 + (multiplier-1)*(1 - ((1/33) + (32/33)*(.01 + .99*(1 - 1/(multiplier-.01)))))

C = 2**52
x_values = [0, 10, 1000, 2**52 - 1]

print("Tracing the function for various x values:")
print("Note: The constant 2^52 is a very large number (4503599627370496)")

for x in x_values:
    # Calculate the function value
    numerator = (100 * C) - x
    denominator = C - x
    result = (numerator / denominator) / 100
    
    # Print the result
    print(f"x = {x:,.0f}, f(x) = {result:,.8f}")