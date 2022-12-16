Inkomst = int(float(input("Ange din månadslön: ")))
Kommunalt = int(Inkomst * 0.2136)
yearinkomst = int(Inkomst * 12)
Landsting = int(Inkomst * 0.1148)
Kvar = Inkomst - Kommunalt - Landsting
if yearinkomst > 19247:
      print("Utskrift\n" 
      "Månadslön        {0}kr (Årslön: {4}kr)\nKommunal skatt   {1}kr\nLandstingskatt   {2}kr\nKvar efter skatt {3}kr"
      " ".format(Inkomst, Kommunalt, Landsting, Kvar, yearinkomst))
else:
      print("Utskrift\nMånadslön        {0}kr  (Årslön: {1}kr)\nKvar efter skatt {0}kr\nEftersom du tjänar under brytpunkten betalar du ingen skatt".format(Inkomst, yearinkomst))
