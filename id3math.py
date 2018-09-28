import math

def get_entropy(collection):
    frequency = dict()
    count = len(collection)

    for item in collection:
        if item in frequency:
            frequency[item]+=1
        else:
            frequency[item]=1

    entropy = 0

    for item in frequency:
        base = frequency[item]/count
        entropy-= base*math.log2(base)
    
    return entropy