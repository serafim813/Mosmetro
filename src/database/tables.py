import sqlalchemy as sa

metadata = sa.MetaData()

news = sa.Table(
    'news',
    metadata,
    sa.Column('id', sa.BigInteger, primary_key=True),
    sa.Column('header', sa.String, nullable=False),
    sa.Column('image', sa.String, nullable=False),
    sa.Column('date', sa.Date, nullable=False),
    sa.Column('item', sa.String, nullable=False),
)
