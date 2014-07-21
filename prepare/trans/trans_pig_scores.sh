#!/bin/sh -x 
in_dir=../../data/pig
out_dir=../../data/pig.stdscore
for ((i=1; i<=15; i++)); do
	python ./trans_score.py ${in_dir}/train_${i}.txt ${out_dir}/train_${i}.txt 
done
