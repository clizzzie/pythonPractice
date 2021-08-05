
# block_to_2Darray.py:
Converts a block style format of a text document to a 2D array with rows containing all Gauss coefficients per block. See text file format for a visual. <br>
Arguments:
* [1] textDoc.txt: original text document
* [2] numberOfLines: number of lines in a block of data
* [3] savedDoc.txt: converted text document

command line: $ python block_to_2Darray.py textDoc.txt numberOfLines savedDoc.txt

## Text file formats:
Block format starting with the year and following coefficient in correct order
The location of each cofficient has to be the same within each block. The size of each line does not matter.

#### Example: ggf100k  (BEFORE)
$ year \quad g_{1}^{0} ... h_{4}^{4} $ &emsp; 25 elements <br>
$ g_{5}^{0} ... h_{6}^{6}   $ &emsp;  24 elements <br>
$ g_{7}^{0} ... h_{8}^{4}   $ &emsp; 24 elements <br>
$ g_{5}^{0} ... h_{6}^{6}   $ &emsp; 24 elements <br>
$ g_{8}^{9} ... h_{10}^{10} $ &emsp; 24 elements

$ year+1 \quad g_{1}^{0} ... h_{4}^{4} $ &emsp; 25 elements <br>
$ g_{5}^{0} ... h_{6}^{6}   $ &emsp;  24 elements <br>
$ g_{7}^{0} ... h_{8}^{4}   $ &emsp; 24 elements <br>
$ g_{5}^{0} ... h_{6}^{6}   $ &emsp; 24 elements <br>
$ g_{8}^{9} ... h_{10}^{10} $ &emsp; 24 elements <br>

The new text file is a 2-D array with every row containing on year of coefficients <br>

#### Example: 2-D array of ggf100k (NEW)
year     $ \quad g_{1}^{0} ... g_{4}^{3}  h_{4}^{3} g_{4}^{4} h_{4}^{4} ...  h_{10}^{10} \quad $ 121 elements  <br>
year+1  $ g_{1}^{0} ... g_{4}^{3} h_{4}^{3} g_{4}^{4} h_{4}^{4} ...  h_{10}^{10} \quad $ 121 elements <br>

## block_to_2Darray.ipynb:
This is the reference notebook for block_to_2Darray.py on how the code works.

