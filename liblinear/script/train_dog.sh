#!/bin/sh -x 

ori_dir=../../data/dog.stdscore.stdfeat
in_dir=../../data/dog.stdscore.svmformat.sample.svmscale
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

	python scale_score.py ${f_train} ${f_train_new} 1 

	../liblinear/train -s 11 -c 100 -p 0.1 -e 0.01 ${f_train_new} ${f_model}
	../liblinear/predict ${f_test} ${f_model} ${f_pred}

	python construct.py $f_valid $f_pred $f_out

	python ../../evaluate/R2.py $f_out $f_truth 
done
