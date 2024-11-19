def conversionBinDec(nbr):
  """Conversion du binaire vers l'hexadecimal

  Args:
      nbr (list): tableau des binaires

  Returns:
      int: decimal calculer d'apres le tableau des binaires
  """
  result = 0
  for i in range(len(nbr)-1):
    result = int(nbr[i])*2**2-i
  return result

def conversionHexBin(nbr):
  """Conversion de l'hexadecimal au binaire

  Args:
      nbr (list): tableau avec deux valeur d'hexadecimal

  Returns:
      list: tableau des valeurs du binaires
  """
  result=[]
  match nbr[0]:
    case "0":
      result.append(0)
      result.append(0)
      result.append(0)
      result.append(0)
    case "1":
      result.append(0)
      result.append(0)
      result.append(0)
      result.append(1)
    case "2":
      result.append(0)
      result.append(0)
      result.append(1)
      result.append(0)
    case "3":
      result.append(0)
      result.append(0)
      result.append(1)
      result.append(1)
    case "4":
      result.append(0)
      result.append(1)
      result.append(0)
      result.append(0)
    case "5":
      result.append(0)
      result.append(1)
      result.append(0)
      result.append(1)
    case "6":
      result.append(0)
      result.append(1)
      result.append(1)
      result.append(0)
    case "7":
      result.append(0)
      result.append(1)
      result.append(1)
      result.append(1)
    case "8":
      result.append(1)
      result.append(0)
      result.append(0)
      result.append(0)
    case "9":
      result.append(1)
      result.append(0)
      result.append(0)
      result.append(1)
    case "A":
      result.append(1)
      result.append(0)
      result.append(1)
      result.append(0)
    case "B":
      result.append(1)
      result.append(0)
      result.append(1)
      result.append(1)
    case "C":
      result.append(1)
      result.append(1)
      result.append(0)
      result.append(0)
    case "D":
      result.append(1)
      result.append(1)
      result.append(0)
      result.append(1)
    case "E":
      result.append(1)
      result.append(1)
      result.append(1)
      result.append(0)
    case "F":
      result.append(1)
      result.append(1)
      result.append(1)
      result.append(1)
    
  match nbr[1]:
    case "0":
      result.append(0)
      result.append(0)
      result.append(0)
      result.append(0)
    case "1":
      result.append(0)
      result.append(0)
      result.append(0)
      result.append(1)
    case "2":
      result.append(0)
      result.append(0)
      result.append(1)
      result.append(0)
    case "3":
      result.append(0)
      result.append(0)
      result.append(1)
      result.append(1)
    case "4":
      result.append(0)
      result.append(1)
      result.append(0)
      result.append(0)
    case "5":
      result.append(0)
      result.append(1)
      result.append(0)
      result.append(1)
    case "6":
      result.append(0)
      result.append(1)
      result.append(1)
      result.append(0)
    case "7":
      result.append(0)
      result.append(1)
      result.append(1)
      result.append(1)
    case "8":
      result.append(1)
      result.append(0)
      result.append(0)
      result.append(0)
    case "9":
      result.append(1)
      result.append(0)
      result.append(0)
      result.append(1)
    case "A":
      result.append(1)
      result.append(0)
      result.append(1)
      result.append(0)
    case "B":
      result.append(1)
      result.append(0)
      result.append(1)
      result.append(1)
    case "C":
      result.append(1)
      result.append(1)
      result.append(0)
      result.append(0)
    case "D":
      result.append(1)
      result.append(1)
      result.append(0)
      result.append(1)
    case "E":
      result.append(1)
      result.append(1)
      result.append(1)
      result.append(0)
    case "F":
      result.append(1)
      result.append(1)
      result.append(1)
      result.append(1)

  return result

