"""empty message

Revision ID: 136bc4841a85
Revises: 350dcca3429b
Create Date: 2022-11-02 18:35:00.211384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '136bc4841a85'
down_revision = '350dcca3429b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comentario', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###
