#!/bin/sh -x 
in_dir=../../data/dog.stdscore.svmformat.sample
out_dir=../../data/dog.stdscore.svmformat.sample.svmscale
for ((i=1; i<=15; i++)); do
	f_train=${in_dir}/fm_traind_${i}
	f_test=${in_dir}/fm_testd_${i}
	f_train_new=${out_dir}/fm_traind_${i}
	f_test_new=${out_dir}/fm_testd_${i}
	f_scale=${out_dir}/scale_${i}

	../libsvm/svm-scale -l 0 -u 5 -s $f_scale $f_train > $f_train_new
	../libsvm/svm-scale -r $f_scale $f_test > $f_test_new
done
