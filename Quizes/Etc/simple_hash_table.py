
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    hash_adr = hash_function(get_key(data))
    hash_table[hash_adr] = value

def read_data(data):
    hash_adr = hash_function(get_key(data))
    return hash_table[hash_adr]


save_data('Dave','01058281727')
save_data('Andy', '01028440000')
print(read_data('Dave'))
print(hash_table)  # 충돌 상황은 고려하지 않은 코드

