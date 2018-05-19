import os
import sys
import marshal
import __builtin__ as pp
import time
#Green = 033[32m Oranye = \033[33m Blue = \033[34m Red = \033[31m White = \033[0m
def restartprogram():
    mulai()

banner="""
\033[31m				 Author : AMRiezz
\033[33m           ___________\033[0m @ @\033[34m	 Github : https://github.com/Amriez
\033[33m          /         (\033[0m@\033[33m\ \033[0m   @a\033[31m	 Blog	: http://anrwiki.blogspot.com
\033[33m          \___________/  _\033[0m @ \033[34m	 youtube: AMRiezz z
\033[0m                    @ \033[33m _/\033[0m@ \033[33m\_____
\033[31m   ANTI   \033[0m           @\033[33m/ \__/\033[0m-="="`
\033[31m   RE-CODE \033[33m           \_ /
\033[31m   RE-CODE \033[0m            <\033[33m| \033[31m	 Tukang-Kunci(c)
\033[31m   CLUB       \033[0m         <\033[33m|
                      \033[0m <\033[33m|
                      \033[33m ` \033[35m
"""
def marsha():
  os.system("clear")
  print banner
  file=raw_input("MamangKey >~# ")
  f=open(file).read()
  s = f.replace("\r\n","\n")
  s = s.replace("\r","\n")
  if s and s[-1] != '\n':
    s = s + '\n'
  asade=pp.compile(s,'<s>','exec')
  todi=marshal.dumps(asade)
  awal="""
import marshal
exec(marshal.loads(''"""
  akhir="''))"
  open(file[:-3]+'-AMR.py', 'w').write(awal+repr(todi)+akhir)
  time.sleep(3)

  try :
	  print "  [+]Succes..."

  except(ImportError):
	  print "  [-]Failed..."

def mulai():
        print banner
        print "         ~{1}--Start             "
        print "         ~{2}--Exit              "
        zz=raw_input("MamangKey >~# ")
        if zz == "1":
                marsha()
        elif zz == "2":
                os.system("clear")
        else :
            time.sleep(3)
            restartprogram()

mulai()

