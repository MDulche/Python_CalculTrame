
def entrerEntete():
  """Prend une entet d'un utilisateur en string et la transforme en tableau."""
  entrer = str(input("Entrer votre trame [00 00 00 00 00 00 etc] : "))
  tableauEntete = []
  for i in range(len(entrer)-1):
    if entrer[i] != " " and entrer[i+1] != " ": 
      tableauEntete.append(entrer[i]+entrer[i+1])
  print("Votre entête est : " + tableauEntete)
  enteteEthernet(tableauEntete)

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