#!/bin/sh -x 
in_dir=../../data/pig.stdscore.svmformat.addid
out_dir=../../data/pig.stdscore.svmformat.addid.sample
cp ${in_dir}/* ${out_dir}/

wc -l ${out_dir}/fm_train_*
awk '{if(NR%3==1)print $0}' ${in_dir}/fm_train_1 > ${out_dir}/fm_train_1
awk '{if(NR%3==1)print $0}' ${in_dir}/fm_train_6 > ${out_dir}/fm_train_6
wc -l ${out_dir}/fm_train_*
