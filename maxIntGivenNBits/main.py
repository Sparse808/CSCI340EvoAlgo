from random import choices

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

def main():
    print("starting")

    popSize = 10
    tournSize = 5
    n = 10

    population = createPop(popSize, n)
    printChomo(population)

    fitnessLookup = findFitness(population)
    printChomo(fitnessLookup)


    matingPool = createPool(population, fitnessLookup, tournSize, popSize)
    printChomo(matingPool)

if __name__ == "__main__":
    main()


