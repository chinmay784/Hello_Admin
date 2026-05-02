



# import boto3
# import uuid
# import os
# from dotenv import load_dotenv

# load_dotenv()

# s3 = boto3.client(
#     "s3",
#     aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
#     aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
#     region_name=os.getenv("AWS_REGION")
# )

# BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")


# def upload_file_s3(file, folder="vendors"):
#     try:
#         file_ext = file.filename.split(".")[-1]
#         file_name = f"{folder}/{uuid.uuid4()}.{file_ext}"

#         s3.upload_fileobj(
#             file.file,
#             BUCKET_NAME,
#             file_name,
#             ExtraArgs={
#                 "ContentType": file.content_type,
#                 "ACL": "public-read"
#             }
#         )

#         file_url = f"https://{BUCKET_NAME}.s3.{os.getenv('AWS_REGION')}.amazonaws.com/{file_name}"

#         return file_url

#     except Exception as e:
#         print("S3 Upload Error:", e)
#         return None






import boto3
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    region_name=os.getenv("AWS_REGION")
)

BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

def upload_file_s3(file, folder="vendors"):
    try:
        file.file.seek(0)

        file_ext = file.filename.split(".")[-1]
        file_name = f"{folder}/{uuid.uuid4()}.{file_ext}"

        s3.upload_fileobj(
            file.file,
            BUCKET_NAME,
            file_name,
            ExtraArgs={
                "ContentType": file.content_type   # ✅ FIXED
            }
        )

        file_url = f"https://{BUCKET_NAME}.s3.{os.getenv('AWS_REGION')}.amazonaws.com/{file_name}"

        print("Uploaded:", file_url)
        return file_url

    except Exception as e:
        print("❌ S3 Upload Error:", e)
        return None