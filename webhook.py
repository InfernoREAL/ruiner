from discord_webhook import DiscordWebhook, DiscordEmbed


title = input("Title: ")
description = input("Description:")
url = input("Webhook URL:")

webhook = DiscordWebhook(url = url)
embed = DiscordEmbed(title= title, description= description)
webhook.add_embed(embed)
webhook.execute()
