from django.db import models

# Create your models here.
class ARTICALS(models.Model):

    Title = models.CharField(max_length=100, unique=True, blank=False, null=True)
    Image = models.ImageField()
    Content = models.TextField()
    Link = models.URLField(max_length=100)
    TIPS = 'TI'
    NEWS = 'NE'
    PROMOTIONS = 'PR'
    TOPIC = (
        (TIPS, 'Tips'),
        (NEWS, 'News'),
        (PROMOTIONS, 'Promotions'),

    )
    Topic = models.CharField(
        max_length=2,
        choices=TOPIC,
        default=TIPS,
    )
