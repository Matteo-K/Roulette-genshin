from random import randint
from PIL import Image
import Boss as BS

Anemo = [("Voyageur","Anemo/Voyageur.png"), ("Xiao","Anemo/Xiao.png"), ("Venti","Anemo/Venti.png"), ("Sucrose","Anemo/Sucrose.png"), 
         ("Jean","Anemo/Jean.png"), ("Kazuha","Anemo/Kazuha.png"), ("Sayu","Anemo/Sayu.png"), ("Heizou","Anemo/Heizou.png"), 
         ("Nomade","Anemo/Nomade.png"), ("Faruzan","Anemo/Faruzan.png"), ("Lynette","Anemo/Lynette.png")]

Pyro = [("Xiangling","Pyro/Xiangling.png"), ("Bennett","Pyro/Bennett.png"), ("Klee","Pyro/Klee.png"), ("Diluc","Pyro/Diluc.png"), 
        ("Amber","Pyro/Amber"), ("Xinyan","Pyro/Xinyan.png"), ("Hu-tao","Pyro/Hutao.png"), ("Yanfei","Pyro/Yanfei.png"), 
        ("Yoimiya","Pyro/Yoimiya.png"), ("Thomas","Pyro/Thomas.png"), ("Dehya","Pyro/Dehya.png"), ("Lyney","Pyro/Lyney.png")]

Electro = [("Raiden","Electro/Raiden.png"), ("Cyno","Electro/Cyno.png"), ("Razor","Electro/Razor.png"), ("Fischl","Electro/Fischl.png"), 
           ("Beidou","Beidou.png"), ("Lisa","Lisa.png"), ("Keqing","Kequing.png"), ("Sara","Sara.png"), 
           ("Yae miko","Yae_miko.png"), ("Kuki Shinobu","Kuki.png"), ("Dori","Dori.png")]

Cryo = [("Chongyun","Chongyun.png"), ("Kaeya","Kaeya.png"), ("Qiqi","Qiqi.png"), ("Diona","Diona.png"),
        ("Ganyu","Ganyu.png"), ("Rosalia","Rosalia.png"), ("Eula","Eula.png"), ("Ayaka","Ayaka.png"), 
        ("Aloy","Aloy.png"), ("Shenhe","Shenhe.png"), ("Layla","Layla.png"), ("Mika","Mika.png"), 
        ("wriothesley","wriothesley.png")]

Geo = [("Noelle"), ("Ningguang"), ("Zhongli"), ("Albedo"), 
       ("Gorou"), ("Itto"), ("Yun-jin"), ("Navia","Geo/")]

Hydro = [("Xingqiu"), ("Barbara"), ("Mona"), ("Tartaglia"), 
         ("Kokomi"), ("Ayato"), ("Yelan"), ("Candace"), 
         ("Nilou"),("Neuvillette"),("Furina")]

Dendro = [("Collei"), ("Tighnari"), ("Alhaitam"), ("Yao Yao"), 
          ("Nahida"), ("Baizhu"), ("Kaveh"), ("Kirara")]

Liste_perso = [Anemo, Pyro, Electro, Cryo, Geo, Hydro, Dendro]

"""LISTE_COOL = ["Kazuha","Tartaglia","Ayaka","CYNO","KEEQUING","NAHIDA","DILUC","VOYAGEUR","MONA","ALOY","ALHAITHAM","ITTO","ALBEDO","ZONGHLI","XIAO","GANYU","RAIDEN","YELAN","JEAN","BAIZHU","TIGHNARI"]
for i in range (4):
    print(LISTE_COOL[randint(0,len(LISTE_COOL)-1)])"""

