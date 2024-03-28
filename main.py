# Euler Algorithm for a Nonlinear System of DE (Fake News)
import matplotlib.pyplot as plt
import numpy as np

def eulerSum(stepInitial, stepFinal, stepSize, cureConstant, infectionConstant, 
             initialSusceptible, initialInfected, initialResistant):
  
  numSusceptible = initialSusceptible
  numInfected = initialInfected
  numResistant = initialResistant
  numTotal = numSusceptible + numInfected + numResistant
  fWrite = open("estimation.txt", "w")
  susceptibles = []
  infecteds = []
  resistants = []
  steps = []

  # Num Interations
  while (stepInitial <= stepFinal):
    stepValues = equationSystem(cureConstant, infectionConstant, numSusceptible, numInfected, numResistant, numTotal)
    numSusceptible += stepSize * stepValues[0]
    numInfected += stepSize * stepValues[1]
    numResistant += stepSize * stepValues[2]
    stepInitial += stepSize
    roundInit = round(stepInitial,3)
    roundSusceptible = round(numSusceptible,3)
    roundInfected = round(numInfected,3)
    roundResistant = round(numResistant,3)
    susceptibles.append(roundSusceptible)
    infecteds.append(roundInfected)
    resistants.append(roundResistant)
    steps.append(roundInit)

    fWrite.write(f"Step Value {roundInit}: {roundSusceptible} {roundInfected} {roundResistant}\n")

  plt.plot(steps, susceptibles, label='Susceptible')
  plt.plot(steps, infecteds, label='Infected')
  plt.plot(steps, resistants, label='Resistant')
  plt.xlabel('Time')
  plt.ylabel('Number of Individuals')
  plt.legend()
  plt.show()

  fWrite.close()
  
def equationSystem(cureConstant, infectionConstant, numSusceptible, numInfected, numResistant, numTotal):
  fS = -1 * infectionConstant * numSusceptible * numInfected / numTotal if numSusceptible > 0 and numInfected > 0 else 0
  fI = infectionConstant * numSusceptible * numInfected / numTotal - cureConstant * numInfected if numSusceptible > 0 and numInfected > 0 else 0
  fR = cureConstant * numInfected if numInfected > 0 else 0
  return [fS, fI, fR]

def main():
  # Testing Parameters
  eulerSum(0, 30, 0.001, 0.07, 1.34,
           134000000,59,13)# Initial Values

if __name__ == "__main__":
  main()





