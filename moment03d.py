inkomst = int(float(input("Ange din månadslön: ")))
kommunalt = int(inkomst * 0.2136)
yearinkomst = int(inkomst * 12)
landsting = int(inkomst * 0.1148)
statskatt = int(0)
if yearinkomst >= 675700:
    statskatt = int(inkomst *0.25)
else:
    statskatt = int(inkomst * 0.20)


kvar = inkomst - kommunalt - landsting - statskatt
kvarpro = int((kvar/inkomst)*100)

if 19247 < yearinkomst < 468700:
      print("Utskrift\n" 
      "Månadslön        {0}kr (Årslön: {4}kr)\nKommunal skatt   {1}kr\nLandstingskatt   {2}kr\nKvar efter skatt {3}kr"
      .format(inkomst, kommunalt, landsting, kvar, yearinkomst))

elif 468699 < yearinkomst < 675700:
    print("Utskrift\n"
         "Månadslön        {0}kr (Årslön: {4}kr)\nKommunal skatt   {1}kr\nLandstingskatt   {2}kr\nStatlig skatt    {5}kr   \nKvar efter skatt {3}kr"
         .format(inkomst, kommunalt, landsting, kvar, yearinkomst, statskatt))

elif yearinkomst > 675700:
    print("Utskrift\n"
         "Månadslön         {0}kr (Årslön:  {4}kr)\nKommunal skatt    {1}kr\nLandstingskatt    {2}kr\nStatlig skatt     {5}kr\nKvar efter skatt  {3}kr\nAndel betald skatt {6}% "
         .format(inkomst, kommunalt, landsting, kvar, yearinkomst, statskatt, kvarpro))

else:
      print("Utskrift\nMånadslön        {0}kr  (Årslön: {1}kr)\nKvar efter skatt {0}kr\nEftersom du tjänar under brytpunkten betalar du ingen skatt".format(inkomst, yearinkomst))


