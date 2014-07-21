#!/bin/sh -x 
for ((i=1; i<=15; i++)); do
	f_in="../pig/train_${i}.txt"
	python split.py ${f_in} ../dog/record_${i}.txt ../dog/validation_${i}.txt ../dog/groundtruth_${i}.txt
done
