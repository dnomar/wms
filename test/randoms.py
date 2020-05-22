import uuid

def random_suffix():
    return uuid.uuid4().hex[:6]


def random_sku(name=''):
    return f'sku-{name}-{random_suffix()}'


def random_product(name=''):
    return f'product-{name}-{random_suffix()}'


def random_orderid(name=''):
    return f'order-{name}-{random_suffix()}'


def random_space(name=''):
    return f'space-{name}-{random_suffix()}'
