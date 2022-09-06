import stock_manipulation

def test_stock_manipulation():
    stock_manipulation.products[1] = stock_manipulation.product(1, 'test', 44, 5.5, 'now','not yet', False)
    stock_manipulation.products[2] = stock_manipulation.product(2, 'testprod', 44, 5.5, 'now','not yet', False)
    stock_manipulation.products[3] = stock_manipulation.product(3, 'prodtest', 44, 5.5, 'now','not yet', False)
    stock_manipulation.products[4] = stock_manipulation.product(4, 'test', 44, 6.5, 'tomorrow','not yet', False)
    
    assert stock_manipulation.products[1].quantity == 44
    
def test_get_new_id():
    assert stock_manipulation.get_new_id() == 5
    
def test_product_exists():
    assert stock_manipulation.product_exists('test')
    assert not stock_manipulation.product_exists('unexisting product')
    
def test_product_id_checker():
    assert stock_manipulation.product_id_checker('test') == [1, 4]
    assert stock_manipulation.product_id_checker('prodtest') == [3]
    assert stock_manipulation.product_id_checker('product') == False
    
def test_new_product_is_different():
    assert stock_manipulation.new_product_is_different('test', 'not yet', 6.5, True) == True
    assert stock_manipulation.new_product_is_different('test', 'not yet', 6.5, False) == 4
    assert stock_manipulation.new_product_is_different('test', 'not yet', 5.5, False) == 1
    assert stock_manipulation.new_product_is_different('test', 'yet', 5.5, False) == True
    stock_manipulation.products[55] = stock_manipulation.product(55, 'prodtest', 44, 6.5, 'now','not yet', False)
    assert stock_manipulation.new_product_is_different('prodtest', 'not yet', 6.5, False) == 55
    
def test_add_stock():
    stock_manipulation.add_stock('new stuff', 50, 1, 'now')
    assert stock_manipulation.products[56].name == 'new stuff'
    assert type(stock_manipulation.products[56].buy_datums) == type({})
    assert stock_manipulation.products[1].quantity == 44
    stock_manipulation.add_stock('test', 100, 5.5, 'not yet')
    assert stock_manipulation.products[1].quantity == 144
    assert len(stock_manipulation.products[1].buy_datums) == 2
   
def test_removing_stock():
    assert stock_manipulation.removing_stock('Not here') == 'not found'
    assert stock_manipulation.products[1].name == 'test'
    stock_manipulation.removing_stock('test')
    try:
        assert not stock_manipulation.products[1]
    except KeyError:
        assert stock_manipulation.products[2].name == 'testprod'
    try:
        assert not stock_manipulation.products[4]
    except KeyError:
        assert stock_manipulation.products[55].name == 'prodtest'
    assert stock_manipulation.products[2].name == 'testprod'
    assert stock_manipulation.products[55].name == 'prodtest'
    