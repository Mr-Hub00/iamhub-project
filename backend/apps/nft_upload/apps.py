from backend.pin_to_ipfs import pin_file_to_ipfs, pin_json_to_ipfs
from django.apps import AppConfig

class NftUploadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.nft_upload'