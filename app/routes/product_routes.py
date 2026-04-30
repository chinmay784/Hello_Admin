
# from fastapi import APIRouter, UploadFile, File, Form
# from typing import List
# import json

# from app.schemas.product_schema import ProductCreate
# from app.services.product_service import create_product
# from app.utils.cloudinary_upload import upload_file

# router = APIRouter(prefix="/vendor/products", tags=["Vendor_Add_Products"])


# @router.post("/add-product")
# async def add_product(
#     product_name: str = Form(...),
#     category: str = Form(...),
#     sub_category: str = Form(None),
#     brand: str = Form(None),
#     model_number: str = Form(None),
#     price: float = Form(...),
#     quantity_available: int = Form(...),
#     minimum_order_quantity: int = Form(...),
#     description: str = Form(...),

#     specifications: str = Form(...),  # JSON string
#     features: str = Form(...),        # JSON string

#     images: List[UploadFile] = File([]),
#     datasheet: UploadFile = File(None),

#     vendor_id: str = Form(...)
# ):
#     # ✅ Convert JSON string → dict/list
#     specs_dict = json.loads(specifications)
#     features_list = json.loads(features)

#     # ✅ Upload Images
#     image_urls = []
#     for img in images:
#         url = upload_file(img, "products/images")
#         if url:
#             image_urls.append(url)

#     # ✅ Upload Document
#     document_urls = {}
#     if datasheet:
#         doc_url = upload_file(datasheet, "products/docs")
#         document_urls["datasheet"] = doc_url

#     # ✅ Create Pydantic object
#     product_data = ProductCreate(
#         product_name=product_name,
#         category=category,
#         sub_category=sub_category,
#         brand=brand,
#         model_number=model_number,
#         price=price,
#         quantity_available=quantity_available,
#         minimum_order_quantity=minimum_order_quantity,
#         description=description,
#         specifications=specs_dict,
#         features=features_list
#     )

#     return create_product(product_data, image_urls, document_urls, vendor_id)



from fastapi import APIRouter, UploadFile, File, Form
from typing import List
import json

from app.schemas.product_schema import ProductCreate
from app.services.product_service import create_product
from app.utils.cloudinary_upload import upload_file

from app.utils.s3_upload import upload_file_s3


router = APIRouter(prefix="/vendor/products", tags=["Vendor_Add_Products"])


@router.post("/add-product")
async def add_product(
    product_name: str = Form(...),
    category: str = Form(...),
    sub_category: str = Form(None),
    brand: str = Form(None),
    model_number: str = Form(None),
    price: float = Form(...),
    quantity_available: int = Form(...),
    minimum_order_quantity: int = Form(...),
    description: str = Form(...),

    specifications: str = Form(...),  # JSON string
    features: str = Form(...),        # JSON string



    images: List[UploadFile] = File([]),
    datasheet: UploadFile = File(None),

    vendor_id: str = Form(...)
):
    # ✅ Convert JSON string → dict/list
    specs_dict = json.loads(specifications)
    features_list = json.loads(features)

    # ✅ Upload Images
    image_urls = []
    for img in images:
        url = upload_file(img, "products/images")
        if url:
            image_urls.append(url)

    # ✅ Upload Document
    document_urls = {}
    if datasheet:
        doc_url = upload_file(datasheet, "products/docs")
        document_urls["datasheet"] = doc_url

    # ✅ Create Pydantic object

    # ✅ Convert JSON
    specs_dict = json.loads(specifications)
    features_list = json.loads(features)

    # ✅ Upload Images to S3
    image_urls = []
    for img in images:
        url = upload_file_s3(img, "products/images")
        if url:
            image_urls.append(url)

    # ✅ Upload Datasheet
    document_urls = {}
    if datasheet:
        doc_url = upload_file_s3(datasheet, "products/docs")
        document_urls["datasheet"] = doc_url

    # ✅ Create Product Object

    product_data = ProductCreate(
        product_name=product_name,
        category=category,
        sub_category=sub_category,
        brand=brand,
        model_number=model_number,
        price=price,
        quantity_available=quantity_available,
        minimum_order_quantity=minimum_order_quantity,
        description=description,
        specifications=specs_dict,
        features=features_list
    )

    return create_product(product_data, image_urls, document_urls, vendor_id)