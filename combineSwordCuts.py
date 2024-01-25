import random

movements = ["Fd", "Fi", "Md", "Mi", "Sd", "Si", "S"]
non_optimal_combinations = set([
    # same movement
    ("Fd","Fd"),("Fi", "Fi"),("Md","Md"), ("Mi","Mi"), ("Sd","Sd"), ("Si","Si"), ("S","S"),
    #same direction
    ("Fi", "Mi"),("Fi", "Si"),("Fd", "Md"),("Fd", "Sd"),("Fi", "Fd"),("Mi", "Si"),("Md", "Sd"),
    ("Si", "Sd"),("S", "Si"),("S", "Sd"),("Mi", "Fi"),("Si", "Fi"),("Md", "Fd"),("Sd", "Fd"),
    ("Fd", "Fi"),("Si", "Mi"),("Sd", "Md"),("Sd", "Si"),("Si", "S"),("Sd", "S"),
    # vertical and horizontal
    ("S", "Md"),("S", "Mi"),("Md", "S"),("Mi", "S")
])

def getPossibleMoves(chain, optimal):
    moves = []
    if type(chain) == str:
        chain = [chain]
    last_movement = chain[-1]
    for movement in movements:
        pair = (last_movement, movement)
        if optimal:
            if pair not in non_optimal_combinations:
                moves.append(chain+[movement])
        else:
            if pair in non_optimal_combinations:
                moves.append(chain+[movement])
    return moves



def addNextMoves(combinations, optimal):
    next_combinations = []
    for combination in combinations:
        next_combinations += getPossibleMoves(combination, optimal)
    return next_combinations

def calculateCombinations(length_combinations=3, optimal=True, combinations=None):
    if combinations is None:
        combinations = list(movements)
    if length_combinations > 1 and type(combinations[0]) == str:
        combinations = addNextMoves(combinations, optimal)
    while len(combinations[0]) < length_combinations:
        combinations = addNextMoves(combinations, optimal)
    return combinations

def printCombinations(combinations):
    for combination in combinations:
        print(" -> ".join(combination))
    print("\n")


sample_size = 4
combinations = calculateCombinations(length_combinations=2, optimal=True)
min_movements = 3
max_movements = 10

print("Pares óptimos (", len(combinations), "):")
printCombinations(combinations)
for i in range(min_movements, max_movements+1):
    combinations = calculateCombinations(length_combinations=i, optimal=True, combinations=combinations)
    print("Combinaciones para cadena de largo ", i, ": ", len(combinations))
    if i == 6:
        random_elements = random.sample(combinations, sample_size)


print("\nMuestreo de combinaciones de golpes óptimos:")
printCombinations(random_elements)
non_optimal_combinations = calculateCombinations(length_combinations=6, optimal=False)
random_elements = random.sample(non_optimal_combinations, sample_size)
print("Muestreo de combinaciones de golpes NO óptimos:")
printCombinations(random_elements)

