import game_framework
import collision

import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = ".\SDL2\x86"
else:
    os.environ["PySDL2_DLL_PATH"] = ".\SDL2\x64"

game_framework.run(collision)
