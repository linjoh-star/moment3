Inkomst = int(float(input("Ange din månadslön: ")))
Kommunalt = int(Inkomst * 0.2136)
Landsting = int(Inkomst * 0.1148)
Kvar = Inkomst - Kommunalt - Landsting
print("Utskrift\n" 
      "Månadslön {0}\nKommunal skatt {1}\nLandstingskatt {2}\nKvar efter skatt {3}"
      " ".format(Inkomst, Kommunalt, Landsting, Kvar))