Character = {"Kazuha" : "", "Sayu" : "Sayu.png", 
             "Heizou" : "Heizou.png", "Nomade" : "Nomade.png", "Faruzan" : "Faruzan.png",
             "Lynette" : "lynette.png", "Xiangling" : "Xiangling.png", "Bennett":"Bennett.png", "Klee" : "Klee.png", 
             "Diluc": "Diluc.png", "Amber":"Amber.png", "Xinyan" : "Xinyan.png", 
             "Hu-tao" : "Hutao.png", "Yanfei": "Yanfei.png", "yoimiya":"Yoimiya.png", "Thomas":"Thomas_2.png", 
             "Dehya":"Dehya.png", "Lyney" : "lyney.png", "Raiden":"Baal.png", "Cyno":"Cyno.png", 
             "Razor":"Razor.png", "Fischl":"Fischl.png", "Beidou":"Beidou.png", "Lisa":"Lisa.png", 
             "Keqing":"Keqing-1.png", "Sara":"Sara.png", "Yae miko":"Yae_small.png", "Kuki Shinobu":"kuki.png", 
             "Dori":"Dori.png","Chongyun":"Chongyun.png", "Kaeya":"Kaeya.png", "Qiqi":"Qiqi-1.png", "Diona":"Diona.png", 
             "Ganyu":"Ganyu.png", "Rosalia":"Rosalia-1.png", "Eula":"Eula.png", "Ayaka":"Ayaka.png", "Aloy":"Aloy.png", 
             "Shenhe":"unknown-3.png", "Layla":"Layla.png", "Mika" : "Mika.png",
             "Noelle":"Noelle.png", "Ningguang":"Ninguan.png", "Zhongli":"Zhongli.png", "Albedo":"Albedo.png", 
             "Gorou":"Gorousmall.png", "Itto":"Ittosmall.png", "Yun-jin":"unknown-1.png","Xingqiu":"Xingqiu.png", 
             "Barbara":"Barbara.png", "Mona":"Mona-1.png", "Tartaglia": "Childe.png", "Kokomi":"Kokomi_icon.png", 
             "Ayato":"Ayato.png", "Yelan":"1.png", "Candace":"candace.png", "Nilou":"Nilou.png",
             "Collei":"Collei.png", "Tighnari":"tighnari.png", "Baizhu" : "Baizhu.png", "Kaveh" : "Kaveh.png",
             "Alhaitam":"Alhaitham.png", "Yao Yao":"Yaoyao.png", "Nahida":"Nahida-1.png", "Kirara" : "Kirara.png"
             }

def Perso(n):
    L,m = [],0
    while m < n:
        a = randint(0,len(Liste_perso)-1)
        b = randint(0,len(Liste_perso[a]))
        if Liste_perso[a][b-1] not in L:
            L.append(Liste_perso[a][b-1][0])
            m+=1
    return L
print(Perso(5))
def l (L):
    for i in range(len(L)):
        print(i+1,"-", L[i])
        
        
def l_image(L:list):
    for i in range(len(L)):
        for cle in Character:
            if cle == L[i]:
                Image.open("D:/Users/kerva/divertissement/Genshin/image perso genshin/"+Character[cle]).show(cle)
                print(i+1,"-", cle)
                
def ll_image(L:list):
    for i in range(len(L)):
        Image.open("D:/Users/kerva/divertissement/Genshin/image perso genshin/"+Character[str(L[i])]).show(str(L[i]))
        print(i+1,"-", L[i])

#print("Le Boss a battre sera", BS.Boss(BS.Liste_zone,BS.Zone(BS.Liste_zone)) )
#print(l(Perso(8)))
#print(l_image(Perso(8)))

#-------------------------
# - Interface Graphique -
#-------------------------

import tkinter
from tkinter import PhotoImage

########################
# Création De La Fenetre
########################

Random_Genshin = tkinter.Tk()
Random_Genshin.title("the Genshin Random Perso and Boss Run")
Random_Genshin.config(bg="#155CA4")
Random_Genshin.geometry("800x800")

#######################
# Marquage Du Contenent
#######################

Header = tkinter.Frame(Random_Genshin, 
                       bg='#124A85')
Content = tkinter.Frame(Random_Genshin,
                       bg='#3FA9C8')
Footer = tkinter.Frame(Random_Genshin, 
                       bg='#124A85')

##################
# Fonction Générer
##################

def Gener_Boss ():
    BOSS.pack_forget()
    BOSS.config(text= f"{BS.Boss(BS.Liste_zone,BS.Zone(BS.Liste_zone))}")
    BOSS.pack()

