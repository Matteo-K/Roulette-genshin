from random import randint

Mondstart = ["Cube anémo", "Stromterror", "Fleurs cryo", "Loup", "Cube électro", "Cube cryo", "Roi sanglier"]
Liyue = ["Océanide", "Azdaha", "Géausore", "Fleurs pyro", "Cube géo", "Tartaglia", "Serpent Mécanique"]
Inazuma = ["Matrice Mécanique", "La raiden", "Cube Pyro", "Signora", "Cube hydro", "Lame Oni", "Manifestation du tonnerre", "Loup alpha doré", "Le Duo dragons"]
Sumeru = ["Fleurs électro", "La dinde", "Philippe", "Serpent ensabler", "Dragon Mécanique", "Cube dendro", "Le drone", "Dragon de Verdure", "Mage Multifonction"]
Fontaine = ["Crabe pyromane", "Danseur", "Danseuse", "Viviane du lac", "Hippocampe"]

Liste_zone = [Mondstart,Liyue,Inazuma,Sumeru,Fontaine]

BossImage = {"Cube anémo" : "cube_anemo.png", "Stromterror" : "Stromterror.png", "Fleurs cryo" : "Fleur_cryo.png", 
             "Loup" : "Loup.png", "Cube électro" : "cube_electro.png", "Cube cryo" : "cube_cryo.png",
             "Roi sanglier" : "Roi-des-sangliers.png", "Océanide" : "oceanide.png", 
             "Azdaha" : "Azdaha.png", "Géausore" : "m_26050101_70.png", "Fleurs pyro" : "Fleur_pyro.png", 
             "Cube géo" : "m_20040301_70.png", "Tartaglia" : "m_29030101_70.png", "Serpent Mécanique" : "Serpent_des_ruines.png", 
             "Matrice Mécanique" : "Matrice_mecanique.png", "La raiden" : "Ei.png", "Cube Pyro" : "cube_pyro.png", 
             "Signora" : "m_29050101_70.png", "Cube hydro" : "cube_hydro.png", "Lame Oni" : "Lame_oni.png", 
             "Manifestation du tonnerre" : "m_20070101_70.png", "Loup alpha doré" : "Loup_alpha_dore.png", 
             "Le Duo dragons" : "Harde-delementosaures-abyssaux-70x70-1.png", "Fleurs électro" : "Fleur_electro.png", 
             "La dinde" : "Dinde.png", "Philippe" : "Nomade_meca.png", "Serpent ensabler" : "Wenut.png", 
             "Dragon Mécanique" : "Dragon-cataclysmique.png", "Cube dendro" : "cube_dendro.png", 
             "Le drone" : "Drone.png", "Dragon de Verdure" : "Garde_de_loasis.png", "Mage Multifonction" : "Lustrateur-inique.png",
             "Crabe pyromane" : "empereur-du-feu.png", "Danseur" : "Danseur.png", "Danseuse" : "Danseur.png", 
             "Viviane du lac" : "Fantasme.png", "Hippocampe" : "Hippocampe.png"
    }

def Zone (liste:list):
    zone = randint(0,len(liste)-1)
    return zone
    
def Boss(liste:list, zone:int):
    boss = randint(0,len(liste[zone])-1)
    return liste[zone][boss]
