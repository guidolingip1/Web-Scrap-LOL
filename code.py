import requests 
from bs4 import BeautifulSoup
from PIL import Image

def getdata(url): 
    r = requests.get(url) 
    return r.text

test_champions = ['Aatrox','Ahri','Akali','Alistar','Amumu','Anivia','Annie','Ashe','Aurelion Sol','Azir','Blitzcrank','Brand','Braum','Caitlyn','Camille','Cassiopeia','ChoGath','Corki','Darius','Diana','Dr.Mundo','Draven','Ekko','Elise','Evelynn','Ezreal','Fiddlesticks','Fiora','Fizz','Galio','Gangplank','Garen','Gnar','Gragas','Graves','Hecarim','Heimerdinger','Illaoi','Irelia','Ivern','Janna','JarvanIV','Jax','Jayce','Jhin','Jinx','KaiSa','Kalista','Karma','Karthus','Kassadin','Katarina','Kayle','Kayn','Kennen','Khazix','Kindred','Kled','Kogmaw','LeBlanc','Leesin','Leona','Lissandra','Lucian','Lulu','Lux','Malphite','Malzahar','Maokai','Master Yi','Miss Fortune','Mordekaiser','Morgana','Nami','Nasus','Nautilus','Neeko','Nidalee','Nocturne','NunuWillump','Olaf','Orianna','Ornn','Pantheon','Poppy','Pyke','Quinn','Rammums','Renekton','Rengar','Riven','Rumble','Ryze','Sejuani','Shaco','Shen','Shyvana','Singed','Sion','Sivir','Skarner','Sona','Soraka','Swain','Sylas','Syndra','Tahm Kench','Taliyah','Talon','Taric','Teemo','Thresh','Tristana','Trundle','Tryndamare','Twisted Fate','Twitch','Udyr','Urgot','Varus','Vayne','Veigar','VelKoz','Vi','Viktor','Vladimir','Volibear','Warwick','Wukong','Xayah','Xerath','XinZhao','Yasuo','Yorick','Zac','Zed','Ziggs','Zilean','Zoe','Zyra']

for i in range(len(test_champions)):
    print(test_champions[i])
    champion = test_champions[i];
    lista_imagens = [];
    list_skills = [];
    final_list_skill = []
      
    htmldata = getdata("https://www.mobafire.com/league-of-legends/champion/" + test_champions[i])
    soup = BeautifulSoup(htmldata, 'html.parser') 
    
    for item in soup.find_all('img'):
        lista_imagens.append(item['src']);
    
    #Aqui adiciona somente os arquivos que são de ability
    for i in lista_imagens:
        if "ability" in i:
            list_skills.append(i);
    #-----------------------------------------------------
    
    #Aqui eu removo todos os arquivos duplicados
    final_list_skill = list(dict.fromkeys(list_skills))
    #--------------------------------------------------

    for j in range(len(final_list_skill)):
        Image_url ="https://www.mobafire.com/" + final_list_skill[j];
        im = Image.open(requests.get(Image_url, stream=True).raw);
        im.save(r"C:\Users\Guilherme\Desktop\Projetos\LolScrap\\" + champion + "_a_" + str(j) + ".png");
    
        
    lista_imagens.clear();
    list_skills.clear();
    final_list_skill.clear();
