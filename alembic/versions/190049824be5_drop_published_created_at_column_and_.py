"""Drop published, created_at column and add content column

Revision ID: 190049824be5
Revises: e2c198c2391c
Create Date: 2026-10-08 22:13:28.690800

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '190049824be5'
down_revision: Union[str, Sequence[str], None] = 'e2c198c2391c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    op.add_column('posts', 
                  sa.Column('content', sa.String(), nullable=False)
                  )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    op.add_column('posts',sa.Column("published", sa.Boolean(), default=True))
    op.add_column('posts',sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()')))
    pass
