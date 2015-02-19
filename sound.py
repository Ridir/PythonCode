import winsound
import defs
import random

def textbeep():
	winsound.PlaySound(defs.gamepath + "\sound\write.wav",  winsound.SND_ASYNC)

def next():
	winsound.PlaySound(defs.gamepath + "\sound\mext.wav",  winsound.SND_ASYNC)

def equip():
	winsound.PlaySound(defs.gamepath + "\sound\equip.wav",  winsound.SND_ASYNC)

def gameover():
	winsound.PlaySound(defs.gamepath + "\sound\gameover.wav",  winsound.SND_ASYNC)

def loot():
	winsound.PlaySound(defs.gamepath + "\sound\loot.wav",  winsound.SND_ASYNC)
