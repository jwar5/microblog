"""new fields in user model

Revision ID: 77b63a60e197
Revises: dbf2be144675
Create Date: 2019-12-03 01:58:48.334384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77b63a60e197'
down_revision = 'dbf2be144675'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
