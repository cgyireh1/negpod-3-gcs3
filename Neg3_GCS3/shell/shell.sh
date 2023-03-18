#!bin/bash
echo "enter file" 
read file1
if [ -f "$file1" ]; then
         if [ -s "$file1" ]; then
echo "0" 
else 
echo "1"
fi
else
echo "2"
fi

