import os
import httpx
from django.core.files.storage import Storage
from django.conf import settings


class SupabaseStorage(Storage):
    def __init__(self):
        self.supabase_url = settings.SUPABASE_URL
        self.supabase_key = settings.SUPABASE_KEY
        self.bucket_id = settings.SUPABASE_BUCKET
        self.headers = {
            "Authorization": f"Bearer {self.supabase_key}",
            "apikey": self.supabase_key
        }
        self.storage_url = f"{
            self.supabase_url}/storage/v1/object/public/{self.bucket_id}"

    def _save(self, name, content):
        file_data = content.read()
        file_name = os.path.basename(name)

        # Upload the file to Supabase storage
        upload_url = f"{
            self.supabase_url}/storage/v1/object/{self.bucket_id}/{file_name}"
        files = {"file": (file_name, file_data)}

        with httpx.Client() as client:
            response = client.post(
                upload_url, headers=self.headers, files=files)
            response.raise_for_status()

        return file_name

    def url(self, name):
        return f"{self.storage_url}/{name}"

    def exists(self, name):
        check_url = f"{
            self.supabase_url}/storage/v1/object/{self.bucket_id}/{name}"
        with httpx.Client() as client:
            response = client.get(check_url, headers=self.headers)
            return response.status_code == 200
