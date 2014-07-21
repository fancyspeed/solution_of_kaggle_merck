#!/bin/sh -x 
in_dir=../../data/pig.stdscore.svmformat.sample
out_dir=../../data/pig.stdscore.svmformat.sample.addqid
for ((i=1; i<=15; i++)); do
	python add_qid.py ${in_dir}/fm_train_${i} ${out_dir}/fm_train_${i}
	python add_qid.py ${in_dir}/fm_test_${i} ${out_dir}/fm_test_${i}
done
