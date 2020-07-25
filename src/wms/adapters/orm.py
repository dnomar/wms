from sqlalchemy import (
    Table, Column, Integer, String, Date,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship
from src.wms import model, config


warehouses = Table(
    'warehouses', config.MetaData(),
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('reference', String(255)),
)

'''batches = Table(
    'batches', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('reference', String(255)),
    Column('sku', ForeignKey('products.sku')),
    Column('_purchased_quantity', Integer, nullable=False),
    Column('eta', Date, nullable=True),
)

allocations = Table(
    'allocations', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('orderline_id', ForeignKey('order_lines.id')),
    Column('batch_id', ForeignKey('batches.id')),
)'''

'''products = Table(
    'products', metadata,
    Column('sku', String(255), primary_key=True),
    Column('version_number', Integer, nullable=False),
)
'''


def start_mappers():
    mapper(model.Warehouse, warehouses)
    '''    lines_mapper = mapper(model.OrderLine, order_lines)
    mapper(model.Batch, batches, properties={
        '_allocations': relationship(
            lines_mapper,
            secondary=allocations,
            collection_class=set,
        )})
    mapper(model.Product, products, properties={
        'batches': relationship(
            model.Batch, backref='product', order_by=batches.c.id
        )})
'''