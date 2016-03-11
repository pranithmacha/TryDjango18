from django.db import models

# Create your models here.


class SignUp(models.Model):

    email = models.EmailField(blank=True, )
    full_name = models.CharField(max_length=130, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) 
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    """
     auto_now_add = True  > set timestamp value when created
     auto_now = False  > do not update the value when model is updated

     auto_now_add = False > do not set timestamp value when inserted 
     auto_now = True  > update value when model is updated


    """

    def __unicode__(self):
    	return self.email
