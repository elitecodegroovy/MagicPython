__author__ = 'JohnLiu'

import redis

POOL = redis.ConnectionPool(host='192.168.124.129', port=6379, db=0)
r_server = redis.Redis(connection_pool=POOL)
# follow the Redis official commands
# r_server = redis.StrictRedis(connection_pool=POOL)
def get_variable(variable_name):
    response = r_server.get(variable_name)
    return response

def set_variable(variable_name, variable_value):
    r_server.set(variable_name, variable_value)

# redis data structure: STRING
str_key = 'hello, redis'
set_variable(str_key, "Welcome to Redis World!")
print get_variable(str_key)

# set an integer to a key
r_server.set('counter', 1)
# we increase the key value by 1, has to be int
r_server.incr('counter')
print 'the counter was increased! '+r_server.get('counter')

# we decrease the key value by 1, has to be int
r_server.decr('counter')
r_server.decr('counter')
print 'the counter was decreased! '+r_server.get('counter')

'''Now we are ready to jump into another redis data type, the list, notice
that they are exactly mapped to python lists once you get them'''
# redis data structure: LIST
print 'our redis list len is: %s' % r_server.llen("list_item")
r_server.rpush("list_item", "item0")
r_server.rpush("list_item", "item1")
r_server.rpush("list_item", "item0")
print 'our redis list len is: %s' % r_server.llen("list_item")
print r_server.lrange("list_item", 0, 1)
print 'our redis list item index 0: %s' % r_server.lindex("list_item", 0)
print 'our redis list item index 2: %s' % r_server.lindex("list_item", 2)
l_len = r_server.llen("list_item")
for i in range(0, l_len):
    print "%s " % r_server.rpop("list_item")

'''Now we are ready to jump into another redis data type, the set, notice
that they are exactly mapped to python set once you get them'''
r_server.sadd("set_collection", "set_0")
r_server.sadd("set_collection", "set_1")
r_server.sadd("set_collection", "set_2")
r_server.sadd("set_collection", "set_0")
print r_server.smembers("set_collection")
print r_server.sismember("set_collection", "set_0")
print r_server.sismember("set_collection", "set_3")
print r_server.srem("set_collection", "set_0")
print r_server.srem("set_collection", "set_1")
print r_server.srem("set_collection", "set_2")


'''Now we are ready to jump into another redis data type, the hash, notice
that they are exactly mapped to python hash once you get them.'''
print r_server.hset("hash_key", "key_0", "value_0")
print r_server.hset("hash_key", "key_1", "value_1")
print r_server.hset("hash_key", "key_0", "value_0")
print r_server.hgetall("hash_key")
print r_server.hdel("hash_key", "key_0")
print r_server.hget("hash_key", "key_1")
print r_server.hdel("hash_key", "key_1")
print r_server.hdel("hash_key", "key_10")
print r_server.hdel("hash_key", "key_1")
print r_server.hgetall("hash_key")
'''
The keys (called members)are unique, and the values (called scores) are
limited to floating-point numbers.
Now we are ready to jump into another redis data type, the ZSET( ordered
set), notice that they are exactly mapped to python ZSET once you get them.
'''
# print r_server.zadd("zset_key", 11.11, "member_3")
# print r_server.zadd("zset_key", 11.00, "member_1")
# print r_server.zadd("zset_key", 11.00, "member_1")
# print r_server.zrange("zset_key", 0, 1, True)