# popNode file
# This file contains the node that holds an array of
# boardNodes, or more accurately a population of boardNodes
# CS 441 assignment 2
# Instructor: Rhoades
# Author: Dominique D. Moore

import boardNode

# population = # of board states
# boards = array of board states (or boardNodes)
# fitnessSum = Sum of all fitnesses
class PopNode:
    def __init__(self,pop,size):
        self.population = pop
        self.boards = [boardNode.boardNode(size) for i in range(pop)]
        self.fitnessSum = 0
        #self.fitnessSum = self.calcFitnessSum()

    # Calculates the total fitness sum of the boards
    def calcFitnessSum(self):
        i = 0
        val = 0
        while i < self.population:
            val = val + self.boards[i].calcFitness()
            i = i + 1
        return val

    def updateFitnessSum(self):
        self.fitnessSum = self.calcFitnessSum()

    # Initializes the boardNode arrays
    # Updates the fitness sum
    def initializeBoards(self):
        for i in range(self.population):
            self.boards[i].initializeBoardNode()
            self.fitnessSum = self.fitnessSum + self.boards[i].fitness

    # Finds a partner for performing crossover
    # This function either finds the most suitable partner or
    # determines the potential matches aren't suitable
    def findParent(self,fitVal,partner):
        parent = -1
        if self.fitnessSum == 0:
            parent = boardNode.random.randrange(self.population)
            return parent

        for i in range(self.population):
            fitInt = round((self.boards[i].fitness / self.fitnessSum) * 100)
            if fitVal in range(fitInt) and partner != i:
                parent = i
                break
        return parent        

    # Finds the board with the highest possible fitness
    # This function runs if there was no suitable partner found
    # by the findParent() function, to ensure that a crossover
    # occurs if initiated
    def findMaxFiteness(self,skip):
        max = -1
        for i in range(self.population):
            if self.boards[i].fitness > self.boards[max].fitness and i != skip:
                max = i
        return max
        
    def findParent1(self,pos):
        if self.fitnessSum == 0:                    
            return self.findParent(0,-1)
        found = -1
        #cross = boardNode.random.randrange(101)
        p1 = pos
        while found == -1:
            if p1 == self.population:
                p1 = 0
            cross = boardNode.random.randrange(101)
            while p1 < self.population:
                val = round((self.boards[p1].fitness / self.fitnessSum) * 100)
                if cross in range(val):
                    #parent1 = p1
                    found = p1
                    break
                p1 = p1 + 1
            cross = boardNode.random.randrange(101)
        return found

    # create a new generation of boardNodes
    # create an empty array of boardNodes
    # loop until # of boardNodes in the empty array == self.population
    # For crossover:
    #   start at beginning of self.boards array (current generation)
    #   determine whether to initiate crossover
    #   if yes:
    #       find second parent by looping through the current generation
    #       start at the beginning of the array
    #       determine whether to do crossover
    #       if yes:
    #           set second parent to current node index
    #       perform crossover function
    #   increase iterator if crossover occured
    #   keep going until # of nodes in next gen array == self.population
    # set self.boards = to next generation
    def doCrossover(self):
        size = self.boards[0].size
        nextGen = [boardNode.boardNode(size) for i in range(self.population)]
        added = 0
        p1 = 0
        parent1 = -1
        parent2 = -1
        while added < self.population:
            parent1 = self.findParent1(p1)                  # Always returns a value > -1
            p1 = parent1 + 1
            #cross = boardNode.random.randrange(101)
            
            while parent2 == -1:
                cross = boardNode.random.randrange(101)
                parent2 = self.findParent(cross,parent1)    # Finds a partner for parent1 that's not parent1
                #cross = boardNode.random.randrange(101)
            # find a number between the boardNode array bounds
            cross = boardNode.random.randrange(size)
            nextGen[added].crossover(self.boards[parent1],self.boards[parent2],cross)
            added = added + 1
            if added == self.population:
                break
            nextGen[added].crossover(self.boards[parent2],self.boards[parent1],cross)
            added = added + 1
            parent1 = -1
        self.boards = nextGen
        #self.updateFitnessSum()
    
    def mutateBoards(self):
        for i in range(self.population):
            self.boards[i].mutate()
        #self.updateFitnessSum()
        
    
    def printPopNode(self):
        print(f"Population size: {self.population}")
        print(f"Fitness Sum: {self.fitnessSum}")
        for i in range(self.population):
            print(self.boards[i].board)
            print(f"Fitness: {self.boards[i].fitness}")

    def printBoardNode(self,index):
        self.boards[index].printBoardNode()
    
    def foundSolution(self,goal):
        for i in range(self.population):
            if self.boards[i].fitness == goal:
                print("SOLUTION!!:")
                print(self.boards[i].board)
                return 1
        return 0

if __name__ == "__main__":
    pop = 10
    sz = 8
    a = PopNode(pop,sz)
    a.initializeBoards()
    a.printPopNode()
    a.doCrossover()
    a.mutateBoards()
    a.updateFitnessSum()
    a.printPopNode()
    m = a.findMaxFiteness(-1)
    print(a.boards[m].board)
    print(a.boards[m].fitness)
    a.printBoardNode(0)
    