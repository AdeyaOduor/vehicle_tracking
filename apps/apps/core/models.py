from django.db import models

class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, 
                                 null=True, related_name='%(class)s_created')
    updated_by = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, 
                                 null=True, related_name='%(class)s_updated')

    class Meta:
        abstract = True