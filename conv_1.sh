#!/bin/sh -x
# $1 - input file, e.g. input.mp4
ffmpeg -i car-accident_20230513_0.mp4 -q:v 2 %06d.jpg
