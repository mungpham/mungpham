from django.db import transaction

from rest_framework.generics import get_object_or_404


from SocialNetwork_API.models import *
from SocialNetwork_API.services.base import BaseService

class CommentService(BaseService):

    @classmethod
    def save(cls, comment_data):
        try:
            with transaction.atomic():
                comment = Comment.objects.create(**comment_data)
                return comment
        except Exception as exception:
            cls.log_exception(exception)
            raise exception
