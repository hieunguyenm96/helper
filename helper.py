## Helper

import sys
import KSR as KSR 

def mod_init():
    KSR.info("===== from Python mod init\n")
    return kamailio()

def test():
    KSR.info("===== from helper.py =====\n")
    return True

class kamailio:
    def __init__(self):
        KSR.info('===== kamailio.__init__\n')
    
    # executed when kamailio child processes are initialized
    def child_init(self, rank):
        KSR.info('===== kamailio.child_init(%d)\n' % rank)
        return 0;

    # SIP request routing
    # -- equivalent of request_route{}
    def ksr_request_route(self, msg):
        KSR.info("===== request - from kamailio python script\n")
        KSR.dbg("method " + KSR.pv.get("$rm") + " r-uri " + KSR.pv.get("$ru"))