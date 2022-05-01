#!/usr/bin/python3

import discord
from discord.ext import commands
from mcstatus import MinecraftServer
import os
import git

start_command = "/home/landonbakken/Desktop/MinecraftModThings/Paper-1.18/start.sh"

scripts_dir = "/home/landonbakken/Desktop/MinecraftModThings/Paper-1.18/plugins/Skript/scripts"
g = git.cmd.Git(scripts_dir)

mcserver = MinecraftServer("192.168.0.24", 25565)

bot = commands.Bot(command_prefix="@")

def start_server(ctx):
	os.system(start_command)

@bot.command()
async def server(ctx, arg):
    global mcserver
    arg = arg.lower()
    try:
        if arg == "ping":
            await ctx.send(mcserver.ping())
        elif arg == "status":
            status = mcserver.status()
            if status.players.online != 1:
                await ctx.send(f"{status.players.online} players with {status.latency} milliseconds of latency")
            else:
                await ctx.send(f"{status.players.online} player with {status.latency} milliseconds of latency")
    except ConnectionRefusedError:
        await ctx.send("The server is not up at the moment, but is starting up now (:")
		start_server(ctx)


@bot.command()
async def git(ctx, arg):
    global mcserver
    arg = arg.lower()
    if arg == "pull":
        try:
            g.pull()
            await ctx.send("Server has been updated")
        except:
            await ctx.send("Git was not able to do a pull request")

bot.run('NzgzMDgxMjE1NjU3MjQ2NzMy.X8VjNg.hq5LbLrn6MlTtsiwf_Smemry0Ws')