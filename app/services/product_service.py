from app.db.database import product_collection
from datetime import datetime
from app.db.database import vendor_collection

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



def getVendorAllProduct(vendor_id):
    try:
        products = list(product_collection.find({"vendor_id": vendor_id}))
        for product in products:
            product["_id"] = str(product["_id"])
        return products
    except Exception as e:
        print("Error fetching products:", e)
        return []


def procureTeamCanSeeProduct():
    try:
        print("Hello")
        # In vendorCollection find Whose Status is Approved find them
        vendors = list(vendor_collection.find({"status": "APPROVED"}))
        if not vendors:
            print("No approved vendors found.")
            return []
        
        vendor_ids = [str(vendor["vendor_id"]) for vendor in vendors]
        # print("Approved Vendor IDs:", vendor_ids)
        products = list(product_collection.find({"vendor_id": {"$in": vendor_ids}}))
        for product in products:
            product["_id"] = str(product["_id"])

        if not products:
            print("No products found for approved vendors.")

        return products
    except Exception as e:
        print("Error fetching products:", e)
        return []