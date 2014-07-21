#!/bin/sh -x 
in_dir1=../../data/dog
in_dir2=../../data/dog.stdscore
out_dir=../../data/dog.stdscore.stdfeat
for ((i=1; i<=15; i++)); do
	python ./trans_feature.py ${in_dir2}/record_${i}.txt ${in_dir1}/validation_${i}.txt ${out_dir}/record_${i}.txt ${out_dir}/validation_${i}.txt
done
