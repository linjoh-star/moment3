Inkomst = int(float(input("Ange din månadslön: ")))
Kommunalt = int(Inkomst * 0.2136)
yearinkomst = int(Inkomst * 12)
Landsting = int(Inkomst * 0.1148)
Statskatt = int(0)
if yearinkomst >= 675700:
    Statskatt = int(Inkomst *0.25)
else:
    Statskatt = int(Inkomst * 0.20)


Kvar = Inkomst - Kommunalt - Landsting - Statskatt


if 19247 < yearinkomst < 468700:
      print("Utskrift\n" 
      "Månadslön        {0}kr (Årslön: {4}kr)\nKommunal skatt   {1}kr\nLandstingskatt   {2}kr\nKvar efter skatt {3}kr"
      .format(Inkomst, Kommunalt, Landsting, Kvar, yearinkomst))

elif 468699 < yearinkomst < 675700:
    print("Utskrift\n"
         "Månadslön        {0}kr (Årslön: {4}kr)\nKommunal skatt   {1}kr\nLandstingskatt   {2}kr\nStatlig skatt    {5}kr   \nKvar efter skatt {3}kr"
         .format(Inkomst, Kommunalt, Landsting, Kvar, yearinkomst, Statskatt))

elif yearinkomst > 675700:
    print("Utskrift\n"
         "Månadslön         {0}kr (Årslön:  {4}kr)\nKommunal skatt    {1}kr\nLandstingskatt    {2}kr\nStatlig skatt     {5}kr\nKvar efter skatt  {3}kr\n "
         .format(Inkomst, Kommunalt, Landsting, Kvar, yearinkomst, Statskatt, ))

else:
      print("Utskrift\nMånadslön        {0}kr  (Årslön: {1}kr)\nKvar efter skatt {0}kr\nEftersom du tjänar under brytpunkten betalar du ingen skatt".format(Inkomst, yearinkomst))
