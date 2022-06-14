import ast
import redis

from Config import Config

INFO = Config.REDIS_URI.split(":")

DB = redis.StrictRedis(
    host=INFO[0],
    port=INFO[1],
    password=var.REDIS_PASS,
    charset="utf-8",
    decode_responses=True,
)

def get_stuff(WHAT):
    n = []
    cha = DB.get(WHAT)
    if not cha:
        cha = "{}"
    n.append(ast.literal_eval(cha))
    return n[0]
