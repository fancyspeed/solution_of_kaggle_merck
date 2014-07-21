#!/bin/sh -x 
in_dir=../../data/dog
out_dir=../../data/dog.stdscore
for ((i=1; i<=15; i++)); do
	python ./trans_score.py ${in_dir}/record_${i}.txt ${out_dir}/record_${i}.txt 
done
