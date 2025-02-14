

from logging import fatal
import discord, configs


def safe_int(value, default):
    try:
        return int(value, 0)  # Automatically detects base (hex, decimal, etc.)
    except (ValueError, TypeError):
        return default  # Fallback to a valid default value

colorforCommonMsg = safe_int(configs.EMBEDS_COLOR, 0xf5c816)
colorforWaitingMsg = safe_int(configs.SECONDARY_EMBEDS_COLOR, 0xF19306)
colorforLockMsg=0xf5c816
colorforShutdownMsg=0xeb0606
colorforHibernateandSleep=0x52e924
colorforError=0xF70000


class recoEmbeds:

    nullFieldName="\u200B"
    banner= f" ┃ **[GitHub](https://bit.ly/recoserver)** ┃ **[Discord](https://discord.gg/THwBTUHnwZ)** ┃ **[YouTube](https://bit.ly/recoYoutube)** ┃ **[Instagram](https://bit.ly/GAKventrueIG)** ┃"
    
    def color(x):
        colors = {
        'colorforCommonMsg': colorforCommonMsg,
        'colorforWaitingMsg': colorforWaitingMsg,
        'colorforLockMsg': colorforLockMsg,
        'colorforShutdownMsg': colorforShutdownMsg,
        'colorforHibernateandSleep': colorforHibernateandSleep,
        'colorforError':colorforError
    }
        return colors[x]

    async def recoOnline(ctx,txt,authorName,authorURL,authorIcon,color=colorforCommonMsg):
        embed=discord.Embed(  description= txt ,color=color)
        embed.set_author(name=authorName, url=authorURL, icon_url=authorIcon)
        embed.add_field(name=recoEmbeds.nullFieldName,value=recoEmbeds.banner+"\n ",inline=False)

        msg=await ctx.send(embed=embed)
    
    async def msg(ctx,txt,color=colorforCommonMsg):
        embed=discord.Embed(  description= txt ,color=color)
        msg=await ctx.send(embed=embed)
        return msg

    
    async def editMsg(ctx,msg,editmsg,color=colorforCommonMsg):
        embed=discord.Embed(  description= editmsg ,color=color)
        await msg.edit(embed=embed)
    
    async def msgwithAttachment(ctx,txt,file,color=colorforCommonMsg):
        embed=discord.Embed(description= txt ,color=color)
        msg=await ctx.send(embed=embed,file=file)
        return msg
    async def editMsgwithAttachment(ctx,msg,editmsg,color=colorforCommonMsg):
        embed=discord.Embed(description= editmsg ,color=color)
        msg=await msg.edit(embed=embed)
        

    async def recoMmsg(ctx,txt,authorName,authorURL,authorIcon,color=colorforCommonMsg,fieldname1="",fieldvalue1="",fieldname2="",fieldvalue2="",fieldname3="",fieldvalue3="",fieldname4="",fieldvalue4="",fieldname5="",fieldvalue5="",fieldname6="",fieldvalue6="",fieldname7="",fieldvalue7="",fieldname8="",fieldvalue8="",fieldname9="",fieldvalue9="",fieldname10="",fieldvalue10="",fieldname11="",fieldvalue11="",fieldname12="",fieldvalue12=""):
        embed=discord.Embed(  description= txt ,color=color)
        embed.set_author(name=authorName, url=authorURL, icon_url=authorIcon)
        if fieldname12!=None:
           embed.add_field(name=fieldname12,value=fieldvalue12,inline=False)
        embed.add_field(name=fieldname1,value=fieldvalue1,inline=True)
        embed.add_field(name=fieldname2,value=fieldvalue2,inline=False)
        embed.add_field(name="\u200B",value="> **[Check Out! Reco Mobile App  🤩](https://bit.ly/RecoApp)**\n\u200B",inline=False)
        if fieldname10!=None:
           embed.add_field(name=fieldname10,value=fieldvalue10,inline=True)
           embed.add_field(name=fieldname11,value=fieldvalue11,inline=True)
           embed.add_field(name="\u200B",value="> **[🔗 Share Reco with your F.R.I.E.N.D.S ✨](https://www.linkedin.com/posts/arvinth-krishna-g-b7638967_arvinth-krishnareco-pc-server-activity-6781461500591788032-bv1M)**\n\u200B",inline=False)

        if fieldname3!=None:
           embed.add_field(name=fieldname6,value=fieldvalue6,inline=True)
           embed.add_field(name=fieldname7,value=fieldvalue7,inline=True)
           embed.add_field(name=fieldname8,value=fieldvalue8,inline=True)
        if fieldname9!=None:
            embed.add_field(name=fieldname9,value=fieldvalue9,inline=True)
        if fieldname3!=None:   
            embed.add_field(name=fieldname3,value=fieldvalue3,inline=True)
        embed.add_field(name=fieldname4,value=fieldvalue4,inline=True)
        
        
        embed.add_field(name=fieldname5,value=fieldvalue5,inline=False)
        await ctx.send(embed=embed)


    
    async def recoVersionEmbed(ctx,txt,authorName,authorURL,authorIcon,color=colorforCommonMsg,fieldname1="",fieldvalue1="",fieldname2="",fieldvalue2="",fieldname3="",fieldvalue3="",fieldname4="",fieldvalue4="",fieldname5="",fieldvalue5="",fieldname6="",fieldvalue6="",fieldname7="",fieldvalue7="",fieldname8="",fieldvalue8="",fieldname9="",fieldvalue9="",fieldname10="",fieldvalue10="",fieldname11="",fieldvalue11="",fieldname12="",fieldvalue12=""):
        embed=discord.Embed(  description= txt ,color=color)
        embed.set_author(name=authorName, url=authorURL, icon_url=authorIcon)
        embed.add_field(name=fieldname1,value=fieldvalue1,inline=False)
        embed.add_field(name=fieldname2,value=fieldvalue2,inline=False)
        await ctx.send(embed=embed)

    async def fieldEmbed(ctx,txt,fieldname1="",fieldvalue1="",color=colorforCommonMsg):
        embed=discord.Embed(  description= txt ,color=color)
        if fieldname1!=None:
            embed.add_field(name=fieldname1,value=fieldvalue1,inline=True)
        await ctx.send(embed=embed)
    
    async def printConfigEmbed(ctx,txt,color=colorforCommonMsg,fieldname1="",fieldvalue1="",fieldname2="",fieldvalue2="",fieldname3="",fieldvalue3="",fieldname4="",fieldvalue4="",fieldname5="",fieldvalue5=""):
        embed=discord.Embed(  description= txt ,color=color)
        embed.add_field(name=fieldname1,value=fieldvalue1,inline=True)
        embed.add_field(name=fieldname2,value=fieldvalue2,inline=True)
        embed.add_field(name=fieldname3,value=fieldvalue3,inline=False)
        embed.add_field(name=fieldname4,value=fieldvalue4,inline=False)
        if fieldname5!=None:
           embed.add_field(name=recoEmbeds.nullFieldName,value=recoEmbeds.banner,inline=False)
        await ctx.send(embed=embed)
    
    def embedExtender(lines, chars=3900):
        size = 0
        message = []
        for line in lines:
            if len(line) + size > chars:
                yield message
                message = []
                size = 0
            message.append(line)
            size += len(line)
        yield message
    
    async def extendableMsg(ctx,txt,color=colorforCommonMsg):
        embed = discord.Embed(color=color)
        for message in recoEmbeds.embedExtender(txt):
                embed.description = ''.join(message)
                msg=await ctx.send(embed=embed)
        return msg
        
