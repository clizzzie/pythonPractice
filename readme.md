## convertGGFtext2plottingtext:
jupyter notebook used to convert GGF100k coefficients to a text that is readable by python
or matlab

Eventually want to create a function that takes in the line length of a block of year data
as an argument and outputs a plottable text file in matrix format

## Text file format:
Block format starting with the year and following coefficient in correct order
The location of each cofficient has to be the same within each block. The size of each line does not matter.

#### Example: ggf100k
$ year \quad g_{1}^{0} ... h_{4}^{4} $ &emsp; 25 elements <br>
$ g_{5}^{0} ... h_{6}^{6}   $ &emsp;  24 elements <br>
$ g_{7}^{0} ... h_{8}^{4}   $ &emsp; 24 elements<br>
$ g_{5}^{0} ... h_{6}^{6}   $ &emsp; 24 elements <br>
$ g_{8}^{9} ... h_{10}^{10} $ &emsp; 24 elements

$ year+1 \quad g_{1}^{0} ... h_{4}^{4} $ &emsp; 25 elements <br>
$ g_{5}^{0} ... h_{6}^{6}   $ &emsp;  24 elements <br>
$ g_{7}^{0} ... h_{8}^{4}   $ &emsp; 24 elements<br>
$ g_{5}^{0} ... h_{6}^{6}   $ &emsp; 24 elements <br>
$ g_{8}^{9} ... h_{10}^{10} $ &emsp; 24 elements <br>
