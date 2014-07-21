#!/bin/sh -x 
in_dir=../../data/dog.stdscore.svmformat.addid
out_dir=../../data/dog.stdscore.svmformat.addid.sample
cp ${in_dir}/* ${out_dir}/

wc -l ${out_dir}/fm_traind_*
awk '{if(NR%3==1)print $0}' ${in_dir}/fm_traind_1 > ${out_dir}/fm_traind_1
awk '{if(NR%3==1)print $0}' ${in_dir}/fm_traind_6 > ${out_dir}/fm_traind_6
wc -l ${out_dir}/fm_traind_*
