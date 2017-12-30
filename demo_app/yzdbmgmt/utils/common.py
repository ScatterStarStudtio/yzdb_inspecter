import datetime

import uuid

name = "yzdb_inspecter"

def getYzDefaultFmtDateTime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def getGUUID():
    yz_uuid = uuid.uuid1()
    yz_uuid_str = str(yz_uuid)
    return yz_uuid_str.replace('-', '')
