


def print_depth(lst, lvl=1):
    '''
    find depth of each key in Nested Dict
    returns a string
    '''
    ans=''
    for ele in lst:
        val = lst[ele]
        #print(ele+' ',lvl)
        ans+=ele+' '+str(lvl)+'\n'
        if isinstance(val,dict):
            ans+=print_depth(val,lvl+1)
    return ans


a= {'key1':1,
    'key2':{
        'key3':1,
        'key4':{
            'key5':5,
        }
    }
}

print(print_depth(a))
    