import stock_manipulation

def test_stock_manipulation():
    stock_manipulation.products[1] = stock_manipulation.product(1, 'test', 44, 5.5, '5-9-2022','9-9-9999', False, 0, 0, '31-12-9999')
    stock_manipulation.products[2] = stock_manipulation.product(2, 'testprod', 44, 5.5, '5-9-2022','9-9-9999', False, 0, 0, '31-12-9999')
    stock_manipulation.products[3] = stock_manipulation.product(3, 'prodtest', 44, 5.5, '5-9-2022','9-9-9999', False, 0, 0, '31-12-9999')
    stock_manipulation.products[4] = stock_manipulation.product(4, 'test', 44, 6.5, '6-9-2022','9-9-9999', False, 0, 0, '31-12-9999')
    
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
    
    
def test_add_stock():
    stock_manipulation.add_stock('new stuff', 50, 1, '11-11-3111')
    assert stock_manipulation.products[5].name == 'new stuff'
    stock_manipulation.add_stock('test', 100, 5.5, '11-11-3111')
    assert stock_manipulation.products[6].quantity == 100
   
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
        assert stock_manipulation.products[3].name == 'prodtest'
    assert stock_manipulation.products[2].name == 'testprod'
    assert stock_manipulation.products[3].name == 'prodtest'

def test_selling_stock():
    assert stock_manipulation.selling_stock('new stuff', 100, 10) == 'not enough inventory'
    assert stock_manipulation.selling_stock('new stuff', 22, 10) == 'done'
    assert stock_manipulation.products[5].quantity == 28
    assert stock_manipulation.products[6].sell_status == 'True'
    
def test_sellable_stock_and_expired_items():
    assert stock_manipulation.print_expired_items() == 'no loss'
    assert stock_manipulation.sellable_stock('new stuff') == 28
    stock_manipulation.add_stock('new stuff', 10000000, 0.1, '1-1-1111')
    assert stock_manipulation.sellable_stock('new stuff') == 28
    assert stock_manipulation.print_expired_items() ==  1000000
    