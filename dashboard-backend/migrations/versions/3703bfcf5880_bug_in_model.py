"""bug in model

Revision ID: 3703bfcf5880
Revises: 2aeea9bdeb73
Create Date: 2020-07-03 22:01:02.314758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3703bfcf5880'
down_revision = '2aeea9bdeb73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('publications', sa.Column('type_of', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('publications', 'type_of')
    # ### end Alembic commands ###
