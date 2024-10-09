"""yusuf

Revision ID: 8b04e680b462
Revises: dd1b708dae5a
Create Date: 2024-09-16 17:28:18.238754+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b04e680b462'
down_revision = 'dd1b708dae5a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('clients', sa.Column('role', sa.String(length=255), nullable=False, server_default='user'))

    op.alter_column('clients', 'role',
               existing_type=sa.VARCHAR(length=255),
               nullable=False,
               server_default=None)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('clients', 'role',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###