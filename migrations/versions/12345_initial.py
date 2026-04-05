"""Initial migration"""

from alembic import op
import sqlalchemy as sa

# revision identifiers
revision = '12345'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('username', sa.String(length=50), nullable=False)
    )

    op.create_table(
        'post',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(length=100)),
        sa.Column('content', sa.Text())
    )

    op.create_table(
        'comment',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('text', sa.Text())
    )


def downgrade():
    op.drop_table('comment')
    op.drop_table('post')
    op.drop_table('user')
