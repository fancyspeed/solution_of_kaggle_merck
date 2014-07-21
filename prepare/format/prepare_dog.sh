#!/bin/sh -x 
in_dir=../../data/dog.stdscore
out_dir=../../data/dog.stdscore.svmformat
for ((i=1; i<=15; i++)); do
	python svm_format.py ${in_dir}/record_${i}.txt ${out_dir}/fm_traind_${i} train
	python svm_format.py ${in_dir}/validation_${i}.txt ${out_dir}/fm_testd_${i} test
done
