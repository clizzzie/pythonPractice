import numpy as np

def main(diction_str, listOfComponents = ['\n', '[', ']']):
    """Converts the dictionary elements from a string to ndarray (json?)
    Input   : diction_str is a dictionary with elements as a string
    Input   : listOfComponents is a list of strings that are unwanted in the strings
    Output  : a new dictionary with elements as np.ndarray
    """

    assert type(diction_str)        == dict, 'dict_str is not a dictionary'
    assert type(listOfComponents)   == list, 'listOfComponents is not a list'

    # get the dictionary keys as a list
    dict_keys = list(dict.keys(diction_str))

    # convert string to array
    diction_array = string_to_array(diction_str, dict_keys)

    return diction_array

def remove_str_components(string, listOfComponents = ['\n', '[', ']']):
    """Removes characters from a string
    Input   : string
    Input   : listOfComponents is a list of the characters to be removed from the string
    Output  : new is the new string without the characters
    """

    assert type(string)           == str  , 'string is not a string'
    assert type(listOfComponents) == list , 'listOfComponents is not a list'
    
    new = string
    for index in listOfComponents:
        withoutComponents = new.replace(index, '')
        new = withoutComponents
    
    return new

def string_to_array(dict_str, dict_keys, listOfComponents = ['\n', '[', ']']):
    """Converts the dictionary elements from strings to ndarrays
    Input   : dict_str is original dictionary with element strings
    Input   : dict_keys is a list of keys for the dictionary
    Input   : listOfComponents is a list of strings that are unwanted in the strings
    Output  : dict_array is the converted dictionary with np.ndarray elements
    """

    assert type(dict_str)           == dict, 'dict_str is not a dictionary'
    assert type(dict_keys)          == list, 'dict_keys is not a list'
    assert type(listOfComponents)   == list, 'listOfComponents is not a list'

    dict_array = {}
    for index, key in enumerate(dict_keys):
        array = np.fromstring(remove_str_components(dict_str[key],listOfComponents), sep=' ')
        dict_array[key] = array

        if index > 0:
            assert len(dict_array[dict_keys[index]]) == len(dict_array[dict_keys[index-1]]), 'The dictionary arrays are not the same length'

    return dict_array

if __name__ == '__main__':
    main()