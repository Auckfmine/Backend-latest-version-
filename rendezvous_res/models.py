
from django.db import models


from django.contrib.auth.models import User


class Rv(models.Model):
    # coté user
    Rv_Requested_Date = models.DateTimeField(auto_now_add=True)
    Rv_user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    # coté admin
    date = models.DateTimeField(auto_now_add = True,null = True,blank = True)
    Rv_available_date = models.DateTimeField(null=True)
    Rv_admin_comment = models.CharField(max_length=120,null=True)

    def __str__(self):
        return str(self.Rv_user)
