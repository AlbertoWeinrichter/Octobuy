"""publication

Revision ID: 0556ae6a92b4
Revises: 9a08d907be80
Create Date: 2020-07-03 23:03:46.789241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0556ae6a92b4'
down_revision = '9a08d907be80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('publications', 'title',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.alter_column('publications', 'type_of',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.create_unique_constraint(None, 'publications', ['title'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'publications', type_='unique')
    op.alter_column('publications', 'type_of',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.alter_column('publications', 'title',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    # ### end Alembic commands ###
