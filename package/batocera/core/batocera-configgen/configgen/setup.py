#!/usr/bin/env python

from distutils.core import setup
setup(name='batocera-configgen',
      version='1.0',
      py_modules=['configgen'],
      packages=[
        'configgen',
        'configgen.generators', 
        'configgen.generators.kodi', 
        'configgen.generators.libretro', 
        'configgen.generators.linapple', 
        'configgen.generators.moonlight', 
        'configgen.generators.mupen', 
        'configgen.generators.scummvm', 
        'configgen.generators.dosbox',
        'configgen.generators.dosboxstaging',
        'configgen.generators.dosboxx',
        'configgen.generators.vice',
        'configgen.generators.fsuae',
        'configgen.generators.amiberry',
        'configgen.generators.ppsspp',
        'configgen.generators.flycast',
        'configgen.generators.dolphin',
        'configgen.generators.pcsx2',
        'configgen.generators.rpcs3',
        'configgen.generators.citra',
        'configgen.generators.daphne',
        'configgen.generators.cannonball',
        'configgen.generators.sdlpop',
        'configgen.generators.openbor',
        'configgen.generators.wine',
        'configgen.generators.cemu',
        'configgen.generators.melonds',
        'configgen.generators.mame',
        'configgen.generators.devilutionx',
        'configgen.generators.hatari',
        'configgen.generators.tsugaru',
        'configgen.generators.solarus',
        'configgen.generators.easyrpg',
        'configgen.generators.redream',
        'configgen.generators.supermodel',
        'configgen.generators.xash3d_fwgs',
        'configgen.generators.mugen',
        'configgen.generators.fpinball',
        'configgen.generators.tsugaru',
        'configgen.generators.ruffle',
        'configgen.generators.lightspark',
        'configgen.generators.duckstation',
        'configgen.generators.drastic',
        'configgen.generators.xemu',
        'configgen.generators.cgenius',
        'configgen.generators.flatpak',
        'configgen.settings',
        'configgen.utils',
        ],
        package_data={
          'configgen.generators.xash3d_fwgs': ['gamepad.cfg'],
        },
      )