def conversionHexDec(nbr):
  """Conversion de l'hexadecimal vers le decimal

  Args:
      nbr (list): tableau d'un hexadecimal

  Returns:
      str: La valeur decimal corespondante
  """
  match nbr:
    case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
      return nbr
    case "a":
      return "10" 
    case "b":
      return "11"
    case "c":
      return "12"
    case "d":
      return "13"
    case "e":
      return "14"
    case "f":
      return "15"
    
def champService(octet):
  """Calcul tout les occupations dans octet du champ service

  Args:
      octet (list): octet du champ service a analyser
  """
  #Priorité dans le champ service
  troisBit = [octet[i] for i in range(2)]
  priorite = conversionBinDec(troisBit)
  match priorite:
    case 0:
      print("Priorité : 0-Routine")
    case 1:
      print("Priorité : 1-Prioritaire")
    case 2:
      print("Priorité : 2-Immédiat")
    case 3:
      print("Priorité : 3-Urgent")
    case 4:
      print("Priorité : 4-Tres urgent")
    case 5:
      print("Priorité : 5-Critique")
    case 6:
      print("Priorité : 6-Supervision interconnexion")
    case 7:
      print("Priorité : 7-Supervision réseau")

  #Le reste du champ service
  delais = octet[3]
  debit = octet[4]
  fiabilite = octet[5]
  cout = octet[6]
  mbz = "0"
  if octet[7] != mbz :
    print("Il y a une erreur le bit pour le MBZ n'est pas a 0")

def enteteIP(tableauEntete):
  """Analyse de l'enteteIP

  Args:
      tableauEntete (_type_): _description_
  """
  #Conversion necessaire (mais un rappel du cours avant de le faire)
  vers = tableauEntete[14][0]
  ihl = tableauEntete[15][1]

def enteteEthernet(tableauEntete):
  """Details l'entête Ethrnet

  Args:
      tableauEntete (list): Tableau avec la trame a anlyser
  """
  i = 0
  adresseDestination = []
  adresseSource = []
  etherType = []

  #Adresse Destination
  print("L'adresse MAC Destination est : ")
  for i in range(0, 6):
    adresseDestination.append(tableauEntete[i])
  print(adresseDestination)

  #Adresse Source
  print("L'adresse MAC Source est : ")
  for i in range(6, 12):
    adresseSource.append(tableauEntete[i])
  print(adresseSource)

  #EtherType
  print("L'Ether type est : ")
  for i in range(12, 14):
    etherType.append(tableauEntete[i])
  print(etherType)

  match etherType:
    case ["08","00"]:
      enteteIP(tableauEntete)

def entrerEntete():
  """Prend une entet d'un utilisateur en string et la transforme en tableau."""
  entrer = str(input("Entrer votre trame [00 00 00 00 00 00 etc] : "))
  tableauEntete = []
  for i in range(len(entrer)-1):
    if entrer[i] != " " and entrer[i+1] != " ": 
      tableauEntete.append(entrer[i]+entrer[i+1])
  print("Votre entête est : ")
  print(tableauEntete)
  enteteEthernet(tableauEntete)

entrerEntete()

















"""          
          & & %@@*/*/
        % @.  %@@@@*@*@&@
     ,#/@@%@@@%@@  *,*/&/@@
    ,,#/  %   @@@  /,**&  @@
   /,,#/@@%   @@@,*/(**&  @@
   //,*#/,*%   @(@  /(**& @@
   / ,%,@@&  *@@@  /(@*&.@@@
   @@/@@@(%,*/ @@  .@@/@@@&@
  @,@@#@@@%% Neiryx *@@*@@@&@@
 @(,@/    (#  /(@@  *@(   .&@@
  @.&     ,#  /*#&@@.@     *@@#
  @.@@#*%%@@  /@@@  *@@%.(%@@@#
    @#*@%@@ *@@@@  *@@%(@%@@
     #(@@(@ @@%&&  *@@%(@&
     #/(@(@ @@@@@& *@@%@/
     #,(@/# @/@@.% *@@%@/
     #,&@,/ @.,&@ .*@@%@(
      .@   @@ &,%.*# %@
                                                            
"""