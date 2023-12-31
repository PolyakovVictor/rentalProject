"""rewrite models in classes

Revision ID: 22688e7e9948
Revises: 6a841a336675
Create Date: 2023-06-28 10:34:24.036296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22688e7e9948'
down_revision = '6a841a336675'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('groupUser', 'group_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('groupUser', 'group_id',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    # ### end Alembic commands ###
