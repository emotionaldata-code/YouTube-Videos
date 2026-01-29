import math

# COINSGAME mult function
def computeCrashPoint_CoinsGame(randomInteger):

    X = randomInteger / (2**52)
    X = 95 / (1 - X)
    result = math.floor(X) 
    crash_point = min(1000, max(1, result / 100))
    return crash_point

# BITSLER mult function
def computeCrashPoint_Bitsler(randomInteger):

    multiplier = 98 / (1 - (randomInteger / (2**52)))
    final_multiplier = max(100, int(multiplier)) / 100
    
    return final_multiplier

# ROOBET mult function
def computeCrashPoint_Roobet(randomInteger):
    if (randomInteger % 33 == 0):
        return 1
    e = 2**52
    return (((100 * e - randomInteger) / (e-randomInteger)) // 1) / 100.0

