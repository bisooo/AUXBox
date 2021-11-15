from django.db import models
from events.models.comment import Comment
from events.daointerface.commentinterface import CommentDaoInterface
from events.dao.base import BaseDao


class CommentDao(BaseDao, CommentDaoInterface):

    model = Comment
