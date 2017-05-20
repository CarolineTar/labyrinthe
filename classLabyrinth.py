"""Classe "Labyrinthe : "attribut map : listes de listes,
    importée au début"""

class Labyrinth:
    def __init__(self):
        self.choose_map()

    def choose_map(self):
        maps_list = self.getMaps()
        print ("Voici les labyrinthes possibles")
        for ind, m in enumerate(maps_list):
            print (ind, m[0])
        choice = input("entrez un numéro pour choisir votre labyrinthe")
        try:
            choice = int(choice)
            assert choice in range(0,len(maps_list))
        except AssertionError:
            print("votre entrée n'est pas valide !")
            raise ValueError
        map_data = maps_list[choice]
        self.map_name = map_data[0]
        self.started = map_data[1]
        if self.started == True:
            print("vous reprenez une partie déjà commencée !")
        
    def getMaps(self):
        """ renvoie liste (=maps_list)de liste (=data_list) (-> pour chaque carte,
        son nom et est-ce qu'une partie est en cours ou pas)"""
        import os
        read_data = os.listdir("maps")
        maps_list = list()
        for data in read_data:
            data_clean = data.split(".")
            data_list = data_clean[0].split("_")
            try:
                assert len(data_list) == 2
            except AssertionError:
                raise ValueError(data, "n'est pas bien nommée")
            maps_list.append(data_list)
        return maps_list

   
