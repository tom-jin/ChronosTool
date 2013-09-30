#!/bin/bash

(
flock -x -w 10 200 || exit 1
cd ~pi/src/ChronosTool/
while true
  do if [ -z `./ChronosTool.py status | grep null` ]
    then  echo "Found watch."
    ./ChronosTool.py sync
    ./ChronosTool.py download
    ./ChronosTool.py erase
    ./ChronosTool.py goodbye
    FILENAME=`ls -t *.bin | head -1 | cut -d. -f1`
    ./ParseMemory.py $FILENAME.bin $FILENAME.csv
    cp $FILENAME.csv /var/www
  fi
done
) 200>/var/lock/.loop.exclusivelock