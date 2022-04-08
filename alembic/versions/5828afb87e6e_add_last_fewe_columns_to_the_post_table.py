"""add last few columns to the post table

Revision ID: 5828afb87e6e
Revises: bd6971550af2
Create Date: 2022-04-07 14:02:59.426844

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '5828afb87e6e'
down_revision = 'bd6971550af2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass