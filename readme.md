
# Block to 2D array (Terminal)
block_to_2Darray.py:
Converts a block style format of a text document to a 2D array with rows containing all Gauss coefficients per block. See text file format for a visual. <br>
Arguments:
* [1] textDoc.txt: original text document
* [2] numberOfLines: number of lines in a block of data
* [3] savedDoc.txt: converted text document

command line: $ python block_to_2Darray.py textDoc.txt numberOfLines savedDoc.txt

## Text file formats:
Block format starting with the year and following coefficient in correct order
The location of each cofficient has to be the same within each block. The size of each line does not matter.

### Example: ggf100k  (BEFORE)
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

The new text file is a 2-D array with every row containing a year of coefficients <br>

### Example: 2-D array of ggf100k (NEW)
year     $ \quad g_{1}^{0} ... g_{4}^{3}  h_{4}^{3} g_{4}^{4} h_{4}^{4} ...  h_{10}^{10} \quad $ 121 elements  <br>
year+1  $ g_{1}^{0} ... g_{4}^{3} h_{4}^{3} g_{4}^{4} h_{4}^{4} ...  h_{10}^{10} \quad $ 121 elements <br>

## block_to_2Darray.ipynb:
This is the reference notebook for block_to_2Darray.py on how the code works.

# 2D Array to Dictionary (Terminal)
2D_to_dictionary.py: Converts a np.ndarray to a dictionary. <br>
Arguments:
* [1] GCtxt.txt : original text document in 2D array format
* [2] saveDocument : converted json file as a dictionary 

command line: $ python 2D_to_dictionary.py GCtxt.txt savedDocument.json

## Text file format:
The text file should be a 2-D array with every row containing a year of coefficients <br>

### Example: ggf100k   (BEFORE)
year     $ \quad g_{1}^{0} ... g_{4}^{3}  h_{4}^{3} g_{4}^{4} h_{4}^{4} ...  h_{10}^{10} \quad $ 121 elements  <br>
year+1  $ g_{1}^{0} ... g_{4}^{3} h_{4}^{3} g_{4}^{4} h_{4}^{4} ...  h_{10}^{10} \quad $ 121 elements <br>

### Example: ggf100k    (NEW)
{'year': ['year year+1 ...'], 'g1_0' : ['...'], 'g1_1': ['...'],...}

## 2D_to_dictionary.ipynb:
This is the reference notebook for a 2D_to_dictionary.py. Not sure if the kernel supports import json or sys.

# Dictionary Element String to Array (Module)
dictionary_str2array.py is a module used to convert a dictionary element strings to a np.ndarray

{'key 1': '1 2 3 4'} to {'key 1': array([1 2 3 4])}

# Spatial Power Variability (Module)
spatial_power_variability.py is a module used to calculate the spatial power variability <br>
SpatialPowerVariability.ipynb: is the reference notebook for details on the code <br>
$ R_{l}\left( t\right) =\left( l+1\right) \sum ^{l}_{m=0}\left\{ \left[ g_{l}^{m}\left( t\right) \right] ^{2}+\left[ h_{l}^{m}\left( t\right) \right] ^{2}\right\} $

# PlotGC.ipynb:

# Text Documents

## ggf100k_coeffs
The original ggf100k Gauss coefficients of degree and order 10

## ggf100k_coeffs_2Darray.txt
This is the converted 2D array from the original ggf100k model text document