def Gener_Image_Perso ():
    label = [LabelImgPerso1,LabelImgPerso2,LabelImgPerso3,LabelImgPerso4]
    img = [ImagePerso1,ImagePerso2,ImagePerso3,ImagePerso4,LabelNomPerso1,LabelNomPerso2,LabelNomPerso3,LabelNomPerso4]
    direction = ["top", "bottom", "left", "right"]
    for i in range(4) :
        label[i].pack_forget()
        img[i+4].pack_forget()
    Liste = Perso(4)
    for i in range(len(Liste)) :
        img[i].config(file = "D:/Users/kerva/divertissement/Genshin/image perso genshin/"+Character[Liste[i]])
        img[i+4].config(text = Liste[i])
    for i in range (len(Liste)) :
        label[i].pack(side = direction[i])
        img[i+4].pack(side = direction[i])

def Gener_Image_Boss ():
    LabelImgBoss.pack_forget()
    LabelNomBoss.pack_forget()
    BigBoss = BS.Boss(BS.Liste_zone,BS.Zone(BS.Liste_zone))
    ImageBoss.config(file = "D:/Users/kerva/divertissement/Genshin/image boss genshin/"+BS.BossImage[BigBoss])
    LabelNomBoss.config(text = BigBoss)
    LabelImgBoss.pack(expand=1)
    LabelNomBoss.pack(pady=25)
    
#########################
# Différente Interraction
#########################

Titre = tkinter.Label(Header,
                       fg = "white",
                       text = "Appuyez Sur Les Bouttons Et Découvrez Les Persos Pour Combattre Le Boss",
                       bg ="#124A85")

GenPerso = tkinter.Button(Random_Genshin,
                         fg = "#E1F7B2",
                         bg = "#0E6ECF",
                         borderwidth = 4,
                         text = "Génère une liste de 4 Persos",
                         command = Gener_Image_Perso)

GenBoss = tkinter.Button(Content,
                         fg = "#E1F7B2",
                         bg = "#0E6ECF",
                         borderwidth = 4,
                         text = "Génère un Boss aléatoire",
                         command = Gener_Image_Boss)

BOSS = tkinter.Label(Content,
                       fg = "white",
                       bg='#3FA9C8',
                       text = "")

Quitter = tkinter.Button(Footer,
                         fg = "#E1F7B2",
                         bg = "#0E6ECF",
                         borderwidth = 4,
                         text = "Quitter",
                         command = Random_Genshin.destroy)



ImagePerso1 = PhotoImage()
ImagePerso2 = PhotoImage()
ImagePerso3 = PhotoImage()
ImagePerso4 = PhotoImage()
ImageBoss = PhotoImage(width=70,height=70)

LabelImgPerso1 = tkinter.Label(
                       image = ImagePerso1,
                       bg = "#155CA4")

LabelNomPerso1 = tkinter.Label(
                       bg = "#155CA4",
                       fg = "white")

LabelImgPerso2 = tkinter.Label(
                       image = ImagePerso2,
                       bg = "#155CA4")

LabelNomPerso2 = tkinter.Label(
                       bg = "#155CA4",
                       fg = "white")

LabelImgPerso3 = tkinter.Label(
                       image = ImagePerso3,
                       bg = "#155CA4")

LabelNomPerso3 = tkinter.Label(
                       bg = "#155CA4",
                       fg = "white")

LabelImgPerso4 = tkinter.Label(
                       image = ImagePerso4,
                       bg = "#155CA4")

LabelNomPerso4 = tkinter.Label(
                       bg = "#155CA4",
                       fg = "white")

LabelImgBoss = tkinter.Label(Content,
                       image = ImageBoss,
                       bg = "#3FA9C8")

LabelNomBoss = tkinter.Label(Content,
                       bg = "#3FA9C8",
                       fg = "white")

#########
# Packing
#########

Header.pack(side = "top", fill = "x", padx = 10, pady = 5)
Footer.pack(side = "bottom", fill = "x", padx = 10, pady = 5)
Content.pack(side = "left", fill = "y", padx = 15, pady = 5)

Titre.pack(pady = 10)
GenPerso.pack(padx = 10, pady = 20)
GenBoss.pack(padx = 10, pady = 20)
Quitter.pack(side="right", padx=10,pady=10)

Random_Genshin.mainloop()
    