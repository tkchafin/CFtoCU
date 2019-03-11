#!/bin/bash

f=$1

awk 'BEGIN{FS=","}{print $1 "," $2 "," $3 "," $4 "," $5 "," $8 "," $11}' $f