"""empty message

Revision ID: e5760fba46c8
Revises: 9dc5333475ff
Create Date: 2024-05-11 15:44:33.889184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5760fba46c8'
down_revision = '9dc5333475ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hills', schema=None) as batch_op:
        batch_op.drop_index('ix_hills_time')
        batch_op.drop_column('time')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hills', schema=None) as batch_op:
        batch_op.add_column(sa.Column('time', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))
        batch_op.create_index('ix_hills_time', ['time'], unique=False)

    # ### end Alembic commands ###