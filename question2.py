class Person:
    def __init__ (self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name =  last_name
        self.father = father

def iterable(item):
    '''
    check if item is dict or person object 
    '''
    if isinstance(item,dict) or isinstance(item,Person):
        return True
    return False


def print_depth(lst, lvl=1):
    '''
    find depth of each key in Nested Dict
    returns a string
    '''
    ans=''
    if isinstance(lst,Person):
        #print('first_name: ',lvl)
        #print('last_name: ',lvl)
        #print('father: ',lvl)
        ans+='first_name: '+str(lvl)+'\n'
        ans+='last_name: '+str(lvl)+'\n'
        ans+='father: '+str(lvl)+'\n'
        if iterable(lst.first_name):
            ans+=print_depth(lst.first_name,lvl+1)
        if iterable(lst.last_name):
            ans+=print_depth(lst.last_name,lvl+1)
        if iterable(lst.father):
            ans+=print_depth(lst.father,lvl+1)
    if isinstance(lst,dict):
        for key in lst:
            #print(key+': ',lvl)
            ans+=str(key)+': '+str(lvl)+'\n'
            val = lst[key]
            if iterable(val):
                ans+=print_depth(val,lvl+1)

    return ans

person_a = Person('User', '1', None)
person_b = Person('User', '2', person_a)

a= {'key1':1,
    'key2':{
        'key3':1,
        'key4':{
            'key5':5,
            'user':person_b,
        }
    }
}

print(print_depth(a))

    