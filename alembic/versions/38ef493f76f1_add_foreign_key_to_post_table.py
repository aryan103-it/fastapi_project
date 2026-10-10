"""add Foreign-key to post table

Revision ID: 38ef493f76f1
Revises: 407c9d47dbac
Create Date: 2026-10-08 22:35:36.532921

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "38ef493f76f1"
down_revision: Union[str, Sequence[str], None] = "407c9d47dbac"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("user_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fkey",
        source_table="posts",
        referent_table="users",
        local_cols=["user_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("posts_users_fkey", table_name="posts")
    op.drop_column("posts", "user_id")

    pass
