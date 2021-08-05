import numpy as np
import sys

def main():
    """ block_to_2Darray creates a new text file that reorganizes a year block format to a 2D array with
    each row containing a year of Gauss coefficients.
    Reference block_to_2Darray.ipynb for more details on how code works.
    Input   : [1] document is a string with the document name
            : [2] blocklinelen is the number of lines in a year block in the text document
            : [3] saveDocument is a string the 2D array will save as
    Output  : coeff2D is a 2D array with each row containing a time increment of Gauss coefficients
    """

    document     = sys.argv[1]
    blocklinelen = sys.argv[2]
    saveDocument = sys.argv[3]

    assert type(document)     == str, 'document is not a string'
    assert type(saveDocument) == str, 'saveDocument is not a string'

    blocklinelen              = int(blocklinelen)
    lines                     = get_lines(document)
    [linecount, eachLine]     = get_eachline(lines, blocklinelen)
    year                      = get_years(lines, blocklinelen)
    l_degree, totalGC         = get_degree(eachLine)
    coeff2D                   = create_2Darray(lines, blocklinelen, totalGC, eachLine)

    print('g10 std:', np.std(coeff2D[:,1]), 'mean:', np.mean(coeff2D[:,1]),'min:', np.min(coeff2D[:,1]),'max:', np.max(coeff2D[:,1]))
    print('g11 std:', np.std(coeff2D[:,2]), 'mean:', np.mean(coeff2D[:,2]),'min:', np.min(coeff2D[:,2]),'max:', np.max(coeff2D[:,2]))
    print('h11 std:', np.std(coeff2D[:,3]), 'mean:', np.mean(coeff2D[:,3]),'min:', np.min(coeff2D[:,3]),'max:', np.max(coeff2D[:,3]))

    np.savetxt(saveDocument, coeff2D)


#####################################################################

# get_lines: reads in lines from the text document
# with open(): context manager, closes file when leaving unindented
# readlines: reads lines as individual elements in the list

def get_lines(textdoc):
    """Reads in a text document.
    Input : textdoc needs to be in string format
    Output: lines comes out as a list, each element in the list is a
            in the text document
    """
    assert type(textdoc) == str, 'textdoc is not a string'
    
    with open(textdoc, mode='r') as f:
        lines = f.readlines()
        
    return lines

# get_eachline: Gets the number per line in a year block and total years
# np.fromstrings: converts the list element string to array float
# for loop: Get the length of each line in a year block
# calculates the total lines in the text document

def get_eachline(lines, blocklinelen):
    """Gets the number of elements in each line for a year block and
    calculate the total number of years.
    Input   : lines is a list, in each element is a line in the text document
            : blocklinelen is the number of lines in a year block in the text document
    Output  : linecount is an integer of the total text document line length
            : eachLine is an array containing the elements in each block of line
    """
    
    assert type(lines)        == list, 'lines is not a list'
    assert type(blocklinelen) == int , 'block line length is not an integer'
    
    eachLine = np.zeros(blocklinelen)
    j = 0
    for index in range(0,blocklinelen):
        blockLine   = np.fromstring(lines[index], dtype=float, sep=' ')
        eachLine[j] = len(blockLine)
        j += 1
        
    linecount  = len(lines)
    totalYears = linecount/blocklinelen
    
    assert totalYears.is_integer(), 'An uneven number of block lines with total years'
    
    print('The total number of lines in the text document:', linecount)
    print('The length of each line is:', eachLine)
    print('The total year blocks:', totalYears)
    
    return linecount, eachLine

# get_years: Extracts the years
# Similar to above cell script
# for loop: collects the year from lines 0, blocklinelen, 2*blocklinelen, ...

def get_years(lines, blocklinelen):
    """ Extracts the years from the lines at the blocklinelen multiple
    Input   : lines is a list, in each element is a line in the text document
            : blocklinelen is the number of lines in a year block in the text document
    Output  : year is a 1-D array of the years
    """
    assert type(lines)        == list, 'lines is not a list'
    assert type(blocklinelen) == int , 'block line length is not an integer'
    
    linecount  = len(lines)
    totalYears = int(linecount/blocklinelen)
    
    year = np.zeros(int(totalYears))
    j=0
    
    for index, line in enumerate(lines, 0):
        if (index % blocklinelen) == 0:
            yearList = np.fromstring(lines[index], dtype=float, sep=' ')
            year[j] = yearList[0]
            j += 1
            
            if j>1:
                assert year[j-1] >= year[j-2], 'Years is not in chronological order'
        
    if len(np.unique(np.diff(year, n=1))) > 1: 
        print('THE YEARS ARE NOT EQUALLY SPACED!!!')
   
    assert len(np.unique(year)) == totalYears , 'There are duplicate years'
    
    return year

# get_degree: Calculates the degree and order
# * Total Gauss Coefficients per year $=2l +1 $
# * While loop: subtracts from the total coefficients in an increasing order until zero

def get_degree(eachLine):
    """ Calculates the degree and order from the total element length of a year block
    Input   : lines is a list, in each element is a line in the text document
            : blocklinelen is the number of lines in a year block in the text document
    Output  : l is the Gauss coefficient degree
            : totalGC is the total number of coefficients per year
    """
    
    assert type(eachLine) == np.ndarray
    
    totalGC = int(sum(eachLine)-1)
    countGC = totalGC
    
    l = 1
    while countGC > 0:
        countGC = countGC - (2*l+1)
        l+=1
    l = l-1
    
    assert countGC == 0, 'The number of cofficients does not equal 2l+1 amounts'
    
    print('Total coefficients per year:', totalGC)
    print('The degree and order is'     , l      )
    
    return l, totalGC

# create_2Darray: Put together the matrix
# for loop: similar to the loops above but creates a 2-D array with every row containing on year of coefficients

def create_2Darray(lines, blocklinelen, totalGC, eachLine):
    """
    Creates the 2D array
    Input   : lines is a list, in each element is a line in the text document
            : blocklinelen is the number of lines in a year block in the text document
    Output  : coeff is the coefficients of the 2D array
    """
    
    assert type(lines)        == list, 'lines is not a list'
    assert type(blocklinelen) == int , 'block line length is not an integer'
    assert type(totalGC)      == int , 'totalGC is not an integer'
     
    coeff = np.zeros((int(len(lines)/blocklinelen), int(totalGC+1)))
    row   = 0
    j     = 0

    for index, line in enumerate(lines, 0):
        
        yearList   = np.fromstring(lines[index], dtype=float, sep=' ')
        elementLen = len(yearList)
        
        assert type(yearList) == np.ndarray, 'One row line is not an array'

        if ((index % blocklinelen) == 0) and (index!=0):
            row += 1
            j    = 0
            
        if (index % blocklinelen) == 0:
            col=0
            coeff[row, col:elementLen]       = yearList
        else:
            coeff[row, col:(elementLen+col)] = yearList
            
        col+=elementLen
        
        assert elementLen == eachLine[j], 'The length of the line is not the correct'
        j+=1
    
    assert coeff.shape  == (int(len(lines)/blocklinelen), int(totalGC+1))
    
    return coeff


if __name__ == '__main__':
    main()