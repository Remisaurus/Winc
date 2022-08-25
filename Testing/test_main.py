import main

def test_get_none():
    assert main.get_none() == None
    
def test_flatten_dict():
    assert type(main.flatten_dict({1:2,3:4,5:6,7:[8,9]})) == type([])
    assert main.flatten_dict({1:2,3:4,5:6,7:[8,9]}) == [2,4,6,[8,9]]
    
def test_flatten_dict_extra_challenge():
    assert type(main.flatten_dict_extra_challenge({1:2,3:4,5:6,7:[8,9]})) == type([])
    assert main.flatten_dict_extra_challenge({1:2,3:4,5:6,7:{8:9,10:11}}) == [2,4,6,9,11]
    assert main.flatten_dict_extra_challenge({1:2,3:4,5:6,7:{8:9,10:11},12:{13:14,15:{16:17,18:19}}}) == [2,4,6,9,11,14,17,19]