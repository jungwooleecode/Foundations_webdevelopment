"""first

Revision ID: e9650ab25e96
Revises: 
Create Date: 2022-04-26 21:54:42.390936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9650ab25e96'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('password', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workshop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('teacher', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Numeric(precision=20, scale=2), nullable=True),
    sa.Column('fixed_spots', sa.Integer(), nullable=True),
    sa.Column('available_spots', sa.Integer(), nullable=True),
    sa.Column('picture_url', sa.String(length=260), nullable=True),
    sa.Column('video_url', sa.String(length=260), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('userinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('workshop_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['workshop_id'], ['workshop.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userinfo')
    op.drop_table('workshop')
    op.drop_table('user')
    # ### end Alembic commands ###