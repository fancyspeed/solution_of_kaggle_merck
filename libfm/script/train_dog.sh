#!/bin/sh -x 
ori_dir=../../data/dog
in_dir=../../data/dog.stdscore.svmformat.sample
#in_dir=../../data/dog.stdscore.svmformat.addid.sample
out_dir=../data
for ((i=1; i<=15; i++)); do
	f_record=${ori_dir}/record_${i}.txt
	f_valid=${ori_dir}/validation_${i}.txt
	f_truth=${ori_dir}/groundtruth_${i}.txt
	f_train=${in_dir}/fm_traind_${i}
	f_test=${in_dir}/fm_testd_${i}
	f_train_new=${out_dir}/fm_traind_${i}
	f_model=${out_dir}/modeld_${i}
	f_pred=${out_dir}/predd_${i}.txt
	f_out=${out_dir}/outd_${i}.txt

	iter=100

	python scale_score.py ${f_train} ${f_train_new} 5 

	../libfm/bin/libFM -task r -dim '1,1,0' -train $f_train_new -test $f_test -out $f_pred -method mcmc -iter $iter -init_stdev 0

	python construct.py $f_valid $f_pred $f_out

	python ../../evaluate/R2.py $f_out $f_truth 
done
