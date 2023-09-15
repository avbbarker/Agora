"""empty message

Revision ID: 9c826be56467
Revises: 24216079167c
Create Date: 2023-09-15 11:24:48.234697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c826be56467'
down_revision = '24216079167c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_user_music_table_music_id_gallery_table', 'user_music_table', type_='foreignkey')
    op.create_foreign_key(op.f('fk_user_music_table_music_id_music_table'), 'user_music_table', 'music_table', ['music_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_user_music_table_music_id_music_table'), 'user_music_table', type_='foreignkey')
    op.create_foreign_key('fk_user_music_table_music_id_gallery_table', 'user_music_table', 'gallery_table', ['music_id'], ['id'])
    # ### end Alembic commands ###
