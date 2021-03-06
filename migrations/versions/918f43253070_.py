"""empty message

Revision ID: 918f43253070
Revises: 
Create Date: 2017-10-15 10:44:52.905096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '918f43253070'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CONTINENTS',
    sa.Column('id', sa.String(length=2), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('COUNTRIES',
    sa.Column('id', sa.String(length=2), nullable=False),
    sa.Column('continent_id', sa.String(length=2), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['continent_id'], ['CONTINENTS.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('CITIES',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ascii_name', sa.String(length=80), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('country_code', sa.String(length=2), nullable=False),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('elevation', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['country_code'], ['COUNTRIES.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('CITIES')
    op.drop_table('COUNTRIES')
    op.drop_table('CONTINENTS')
    # ### end Alembic commands ###
