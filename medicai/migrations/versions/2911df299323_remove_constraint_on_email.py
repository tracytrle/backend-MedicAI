"""remove constraint on email

Revision ID: 2911df299323
Revises: c430e22b4615
Create Date: 2024-07-30 23:23:45.720968

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2911df299323'
down_revision = 'c430e22b4615'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('user_email_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint('user_email_key', ['email'])

    # ### end Alembic commands ###