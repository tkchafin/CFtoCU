#!/usr/bin/python

using sys
using os
using dendropy

def main():
	params = parseArgs()





Object to parse command-line arguments
class parseArgs():
	def __init__(self):
		#Define options
		try:
			options, remainder = getopt.getopt(sys.argv[1:], 't:c:fh', \
			["help"])
		except getopt.GetoptError as err:
			print(err)
			self.display_help("\nExiting because getopt returned non-zero exit status.")
		#Default values for params
		#Input params
		self.tree=None
		self.cf=None
		self.fill=False

		#First pass to see if help menu was called
		for o, a in options:
			if o in ("-h", "-help", "--help"):
				self.display_help("Exiting because help menu was called.")

		#Second pass to set all args.
		for opt, arg_raw in options:
			arg = arg_raw.replace(" ","")
			arg = arg.strip()
			opt = opt.replace("-","")
			#print(opt,arg)
			if opt == "t":
				self.tree = arg
			elif opt in ('h', 'help'):
				pass
			elif opt == "c":
				self.cf =arg
			elif opt == "f":
				self.fill = True
			else:
				assert False, "Unhandled option %r"%opt

		#Check manditory options are set
		if not self.tree:
			self.display_help("Error: Need treefile <-t>")
		if not self.cf:
			self.display_help("Error: Need concordance factors <-c>")


	def display_help(self, message=None):
		if message is not None:
			print ("\n",message)
		print ("\nannotateBranches.py\n")
		print ("Contact:Tyler K. Chafin, University of Arkansas,tkchafin@uark.edu")
		print ("\nUsage: ", sys.argv[0], "-f <fasta> -p <popmap> \n")
		print ("Description: Calculates coalescent units from concordance factors and annotates tree")

		print("""
	Arguments:
		-t		: NEWICK-formatted phylogenetic tree or set of trees
		-c		: Comma-delimited table of concordance factors
		-f		: Treat missing quartet CFs as uniform (e.g. 0.33, 0.33, 0.33)
			--Default behaviour is to exit with an error code
		-h		: Displays help menu

""")
		sys.exit()

#Call main function
if __name__ == '__main__':
    main()
