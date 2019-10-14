import declPY
import make

def get_data():
    data = declPY.namespace(make.parseCpp("./OneLife/server/map.h"),0)
    return data
