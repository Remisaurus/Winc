import stock_manipulation

def test_stock_manipulation():
    stock_manipulation.products[1] = stock_manipulation.product(1, 'test', 44, 5.5, 'now','not yet')
    stock_manipulation.products[2] = stock_manipulation.product(2, 'testprod', 44, 5.5, 'now','not yet')
    stock_manipulation.products[3] = stock_manipulation.product(3, 'prodtest', 44, 5.5, 'now','not yet')
    assert stock_manipulation.products[1].quantity == 44
    
def test_product_exists():
    assert stock_manipulation.product_exists('test')
    assert not stock_manipulation.product_exists('unexisting product')
    
def test_product_id_checker():
    assert stock_manipulation.product_id_checker('test') == 1
    assert stock_manipulation.product_id_checker('prodtest') == 3
    assert stock_manipulation.product_id_checker('product') == 4
    
def test_new_product_expiry_date_is_different():
    assert stock_manipulation.new_product_expiry_date_is_different('test', 'not yet') == False
    assert stock_manipulation.new_product_expiry_date_is_different('test', 'yet') == True
    
def test_product_id_checker_with_expiry_date():
    assert stock_manipulation.product_id_checker_with_expiry_date('test', 'other date') == 4
    assert stock_manipulation.product_id_checker_with_expiry_date('test', 'not yet') == 1
 
def test_add_stock():
    assert stock_manipulation.products[1].quantity == 44
    stock_manipulation.add_stock('test', 100, 5.5, 'not yet')
    assert stock_manipulation.products[1].quantity == 144
    assert len(stock_manipulation.products[1].buy_datums) == 2
    stock_manipulation.add_stock('new stuff', 50, 1, 'now')
    assert stock_manipulation.products[4].name == 'new stuff'
    assert type(stock_manipulation.products[4].buy_datums) == type({})