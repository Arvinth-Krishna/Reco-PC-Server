# Module: reco
# Description: Show all Reco information.
# Usage: !reco 
# Dependencies: os

import  asyncio, configs


async def reco(ctx,client,discord,embeds):
    await ctx.send(f"Gathering information from **{client.user.name}**...")
    

    print(f"Server count:{client.guilds}")


    


