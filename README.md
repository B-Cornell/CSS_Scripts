# CSS_Scripts
Project constraining the angle alpha of well known galaxy cluster mergers.

-----------

1. Retrieve all possible clusters at Redshift 0 over 6e13 solar masses. Sorted by x position.

Code- SQL on cosmosim website

Input- BigMDPL database

Output- BigMDPL_6e13_X_depthfirstid.csv

-----------

2. Find all pairs of clusters within 5Mpc of eachother.

Code- CosmoSimSeparationCutoff.py

Input- BigMDPL_6e13_X_depthfirstid.csv

Output- reduced_cosmo_pairs.txt

-----------

3. Check all of the pairs are bimodal. This makes sure we only use pairs where both halos aren't part of any other pairs

Code-uniquepair.cpp

Input- reduced_cosmo_pairs.txt

Output- uniquedata.csv

----------

4. Get tree data for all possible pairs

Code- SQL on website

Input- BigMDPL database

Output- trees/Trees_sn68_m6e13_X00_Y00.csv

----------

5. Attach MainleafIds to each of the halos in the viable pairs.

Code- mainleaffinder.py

Input- uniquedata.csv

Output- realmainleafdfifds.csv

----------

6. Find all pairs that have been within .35 Mpc in the last 1.8 Gyrs

Code- treesfinder[X00].py

Input- realmainleafdfids.csv trees/Trees_sn68_m6e13_X00_Y00.csv

Output- treefile_X00_Y00.csv

----------

7. Manually push all of the treefiles together and run probability finding code

Code- CosmoSimProbabilityFinder.py

Input-treesfile

Output- DataFiles/XXX.txt

----------

8. Show all the PDFs of each cluster at different impact parameters

Code- PDFmaker.py

Input- (copied DataFiles into PDFmaker.py)

Output- PDFs of each cluster
