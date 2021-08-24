import encryption

decode = encryption.Decoder(
    ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "o", "ó", "p", "r", "s",
     "ś", "t", "u", "v", "w", "x", "y", "z", "ź", "ż", "A", "Ą", "B", "C", "Ć", "D", "E", "Ę", "F", "G", "H", "I", "J",
     "K", "L", "Ł", "M", "N", "O", "Ó", "P", "Q", "R", "S", "Ś", "T", "U", "V", "W", "X", "Y", "Z", "Ź", "Ż", "0", "1", "2",
     "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "/", "\\",
     ",", ".", "?", "|", ":", ";", "[", "]", "{", "}", "`", "~", " "])


def compilePyBot(commandList, prefix, tokenEncrypted, statusText):
    with open("bot.py", "w") as f:
        f.write(f"import discord\nfrom discord.ext import commands\nbot = commands.Bot(command_prefix='{prefix}'"
                f")\n\n\n@bot.event\nasync def on_ready():\n\tawait bot.change_presence(activity=discord.Game("
                f"'{statusText}'))\n\tprint('Logged in as')\n\tprint(bot.user.name)\n\tprint("
                f"bot.user.id)\n\tprint('------')\n\n\n")
        f.close()

    with open("bot.py", "a") as f:
        for cmd in commandList:
            cmdName = cmd.split(': ')[0]
            cmdMsg = cmd.split(': ')[1]
            f.write(f"@bot.command()\nasync def {cmdName}(ctx):\n\tawait "
                    f"ctx.send('{cmdMsg}')\n\n")

        f.write(f"bot.run('{decode.decode(tokenEncrypted)}')")
        f.close()
