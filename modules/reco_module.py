# Module: reco
# Description: Show all Reco information.
# Usage: !reco 
# Dependencies: os

import  asyncio, configs


async def reco(ctx,client):
    await ctx.send(f"Gathering information from **{client.user.name}**...")
    await ctx.send("Testing reco")

    print(f"Server count:{client.guilds}")


    


