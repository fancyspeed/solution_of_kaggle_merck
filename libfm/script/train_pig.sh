#!/bin/sh -x 
out_file=output.csv
rm -f $out_file
echo \"MOLECULE\",\"Prediction\" >> $out_file

ori_dir=../../data/pig
in_dir=../../data/pig.stdscore.svmformat.addid.sample
out_dir=../data

for ((i=1; i<=15; i++)); do
	f_record=${ori_dir}/train_${i}.txt
	f_valid=${ori_dir}/test_${i}.txt
	f_train=${in_dir}/fm_train_${i}
	f_test=${in_dir}/fm_test_${i}
	f_train_new=${out_dir}/fm_trainp_${i}
	f_model=${out_dir}/modelp_${i}
	f_pred=${out_dir}/predp_${i}.txt
	f_out=${out_dir}/outp_${i}.txt

	iter=1000

	python scale_score.py ${f_train} ${f_train_new} 5 

	../libfm/bin/libFM -task r -dim '1,1,0' -train $f_train_new -test $f_test -out $f_pred -method mcmc -iter $iter -init_stdev 0

	python construct.py $f_valid $f_pred $f_out
	cat $f_out >> $out_file
done
