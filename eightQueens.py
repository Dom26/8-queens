# eightQueens file
# This file contains the driver for running the 8 eight queens
# problem.
# CS 441 assignment 2
# Instructor: Rhodes
# Author: Dominique D. Moore

import popNode
import random

def printInstructions():
    print("This program will run 6 tests using the Genetic Algorithm. The first three tests run until a solution is")
    print("found, or until 1000 iterations have been ran. These tests will print a random board state every 250th")
    print("iteration. If the solution is found the program will break from the loop and print the solution to the")
    print("8-Queens problem. After every generation is created the sum total of the fitness values are added to the")
    print("overall sum calculated. When the test is finished the average is calculated and displayed along with either")
    print("the solution state, or a state with the highest fitness value.\n")
    print("The second three tests that are ran are similar to the first three tests, but this time an infinite loop is")
    print("ran. So the test will keep running and breaks only when a solution is found. These tests will print a random")
    print("board state every 100th generation. After a solution has been found the program will break from the infinite")
    print("loop and print the generation the solution was found at, the average fitness, the population, and the solution state.")
    print("For both types of tests the population used will in this order: 10, 50, 100")
    print("Before the last test runs the program will ask the user if they want to run the final test with population 100.")
    print("This is because the population of 100 or more causes the program to slow down a lot, so running an infinite loop")
    print("with population 100 may not be worth the hassle.\n")
    userInput = input("Hit any key and/or press enter to continue: ")

def run_GA_test(population):
    numIterations = 1000
    boardSize = 8
    a = popNode.PopNode(population,boardSize)
    a.initializeBoards()
    avgFitness = a.fitnessSum

    printQuarter = round(numIterations/4)
    for i in range(numIterations):
        if a.foundSolution(56):
            print(f"Solution found at generation: {i}")        
            break
        a.doCrossover()
        a.mutateBoards()
        a.updateFitnessSum()
        if i % printQuarter == 0:
            print(f"Population: {population}")
            print(f"Generation: {i}")
            printNode = random.randrange(population)
            a.printBoardNode(printNode)
            
        avgFitness = avgFitness + a.fitnessSum

    avgFitness = avgFitness / (i+1)
    print(f"Average Fitness with {i+1} iterations: {avgFitness}")

    max = a.findMaxFiteness(-1)

    print(f"Printing board with highest fitness at generation: {i+1}")
    a.printBoardNode(max)

def find_GA_solution(population):
    boardSize = 8
    a = popNode.PopNode(population,boardSize)
    a.initializeBoards()
    avgFitness = a.fitnessSum
    iterator = 0
    while 1:
        if a.foundSolution(56):
            print(f"Solution found at generation: {iterator}")        
            break
        a.doCrossover()
        a.mutateBoards()
        a.updateFitnessSum()
        if iterator % 100 == 0:
            print(f"Population: {population}")
            print(f"Generation: {iterator}")
            printNode = random.randrange(population)
            a.printBoardNode(printNode)
            
        avgFitness = avgFitness + a.fitnessSum
        iterator = iterator + 1
    
    avgFitness = avgFitness / (iterator+1)
    print(f"Average Fitness with {iterator+1} iterations: {avgFitness}")

    max = a.findMaxFiteness(-1)
    print(f"Solution found in {iterator+1} iterations with population of {population}")
    print(f"Printing board with solution:")
    a.printBoardNode(max)


userInput = input("Press y if you would like to see an explanation of how the code runs: ")
if userInput.lower() == "y":
    printInstructions()

print(f"<-----------------------Running Genetic Algorithm test with population of 10------------------------>")
run_GA_test(10)

print(f"<-----------------------Running Genetic Algorithm test with population of 50------------------------>")
run_GA_test(50)

print(f"<-----------------------Running Genetic Algorithm test with population of 100------------------------>")
run_GA_test(100)

print("<-------------Running Genetic Algorithm test until Solution is found with population of 10------------->")
find_GA_solution(10)

print("<-------------Running Genetic Algorithm test until Solution is found with population of 50------------->")
find_GA_solution(50)

print("\n********Genetic Algorithm test until a solution is found with population of 100 can take a while sometimes********")
userInput = input("Press y to run test with population 100, and anything else to skip and end program: ")
if userInput.lower() == "y":
    print("<-------------Running Genetic Algorithm test until Solution is found with population of 100------------->")
    find_GA_solution(100)

#print(f"<-----------------------Running Genetic Algorithm test with population of 1000------------------------>")
#run_GA_test(1000)      # Don't run this, takes too long

# Take str input from user
#populationSize = input("Enter population size: ")
# cast str as int
#populationSize = int(populationSize)
#print(f"Population = {populationSize}")
#numIterations = input("Enter max iterations to run: ")
#numIterations = int(numIterations)
