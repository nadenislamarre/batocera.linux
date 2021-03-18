#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Command
import batoceraFiles
from generators.Generator import Generator
import os.path
import glob


class DosBoxStagingGenerator(Generator):

    def getResolutionMode(self, config):
        return 'default'
    
    # Main entry of the module
    # Return command
    def generate(self, system, rom, playersControllers, gameResolution):
        # Find rom path
        gameDir = rom
        batFile = gameDir + "/dosbox.bat"
        gameConfFile = gameDir + "/dosbox.cfg"
           
        commandArray = [batoceraFiles.batoceraBins[system.config['emulator']],
			"-fullscreen",
			"-userconf", 
			"-exit", 
			"""{}""".format(batFile),
			"-c", """set ROOT={}""".format(gameDir)]
        if os.path.isfile(gameConfFile):
            commandArray.append("-conf")
            commandArray.append("""{}""".format(gameConfFile))
        else:
            commandArray.append("-conf")
            commandArray.append("""{}""".format(batoceraFiles.dosboxStagingConfig))

        return Command.Command(array=commandArray)
