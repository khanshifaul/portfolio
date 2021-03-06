"""empty message

Revision ID: 00bbdc259489
Revises: 
Create Date: 2020-01-11 05:34:55.740207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00bbdc259489'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('subject', sa.String(length=50), nullable=False),
    sa.Column('message', sa.String(length=250), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_message_date'), 'message', ['date'], unique=False)
    op.create_index(op.f('ix_message_email'), 'message', ['email'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_index(op.f('ix_message_email'), table_name='message')
    op.drop_index(op.f('ix_message_date'), table_name='message')
    op.drop_table('message')
    # ### end Alembic commands ###
