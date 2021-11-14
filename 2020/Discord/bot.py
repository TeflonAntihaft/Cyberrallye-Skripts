import os
import discord
from discord.ext import commands
from random import randrange
from pygame import mixer

from dotenv import load_dotenv
load_dotenv()
TOKEN = 'NzU4Mzg5Mjk0ODU5MTU3NTQ1.X2uPEg.GOjLJZoMdJdmfNlvs5eHV9eZL_U'
admins = [248212736578682890]

hint5_1="""**klick**
Hey, wer da? Ah, hi!

Stimmt, ich erinnere mich! Ich hatte das Passwort im Power Grid geändert. Wie konnte ich das nur vergessen...

Egal, gut das die Typen immer brav alles mitschreiben. Vieleicht sollte ich sicherheitshalber meine Dateien und Ordner ein bissl weniger auffällig bennen. Was hälst du von /homework oder /kamera_backup?
*Ein bisschen gruselig ist trotzdem*

Was anderes: Haste eigentlich inzwischen schon das Passwort dazu gefunden? Bin mir sicher, dass das irgendwo im Piloty noch rumfliegt... Die räumen da so selten auf, dass man da sicher noch 'n Mammut finden kann xP 

Meld dich wieder mit dem Namen und dem Passwort, wenn du es gefunden hast. Opheus wird sicher dran gehn ;)
Bye!
**klick**
"""

hint5_2 ="""**klick**
Ah, du bist es. 
Sehr gut, 'P1L0T10N0101' sieht nach einem Passwort aus, das Trinity benutzen würde. Extrem unverantwortlich von ihr, dass es nach all den Jahren immer noch im Piloty zu finden war. Ich sollte sie dringend erneut zur Sicherheitsschulung schicken.

Hast du bereits herausgefunden, wofür sie dieses Passowort überhaupt gesetzt hatte? Falls sich die Sicherheitslücken durch die ganze Tutrix ziehen sollten, kannst du wahrscheinlich auf den Seiten der jeweiligen Arbeitsgruppen alte Log-Daten finden. 

Komm mit dem Passwort von eben und dem Namen zusammen zurück zu mir, falls du etwas finden solltest.
**klick**"""

hint6 = """
**zkrrzz...**
**klick**
Wunderbar, du hast tatsächlich beide Teile gefunden. Hast du bereits versucht sie zu benutzen, um im Informatik Moodle einzubrechen?
Falls sich die Vermutung bestätigen sollte, finden wir dort sicher einen weiteren Hinweis, wie wir tiefer in die Tutrix eindringen können.

Viel Erfolg. Die Angelegnheit wird langsam heißer.
**klick**
"""
hint8 = """**klick**
Hä, wer da? Ah, du bist es! Trinity am Apparat.

whatisthetutrix.de? Lustig. Das klingt ja fast wie TU und Matrix! Aber das klingt nach einer echt heißen Spur! Ich hab das Gefühl, wir sind da ganz knapp an was Riesigem dran. Schon versucht drauf zu zugreifen?
 
What, der Server ist nicht erreichbar? Ganz sicher, dass du ne direkte, verschlüsselte Verbindung in die Tutrix hast?
Naja, aber selbst wenn... Das Teil ist sicher noch Passwort geschützt. 

Manno, wir sind soooo close das System zu zerstören. Da darf jetzt nicht an sowas oder einem crappy Password scheitern!

Veleicht findest du ja in alten Hinweisen ne Idee, mit was die Tutrix läuft, und kannst da wat ableiten. 
Aber was das Passwort angeht... Hmm, tja, sorry,hab' auch keinen Plan. Könntest ja nochmal ins Wissenarchiv der Menscheit, good ol' Google, schau'n oder so, ob da noch was heraus zu finden ist. Tut mir leid, aber da bist wohl auf dich allein gestellt...
**klick**"""
rand_txt1="""**krzrzz... krrr...**

*Nichts. Nichts als das endlose Rauschen das Äthers dringt aus dem Communicator.*"""

rand_txt2="""**klick**
Hallo, Vesuivo-Pizza's hier. Was kann ich für Sie tun?
Wie?
Sie wollten gar keine Pizza bestellen? Warum rufen sie dann überhaupt an?! Unerhört...
**klick**"""

rand_txt3="""**tschhh... tzrischh...**

*Es klingt nicht als ob der Communicator auf diese Nachricht anspringt*"""

rand_txt4="""**klick**
Jaaa, IT-Service Brunsmaier, Sie sprechen mit Jürgen. Wie kann ich Ihnen weiterhelfen? 

Ja, äh, hmm,... Haben sie mal versucht, das Gerät aus und wieder einzuschalten?

Hat nix gebracht, ja, hmm, verstehe...
Probier'n sie doch mal zum letzten Hinweis zurück zu kehren. Ja genau, den meine ich... 

Ja, keine Sorge, ich bleibe in der Leitung.
**klick** 
**tuut, tuuut, tuuuut...**"""

rand_txt = [rand_txt1, rand_txt2, rand_txt3, rand_txt4]

rage = """*Du schreist in das Gerät, aber es hilft nichts: Niemand hört deine Verzweiflung.
Und wenn doch, ist er zumindest nicht sofort gewillt darauf zu antworten...*"""


mixer.init()
mixer.music.load("dot.wav")

def is_similar(text, keyword):
	if keyword.upper().replace(" ", "") in text.upper().replace(" ", ""):
		return True
	else:
		return False

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'Willkomen in Discord, dem Kommunikationskanal der letzten, freien Informatiker, {member.name}!'
	)

@bot.command()
async def write(ctx, id, msg):
	await bot.get_user(int(id)).dm_channel.send(msg)

@bot.event
async def on_message(message):
	if message.author.id in admins and message.content[0] == '$':
		await bot.process_commands(message)
		return
	if message.author == bot.user:
		return
	if message.channel.type == discord.ChannelType.private:
		print(message.author.name + " " + str(message.author.id) + ": " + message.content)
		if is_similar(message.content ,'P1L0T10N0101') and is_similar(message.content,'Power Grid'):
			await message.channel.send(hint6)
		elif is_similar(message.content ,'P1L0T10N0101'):
			await message.channel.send(hint5_2)
		elif is_similar(message.content,'Power Grid'):
			await message.channel.send(hint5_1)
		elif is_similar(message.content, 'whatisthetutrix'):
			await message.channel.send(hint8)
		elif is_similar(message.content, '!!') or is_similar(message.content, "hilf") or is_similar(message.content, "helf"):
			await message.channel.send(rage)
			mixer.music.play()
		else:
			await message.channel.send(rand_txt[randrange(len(rand_txt))])

bot.run(TOKEN)
