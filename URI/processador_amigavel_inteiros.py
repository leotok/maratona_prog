# https://www.urionlinejudge.com.br/judge/pt/problems/view/1287

def friendlyProcessor(s):
	s=s.replace("l", "1")
	
	if len(s) == 0:
		return "error"
	
	if s.count("0") == len(s):
		return 0

	for x in [","," "]:
		s=s.replace(x, '')

	if s == '':
		return "error"

	for k in ["o", "O"]:
		s=s.replace(k, "0")	
	
	if s.isalpha():
		return "error"
	
	if s.isdigit():
		if int(s) > 2147483647:
			return "error" 
	
	if s.isdigit():
		return str(int(s))
	else:
		return "error"

while True:
	try:
		print "%s" %friendlyProcessor(raw_input())
	except:
		break
