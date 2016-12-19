#!/bin/bash

for i in {00000001..00200000} 
do 
    cat ./"${i}".txt 
    sleep .1 
done
