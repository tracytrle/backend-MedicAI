"""change colomn year to dateOfBirth

Revision ID: 21ddbb3872f2
Revises: 7dae1f914dc1
Create Date: 2024-07-28 17:13:22.597751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21ddbb3872f2'
down_revision = '7dae1f914dc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('firstName', sa.String(length=150), nullable=True))
        batch_op.add_column(sa.Column('middleName', sa.String(length=150), nullable=True))
        batch_op.add_column(sa.Column('lastName', sa.String(length=150), nullable=True))
        batch_op.add_column(sa.Column('gender', sa.String(length=10), nullable=True))
        batch_op.add_column(sa.Column('year', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('city', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('country', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('country')
        batch_op.drop_column('city')
        batch_op.drop_column('year')
        batch_op.drop_column('gender')
        batch_op.drop_column('lastName')
        batch_op.drop_column('middleName')
        batch_op.drop_column('firstName')
        batch_op.drop_column('phone')

    # ### end Alembic commands ###
