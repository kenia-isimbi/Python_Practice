def test(N):
    result = []
    
    for i in range(N):
        result.append([N] * N)
    
    return result

N = int(input("Input an integer: "))

print(test(N))
