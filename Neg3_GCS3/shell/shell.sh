#!bin/bash
touch file.txt
if [ -f "$file.txt" ]; then
         if [ -s "$file.txt" ]; then
echo "0" 
else 
echo "1"
fi
else
echo "2"
fi

