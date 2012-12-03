# !/usr/bin/env python
# -*- coding: utf-8 *-*

# Import modules
import os
import sys

"""
With the configFile, we can have access to all global variables
"""

import ConfigParser
main_dir = os.path.split(os.path.abspath(__file__))[0]
config_file = os.path.join(main_dir,'config.cfg')

if os.path.isfile(config_file):
    """ We load the configFile """
    config=ConfigParser.ConfigParser()
    config.read(config_file)
else:
    sys.exit("Error, config_file : " + config_file +" cannot be found")

def setConfigValue(section,option,value):
    if config.has_section(section) and config.has_option(section,option):
        config.set(section,option,value)
        f = open(config_file,"w")
        config.write(f)
        f.close()
    else:
        sys.exit("mauvaise section ou option ")



def getDataDir():
    return config.get('PROGRAMS','DATA_DIR')

def getImageDir():
    return os.path.join(getDataDir(),config.get('PROGRAMS','IMAGE_DIR'))

def getSoundDir():
    return os.path.join(getDataDir(),config.get('PROGRAMS','SOUND_DIR'))

def getFontDir():
    return os.path.join(getDataDir(),config.get('PROGRAMS','FONT_DIR'))

def getEnemyFrame(num):
    return config.get('ENEMY','FRAME_XXX').replace("XXX",str(num))

def getPlayerFrame(num):
    return config.get('PLAYER','FRAME_XXX').replace("XXX",str(num))

def getEnemyHitSound():
    return config.get('ENEMY','HIT_SOUND')

def getThrowSound():
    return config.get('PLAYER','THROW_SOUND')

def getNumberFrameEnemy():
    return int(config.get('PLAYER','NUMBER_FRAME'))

def getNumberFramePlayer():
    return int(config.get('PLAYER','NUMBER_FRAME'))

def getHudFont():
    return config.get('HUD','FONT')

def getHudFontSize():
    return int(config.get('HUD','FONT_SIZE'))

def getComboFont():
    return config.get('COMBO','FONT')

def getComboFontSize():
    return int(config.get('COMBO','FONT_SIZE'))

def getHighScoresImage():
    return config.get('HIGHSCORES','BACKGROUND')

def getHighScoresHeaderManagerFont():
    return config.get('HIGHSCORES','HEADER_MANAGER_FONT')

def getHighScoresHeaderManagerFontSize():
    return int(config.get('HIGHSCORES','HEADER_MANAGER_FONT_SIZE'))

def getHighScoresFontManagerFont():
    return config.get('HIGHSCORES','FONT_MANAGER')

def getHighScoresFontManagerFontSize():
    return int(config.get('HIGHSCORES','FONT_MANAGER_SIZE'))

def getHighScoresMusic():
    return config.get('HIGHSCORES','MUSIC')

def getHighScoresFile():
    return config.get('HIGHSCORES','FILE')

def getLevelImage():
    return config.get('LEVEL','IMAGE')

def getLevelPlatformImage():
    return config.get('LEVEL','PLATFORM')

def getLevelNumberOfPlatform():
    return int(config.get('LEVEL','NUMBER_OF_PLATFORM'))

def getPowerUpBonusSound():
    return config.get('POWERUP','BONUS_SOUND')

def getPowerUpShirukenImage():
    return config.get('POWERUP','SHIRUKEN_IMAGE')

def getProjectileImage():
    return config.get('PROJECTILE','IMAGE')

def getGameBackground():
    return config.get('GAME','BACKGROUND')

def getGameSound():
    return config.get('GAME','SOUND')

def getTitleBackground():
    return config.get('TITLE','BACKGROUND')

def getTitleFont():
    return config.get('TITLE','FONT')

def getTitleFontSize():
    return int(config.get('TITLE','FONT_SIZE'))

def getTitleHelpFont():
    return config.get('TITLE','HELP_FONT')

def getTitleHelpFontSize():
    return int(config.get('TITLE','HELP_FONT_SIZE'))

def getTitleTitleFont():
    return config.get('TITLE','TITLE_FONT')

def getTitleTitleFontSize():
    return int(config.get('TITLE','TITLE_FONT_SIZE'))

def getTitleHelpImage():
    return config.get('TITLE','HELP_IMAGE')

def getTitleSound():
    return config.get('TITLE','SOUND')


