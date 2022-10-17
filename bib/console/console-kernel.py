import os
import bib

import math
from bib.gui.engine_main import *


def EngineRunConf(engineDim, openGLSup):
    if engineDim == "3D":
        if openGLSup == "y" or openGLSup=="yes":
            #idk
            print("in build")
        elif openGLSup == "n" or openGLSup=="no":
            engine3DRun()
        else:
            return 0
    if engineDim == "2D":
        if openGLSup == "y" or openGLSup=="yes":
            #idk
            print("in build")
        elif openGLSup == "n" or openGLSup=="no":
            #engine2DRun()
            print("in build")
        else:
            return 0


def runOutEngine():
    engineDim = input("[SYSTEM] Select supported version (2D/3D)")
    if engineDim == "2D" or engineDim == "3D":
            openGLSup = input("[SYSTEM] OpenGL support? (y/n)")
            if openGLSup == "y" or "yes" or "n" or "no":
                EngineRunConf(engineDim, openGLSup)
            else:
                return "[SYSTEM] (ERROR!) Wrong OpenGL statement"
    else:
        return "[SYSTEM] (ERROR!) Wrong engine version"

def CheckCom(com, user):
    if com == 'engineRun': runOutEngine()
    else: return "[SYSTEM] (ERROR!) Wrong command"

#def LoginShell(login, passw):

