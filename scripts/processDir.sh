#!/bin/bash
count=0
IFS=$'\n'
for FILE in $1/*.jpg; do
        echo  "Processing $FILE - Image Number: $count"
        count=$((count+1))
        echo $FILE
    python3 ./findOCR.py $FILE
done

