#!/bin/sh -x 

ori_dir=../../data/dog
#in_dir=../../data/dog.stdscore.svmformat.sample.svmscale
in_dir=../../data/dog.stdscore.svmformat.sample
out_dir=../data

t1=`date +"%s"`

for ((i=6; i<=6; i++)); do
	f_record=${ori_dir}/record_${i}.txt
	f_valid=${ori_dir}/validation_${i}.txt
	f_truth=${ori_dir}/groundtruth_${i}.txt

	f_train=${in_dir}/fm_traind_${i}
	f_test=${in_dir}/fm_testd_${i}

	f_train_new=${out_dir}/fm_traind_${i}
	f_model=${out_dir}/modeld_${i}
	f_pred=${out_dir}/predd_${i}.txt
	f_out=${out_dir}/outd_${i}.txt

	python scale_score.py ${f_train} ${f_train_new} 3 

	var=`python calc_stdv.py ${f_record} 10`
	#var=0.0001

	../libsvm/svm-train -s 3 -t 2 -c 100 -g ${var} -p 0.01 -e 0.001 -h 1 -m 3096 ${f_train_new} ${f_model}
	#../libsvm/svm-train -s 4 -t 2 -c 100 -g ${var} -n 0.5 -e 0.001 -h 1 -m 3096 ${f_train_new} ${f_model}
	../libsvm/svm-predict ${f_test} ${f_model} ${f_pred}

	python construct.py $f_valid $f_pred $f_out

	python ../../evaluate/R2.py $f_out $f_truth 
done

t2=`date +"%s"`
echo `expr $t2 - $t1`
