from django.db import models

class Thought(models.Model):
    """Model for storing daily thoughts in the database.""" #this is a docstring
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='uploads/thoughts')
    created_ts = models.DateTimeField(auto_now_add=True)
    published_date = models.DateField(null=True, blank=True, unique=True)

    def __unicode__(self):
        return self.content

    class Meta:
        ordering = ["-created_ts"]