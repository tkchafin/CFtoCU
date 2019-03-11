# CFtoCU
Scripts to scale branch lengths of a tree to coalescent units, given a table of concordance factors

This is my version of code implemented in Noah Stenz's [TICR](https://github.com/nstenz/TICR) 'getTreeBranchLengths.R' script

If you use this, you should cite the following:
* Stenz et al (2015).
  Exploring tree-like and non-tree-like patterns using genome sequences:
  An example using the inbreeding plant species *Arabidopsis thaliana* (L.) Heynh.
  Systematic Biology, 64(5):809-823.
  [doi: 10.1093/sysbio/syv039](https://doi.org/10.1093/sysbio/syv039)
* Allman E.S. Degnan J.H. Rhodes J.A. 2011. Identifying the rooted species tree from the distribution  
  of unrooted gene trees under the coalescent. J. Math. Biol. 62:833–862.


## Scripts

```
annotateBranches.py   - Annotates branches from input treefile with coal units calculated from CFs
duplicate_quartets.py - Prints duplicated quartets in a CF file
missing_quartets.py   - Prints missing quartets in a CF file
sample_quartets.py    - Prints all possible quartets given a taxon list
ticr2cfs.sh           - Prints relevant columns from TICR output CFs file (to stdout)
```
