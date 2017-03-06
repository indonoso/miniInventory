"""empty message

Revision ID: f719fe7c700a
Revises: b8fa640ec739
Create Date: 2017-02-15 19:55:55.163798

"""

# revision identifiers, used by Alembic.
revision = 'f719fe7c700a'
down_revision = 'b8fa640ec739'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('production_needs', sa.Column('product', sa.Integer(), nullable=False))
    op.drop_constraint('production_needs_product_out_fkey', 'production_needs', type_='foreignkey')
    op.create_foreign_key(None, 'production_needs', 'product', ['product'], ['id_'])
    op.drop_column('production_needs', 'product_out')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('production_needs', sa.Column('product_out', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'production_needs', type_='foreignkey')
    op.create_foreign_key('production_needs_product_out_fkey', 'production_needs', 'product', ['product_out'], ['id_'])
    op.drop_column('production_needs', 'product')
    # ### end Alembic commands ###