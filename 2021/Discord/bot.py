import os
import discord
from discord.ext import commands
from random import randrange

TOKEN = 'NzU4Mzg5Mjk0ODU5MTU3NTQ1.X2uPEg.GOjLJZoMdJdmfNlvs5eHV9eZL_U'
admins = [248212736578682890]

welcome_1="""
???: "Huch! Was macht ihr denn hier? Wie seid ihr auf mein Schiff gekommen? Wo sind wir jetzt schon wieder gestrandet?"
Du: "Wir sind Studierende der TU-Darmstadt! Und wir sind durch irgendeine Anomalie in unserem Fachschaftsraum hierhergekommen. Mit wem haben wir das Vergnuegen?"
Cpt. Kirk: "Ich bin Captain James Pike Tiberius Picar Kirk. Es freut mich euch kennenzulernen. Wir sind also schon wieder auf der Erde und noch dazu wieder in der TU-Darmstadt gelandet. Irgendwas muss noch immer nicht mit unserem Schiff stimmen..."
Cpt. Kirk: "Seufts..."
Du: "Schon wieder?"
Cpt. Kirk: "Ja, wir sind vor einiger Zeit erst hier gestrandet und waren dann in eurem Lager, dem LZI, glaube ich, um einen Phasen Impuls Generator abzuholen."
Du: "Lager? Das LZI ist kein Lager! Es ist ein Lernzentrum fuer die Studierenden!"
Cpt. Kirk: "Lernzentrum? Welches Jahr haben wir?"
Du:  "2021?"
"""
welcome_2="""
Cpt. Kirk: "* murmelnd *: Was? Das kann nicht sein! Eben war es doch noch ein Lagerzentrum. Und die Zeit stimmt auch... Es sei denn... Aber nein, das waere laecherlich..."
Du:  "Was kann nicht sein?"
Cpt. Kirk: "Nun, wir waren erst vor kurzem hier, in der TU Darmstadt... Allerdings war dort alles ein wenig anders... nicht so... pixelig und alles wurde anders betitelt... Wie gesagt, es ist ein wenig seltsam. Wir sind uns selbst noch nicht ganz sicher, ob wir wissen was hier vor geht. Waere es euch moeglich euch ein wenig in der TU umzusehen und uns darueber zu informieren, ob ihr hier irgendetwas Seltsames bemerkt? "
Du:  "Aber wir sind doch erst Erstsemester, wir kennen uns doch hier selbst noch fast gar nicht aus!"
Cpt. Kirk: "Aber ihr gehoehrt doch zur TU, oder?"
Du:  "Ja, dass schon..."
Cpt. Kirk: "Das reicht mir schon! Solange ihr zur TU gehoert, muesst ihr den Ort doch so oder so kennenlernen, da ist es mehr eine Win-Win-Situation: Ihr lernt die TU kennen und wir bekommen Infos!"
Du:  "Nagut, also wieso auch nicht... Habt ihr den eine Idee wo wir mit der Suche anfangen koennten?"
Cpt. Kirk: "Lasst mich ueberlege: Ich glaube es waere ganz gut an der Stelle zu starten, wo auch unsere Reise zur TU begann. Ich kann mich nur nicht mehr an diesen Namen erinnern. Es war irgendetwas... mit einem Vogel... und dort konnte man etwas namens 'Mentorensystem' finden. Vielleicht hilft euch das ja!"
"""

hint5_opt ="""
Cpt. Spock: "Und, war die Suche erfolgreich?"
Du:  "(...)"
Cpt. Spock: "Aha, sehr Interessant und auf der anderen Seite sehr beunruhigend. Denn warum sollten Transkripte unserer Logbucheintraege sich auf einem Rechnersystem hier in der TU befinden. Ich werde einmal mir unserem Techniker reden muessen ob es in den letzten Stunden einige Dataleaks gegeben hat... " 
Cpt. Spock: "Aber die Sache mit der Katze... Sehr seltsam. Ja, wir hatten nachdem wir zum LZI aufgebrochen waren kurz den Kontakt zu einem unserer Leute verloren, aber ich hatte mir nicht mehr viel dabei gedacht, da er vor allem auch kurz darauf wieder aufgetaucht ist. Zwar ein wenig blass, wie ich zugeben muss, aber unversehrt. "
Cpt. Spock: "Wie jetzt aber weiter? Um ehrlich zu sein haben wir ausser diesen Logfiles keine weiteren Hinweise. Wie waere es wenn ihr einmal versucht herauszufinden was es mit diesem Tier auf sich hat? Die ganze Angelegenheit ist noch nicht so lange her, eventuell findet ihr ja noch eine neue Spur."

"""

