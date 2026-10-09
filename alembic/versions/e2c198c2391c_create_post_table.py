"""create_post table

Revision ID: e2c198c2391c
Revises: 
Create Date: 2026-10-08 21:52:28.263613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2c198c2391c'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("posts",
                    sa.Column('id', sa.Integer(), primary_key= True, nullable=False),
                    sa.Column('title', sa.String(), nullable=False, unique=True),
                    sa.Column("published", sa.Boolean(), default=True),
                    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'))
                    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
