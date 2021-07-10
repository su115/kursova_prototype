#! /bin/bash
test_list="Activity Teacher Group Subject Profession Board"
for i in $test_list
do
	echo "test $i"
	python3 $i.py
done

# Create backup
path="../value"
num=$(< $path)
let num=$num+1
echo "CREATE BACKUP #"$num
tar cfv ../backup$num.tar ../class/*
echo $num>../value

