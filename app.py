import argparse
import os
from core.generator import Generator, NumbersPlugin, SymbolesPlugin


parser = argparse.ArgumentParser()
parser.add_argument('--output')
parser.add_argument('--extend')

args = parser.parse_args()


def showHelp():
	return'''
Usage : app.py --extend names.txt  --output myWordlist.txt
	--extend : the list of words or name you want to extend
	--output : name of the generated wordlist 
	'''

if(args.output is None) or (args.extend is None):
	print("[-] Args not found : ".title())
	print(showHelp())
	exit(1)

args.output = os.path.join("results",args.output)
if not os.path.isfile(args.extend) and not args.extend.endswith('.txt'): # check if file exist
		print("[-] Extend option needs a txt file!".title())
		exit(1)



def Ignore(line):
	return line.startswith("#") or  line.strip() == ""


res = []

if not os.path.exists("extend.conf"): # check if file exist
	print("Could not start : extend.conf not Found".title())
	exit(1)


if os.path.exists(args.output):
	os.remove(args.output)

config = open("extend.conf", 'r')
names = open(args.extend, 'r')
wordlist = open(args.output, 'a')



g = Generator([
	NumbersPlugin(),
	SymbolesPlugin()
	])

for line in config:
	if Ignore(line.strip('\n')): continue
	for name in names:
		print("Generating for  : ", name.strip("\n"))
		_line = line.strip('\n').replace("{name}", name.strip("\n"))
		_line = _line.replace("%s"," ")
		# g.run(line)
		[ res.append(x) for x in g.run(_line,None,0,0) ]
	
	for p in res:
		wordlist.write(p.lower() + "\n")
		wordlist.write(p.upper() + "\n")
		if "s" in p:
			wordlist.write(p.lower().replace("s","$") + "\n")
			wordlist.write(p.upper().replace("s","$") + "\n")
		if "a" in p:
			wordlist.write(p.lower().replace("a","@") + "\n")
			wordlist.write(p.upper().replace("a","@") + "\n")
	res = []

