"""empty message

Revision ID: 99eec5598832
Revises: 4c468b757cec
Create Date: 2023-10-19 08:54:44.408085

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "99eec5598832"
down_revision = "4c468b757cec"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(sa.Column("email", sa.String(), nullable=False))
        batch_op.create_unique_constraint("email", ["email"])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_constraint("email", type_="unique")
        batch_op.drop_column("email")

    # ### end Alembic commands ###
