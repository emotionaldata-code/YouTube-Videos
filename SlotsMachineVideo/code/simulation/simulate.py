import random
import string
import hashlib
from multiplayer import computeCrashPoint_Bitsler, computeCrashPoint_CoinsGame, computeCrashPoint_Roobet
import numpy as np

def generate_random_string(length: int) -> str:

    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(characters, k=length))
    
    return random_string

if __name__ == "__main__":

    randomStrings = [generate_random_string(random.randint(16,32)) for t in range(1_000_000)]
    hashedRandomStrings = [hashlib.sha512(randomString.encode()).hexdigest() for randomString in randomStrings]

    bitlserM, roobetM ,cashCoinM = [], [], []
    
    for hashedString in hashedRandomStrings:

        randomNumber = int(hashedString[:13], 16)

        bitlserM.append(computeCrashPoint_Bitsler(randomNumber))
        roobetM.append(computeCrashPoint_Roobet(randomNumber))
        cashCoinM.append(computeCrashPoint_CoinsGame(randomNumber))

    bitlserM, roobetM ,cashCoinM = np.array(bitlserM), np.array(roobetM), np.array(cashCoinM),
    multiplier = 3
    print((cashCoinM <= multiplier).mean())
    print(1-(0.95/multiplier))

    print((1-(0.95/multiplier))*-1 + (multiplier-1)*(1 - (1-(0.95/multiplier))))
    print((cashCoinM < multiplier).mean() * -1 + (multiplier - 1)*(cashCoinM >= multiplier).mean())