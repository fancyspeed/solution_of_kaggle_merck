#!/bin/sh -x 
in_dir=../../data/pig.stdscore
out_dir=../../data/pig.stdscore.svmformat.addid
for ((i=1; i<=15; i++)); do
	python svm_format_addid.py ${in_dir}/train_${i}.txt ${out_dir}/fm_train_${i} train
	python svm_format_addid.py ${in_dir}/test_${i}.txt ${out_dir}/fm_test_${i} test
done
