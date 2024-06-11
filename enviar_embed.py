import discord
from discord.ext import commands

# Token do seu bot
TOKEN = 'MTE5NzU5NDM1MTQ1OTY1MTcwNw.Gfo_Bq.YDJiYbdDe-1sITIBIx9--fNNfTbs_xHGiv9y9I'

# Definindo as intenções do bot
intents = discord.Intents.default()
intents.messages = True  # Ativar a intenção de receber mensagens
intents.message_content = True

# Inicialização do bot com as intenções
bot = commands.Bot(command_prefix='!', intents=intents)

# ID do canal onde você deseja monitorar as mensagens
canal_id = 1249607793833676893

# Evento de inicialização do bot
@bot.event
async def on_ready():
    print(f'Bot iniciado como {bot.user}')

# Evento para monitorar as mensagens no canal especificado
@bot.event
async def on_message(message):
    # Verifica se a mensagem foi enviada no canal desejado e não foi enviada pelo bot
    if message.channel.id == canal_id and not message.author.bot:
        # Verifica se a mensagem contém anexos ou URLs
        if message.attachments or 'http' in message.content:
            # Cria um embed para a mensagem privada
            embed_private = discord.Embed(
                description=f'> **Ok, Espere a análise do seu vídeo e iremos te dar o Resultado :kissing_heart:**\n{message.author.mention}',
                color=discord.Color.red()
            )
            embed_private.set_footer(text='Produzido por thebigbadass')

            # Define a imagem do embed
            embed_private.set_thumbnail(url='https://i.ibb.co/ZzL6982/Fashion-Z-BOT.png')

            # Envia o embed privado ao autor
            await message.author.send(embed=embed_private)
        else:
            # Cria um embed para a mensagem privada
            embed_private = discord.Embed(
                description=f'> **Apenas vídeos! Certifique-se de enviar apenas vídeos :rage:**\n{message.author.mention}',
                color=discord.Color.red()
            )
            embed_private.set_footer(text='Produzido por thebigbadass')

            # Define a imagem do embed
            embed_private.set_thumbnail(url='https://i.ibb.co/ZzL6982/Fashion-Z-BOT.png')

            # Exclui a mensagem original
            await message.delete()
            # Envia o embed privado ao autor
            await message.author.send(embed=embed_private)

    # Permite que outros comandos continuem funcionando normalmente
    await bot.process_commands(message)

# Rodando o bot
bot.run(TOKEN)
