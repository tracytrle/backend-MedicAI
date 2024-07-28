"""add dateOfBirth

Revision ID: f019c8f0c634
Revises: 21ddbb3872f2
Create Date: 2024-07-28 17:17:34.938676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f019c8f0c634'
down_revision = '21ddbb3872f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dateOfBirth', sa.Date(), nullable=True))
        batch_op.drop_column('year')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('year', sa.DATE(), autoincrement=False, nullable=True))
        batch_op.drop_column('dateOfBirth')

    # ### end Alembic commands ###
