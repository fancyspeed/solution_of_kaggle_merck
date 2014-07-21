#!/bin/sh -x

ori_dir=../../data/dog
in_dir=../../data/dog.stdscore.svmformat.sample
out_dir=../data

i=4

f_record=${ori_dir}/record_${i}.txt
f_valid=${ori_dir}/validation_${i}.txt
f_truth=${ori_dir}/groundtruth_${i}.txt

f_train=${in_dir}/fm_traind_${i}
f_test=${in_dir}/fm_testd_${i}

f_pred=${out_dir}/knn_predd_${i}
f_out=${out_dir}/knn_outd_${i}

K=9
gamma=0.001

NF=`python get_nfeat.py ${f_record}`
#python knn_var_svmformat.py ${f_train} ${f_test} ${f_pred} ${NF} ${K}
python wknn_svmformat.py ${f_train} ${f_test} ${f_pred} ${NF} ${K} ${gamma}

python construct.py $f_valid $f_pred $f_out
python ../../evaluate/R2.py $f_out $f_truth
