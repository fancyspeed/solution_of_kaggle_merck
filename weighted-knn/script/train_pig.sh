#!/bin/sh -x
out_file=output.csv
rm -f $out_file
echo \"MOLECULE\",\"Prediction\" >> $out_file

ori_dir=../../data/pig
in_dir=../../data/pig.stdscore.svmformat.sample
out_dir=../data

K=5

for ((i=1; i<=15; i++)); do
	f_record=${ori_dir}/train_${i}.txt
	f_valid=${ori_dir}/test_${i}.txt

	f_train=${in_dir}/fm_train_${i}
	f_test=${in_dir}/fm_test_${i}

	f_pred=${out_dir}/knn_predp_${i}
	f_out=${out_dir}/knn_outp_${i}

	NF=`python get_nfeat.py ${f_record}`
	python knn_svmformat.py ${f_train} ${f_test} ${f_pred} ${NF} ${K}

	python construct.py $f_valid $f_pred $f_out
	cat $f_out >> $out_file
done
