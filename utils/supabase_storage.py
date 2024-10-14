import boto3
from django.core.files.storage import Storage
from django.conf import settings
from botocore.exceptions import NoCredentialsError


class SupabaseStorage(Storage):
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.SUPABASE_ACCESS_KEY_ID,
            aws_secret_access_key=settings.SUPABASE_SECRET_ACCESS_KEY,
            region_name=settings.SUPABASE_REGION,
            endpoint_url='https://cvherctwrqdsaxgjftay.supabase.co/storage/v1/s3'
        )
        self.bucket_name = settings.SUPABASE_BUCKET

    def _save(self, name, content):
        try:
            # Upload the file and set ACL to public-read
            self.s3_client.upload_fileobj(
                content,
                self.bucket_name,
                name,
                ExtraArgs={'ACL': 'public-read'}
            )
        except NoCredentialsError:
            print("Credentials not available")
        return name

    def url(self, name):
        return f"https://{self.bucket_name}.s3.amazonaws.com/{name}"

    def exists(self, name):
        try:
            self.s3_client.head_object(Bucket=self.bucket_name, Key=name)
            return True
        except self.s3_client.exceptions.ClientError:
            return False
