def champService(octet):
  """Calcul tout les occupations dans octet du champ service

  Args:
      octet (list): octet du champ service a analyser
  """
  #Priorité
  priorite = [octet[i] for i in range(2)]
  priorite = conversionBinDec(priorite)
  match priorite:
    case 0:
      print("Priorité : 0 - Routine")
    case 1:
      print("Priorité : 1 - Prioritaire")
    case 2:
      print("Priorité : 2 - Immédiat")
    case 3:
      print("Priorité : 3 - Urgent")
    case 4:
      print("Priorité : 4 - Tres urgent")
    case 5:
      print("Priorité : 5 - Critique")
    case 6:
      print("Priorité : 6 - Supervision interconnexion")
    case 7:
      print("Priorité : 7 - Supervision réseau")

  #Délais
  delais = "0 - Normal" if octet[3] == 0 else "1 - Bas"

  print("Délais : " + delais)

  #Débit
  debit = "0 - Normal" if octet[4] == 0 else "1 - Haut"
  print("Débit : " + debit)

  #Fiabilité
  fiabilite = "0 - Normal" if octet[5] == 0 else "1 - Haute"
  print("Fiabilité : " + fiabilite)

  #Cout
  cout = "0 - Normal" if octet[6] == 0 else "1 - Faible"
  print("Cout : " + cout)

  #Must be zero
  mbz = octet[7]
  print("MBZ : ", mbz)
  if octet[7] != mbz :
    print("Il y a une erreur le bit pour le MBZ n'est pas a 0")

def enteteIP(trame):
  """Analyse de l'enteteIP

  Args:
      trame (list): trame fournie par l'utilisateur
  """
  entete = [trame[i] for i in range(14, 34)]
  print("Entete IP :")
  print(entete)

  #Vers
  vers = conversionHexDec(entete[0][0])
  match vers:
    case 0:
      print("Vers : 00 - Reserve")
    case 4:
      print("Vers : 04 - IPV4")
    case 5:
      print("Vers : 05 - ST Datagram Mode")
    case 6:
      print("Vers : 06 - IPV6")
    case 15:
      print("Vers : 15 - Reserve") 
  
  #IHL
  ihl = conversionHexDec(entete[0][1])*4 # IHL x*32/8  donc x*4
  print("IHL : ", ihl," octets")

  #Service
  champService(conversionHexBin(entete[1]))

  #Longueur totale(a corriger)
  longueurTotale =[]

  for i in range(2):
    temp1 = conversionHexBin(entete[2])
    temp2 = conversionHexBin(entete[3])

  for i in range (8):
    longueurTotale.append(temp1[i])
  for i in range (8):
    longueurTotale.append(temp2[i])

  longueurTotale = conversionBinDec(longueurTotale)
  print("Longueur totale : ", longueurTotale)

  #Identification
  identification = [entete[4], entete[5]]
  print("Identification : ", identification)

  #Flag/Position frgment (a corriger)
  total =[]

  for i in range(2):
    temp1 = conversionHexBin(entete[6])
    temp2 = conversionHexBin(entete[7])

  for i in range (8):
    total.append(temp1[i])
  for i in range (8):
    total.append(temp2[i])

  flag = [total[i] for i in range(3)]
  flag = conversionBinDec(flag)
  print("Flag : ", flag)

  positionFragment = [total[i] for i in range(3, 8)]
  positionFragment = conversionBinDec(positionFragment)
  print("Position fragment : ", positionFragment)

  #TTL (a corriger)
  ttl = conversionHexBin(entete[8])
  ttl = conversionBinDec(ttl)
  print("TTL : ", ttl)

  #Protocle
  protocole = conversionHexBin(entete[9])
  protocole = conversionBinDec(protocole)

  match protocole:
    case 1:
      print("Protocole : 01 - ICMP")
    case 2:
      print("Protocole : 02 - IGMP")
    case 6:
      print("Protocole : 06 - TCP")
    case 17:
      print("Protocole : 17 - UDP")

  #Checksum
  checksum = [entete[10], entete[11]]
  print("Checksum : ", checksum)

  #IP Source
  a=conversionHexBin(entete[12])
  b=conversionHexBin(entete[13])
  c=conversionHexBin(entete[14])
  d=conversionHexBin(entete[15])

  a=conversionBinDec(a)
  b=conversionBinDec(b)
  c=conversionBinDec(c)
  d=conversionBinDec(d)
 
  print("IP Source : ", a,".",b ,".",c ,".",d)

  #IP Destination
  a=conversionHexBin(entete[16])
  b=conversionHexBin(entete[17])
  c=conversionHexBin(entete[18])
  d=conversionHexBin(entete[19])

  a=conversionBinDec(a)
  b=conversionBinDec(b)
  c=conversionBinDec(c)
  d=conversionBinDec(d)
 
  print("IP Destination : ", a,".",b ,".",c ,".",d)


