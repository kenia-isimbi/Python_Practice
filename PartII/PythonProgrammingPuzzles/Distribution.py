def generate_stone_piles(n):
    if n <= 0:
        return []
    
    return [n + 2 * i for i in range(n)]

n = 4
print(f"Stones in each pile for n = {n}: {generate_stone_piles(n)}")

n = 7
print(f"Stones in each pile for n = {n}: {generate_stone_piles(n)}")
