# -*- coding: utf-8 -*-
"""
Created on Sunday Jan 19 2020

@author: Luke Carter    
"""

import Dominion
import random
from collections import defaultdict


def CreateBox(nV):
#Define box
	box = {}
	box["Woodcutter"]=[Dominion.Woodcutter()]*10
	box["Smithy"]=[Dominion.Smithy()]*10
	box["Laboratory"]=[Dominion.Laboratory()]*10
	box["Village"]=[Dominion.Village()]*10
	box["Festival"]=[Dominion.Festival()]*10
	box["Market"]=[Dominion.Market()]*10
	box["Chancellor"]=[Dominion.Chancellor()]*10
	box["Workshop"]=[Dominion.Workshop()]*10
	box["Moneylender"]=[Dominion.Moneylender()]*10
	box["Chapel"]=[Dominion.Chapel()]*10
	box["Cellar"]=[Dominion.Cellar()]*10
	box["Remodel"]=[Dominion.Remodel()]*10
	box["Adventurer"]=[Dominion.Adventurer()]*10
	box["Feast"]=[Dominion.Feast()]*10
	box["Mine"]=[Dominion.Mine()]*10
	box["Library"]=[Dominion.Library()]*10
	box["Gardens"]=[Dominion.Gardens()]*nV
	box["Moat"]=[Dominion.Moat()]*10
	box["Council Room"]=[Dominion.Council_Room()]*10
	box["Witch"]=[Dominion.Witch()]*10
	box["Bureaucrat"]=[Dominion.Bureaucrat()]*10
	box["Militia"]=[Dominion.Militia()]*10
	box["Spy"]=[Dominion.Spy()]*10
	box["Thief"]=[Dominion.Thief()]*10
	box["Throne Room"]=[Dominion.Throne_Room()]*10
	return box


def InitializePlayers(player_names):
	players = []
	for name in player_names:
		if name[0]=="*":
			players.append(Dominion.ComputerPlayer(name[1:]))
		elif name[0]=="^":
			players.append(Dominion.TablePlayer(name[1:]))
		else:
			players.append(Dominion.Player(name))
	return players


def GetPlayers(numPlayers):
	playerplayer_Names = ["Annie", "Bob", "Charles"]
	playerComp_Names = ["*Ben", "*Carla", "*David", "*Adam", "Fred"]
	player_names = [playerplayer_Names[random.randint(0, 2)]]
	while len(player_names) < numPlayers:
		number = random.randint(0, len(playerComp_Names)-1)
		name = playerComp_Names[number]
		player_names.append(name)
		playerComp_Names.remove(name)
	pass
	return player_names
