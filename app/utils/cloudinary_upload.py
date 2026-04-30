# import cloudinary.uploader
# import uuid

# def upload_file(file, folder="Vendors"):
#     try:
#         public_id = f"{folder}/{uuid.uuid4()}"

#         result = cloudinary.uploader.upload(
#             file.file,
#             public_id=public_id,
#             resource_type="auto"
#         )

#         return result["secure_url"]

#     except Exception as e:
#         print("Cloudinary Upload Error:", e)
#         return None



import cloudinary.uploader
import uuid
import os

def upload_file(file, folder="Vendors"):
    try:
        # ✅ Extract file extension (.pdf, .jpg, etc.)
        filename = file.filename
        extension = os.path.splitext(filename)[1]

        # ✅ Keep extension in public_id
        public_id = f"{folder}/{uuid.uuid4()}{extension}"

        result = cloudinary.uploader.upload(
            file.file,
            public_id=public_id,
            resource_type="auto"
        )

        return result["secure_url"]

    except Exception as e:
        print("Cloudinary Upload Error:", e)
        return None