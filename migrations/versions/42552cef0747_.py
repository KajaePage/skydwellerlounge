"""empty message

Revision ID: 42552cef0747
Revises: 
Create Date: 2022-04-12 19:22:41.068490

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '42552cef0747'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=80), nullable=True),
    sa.Column('lastname', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=400), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customerid', sa.Integer(), nullable=True),
    sa.Column('cartinfo', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customerid', sa.Integer(), nullable=True),
    sa.Column('eventtype', sa.String(length=80), nullable=True),
    sa.Column('session', sa.String(length=80), nullable=True),
    sa.Column('eventstatus', sa.String(length=80), nullable=True),
    sa.Column('eventdate', sa.String(length=80), nullable=True),
    sa.Column('eventtime', sa.String(length=80), nullable=True),
    sa.Column('expectguestCount', sa.Integer(), nullable=True),
    sa.Column('tablecount', sa.Integer(), nullable=True),
    sa.Column('specialrequests', sa.String(length=1000), nullable=True),
    sa.Column('phonenumber', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('itemtype', sa.String(length=80), nullable=True),
    sa.Column('itemtitle1', sa.String(length=200), nullable=True),
    sa.Column('itemtitle2', sa.String(length=200), nullable=True),
    sa.Column('itemprice1', sa.Integer(), nullable=True),
    sa.Column('itemprice2', sa.Integer(), nullable=True),
    sa.Column('itemdiscription', sa.String(length=1000), nullable=True),
    sa.Column('itemadditionaldetails', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customerid', sa.Integer(), nullable=True),
    sa.Column('orderdetails', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('status', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('menu')
    op.drop_table('events')
    op.drop_table('cart')
    op.drop_table('accounts')
    # ### end Alembic commands ###
