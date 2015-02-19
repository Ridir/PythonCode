import defs
import configparser

configPath =  (defs.gamepath) + "\data.cfg"
config = configparser.RawConfigParser()
config.read(configPath)

if config['info']['speed'] == "instant":
    numberspeed = 0
if config['info']['speed'] == "fast":
    numberspeed = 0.02
if config['info']['speed'] == "medium":
    numberspeed = 0.03
if config['info']['speed'] == "slow":
    numberspeed = 0.04


import textygame