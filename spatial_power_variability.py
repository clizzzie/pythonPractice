import numpy as np

# Personal modules:
from Array2D_to_dictionary import get_degree

def main(dictionary_array, needed_l):
    """Calculates the spatial power variability
    Refer to SpatialPowerVariability.ipynb for more details on the code
    Input   : dictionary_array is a dictionary with the coefficients as keys
    Input   : needed_l is the desired degree
    Output  : R is a column of spatial power variability as a time series
    """

    assert type(dictionary_array) == dict   , 'dictionary_array is not a dictionary'
    assert type(needed_l)         == int    , 'needed_l is not an integer'
    assert needed_l               > 0       , 'needed_l is not greater than zero'

    # get degree and order
    degreeAndOrder = get_degree(len(dictionary_array)-1)
    
    assert needed_l <= degreeAndOrder, 'needed_l is greater than degree and order of dictionary' 

    # convert dictionary keys as a list
    GClist         = list(dict.keys(dictionary_array))

    # get the keys for the dictionary for a specific degree
    lforR_list     = get_l_from_GClist(GClist, needed_l)

    # calculate spatial power variablility 
    R              = calculate_R(dictionary_array, lforR_list, needed_l)

    print_R_stats(R, needed_l)

    return R

###########################################################################

# ### get_l_from_GClist
# Uses GClist to extract the l's from the dictionary keys

def get_l_from_GClist(GClist, l):
    """Gets the string elements for specific degree order
    Input   : GClist should be a list containing all the dictionary keys
    Input   : l is the desired degree
    Output  : lforR is a list that contains only the dictionary keys with the degree
    """

    assert type(GClist) == list , 'GClist is not a list'
    assert type(l)      == int  , 'l is not an integer'
    
    lforR=[]
    for index in GClist:
        underScore = index.find('_')
        if index[1:underScore] == str(l):        
            lforR.append(index)    
    
    assert len(lforR) == (2*l+1), "The length of the list is the wrong size"
    
    return lforR

# ### calculate_R: calculates the spatial power variability
# #### Spatial power variability equation:
# 
# $ R_{l}\left( t\right) =\left( l+1\right) \sum ^{l}_{m=0}\left\{ \left[ g_{l}^{m}\left( t\right) \right] ^{2}+\left[ h_{l}^{m}\left( t\right) \right] ^{2}\right\} $

def calculate_R(diction_array, list_lforR, needed_l):
    """Calculates the spatial power variability for a single degree
    Input   : diction_array is the dictionary that contains the coefficients in ndarray format
    Input   : list_lforR is the list that contains the strings that call the diction_array
    Output  : R is the spatial power variability for a single degree in column form
    """

    assert type(diction_array)  == dict, 'diction_array is not a dictionary'
    assert type(list_lforR)     == list, 'list_lforR is not a list'
    
    arrayLen = len(diction_array['year'])

    R = np.zeros(arrayLen)
    for index in list_lforR:
        
        assert type(diction_array[index]) == np.ndarray, 'Dictionary element is not an array'
        assert len(diction_array[index])  == arrayLen  , 'Array length is not the right size'
 
        R += np.square(diction_array[index])
    
    R = (needed_l+1)*R
    R = (np.array([R])).T

    return R

def print_R_stats(R, needed_l):
    print('R_',needed_l,'(t)','min:', np.min(R), 'mean:',np.min(R), 'max:', np.max(R), 'std:',np.std(R))

if __name__ == '__main__':
    main()