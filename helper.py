## Helper

import sys
import KSR as KSR # type: ignore

def mod_init():
    KSR.info("===== from Python mod init\n")
    return kamailio()

def test():
    KSR.info("===== from helper.py =====\n")
    return True

class kamailio:
    def __init__(self):
        KSR.info('===== kamailio.__init__\n')