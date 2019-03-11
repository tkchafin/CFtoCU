#!/usr/bin/python

import os
import sys
import itertools
import collections

if len(sys.argv) < 2:
	print("Usage: sample_quartets.py <taxon list>")

all=sys.argv[1]

#for testing only, don't use this for analysis
spoof=False #hard coded option

#print("Total observed quartets:",len(sampled))
all_quartets=list()
all_tax = list()
with open(all, 'r') as fh:
	try:
		all = list()
		for line in fh:
			line=line.strip()
			if not line:
				continue
			else:
				all_tax.append(line)
	except IOError:
		print("Could not read file ",CF)
		sys.exit(1)
	finally:
		fh.close()

all_comb = list(itertools.combinations(all_tax,4))
#print("Total expected quartets:",len(all_comb))
for comb in all_comb:
	all_quartets.append(sorted(list(comb)))

#print("Writing all missing quartets to stdout...")

for quartet in all_quartets:

	if spoof:
		oline = "";
		for tax in quartet:
			oline = oline + str(tax) + ","
		oline = oline + "0.333333333333334,0.333333333333333,0.333333333333333"
		print(oline)
	else:
		#oline = quartet
		print(quartet)