hint5 = """ 
Cpt. Spock: "Was habt ihr denn da fuer ein Teil gefunden? Das sieht ja aus, ja, wie ein Anker! Aber es wirkt nicht wie ein gewoehnlicher Anker... Wartet, ich messe das kurz nach." 
Cpt. Spock: "Ja, zweifelslos, von diesem Objekt geht eine starke molekulare Quasarkraft aus. Wenn auch die Geraete ihm auch noch ein noch verborgenes, unbestimmtes Potential bescheinigen."
Cpt. Spock: "Zu meinem Leidwesen muss ich aber zugeben kein Experte auf dem Bereich der praktischen Ankerologie zu sein. Jedoch der Dozent, welchen wir bei unserm ersten Besuch hier, beziehungsweise auf der anderen Version der Erde, getroffen haben schien ein Fachmann fuer angewandte interdimensionale Programmierung, der haertesten aller modernen Disziplinen, zu sein. Falls auch in diesem Universum eine Version von ihm existiert, koennte diese uns ja vielleicht weiterhelfen. "
Cpt. Spock: "Nur wo sollen wir ihn finden... Beim letzten Mal hatten wir den Kontakt zu ihm ueber das offizielle Abschlussportal der Fachschaft aufgenommen. Basierend auf der Theorie von Soong gehe ich davon aus, das die Divergenz zwischen den Welten nicht gross genug sein sollte um diesen generellen Eintrittspunkt beeinflussen zu koennen."
"""

hint7 = """ 
Cpt. Spock: "Ah! Stimmt, genau, 'Goessling' war sein Name gewesen. Und, habt ihr mit ihm gesprochen? "
Du: "(...)", 
Cpt. Spock: "Interessant! Ich hatte bereits laenger den Verdacht gehabt das hier etwas in dieser Welt nicht stimmt. Diese Beobachtung von einem Experten noch einmal bestaetigt zu bekommen verleiht dem ganzen natuerlich eine gewisse Dringlichkeit dadurch. Nun, aber was sind nun unserer naechsten Schritte? Also zunaechst waere es hilfreich diesen Kurs ausfindig zu machen. Als Anhaltspunkt haben wir bisher nur das er sich auf der die Informatik-Lernplatform befindet... Ich glaube wir werden nicht drum herum kommen uns dort einfach ein wenig nach verdaechtigen Kursen umzusehen. "
Cpt. Spock: "Zusaetzlich werden wir aber auch ein Passwort brauchen, um den Anker dort platzieren zu koennen. Hmm... Also wenn ich ein verrueckter Dr. waere wuerde ich meine Geheimnis natuerlich in meinem Geheimversteck aufbewahren. Warum versucht ihr nicht dem letzten Hinweis von Herr Goessling nach zu gehen? Ihr muesstet nur aus diesem Raetsel den Sinn ziehen, aber ich bin mir sicher, solch intelligente Studenten wie ihr schafft das mit Leichtigkeit! "
"""

rand_txt1 ="""
"USS Enterprise Kommunikationsleitstelle, mit wem haben wir das Vergnügen?"
"Wer... wer wollen sie nochmal sein? Entschuldigung, aber wir sind hier aktuell sehr ausgelastet."
"Kommen sie bitte wieder wenn sie ein wichtiges Anliegen haben..."
"""

rand_txt = [rand_txt1]

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
		if is_similar(message.content ,'krach') or is_similar(message.content ,'rumms'):
			await message.channel.send(welcome_1)
			await message.channel.send(welcome_2)
		elif is_similar(message.content ,'katz'):
			await message.channel.send(hint5_opt)
		elif is_similar(message.content,'anker'):
			await message.channel.send(hint5)
		elif is_similar(message.content, 'goessling') or is_similar(message.content, 'gössling'):
			await message.channel.send(hint7)
		elif is_similar(message.content, '!!') or is_similar(message.content, "hilf") or is_similar(message.content, "helf"):
			await message.channel.send(rage)
		else:
			await message.channel.send(rand_txt[randrange(len(rand_txt))])

bot.run(TOKEN)
