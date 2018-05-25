# CSS_Scripts
Project constraining the angle alpha of well known galaxy cluster mergers.

-----------

1. Retrieve all possible clusters at Redshift 0 over 6e13 solar masses. Sorted by x position.

Code- SQL on Cosmosim website

Input- BigMDPL database

Output- CSVFiles/BigMDPL_6E13_Snap_##.csv

-----------

2. Find all pairs of clusters within 5Mpc of eachother.

Code- CosmoSimSeparationCutoff.py

Input- CSVFiles/BigMDPL_6e13_X_depthfirstid.csv

Output- reduced_cosmo_pairs_increased_timeframe_##.txt

-----------

3. Check all of the pairs are bimodal. This makes sure we only use pairs where both halos aren't part of any other pairs

Code- uniquepairs.cpp

Input- reduced_cosmo_pairs.txt

Output- UniquePairData/separation_data_increased_timeframe##.csv

----------

4. Catalog the treehistory of each halo pair

Code- treemerger_increased_timeframe.py

Input- UniquePairData/separation_data_increased_timeframe##.csv

Output- full_tree_data_##.txt

----------

5. Check that each pair has merged exactly once in the past

Code- doubleperi.py

Input- full_tree_data_##.txt

Output- final_data_##.txt

----------

6. Perform the final calculations on each pair that create the PDFs we are interested in

Code- ProbabilityFinder.py

Input- final_data_##.txt

Output- DataFiles/ClusterPDFs.txt

----------

7. Displays the PDFs and CDFs of each cluster

Code- PDFmaker.py

Input- DataFiles/ClusterPDFs.txt

Output- Plots/

----------
