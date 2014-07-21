#!/bin/sh -x 
in_dir=../../data/dog.stdscore.svmformat.sample
out_dir=../../data/dog.stdscore.svmformat.sample.addqid
for ((i=1; i<=15; i++)); do
	python add_qid.py ${in_dir}/fm_traind_${i} ${out_dir}/fm_traind_${i}
	python add_qid.py ${in_dir}/fm_testd_${i} ${out_dir}/fm_testd_${i}
done
