# Euler Algorithm for a Nonlinear System of DE (Fake News)

def eulerSum(stepInitial, stepFinal, stepSize, cureConstant, infectionConstant, 
             initialSusceptible, initialInfected, initialResistant):
  
  numSusceptible = initialSusceptible
  numInfected = initialInfected
  numResistant = initialResistant
  numTotal = numSusceptible + numInfected + numResistant
  fWrite = open("estimation.txt", "w")

  # Num Interations
  while (stepInitial <= stepFinal):
    stepValues = equationSystem(cureConstant,infectionConstant, numSusceptible, numInfected, numResistant, numTotal)
    numSusceptible += stepSize * stepValues[0]
    numInfected += stepSize * stepValues[1]
    numResistant += stepSize * stepValues[2]
    stepInitial += stepSize
    fWrite.write(f"Step Value {round(stepInitial,3)}: {round(numSusceptible,3)} {round(numInfected,3)} {round(numResistant,3)}\n")

  fWrite.close()
  
def equationSystem(cureConstant, infectionConstant, numSusceptible, numInfected, numResistant, numTotal):
  fS = -1 * infectionConstant * numSusceptible * numInfected / numTotal if numSusceptible > 0 and numInfected > 0 else 0
  fI = infectionConstant * numSusceptible * numInfected / numTotal - cureConstant * numInfected if numSusceptible > 0 and numInfected > 0 else 0
  fR = cureConstant * numInfected if numInfected > 0 else 0
  return [fS, fI, fR]

def main():
  # Testing Parameters
  eulerSum(0, 30, 0.05, 0.7, 1.34,
           134000000,59,13)# Initial Values

if __name__ == "__main__":
  main()





