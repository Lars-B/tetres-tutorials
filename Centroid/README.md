# Reference

If you publish a paper using this software, please cite<br>
Lars Berling, Lena Collienne, and Alex Gavryushkin<br>
**Estimating the mean in the space of ranked phylogenetic trees**<br>
*bioRxiv* 2023<br>
[https://doi.org/10.1101/2023.05.08.539790](https://doi.org/10.1101/2023.05.08.539790) 


# Execute

Execute the script via `python DS1-centroid.py` in the command line. This will create the nexus tree file `centroid_{sos-value}.trees`.

## Further annotations

The output of this script produces a NEXUS file that can be used in the BEAST treeannotator software.
Using the option `keep-target-tree-heights` treeannotator can be used to summarize other parameters from the beast 
 analysis on top of the centroid tree. 

In the terminal you can run this via
`Path/to/BEAST/bin/treeannotator -heights keep -target centroid_{sos-value}.tree DS1.trees annotated_centroid{sos-value}.tree`
or use the GUI provided.
