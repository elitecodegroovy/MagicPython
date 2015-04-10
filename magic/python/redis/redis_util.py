__author__ = 'JohnLiu'

import redis

POOL = redis.ConnectionPool(host='192.168.124.129', port=6379, db=0)

def getVariable(variable_name):
    my_server = redis.Redis(connection_pool=POOL)
    response = my_server.get(variable_name)
    return response

def setVariable(variable_name, variable_value):
    my_server = redis.Redis(connection_pool=POOL)
    my_server.set(variable_name, variable_value)

str_key = 'hello, redis'
setVariable(str_key, "Welcome to Redis World!")
print getVariable(str_key)