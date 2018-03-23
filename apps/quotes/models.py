from __future__ import unicode_literals
from ..login.models import User
from django.db import models

# ==========================================================================
#                             QUOTE MANAGER
# ==========================================================================
class QuoteManager(models.Manager):

# ==========================================================================
# ==========================================================================
    def validate(self, form_data):
        errors = []

        if len(form_data['quoted_by']) < 3:
            errors.append("Quoted by must be more than 3 char")

        if len(form_data['message']) < 10:
            errors.append("Type more than 10 char for the message")
    
        return errors
# ==========================================================================
# ==========================================================================
    def create_quote(self, form_data, user_id):

#QUOTE HAS AN AUTHOR AND THE QUOTE ITSELF (MESSAGE)
        quoted_by = form_data['quoted_by']
        message = form_data['message']

#SET VARIABLE USER TO EQUAL THE USER_ID
        user = User.objects.get(id=user_id)

#USE THE USER VARIABLE ABOVE AND SET IT TO POSTED_BY 
        posted_by = user

#CREATE THE QUOTE AND USE THE USER VARIABLE ABOVE
        self.create(message=message, quoted_by=quoted_by, posted_by=user)

# ==========================================================================
#                                QUOTE CLASS
# ==========================================================================
class Quote(models.Model):

#QUOTE HAS AN AUTHOR AND THE QUOTE ITSELF (MESSAGE)
    quoted_by = models.CharField(max_length=150)
    message = models.CharField(max_length=150)

#CREATED_AT & UPDATED_AT
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#ONE TO MANY // ONE USER CAN POST MANY QUOTES
    posted_by = models.ForeignKey(User, related_name="posted_quotes")

#MANY TO MANY  // USER CAN FAVORITE MANY QUOTE && ONE QUOTE CAN BE FAVORITED BY MANY USERS
    favorited_by = models.ManyToManyField(User, related_name="favorites")

# SET THE OBJECTS OF USER TO EQUAL THE QUOTE MANAGER
    objects = QuoteManager()

    def __str__(self):
        return "{} {} {}".format(self.quoted_by, self.message, self.posted_by)
