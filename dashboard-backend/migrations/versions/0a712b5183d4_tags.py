"""tags

Revision ID: 0a712b5183d4
Revises: 0e2557fdb1a5
Create Date: 2020-07-09 03:01:04.001915

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0a712b5183d4'
down_revision = '0e2557fdb1a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('publication', sa.Column('elements', postgresql.ARRAY(sa.String()), nullable=True))
    op.add_column('publication_tags', sa.Column('publication_id', sa.Integer(), nullable=False))
    op.add_column('publication_tags', sa.Column('tag_id', sa.Integer(), nullable=False))
    op.drop_constraint('publication_tags_department_id_fkey', 'publication_tags', type_='foreignkey')
    op.create_foreign_key(None, 'publication_tags', 'tag', ['tag_id'], ['id'])
    op.create_foreign_key(None, 'publication_tags', 'publication', ['publication_id'], ['id'])
    op.drop_column('publication_tags', 'department_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('publication_tags', sa.Column('department_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'publication_tags', type_='foreignkey')
    op.drop_constraint(None, 'publication_tags', type_='foreignkey')
    op.create_foreign_key('publication_tags_department_id_fkey', 'publication_tags', 'publication', ['department_id'], ['id'])
    op.drop_column('publication_tags', 'tag_id')
    op.drop_column('publication_tags', 'publication_id')
    op.drop_column('publication', 'elements')
    # ### end Alembic commands ###
