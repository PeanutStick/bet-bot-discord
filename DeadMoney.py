import urllib.request
import re
import os 
import discord
import time
from random import randint
import asyncio

TOKEN = 'your token here!!!'
loop = asyncio.get_event_loop()
client = discord.Client()
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    mention = message.author.mention
    channel = client.get_channel("channel id")

    if message.author == client.user:
        return
    # 
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send("hi "+mention)
    elif message.content.startswith('!help'):
        await message.channel.send("OK "+mention+"... je te montre.\n!hello : none \n!show : la bourse\n!rusian : un jeu ou tu ne perd qu'une fois...");
    elif message.content.startswith('!rules'):
        await message.channel.send("---_Rusian_---\nUn Colt 1860 Army, une balle, la partie est finis lorsqu'elle est logé dans un crane.\n---_Black_---\nL'objectif c'est 21, trop haut tu perd, trop bas le bot l'emporte.")
    elif message.content.startswith('!show'):
        await message.channel.send("I can't show you  "+mention)
        await message.channel.send("I whill show you  "+mention)
        url = 'https://www.boursorama.com/bourse'
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        pourcents = re.findall(r'(.....)%</span>',str(respData))
        nom0 = re.findall(r'c-list-trading__item c-list-trading__item--name c-homepage-tradingboard__list-item / u-ellipsis">(.*?)</div',str(respData))
        nom1 = re.findall(r'([A-Z0-9])',str(nom0))
        for entrepr, pour in zip(nom0, pourcents):
            print(pour,entrepr [34:-30])
            kak40 = pour,entrepr [34:-30]
            await message.channel.send(kak40)
    elif message.content.startswith('!news'):
        await message.channel.send("Des news pour "+mention+" !")
    elif message.content.startswith('!black'):                                                                  #   #   #   # Black #  #  #  #
        i=0
        await message.channel.send("Je te passe deux cartes "+mention); ### deux premières cartes
        while i != 2:
            carte1 = randint(1, 10)
            couleur1 = randint(1, 4)
            if couleur1 == 1:
                couleur1 = "de pique"
            elif couleur1 == 2:
                couleur1 = "de trèfle"
            elif couleur1 == 3:
                couleur1 = "de coeur"
            else:
                couleur1 = "de carreaur"
            print(str(carte1)+couleur1)                         #carte1 a additioné 
            cartef = carte1
            await message.channel.send(str(carte1)+" "+couleur1+" pour "+mention);
            if i == 0:
                carte2 = carte1
            elif i == 1:
                somme = carte1 + carte2
            i = i+1
        await message.channel.send("Un totale de "+str(somme)+" pour "+mention+"\n!T Pour tirer\n!D pour doubler\n!R Pour rester");
        def pred(m):
            return m.author == message.author and m.channel == message.channel
        #if somme > 21:
        #    await message.channel.send("Perdu tu as"+somme);
        #    somme =30
        #else:
        try:
            msg = await client.wait_for('message', check=pred, timeout=30.0)
        except:
            await message.channel.send('Trop lent!\nRentre chez toi!')
            somme = 30
        else:
            choix = ('{0.content}'.format(msg))
            print(choix)
            if choix == "!T":
                continuer = 1
                loop.create_task(askcard(message,mention,somme,continuer))
            elif choix == "!D":
                await message.channel.send("Prêt a perdre le double ?");
                continuer = 1
                loop.create_task(askcard(message,mention,somme,continuer))
            elif choix == "!R":
                await message.channel.send("Ok voyon voir ton score\nUn totale de "+str(somme));
                #await message.channel.send("Un totale de "+str(somme));
                continuer = 0
                n = randint(15, 25)
                if n >21:
                    await message.channel.send("tu gagne! le bot a eu "+str(n)+".");
                elif n > somme:
                    await message.channel.send("Perdu, le bot a eu "+str(n)+".");
                else:
                    await message.channel.send("tu gagne! le bot a eu "+str(n)+".");
                loop.create_task(askcard(message,mention,somme,continuer))
                somme = 30
            else:
                await message.channel.send("Bha ... t'as perdu ^^'");
                somme = 30


    elif message.content.startswith('!rusian'):
        first = mention
        fichier = open("rusian.txt", "w")
        fichier.write(first+" V")
        fichier.close()
        await message.channel.send("the first player is "+mention);
        await message.channel.send("the seconde player should type !rjoin");
    elif message.content.startswith('!rjoin'):
        second = mention
        fs = open("rusian.txt", 'r')            # ouvre pour vérifie le longueur
        texte = fs.read()
        longueur=len(texte)
        fs.close()
        print(longueur)
        if longueur == 0:
            await message.channel.send("wait the first player !");
        elif longueur == 23:
            fichier = open("rusian.txt", "a")
            fichier.write("S "+second)
            fichier.close()

            fs = open("rusian.txt", 'r')            # ouvre pour vérifie le longueur
            texte = fs.read()

            fs.close()

            await message.channel.send(texte);
            print("effacé le fichier")
            fichier = open("rusian.txt", "w")
            fichier.write("")                   # éfface
            fichier.close()
            barille = randint(1, 5)
            await message.channel.send("la balle est prète\n!shoot pour tirer\n!roll pour tourné puis tirer");
            print(barille)
            tim = 10
            while barille != 0 and tim != 0:
                time.sleep(0.5)
                tim = tim - 1
                print(tim)
                if tim == 0:
                    await message.channel.send("Tu as pris trop de temps.");
            

###################################################################################################################################################
################################################################------FONCTIONS------##############################################################

async def askcard(message,mention,somme,continuer):
    while somme < 21 and continuer == 1: #signe + nombre
        carte1 = randint(1, 10)             
        couleur1 = randint(1, 4)
        if couleur1 == 1:
            couleur1 = "de pique"
        elif couleur1 == 2:
            couleur1 = "de trèfle"
        elif couleur1 == 3:
            couleur1 = "de coeur"
        else:
            couleur1 = "de carreaur"
        print(str(carte1)+couleur1)
        somme = somme + carte1
        await message.channel.send(str(carte1)+" "+couleur1+" pour "+mention+"\nUn totaleee de "+str(somme));
        continuer = 1
        if somme < 22 and continuer == 1:
            def pred(m):
                return m.author == message.author and m.channel == message.channel
            try:
                msg = await client.wait_for('message', check=pred, timeout=30.0)
            except:
                await message.channel.send('Trop lent!\nRentre chez toii!')
                #deja = 1000
                continuer = 0
            else:
                choix = ('{0.content}'.format(msg))
                print(choix)
                if choix == "!T":
                    print("continue")
                elif choix == "!D":
                    await message.channel.send("Prêt a perdre le double ?");
                    print("continue")
                elif choix == "!R":
                    await message.channel.send("Ok voyon voir ton score \nUn trotale de "+str(somme));
                    continuer = 0
                    n = randint(15, 25) #resultat du BOT
                    if n > 21:
                        await message.channel.send("tu gagne! le bot a eu "+str(n)+".");
                    elif n > somme:
                        await message.channel.send("Perdu, le bot a eu "+str(n)+".");
                    else:
                        await message.channel.send("tu gagne! le bot a eu "+str(n)+".");
                    loop.create_task(askcard(message,mention,somme,continuer))
                    somme = 30
                    continuer = 0
                    deja = 1000
                else:
                    await message.channel.send("Bha ... je pige pas dsl t'as perdu ^^'");
        else:
            await message.channel.send("perdu!");

###################################################################################################################################################

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
