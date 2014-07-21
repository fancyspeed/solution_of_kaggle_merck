#!/bin/sh -x 
out_file=output.csv
rm -f $out_file
echo \"MOLECULE\",\"Prediction\" >> $out_file

ori_dir=../../data/pig
in_dir=../../data/pig.stdscore.svmformat
out_dir=../data

for ((i=9; i<=9; i++)); do
	f_record=${ori_dir}/train_${i}.txt
	f_valid=${ori_dir}/test_${i}.txt

	f_train=${in_dir}/fm_train_${i}
	f_test=${in_dir}/fm_test_${i}

	f_train_new=${out_dir}/fm_trainp_${i}
	f_model=${out_dir}/modelp_${i}
	f_pred=${out_dir}/predp_${i}.txt
	f_out=${out_dir}/outp_${i}.txt

	python scale_score.py ${f_train} ${f_train_new} 5 

	var=`python calc_stdv.py ${f_record} 10`
	#var=0.0001

	#../libsvm/svm-train -s 3 -t 2 -c 100 -g ${var} -p 0.01 -e 0.001 -m 3096 ${f_train_new} ${f_model}
	../libsvm/svm-train -s 4 -t 2 -c 100 -g ${var} -n 0.5 -e 0.001 -h 1 -m 3096 ${f_train_new} ${f_model}
	../libsvm/svm-predict ${f_test} ${f_model} ${f_pred}

	python construct.py $f_valid $f_pred $f_out
	cat $f_out >> $out_file
done
