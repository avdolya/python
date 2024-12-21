def secret_replace(test, **replaces):
    n = ''
    indexes = {key: 0 for key in replaces.keys()} 
    for i in test:
        if i in replaces:
            n += replaces[i][indexes[i]] 
            indexes[i] += 1 
            if indexes[i] >= len(replaces[i]):  
                indexes[i] = 0
        else:
            n += i  
    return n
result = secret_replace("ABRA-KADABRA", A=("Z", "1", "!"), B=("3",), R=("X", "7"), K=("G", "H"), D=("0", "2"))
print(result)
