#!/usr/bin/python

import os
import sys
import itertools
import collections

if len(sys.argv) < 2:
	print("Usage: duplicate_quartets.py <CF_file>")

CF=sys.argv[1]

spoof=True #hard coded option

#list of lists, capturing sampled quartets
sampled = list()

with open(CF, 'r') as fh:
	try:
		seen = list()
		for line in fh:
			if not line:
				continue
			else:
				stuff = line.split(",")
				seen = (stuff[0:4])
				sampled.append(seen)
	except IOError:
		print("Could not read file ",CF)
		sys.exit(1)
	finally:
		fh.close()


for i in range(len(sampled)):
	for j in range(i + 1, len(sampled)):
		if sorted(sampled[i]) == sorted(sampled[j]):
			print(",".join(sampled[j]))
			continue

