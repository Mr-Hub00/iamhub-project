from django.db import models

class NFTAsset(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='nfts/')
    cid = models.CharField(max_length=255, blank=True, null=True)  # Add this
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title