def enteteEthernet(trame):
  """Analyse l'entet Ethernet de la trame donnée

  Args:
      trame (list): trame donnée

  Returns:
      list: etherType
  """

  entete = [trame[i] for i in range(14)]
  print("Entete Ethernet :")
  print(entete)

  #Adresse Mac Destination
  adresseDestination = []
  print("L'adresse MAC Destination est : ")
  for i in range(0, 6):
    adresseDestination.append(entete[i])
  print(adresseDestination)

  #Adresse Mac Source
  adresseSource = []
  print("L'adresse MAC Source est : ")
  for i in range(6, 12):
    adresseSource.append(entete[i])
  print(adresseSource)

  #EtherType
  etherType = []
  print("L'Ether type est : ")
  for i in range(12, 14):
    etherType.append(entete[i])
  print(etherType)

  return etherType

def conversionHexDec(nbr):
  """Conversion de l'hexadecimal vers le decimal

  Args:
      nbr (list): tableau d'un hexadecimal

  Returns:
      str: La valeur decimal corespondante
  """
  match nbr:
    case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
      return int(nbr)
    case "a":
      return 10
    case "b":
      return 11
    case "c":
      return 12
    case "d":
      return 13
    case "e":
      return 14
    case "f":
      return 15

def conversionBinDec(binaire):
  """Conversion du binaire vers decimal

  Args:
      nbr (list): tableau des binaires

  Returns:
      int: decimal calculer d'apres le tableau des binaires
  """
  decimal = 0
  for i in range(len(binaire)):
    decimal += int(binaire[i])*2**((len(binaire)-1)-i)
  return decimal

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
    case "a":
      result.append(1)
      result.append(0)
      result.append(1)
      result.append(0)
    case "b":
      result.append(1)
      result.append(0)
      result.append(1)
      result.append(1)
    case "c":
      result.append(1)
      result.append(1)
      result.append(0)
      result.append(0)
    case "d":
      result.append(1)
      result.append(1)
      result.append(0)
      result.append(1)
    case "e":
      result.append(1)
      result.append(1)
      result.append(1)
      result.append(0)
    case "f":
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
    case "a":
      result.append(1)
      result.append(0)
      result.append(1)
      result.append(0)
    case "b":
      result.append(1)
      result.append(0)
      result.append(1)
      result.append(1)
    case "c":
      result.append(1)
      result.append(1)
      result.append(0)
      result.append(0)
    case "d":
      result.append(1)
      result.append(1)
      result.append(0)
      result.append(1)
    case "e":
      result.append(1)
      result.append(1)
      result.append(1)
      result.append(0)
    case "f":
      result.append(1)
      result.append(1)
      result.append(1)
      result.append(1)

  return result

def conversionTableau(chaine):
  """Convertit une chaine de caractere avec de l'exadecimal en list(tableau)

  Args:
      trameC (string): trame entrer par l'utilisateur
  """
  tableau = []

  for i in range(len(chaine)-1):

    if chaine[i] != " " and chaine[i+1] != " ": 
      tableau.append(chaine[i]+chaine[i+1])

  return tableau

#Début du programme
trameC = str(input("Entrer votre trame [00 00 00 00 00 00 etc] (avec un copié coller par exemple): "))
trameT = conversionTableau(trameC)

print("Votre Trame est : ")
print(trameT)

etherType = enteteEthernet(trameT)

match etherType:
  case ["08","00"]:
    enteteIP(trameT)



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