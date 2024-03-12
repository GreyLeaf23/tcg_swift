#!/usr/bin/python3
import random

ET = ["Fire", "Grass", "Water",
      "Lightning", "Metal", "Fighting",
      "Psychic", "Dark", "Dragon",
      "Fairy", "Colorless"]
CE = [0, 0, 0,
     0, 0, 0,
     0, 2, 0,
     0, 1]
AE = [0, 0, 0,
      0, 0, 0,
      0, 1, 0
      0, 2]
D = 40
A = 1


EnergyColoress = []
EnergyNonColorless = []

def CheckEnergy(CurrEnergy, AtkEnergy):
    i = 0
    j = 0

    # This will check for each colorless of the attack
    while i <= len(AtkEnergy):
        if AtkEnergy[i] == "Colorless":
            EnergyColoress.append = i
        if AtkEnergy[i] != "Colorless":
            EnergyNonColorless.append = i

        i += 1
    
    i = 0
    j = 0
    found = None

    # This will check if it has enough energy for
    # each non-colorless energy of the attack
    while i <= len(EnergyNonColorless):
        while found == None:
            if j <= len(CurrEnergy):
                if AtkEnergy[EnergyNonColorless[i]] == CurrEnergy[j]:
                    found = True
                    CurrEnergy = None
            else:
                found = False
            j += 1

        if found == True:
            i += 1
            found = None
        elif found == False:
            return(False)
    
    return(True)

def Attack(CurrEnergy, Energy, Damage, Amount):
    if Amount == 1:
        if CheckEnergy(CurrEnergy, Energy) == True:
            print("It dealt " + Damage)


    #elif Amount < 1:


    #elif Amount == 0:

# //////////////////////////// Tests ///////////////////////////
Attack(CE, AE, D, A)
