#!/bin/bash

for f in {00000001..00200000} 
do 
    jp2a --background=dark --term-width --chars=" .!!\\:;civouxkld00&@XHBNWM" --clear -b -z "${f}".jpg --output="${f}".txt 
	#./"${f}".jpeg --output=./"${f}".txt 
    rm "${f}".jpg 
    sleep .1 
done
