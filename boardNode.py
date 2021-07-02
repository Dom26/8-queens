# boardNode file
# This file contains the definition of the board for the 8 queens problem
# CS 441 assignment 2
# Instructor: Rhoades
# Author: Dominique D. Moore

import random

# Initializes the board for the 8 queens problem
def initBoard(arr, size):
    i = 0
    while i < size:        
        arr[i] = random.randrange(size)
        i = i + 1

# Finds if the queen at board[position] is attacking
# For every queen the board[position] queen is not attacking it adds 1 to a sum
# Search through a lower and upper bound:
#   lower bound: [0,position)
#   upper bound: [position+1,size)
# Returns the sum of the queens not attacking
def underAttack(arr,position,size):
    sum = 0
    i = 0
    if i != position:
        while i < position:
            if arr[i] == arr[position]:
                sum = sum
            elif arr[i] == arr[position] - (position - i):
                sum = sum
            elif arr[i] == arr[position] + (position - i):
                sum = sum
            else:
                sum = sum + 1
            i = i + 1
    i = position + 1
    if i < size:
        while i < size:
            if arr[i] == arr[position]:
                sum = sum
            elif arr[i] == arr[position] - (i - position):
                sum = sum
            elif arr[i] == arr[position] + (i - position):
                sum = sum
            else:
                sum = sum + 1           
            i = i + 1
    return sum

# size = size of the board (array)
# board = array of value where each element is in range: [0,7]
# fitness = value that represents how many queens aren't under attack
class boardNode:
    def __init__(self,size):
        self.size = size
        self.board = [0 for i in range(size)]
        self.fitness = 0   

    # Calculates the fitness of the board
    # fitness is determined by number of queens not attacking each other
    # Range of fitness: [0,56]
    # 56 because there are 8 queens, so for every queen it can be
    # attacking at most 7 other queens, and for every queen that it's not
    # attacking it gains one point. In total if no queens are attacking
    # each other then 56 is the maximum.
    # 8 x 7 = 56 (8 queens, 7 max points each)
    def calcFitness(self):
        i = 0
        value = 0
        while i < self.size:
            #if underAttack(self.board,i,self.size) == 0:
                #value = value + 1
            value = value + underAttack(self.board,i,self.size)
            i = i + 1
        return value

    # Initializes the board, called when initial generation is created
    def initializeBoardNode(self):
        initBoard(self.board,self.size)
        self.fitness = self.calcFitness()

    # takes in two boardNodes and performs the crossover
    # calculates the fitness value for boardNode
    def crossover(self,partner1,partner2,crossIndex):
        #target = random.randrange(self.size)
        i = 0
        
        while i <= crossIndex:
            self.board[i] = partner1.board[i]
            i = i + 1
        while i < self.size:
            self.board[i] = partner2.board[i]
            i = i + 1
        self.fitness = self.calcFitness()
    
    # 1/14 or 7.14% chance that a mutation occurs, but I like to round down to believe it's just 7%
    # I choose 7 because if I'm lucky this program will behave
    # as expected.
    def mutate(self):
        #num = random.randrange(15)
        for i in range(self.size):
            num = random.randrange(14)
            if num == 7:
                #target = random.randrange(self.size)
                toChange = random.randrange(self.size)
                self.board[i] = toChange
        self.fitness = self.calcFitness()

    def printBoardNode(self):
        toPrint = ""
        print(f"Printing board state {self.board}")
        print(f"Board State fitness: {self.fitness}")
        for i in range(self.size):
            j = 0
            while j < self.size:
                if j == self.board[i]:
                    toPrint = toPrint + "Q "
                else:
                    toPrint = toPrint + "- "
                j = j + 1
            toPrint = toPrint + "\n"
        print(toPrint)


if __name__ == "__main__":
    sz = 8
    board = boardNode(sz)
    board.initializeBoardNode()
    print("Board 1, pre-crossover:")
    print(board.board)
    print(board.fitness)
    board2 = boardNode(sz)
    board2.initializeBoardNode()
    print("Board 2, pre-crossover:")
    print(board2.board)
    print(board2.fitness)

    print("Performing crossover")
    cross = random.randrange(sz)
    crossBoard = boardNode(sz)
    crossBoard.crossover(board,board2,cross)
    crossBoard2 = boardNode(sz)
    crossBoard2.crossover(board2,board,cross)
    #board.crossover(board2)
    print("Board 1, post-crossover:")
    print(crossBoard.board)
    print(crossBoard.fitness)
    
    print("Board 2, post-crossover:")
    print(crossBoard2.board)
    print(crossBoard2.fitness)

    print("Board 1 calling mutate")
    crossBoard.mutate()
    print(crossBoard.board)
    print(crossBoard.fitness)

    print("Board 2 calling mutate")
    crossBoard2.mutate()
    print(crossBoard2.board)
    print(crossBoard2.fitness)
    crossBoard2.printBoardNode()
    