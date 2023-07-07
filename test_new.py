def aggregate_avg(data):
    ''' A function that aggregates a list of 2-tuples into a dictionary. 
    The average of values for each unique key is aggregated.
    Parameters:
    data - takes the list of 2-tuples.
    Return:
    The function returns the aggregated dictionary.
    '''
    just_dict = {}
    for i in data:
        key, value = i
        if key not in just_dict:
            just_dict[key] = []
        
        just_dict[key].append(value)

    for k, v in just_dict.items():
        res = (sum(v) / len(v))
        res_format = f'{res:.1f}'
        just_dict[k] = res_format

    return just_dict

def dicts_symmetric_difference(first_dict, second_dict):
    ''' A function that returns a new dictionary where duplicate keys are excluded.
    Parameters:
    first_dict - the first dictionary.
    second_dict - the second dictionary.
    Return;
    The functions returns the resulting dictionary
    '''
    result = {}
    for name_1, age_1 in first_dict.items():
        if name_1 not in second_dict:
            result[name_1] = age_1

    for name_2, age_2 in second_dict.items():
        if name_2 not in first_dict:
            result[name_2] = age_2
    
    return result

def merge_tuples(first_tuple, second_tuple):
    '''Returns a list of 2-tuples that is the product of the merging of two variable-length tuples. 
    None is used to fill missing values in case of different lengths.
    Parameters:
    first_tuple (tuple) - gives the first tuple
    second_tuple (tuple) - gives the second tuple
    Return:
    The function returns a list containing the merge 2-tuples
    '''
    list_of_tuples = []
    first = list(first_tuple)
    second = list(second_tuple)
    if len(first) > len(second):
        for _ in range(len(first) - len(second)):
            second.append(None)
    else:
        for _ in range(len(second) - len(first)):
            first.append(None)
    
    for i, j in zip(first, second):
        res = i, j
        list_of_tuples.append(res)
    
    return list_of_tuples

def concat_tuples(*tuples):
    ''' A function that returns a new tuple that is the result of the concatenation of zero or more other tuples.
    Parameters: 
    *tuples - the function can accept zero or more tuples to concat.
    return - the function returns the resutlt of the concatination.
    '''
    result = ()
    if len(tuples) == 0:
        return ()
   
    for i in tuples:
        result += i

    return result





