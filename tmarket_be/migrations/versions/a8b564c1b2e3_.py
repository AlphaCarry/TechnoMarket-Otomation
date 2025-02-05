"""empty message

Revision ID: a8b564c1b2e3
Revises: 3b4662a30e8e
Create Date: 2025-01-01 17:57:36.156821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8b564c1b2e3'
down_revision = '3b4662a30e8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('alis_hareketleri', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'urun', ['urun_id'], ['id'])

    with op.batch_alter_table('satis_hareketleri', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'urun', ['urun_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('satis_hareketleri', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('alis_hareketleri', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
