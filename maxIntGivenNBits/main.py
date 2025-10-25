from random import choices, random, randint


def printChomo(chromos: list):
    print("set:")
    for item in chromos:
        print(item)

def createPop(popSize: int, n: int) -> list[list[int]]:
    population = []
    for _ in range(popSize):
        population.append(choices([0,1], k=n))
    return population

def findFitness(population: list[list[int]]) -> list[int]:
    fitness = []
    for item in population:
        fitness.append(int("".join(str(bit) for bit in item),2))
    return fitness

def createPool(population: list[list[int]], fitnessLookup: list[int], tournSize: int, popSize: int) -> list[list[int]]:
    matingPool = []

    for _ in range(popSize):
        indices = choices(range(popSize), k=tournSize)
        maxFitness = fitnessLookup[indices[0]]
        maxIndex = indices[0]
        for index in indices:
            if fitnessLookup[index] >= maxFitness:
                maxFitness = fitnessLookup[index]
                maxIndex = index
        matingPool.append(population[maxIndex])

    return matingPool

def createCrossOver(matingPool: list[list[int]], crossoverRate: float, popSize: int, n: int) -> list[list[int]]:
    for i in range(0, popSize, 2):
        if random() < crossoverRate:
            position = randint(0, n - 1)
            matingPool[i][position], matingPool[i+1][position] = matingPool[i+1][position], matingPool[i][position]

    return matingPool

def createMutate(matingPool: list[list[int]], mutationRate: float, popSize: int, n: int) -> list[list[int]]:
    for i in range(popSize):
        if random() < mutationRate:
            position = randint(0, n-1)
            matingPool[i][position] = (matingPool[i][position] +1) %2
            
    return matingPool
def main():
    print("starting")

    popSize = 10
    tournSize = 5
    n = 20
    crossoverRate = .5
    mutationRate = .1
    generations = 1000

    population = createPop(popSize, n)
    printChomo(population)

    for generations in range(generations):
        fitnessLookup = findFitness(population)
        matingPool = createPool(population, fitnessLookup, tournSize, popSize)
        crossover = createCrossOver(matingPool, crossoverRate,popSize, n)
        mutation = createMutate(crossover, mutationRate, popSize, n)

        maxValue = fitnessLookup[0]
        fitnessLookup = findFitness(population)
        maxValue = max(fitnessLookup)
        bestIndex = fitnessLookup.index(maxValue)
        bestChromosome = population[bestIndex][:]  # copy best

        print(f"Gen {generations:4d} | Max fitness: {maxValue}")

        population = [bestChromosome] + mutation[1:]
        popSize = len(population)

    printChomo(population)

    

if __name__ == "__main__":
    main()


