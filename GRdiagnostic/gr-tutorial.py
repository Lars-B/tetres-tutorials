from tetres.judgment.multichain import MultiChain
from pathlib import Path
import os


if __name__ == "__main__":
	# The MultiChain object is read to read in multiple tree files with additonal log files
	# It creates a plots and a data folder within the given Working directory where it stores distance matrices and plotted figures
	mychain = MultiChain(m_chains=3,
							trees=["chain0.trees", "chain1.trees", "chain0_1.trees"],
                        	log_files=["chain0.log", "chain1.log", "chain0_1.log"],
                            working_dir=f"{Path().resolve()}",
                            name=f"GRtutorial")  # name of the MultiChain object, used to identify files in the working directory	
	# Chain indeces to compare, using j=1 will detect no convergent subset as chain0 and chain1 are dfiferent datasets!
	i = 0
	j = 2

	burn = mychain.detect_burnin(i=0, j=2)  # number of samples to delete as burnin
	print(f"Number of burnin samples that will be discarded: {burn}")
	# This will need to compute pairwise distance matrices on first computation, so it will take some time!
	# This will also use all available cores of your CPU if not restricted by something like slurm!
	start, end = mychain.gelman_rubin_cut(i=0, j=2, # indeces of the chains to compare
								ess_threshold=200,  # ESS threshold of the Cut out portion
								pseudo_ess_range=100,  # number of tree samples to use when calulating the pseudo ESS, set to 'all' to use all trees
								smoothing_average="mean",  # using the mean to smooth the GR value
								_gr_boundary=0.05,  # Setting the tolerance value
								burnin=burn  # number of samples to be deleted before computation
								)

	if start < 0 or end < 1:
		print("The given Sets of trees do not contain a converged sub set of trees according to the tree GR diagnostic!")
	else:
		# We can extract the subset of trees and subset of the corresponding log files into its own files for further analysis
		# This will extract the subset from chain 0, as compared to chain 2
		mychain.extract_cutoff(i=0, j=2, # again indices of the individual chains to use
		 						ess_threshold=200,
		 						gr_boundary=0.05, 
		 						smoothing_average="mean",
		 						burnin=burn)  # number of samples to be deleted before computation
		# This will extract the subset from chain 2, as compared to chain 0
		mychain.extract_cutoff(i=2, j=0, # again indices of the individual chains to use
		 						ess_threshold=200,
		 						gr_boundary=0.05, 
		 						smoothing_average="mean",
		 						burnin=burn)  # number of samples to be deleted before computation


	# This will creat a psrf density and trace plot
	mychain.psrf_density_trace_plot(interval=mychain[0].tree_sampling_interval, i=0, j=2)  # Creating a PSRF trace and density plot for two independent chains
	mychain.psrf_density_trace_plot(interval=mychain[0].tree_sampling_interval, i=0, j=1)  # The PSRF trace and density plot for two different simualtions