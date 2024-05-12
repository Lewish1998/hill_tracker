"""optional test

Revision ID: 9dc5333475ff
Revises: 1af56fa6e0ba
Create Date: 2024-05-11 15:42:41.353288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dc5333475ff'
down_revision = '1af56fa6e0ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hills', schema=None) as batch_op:
        batch_op.alter_column('height',
               existing_type=sa.FLOAT(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hills', schema=None) as batch_op:
        batch_op.alter_column('height',
               existing_type=sa.FLOAT(),
               nullable=False)

    # ### end Alembic commands ###