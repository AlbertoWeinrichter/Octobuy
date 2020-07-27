"""initial

Revision ID: 2aeea9bdeb73
Revises:
Create Date: 2020-06-17 13:20:44.826626

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2aeea9bdeb73"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "publications",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=256), nullable=True),
        sa.Column("description", sa.String(length=256), nullable=True),
        sa.Column("slug", sa.String(length=256), nullable=False),
        sa.Column("comments_count", sa.Integer(), nullable=True),
        sa.Column("reactions_count", sa.Integer(), nullable=True),
        sa.Column("published_at", sa.Date(), nullable=True),
        sa.Column("created_at", sa.Date(), nullable=True),
        sa.Column("edited_at", sa.Date(), nullable=True),
        sa.Column("cover_image", sa.String(length=256), nullable=True),
        sa.Column("social_image", sa.String(length=256), nullable=True),
        sa.Column("body_html", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("publications")
    # ### end Alembic commands ###
