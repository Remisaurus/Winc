
def flatten_dict(dict):
    list = []
    for key in dict:
        list.append(dict[key])
    return list



def flatten_dict_extra_challenge(dict):
    list = []
    for key in dict:
        if type(dict[key]) == type({}):
            def deeperdicts(dictkey):
                for key in dictkey:
                    if type(dictkey[key]) == type({}):
                        deeperdicts(dictkey[key])
                    else:
                        list.append(dictkey[key])
            deeperdicts(dict[key])
        else:
           list.append(dict[key])
    return list
