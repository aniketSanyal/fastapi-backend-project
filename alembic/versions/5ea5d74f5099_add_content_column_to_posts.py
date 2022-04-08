"""add content column to posts

Revision ID: 5ea5d74f5099
Revises: e18f9e1bff15
Create Date: 2022-04-07 13:09:19.377275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ea5d74f5099'
down_revision = 'e18f9e1bff15'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    pass
