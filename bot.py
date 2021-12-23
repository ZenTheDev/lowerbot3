from os import system, listdir, path, environ
from re import split
from random import choice as rchoice
from traceback import print_exc
from requests import get
from asyncio import TimeoutError
from _thread import start_new_thread as start_thread
import os

system('')
env = environ.get("BOT_TOKEN")
question_number = 1

try:
    import discord

    class Functions:
        @staticmethod
        def URLStatus(value) -> bool:
            request = get(value)
            if request.status_code == 200:
                return True
            return False

    class Logging:
        @staticmethod
        def LogCommand(com, msg):
            print(f'    \033[33m~\033[0m\033[36m{msg.author}\033[0m: \033[36m{com}\033[0m> \033[34m{msg.content}\033[0m')

        @staticmethod
        def LogMessage(msg):
            print(f'\033[36m{msg.author}\033[0m: \033[34m{msg.content}\033[0m')

    class LowerBot3(discord.Client):
        async def on_ready(self):
            print('Logged in as: ', self.user)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='for \'l3!\'...'))

        async def on_message(self, message):  # noqa
            author = message.author
            content = message.content.lower()
            send = message.channel.send  # noqa
            if author.bot:
                return
            elif content == 'l3!ping':
                Logging.LogCommand('Ping', message)

                pingEmbed = discord.Embed(title='🏓 Pong', description=f'Requested by {author}', color=0x3E9AEA)
                pingEmbed.add_field(name='Ping', value=f'{round(client.latency * 1000)}ms', inline=False)
                await send(embed=pingEmbed)
            elif content == 'l3!help':
                Logging.LogCommand('Help', message)

                helpEmbed = discord.Embed(title='Commands', description=f'Requested by {author}', color=0x3E9AEA)
                helpEmbed.add_field(name='🤖 Main Commands', value='**l3!help:** Gives you this embed\n' + '**l3!ping:** Returns the bot client\'s ping\n' + '**l3!info:** Returns info about the author and guild\n' + '**l3!status [url]:** Returns the status of a URL')
                helpEmbed.add_field(name='📷 Server Utilities', value='**l3!ban [user] <reason>:** Bans a user from the guild')
                helpEmbed.add_field(name='📷 Image Commands', value='**l3!cat:** Returns an image of a cat\n' + '**l3!dog:** Returns an image of a dog')
                helpEmbed.add_field(name='🎮 Fun Commands', value='**l3!murder [user]:** Murders somebody\n' + '**l3!rps:** Plays Rock Paper Scissors')
                await send(embed=helpEmbed)
            elif content.startswith('l3!status'):
                try:
                    Logging.LogCommand('Status', message)

                    args = split(' ', content)[1]
                    try:
                        if Functions.URLStatus(args):
                            statusEmbed = discord.Embed(title='Website Status', description=f'Requested by {author}',
                                                        color=0x3E9AEA)
                            statusEmbed.add_field(name='Status of *' + args + '*',
                                                  value=args + ' is currently up.')
                            await send(embed=statusEmbed)
                        else:
                            statusEmbed = discord.Embed(title='Website Status', description=f'Requested by {author}',
                                                        color=0x3E9AEA)
                            statusEmbed.add_field(name='Status of *' + args + '*',
                                                  value=args + ' is currently down.')
                            await send(embed=statusEmbed)
                    except:
                        statusEmbed = discord.Embed(title='Website Status', description=f'Requested by {author}',
                                                    color=0x3E9AEA)
                        statusEmbed.add_field(name='Status of *' + args + '*',
                                              value=args + ' is currently down.')
                        await send(embed=statusEmbed)
                except:
                    await send('Please enter proper arguments')
            elif content == 'l3!cat':
                Logging.LogCommand('Cat', message)

                catEmbed = discord.Embed(title='Random Cat', description='Images are from [r/Cats](https://www.reddit.com/r/cats/) and [r/catselfies](https://www.reddit.com/r/catselfies/)', color=0x3E9AEA)
                random_file = str(rchoice(listdir(path.dirname(__file__) + 'Cats/')))
                file = discord.File('Cats/' + random_file, filename='image.jpeg')
                catEmbed.set_image(url='attachment://image.jpeg')
                await send(embed=catEmbed, file=file)
            elif content == 'l3!dog':
                Logging.LogCommand('Dog', message)

                dogEmbed = discord.Embed(title='Random Dog', description='Images are from [r/dogpictures](https://www.reddit.com/r/dogpictures/) and [r/doggos](https://www.reddit.com/r/doggos/)', color=0x3E9AEA)
                random_file = str(rchoice(listdir(path.dirname(__file__) + 'Dogs/')))
                file = discord.File('Dogs/' + random_file, filename='image.jpeg')
                dogEmbed.set_image(url='attachment://image.jpeg')
                await send(embed=dogEmbed, file=file)
            elif content == 'l3!info':
                Logging.LogCommand('Info', message)

                infoEmbed1 = discord.Embed(title='Information (Author)', description=f'Requested by {author}', color=0x3E9AEA)
                infoEmbed1.add_field(name='Author Info', value=f'Name: *{author}*\n' + f'ID: *{author.id}*\n' + 'Avatar: ', inline=True)
                infoEmbed1.set_image(url=(str(author.avatar_url) + '?size=200'))
                infoEmbed2 = discord.Embed(title='Information (Guild)', color=0x3E9AEA)
                infoEmbed2.add_field(name='Guild Info', value=f'Name: *{message.guild.name}*\n' + f'ID: *{message.guild.id}*\n' + 'Icon: ', inline=True)
                infoEmbed2.set_image(url=(str(message.guild.icon_url) + '?size=200'))
                infoEmbed2.set_footer(text='Bot made by Zen#0613', icon_url=self.user.avatar_url)
                await send(embed=infoEmbed1)
                await send(embed=infoEmbed2)
            elif content.startswith('l3!murder '):
                try:
                    Logging.LogCommand('Murder', message)
                    death = [
                        'insulted Zen',
                        'insulted Lowerbot',
                        'insulted Crow',
                        'ate too much ass',
                        'loli fart sex',
                        'got came on by a dog and drowned',
                        'got cat cum all over them and drowned',
                        'got a cat penis stuck in their ass and died',
                        'drowned in piss',
                        'sucked a little bit too much puppy cock',
                        'being a step-sister, got stuck, and their big brother came in to \'help\'',
                        'fucked a dog, but the dog was too tight and so their dick got ripped off',
                        'ate feces',
                        'became monki',
                        'disrespected Lowerbot\'s sexiness',
                        'got impaled by Zen\'s massive cock',
                        'had sex with an actual crow instead of Crow',
                        'got their leg\'s broken because people thought they were Mick',
                        'accidentally revealed their token',
                        'got scammed because they wanted free robux',
                        'shat too hard and died',
                        'supported Mick',
                        'didn\'t have enough sex',
                        'peed and farded and shidded in their pant',
                        'pooped out cum',
                        'was named Yoshikage Kira. They were 33 years old. Their house is in the northeast section of Morioh, where all the villas are, and they were not married. They worked as an employee for the Kame Yu department stores, and got home every day by 8 PM at the latest. they didn\'t smoke, but they occasionally drank',
                        'fucked a snapping turtle',
                        'refused sex from zen',
                        'died',
                        'died sexually',
                        'had sex, but it wasn\'t sexual or anything',
                        'reactivated lowerbot 1, but in doing so, fucking died',
                        'reactivated lowerbot 2, but in doing so, fucking died',
                        'has big booby minceraft sex',
                        'didn\'t subscribe to Zen\'s youtube channel',
                        'didn\' watch enough Pewdiepie',
                        'knew what happened to dr. disrespect',
                        f'opened cmd and typed `taskkill /IM "{(message.mentions[0]).name}" /F`',
                        'had sexy sex with big boob ps5 hot sex shrexy fiona donkey moment keanu reddit 520 bro, investigate 311',
                        'had sexy sex with big boob ps5 hot sex shrexy fiona donkey moment keanu reddit 520 bro, investigate 311',
                        'had sexy sex with big boob ps5 hot sex shrexy fiona donkey moment keanu reddit 520 bro, investigate 311',
                        '\\*insert death message here\\*',
                        'stole a rednecks beer',
                        'died of chugging cum too fast',
                        'met chris hansen',
                        'went to brazil',
                        'was sent to brazil and was gangbanged to death',
                        'actually quite enjoyed it in brazil',
                        'caught corona',
                        'didn\'t wear their face mask',
                        f'got coughed on by {author.mention}',
                        'didn\'t play lowergame',
                        'got hit by a mitsubishi mini active urban sandal 1995',
                        'subscribed to cocomelon',
                        'got pinged and just had to suck on their thumb and cwy all nitesy longy because they shidded in their pants',
                        'questioned the death message, \'User, got hit by a mitsubishi mini active urban sandal 1995\'',
                        'didn\'t like it here in brazil',
                        'chugged too much horse piss',
                        'slurped up too much horse cum',
                        f'tried to have premarital sex and {author.mention} blew them up',
                        'got CBTed too hard and died',
                        'tried to use an ant mound as a fleshlight, and didn\'t realize it was a bullet ant mound',
                        'failed the vibe check',
                        'went passed the integer limit',
                        'watched Amy Schumer',
                        'posted memes in general',
                        'was pinged and got so mad they shit themselves and started cwying wike a wittwe baby boi boohoo shit turd poopy in their diaper cuz they are a totaw baby about getting pingwed boohoo ):',
                        'was pinged and got so mad they shit themselves and started cwying wike a wittwe baby boi boohoo shit turd poopy in their diaper cuz they are a totaw baby about getting pingwed boohoo ):',
                        'didn\'t know kanna is underaged, and masturbating to kanna hentai',
                        'was a boomer on the internet',
                        'got offended because jschlatt laughed at blackface',
                        'throat fucked a snapping turtle',
                        'POSSESSIVE_MARKER_NATURAL family caught them fucking the dog',
                        'got sent back to the times of middle english',
                        'ðrâg cuman wægn of middeld¯æl Englaland (was sent back to middle england)',
                        'created a boolean pointer with a size of 8 bytes despite the fact that it could have been a single byte',
                        'er könnte diese Tod nicht Meldung lesen',
                        'はこれ伝言を読んでできなかったよ',
                        'はこれ伝言を読んでできなかったよ',
                        'はこれ伝言を読んでできなかったよ',
                        'はこれ伝言を読んでできなかったよ',
                        'はこれ伝言を読んでできなかったよ',
                        'はこれ伝言を読んでできなかったよ',
                        'drank localized beer in a country that ate and drank tape worms',
                        'shat out blood',
                        'came, but in french',
                        'shitted & peepeed & coomed',
                        'fucked a praying mantis',
                        'was a dog in jojo no kimyou na bouken',
                        'bought a blue yeti but then didn\'t have the confidence to reveal their voice',
                        'acted like a little bitch because zen made an offensive joke',
                        'was under 13 on the lowercase discord server',
                        'went into an nsfw channel and openly told everybody they were underaged',
                        'was too cringey and zen kicked them',
                        'ate a s̶̡̬̉h̵̹̓̓i̷͖̐́͘͘͝ṉ̷̝̕ǫ̶̻̫̖͎̊̕͝p̵̤͍̋̓e̸͇͍̝̰͂̐̍͛d̸̞̘͉̣͎̽̅̆a̶̹̖̰̅̈́ḳ̴̢̖͇̒̋̐ợ̸̩͐͌̚̕ų̷̳̪̟̺̃̅n̵̪̐ȩ̷̤͌͒̕͜p̷͖͍̲̀͂͘p̴͕̺̕e̷͈͕̗̿̾͘n̵̖̰̣̜̹͌̕s̵̛̹̰h̴͚̥̃͌e̶̞̼̤̟͐̀r̷̡̹̱͓̬͋̑̇ḏ̶̝̙̦̗̓ḛ̸͎̻̤̦̏͛n̴̟̖̟̳̥͌̈́͛̇͘ fruit',
                        'Believed in JeSus, but jeSus was the imposter',
                        'please help zen holds me hostage in his basement',
                        'played amogus',
                        'didn\'t play minecraft',
                        'unironically liked fortnite',
                        'accidentally made arashi drink distilled water instead of spring water, which made zen so made he flooded their guts with cum',
                        'took that bruh pill',
                        'smoked that good kush',
                        'went gentle into that good night',
                        'listened to zen\'s voice then fucking exploded',
                        'was a furry on tiktok who liked fortnite and had \'undiagnosed depression\'',
                        'liked amogus and for fuck\'s sake I FUCKING HATE AMONG US ITS SO FUCKING ANNOYING "SUS SUS YOU SUS" LIKE BRO SHUT THE FUCK UP YOU ANNOYING LITTLE SHIT NOBODY CARES ABOUT YOUR STUPID FUCKING GAME. I\'M SICK AND TIRED OF HEARING "SUS SUS YOU SUS" EVERY FUCKING TIME I BREATHE. PLEASE SHUT THE FUCK UP'
                    ]
                    if rchoice(death).startswith('POSSESSIVE_MARKER_NATURAL'): await send(f'{(message.mentions[0]).mention}\'s ' + rchoice(death).replace('POSSESSIVE_MARKER_NATURAL ', '') + '.')
                    elif rchoice(death).startswith('POSSESSIVE_MARKER_UNNATURAL_PLURAL'): await send(f'{(message.mentions[0]).mention}\' ' + rchoice(death).replace('POSSESSIVE_MARKER_UNNATURAL_PLURAL ', '') + '.')
                    elif rchoice(death).startswith('POSSESSIVE_MARKER_UNNATURAL_NAME'): await send(f'{(message.mentions[0]).mention}\' ' + rchoice(death).replace('POSSESSIVE_MARKER_UNNATURAL_NAME ', '') + '.')
                    else: await send(f'{(message.mentions[0]).mention}, ' + rchoice(death) + '.')
                except:
                    await send('Please enter proper arguments')
            elif content == 'l3!rps':
                Logging.LogCommand('Rock Paper Scissors', message)

                try:
                    rpsEmbed = discord.Embed(title='Rock Paper Scissors', description=f'Requested by {author}', color=0x3E9AEA)
                    rpsEmbed.add_field(name='Bot choice', value='?', inline=True)
                    rpsEmbed.add_field(name='Your choice', value='?', inline=True)
                    rpsEmbed.set_footer(text='React with 🗿, 📄, or ✂ to play')
                    rpsMessage = await send(embed=rpsEmbed)
                    await rpsMessage.add_reaction('🗿')
                    await rpsMessage.add_reaction('📄')
                    await rpsMessage.add_reaction('✂')

                    def check(reaction, user):
                        if user == author and str(reaction.emoji) == '🗿':
                            return True
                        if user == author and str(reaction.emoji) == '📄':
                            return True
                        if user == author and str(reaction.emoji) == '✂':
                            return True
                        else:
                            return False

                    def getChoice(reaction, user) -> str:
                        if user == author and str(reaction.emoji) == '🗿':
                            return '🗿'
                        if user == author and str(reaction.emoji) == '📄':
                            return '📄'
                        if user == author and str(reaction.emoji) == '✂':
                            return '✂'
                        else:
                            return '?'
                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
                    except TimeoutError:
                        await send(':thumbsdown: Timed out, you took too long! ):')
                    else:
                        continueBool = True
                        _options = [
                            '🗿',
                            '📄',
                            '✂'
                        ]
                        choice = getChoice(reaction, user)
                        if choice == '?':
                            continueBool = False
                        if continueBool:
                            botChoice = rchoice(_options)
                            newRpsEmbed = discord.Embed(title='Rock Paper Scissors', description=f'Requested by {author}', color=0x3E9AEA)
                            newRpsEmbed.add_field(name='Bot choice', value=botChoice, inline=True)
                            newRpsEmbed.add_field(name='Your choice', value=choice, inline=True)
                            newRpsEmbed.set_footer(text='React with 🗿, 📄, or ✂ to play')
                            await rpsMessage.edit(embed=newRpsEmbed)
                            if choice == botChoice:
                                await send('We\'re tied!')
                            elif choice == '🗿' and botChoice == '📄':
                                await send('You lose!')
                            elif choice == '🗿' and botChoice == '✂':
                                await send('You win!')
                            elif choice == '📄' and botChoice == '🗿':
                                await send('You win!')
                            elif choice == '📄' and botChoice == '✂':
                                await send('You lose!')
                            elif choice == '✂' and botChoice == '📄':
                                await send('You win!')
                            elif choice == '✂' and botChoice == '🗿':
                                await send('You lose!')
                        else:
                            await send('Please send a proper emoticon')
                except:
                    await send('Please enter proper arguments')
                    print_exc()
            elif content.startswith('l3!ban '):
                ban_members = [p for p in author.guild_permissions if p[0] == "ban_members"][0][1]
                if ban_members:
                    try:
                        Logging.LogCommand('Ban', message)

                        member = message.mentions[0]
                        try:
                            if len(content.split(' ', 2)[2]) != 0:
                                reason = content.split(' ', 2)[2]
                            else:
                                reason = None
                        except:
                            reason = None
                        if member is None or member == author:
                            await send('You cannot ban yourself')
                            return
                        if reason is None:
                            reason = 'an unspecified reason'
                        msg = f'You have been banned from **{message.guild.name}** for {reason}'
                        await member.send(msg)
                        await message.guild.ban(member, reason=reason)
                        await message.channel.send(f'{member} is banned!')
                    except:
                        await send('Please enter proper arguments')
                        print_exc()
                else:
                    await send('You do not have the permissions to ban this user')
            elif content.startswith('l3!kick '):
                kick_members = [p for p in author.guild_permissions if p[0] == "kick_members"][0][1]
                if kick_members:
                    try:
                        Logging.LogCommand('Kick', message)

                        member = message.mentions[0]
                        try:
                            if len(content.split(' ', 2)[2]) != 0:
                                reason = content.split(' ', 2)[2]
                            else:
                                reason = None
                        except:
                            reason = None
                        if member is None or member == author:
                            await send('You cannot kick yourself')
                            return
                        if reason is None:
                            reason = 'an unspecified reason'
                        msg = f'You have been kicked from **{message.guild.name}** for {reason}'
                        await member.send(msg)
                        await message.guild.kick(member, reason=reason)
                        await message.channel.send(f'{member} has been kicked!')
                    except:
                        await send('Please enter proper arguments')
                        print_exc()
                else:
                    await send('You do not have the permissions to kick this user')
            else:
                Logging.LogMessage(message)

    client = LowerBot3()

    client.run(env)
except:
    print_exc()
    input()
while 1:
    pass
