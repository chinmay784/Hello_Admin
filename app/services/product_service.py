from app.db.database import product_collection
from datetime import datetime

def create_product(data, image_urls, document_urls, vendor_id):
    product_data = {
        "vendor_id": vendor_id,

        "basic_info": {
            "product_name": data.product_name,
            "category": data.category,
            "sub_category": data.sub_category,
            "brand": data.brand,
            "model_number": data.model_number,
            "description": data.description
        },

        "pricing": {
            "price": data.price,
            "quantity_available": data.quantity_available,
            "minimum_order_quantity": data.minimum_order_quantity
        },

        "specifications": data.specifications,
        "features": data.features,

        "media": {
            "images": image_urls,
            "documents": document_urls
        },

        "status": "PENDING",
        "created_at": datetime.utcnow()
    }

    result = product_collection.insert_one(product_data)
    product_data["_id"] = str(result.inserted_id)

    return product_data