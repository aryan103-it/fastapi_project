"""Add published, created_at column

Revision ID: f38340534dfd
Revises: 190049824be5
Create Date: 2026-10-08 22:20:43.640427

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f38340534dfd'
down_revision: Union[str, Sequence[str], None] = '190049824be5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column("published", sa.Boolean(), default=True))
    op.add_column('posts',sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
