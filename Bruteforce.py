import requests

link1="https://"
link2=".facebook.com"

for i in range(97,123):
	for j in range(97,123):
		for k in range(97,123):
			for l in range(97,123):
				for m in range(97,123):
					try:
						print("testing -> "+link1+chr(i)+chr(j)+chr(k)+chr(l)+chr(m)+link2)
						requests.get(link1+chr(i)+chr(j)+chr(k)+chr(l)+chr(m)+link2)

					except:
						print("Doesn't exists")
