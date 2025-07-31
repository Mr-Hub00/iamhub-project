from django.db import models

class NFTAsset(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='nfts/')
    metadata_url = models.URLField(blank=True)
    ipfs_cid = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    minted = models.BooleanField(default=False)

    def __str__(self):
        return self.title