#!/bin/bash
#Be sure to chmod u+x this file!

#Your team name (Please keep this the same, and make sure it is a legal filename... no spaces/symbols/etc)
#NO, SERIOUSLY, NO SPACES.  I, Stephen Mues, should never write shell scripts.
TEAM='SMdefault'

#Uncomment the line that describes the language you want to use.
#LANGUAGE='java'
#LANGUAGE='cpp'
LANGUAGE='python'


#Do not modify anything below this line ===================================

if [ "$TEAM" == 'default' ];
then
   echo 'Please edit submit.sh and change your team name.'
else


EXT=''
if [ "$LANGUAGE" != 'cpp' ];
then
   EXT='.tar.gz'
fi

FILENAME="$TEAM.$LANGUAGE.client${EXT}"

if [ $# -ne 1 ]; then
   echo 1>&2 Usage: $0 filename
   exit 127
fi

#python fileclient.py localhost 18000 $1 $FILENAME
python fileclient.py rc14xcs213.managed.mst.edu 18000 $1 $FILENAME
#python fileclient.py 66.43.41.226 18000 $1 $FILENAME

echo 'File submitted'


fi

