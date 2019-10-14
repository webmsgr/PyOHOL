import declPY
import make

def get_data():
    data = declPY.namespace(make.parseCpp("./OneLife/server/map.h"),0)
    return data
def test_type():
    data = get_data()
    assert isinstance(data,declPY.namespace)
