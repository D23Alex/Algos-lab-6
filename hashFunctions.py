from random import randint
import settings


def uni_hash(key, m, a=randint(1, settings.uni_hash_p), b=randint(0, settings.uni_hash_p - 1), p=settings.uni_hash_p):
    return ((a * key) % p) % m


def ascii_task_3(str_given, m):
    answer = 0
    for i in range(len(str_given)):
        answer += ord(str_given[i]) * (263 ** i)
    return (answer % 1000000007) % m
