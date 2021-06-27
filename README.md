# Web scrap dinâmico em Python
![WebScrap]('https://github.com/guidolingip1/Web-Scrap-LOL/blob/main/webscrap.gif')

## Mas Gui, O que é Web Scrap?
Coletar dados da Web usando scripts que vão "raspar" a informação e utilizar ela a nosso favor.

## Mas e o Scrap Dinâmico?
Isso significa que eu irei escrever um código que pega o URL base do site e percorre as páginas que eu bem entender, não focando somente em uma única página (se não entendeu não se preocupe, veremos melhor adiante)

## O que vamos coletar?
Vamos coletar as Imagens de todas as habilidades de todos os campeões do League of Legends.

## Mas porque vamos coletar isso?
Porque eu tenho vontade de escrever um APP em que eu vou utilizar as imagens, e para não ter que baixar na mão mais de 140 (campeões) * 4 (Habilidades) = 560 imagens e além disso ter que renomear cada uma para o padrão de nomes que eu escolher.

Isso levaria um bom tempo, além de ser chato e repetitivo.

## Falta escolhermos um site para o Scrap
Eu escolhi o site https://www.mobafire.com.



## Bora começar?
Primeiro você deve instalar as bibliotecas abaixo

    pip install requests
    pip install beautifulsoup4
    pip install Pillow
1. Requests será usada para fazer a requisição para o servidor do site escolhido.
2. bs4 será utilizada para fazermos a extração dos dados do site (web scrap).
3. PIL ou Pillow, serve para manipularmos e salvarmos as imagens que escolhermos.



## Depois de instaladas as bibliotecas vamos ao código
Começamos importando nossas bibliotecas

	import requests 
    from bs4 import BeautifulSoup
    from PIL import Image

## Vamos criar uma função para pegar a data

    def getdata(url): 
        r = requests.get(url) 
        return r.text
Aqui estamos fazendo uma requisição da URL escolhida e imprimindo o texto de resposta, que normalmente é o HTML inteiro da página, um exemplo de print do próprio código é.

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="https://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    .
    .
    .
    .
    Muitas e muitas linhas retornadas.

## Adicionando a dinâmica
Como queremos as imagens de todos os campeões precisamos de uma lista com os nomes.

    test_champions = ['Aatrox','Ahri','Akali','Alistar','Amumu','Anivia','Annie','Ashe','Aurelion Sol','Azir','Blitzcrank','Brand','Braum','Caitlyn','Camille','Cassiopeia','ChoGath','Corki','Darius','Diana','Dr.Mundo','Draven','Ekko','Elise','Evelynn','Ezreal','Fiddlesticks','Fiora','Fizz','Galio','Gangplank','Garen','Gnar','Gragas','Graves','Hecarim','Heimerdinger','Illaoi','Irelia','Ivern','Janna','JarvanIV','Jax','Jayce','Jhin','Jinx','KaiSa','Kalista','Karma','Karthus','Kassadin','Katarina','Kayle','Kayn','Kennen','Khazix','Kindred','Kled','Kogmaw','LeBlanc','Leesin','Leona','Lissandra','Lucian','Lulu','Lux','Malphite','Malzahar','Maokai','Master Yi','Miss Fortune','Mordekaiser','Morgana','Nami','Nasus','Nautilus','Neeko','Nidalee','Nocturne','NunuWillump','Olaf','Orianna','Ornn','Pantheon','Poppy','Pyke','Quinn','Rammums','Renekton','Rengar','Riven','Rumble','Ryze','Sejuani','Shaco','Shen','Shyvana','Singed','Sion','Sivir','Skarner','Sona','Soraka','Swain','Sylas','Syndra','Tahm Kench','Taliyah','Talon','Taric','Teemo','Thresh','Tristana','Trundle','Tryndamare','Twisted Fate','Twitch','Udyr','Urgot','Varus','Vayne','Veigar','VelKoz','Vi','Viktor','Vladimir','Volibear','Warwick','Wukong','Xayah','Xerath','XinZhao','Yasuo','Yorick','Zac','Zed','Ziggs','Zilean','Zoe','Zyra']

Agora com os nomes em mãos precisamos percorrer esta lista e gerar uma URL diferente para cada campeão.

    for i in range(len(test_champions)):
        print(test_champions[i])
        champion = test_champions[i];
        lista_imagens = [];
        list_skills = [];
        final_list_skill = []
        
        #O código continua, explicando no próximo passo
1. Uso o for para iterar a lista.
2. O print é por estética, posso mostrar depois.
3. Em champio = test_champions[i], eu apenas determino que a variável champions tem o valor do campeão atual que está sendo iterado, sendo assim essa variável desnecessária, é apenas para facilitar o entendimento do código.
4. lista_imagens é onde eu vou salvar todos os links que são de imagens do site, independente se são as imagens que quero ou não.
5. list_skills é onde eu vou colocar apenas os links das imagens que são relacionadas a habilidades, farei isso filtrando lista_imagens.
6. final_list_skill é onde eu vou colocar apenas os links das habilidades que eu quero sem duplicidade.

Como isso está em um for  que itera os campeões, para cada campeão eu terei listas novas.

## Agora que temos que pegar as informações de cada campeão

     htmldata = getdata("https://www.mobafire.com/league-of-legends/champion/" + test_champions[i])
        soup = BeautifulSoup(htmldata, 'html.parser') 
Eu crio uma variável chamada htmldata onde eu irei aplicar a função getdata() que criamos lá em cima.
Dentro  da função getdata passamos uma url dinâmica, que aponta para o campeão que está sendo iterado no momento.

Depois disso usamos o BeautifulSoup para fazer um parse na data que retornamos, fazer um parse é quebrar a informação para facilitar o manuseio.

## Depois que pegamos a informação de cada campeão filtramos aquelas listas declaradas previamente
Pegamos o URL de todas as imagens do site e colocamos em lista_imagens.

    for item in soup.find_all('img'):
            lista_imagens.append(item['src']);


Filtramos lista imagens e selecionamos apenas as imagens que tem "ability" na url, se sim, adicionamos em list_skills

    for i in lista_imagens:
            if "ability" in i:
                list_skills.append(i);

Após isso temos as urls de todas as habilidades do campeão escolhido, porém muitas são repetidas, então precisamos remover os duplicados.

    final_list_skill = list(dict.fromkeys(list_skills))
Agora sim tenho uma lista contendo os links das 4 habilidades do campeão "i".

## Após isso, temos que salvar as imagens

    for j in range(len(final_list_skill)):
        Image_url ="https://www.mobafire.com/" + final_list_skill[j];
        im = Image.open(requests.get(Image_url, stream=True).raw);
        im.save(r"C:\Users\Guilherme\Desktop\Projetos\LolScrap\\" + champion + "_a_" + str(j) + ".png");

1. Pegamos cada url que se encontra na final_list_skill (lista que contém somente as urls das 4 habilidades) 
2. Depois disso usamos o PIL e o Request para pegarmos as informações
3. Por último salvamos cada imagem como um nome diferente, porém padronizado.

## Limpando as listas
Para garantir que eu limpo cada uma das listas eu utilizo a função clear()

     lista_imagens.clear();
     list_skills.clear();
     final_list_skill.clear();

## Código inteiro

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

## Conclusão
Gostei muito de fazer o projeto, além de ser interessante ele me poupou bastante tempo que eu pude usar para escrever este artigo.
Se você não percebeu mas a capa do artigo é o projeto rodando.
Se você achou interessante, favor curtir pois estará me ajudando.
