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


def main():
    print("starting")

    popSize = 10
    tournSize = 5
    n = 10

    population = createPop(popSize, n)
    printChomo(population)


    matingPool = []





if __name__ == "__main__":
    main()


