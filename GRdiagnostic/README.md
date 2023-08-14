# Paper 

If you publish a paper using this package, please cite<br>
Lars Berling, Remco Bouckaert, and Alex Gavryushkin<br>
**Automated convergence diagnostic for phylogenetic MCMC analyses**<br>
*BioRxiv 2023*<br>
[https://doi.org/10.1101/2023.08.10.552869](https://doi.org/10.1101/2023.08.10.552869)<br>


# Execute

Execute the script via `python gr-tutorial.py` in the command line. This will create several directories.


## What is the output

The execution will create two figures in the `plots` directroy showcasing the PSRF trace and density for two combinations of the provided chains.
The folder `cutoff_files` contains the tree and log files of the subsets that have been considers congerent subsets by the tree GR diagnostic.
These can be used as regular BEAST2 outputs, i.e. the log files can be analysed in tracer or tree files can be input into the treeannotator software.
