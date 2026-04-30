from app.db.database import vendor_collection

def generate_vendor_code():
    last_vendor = vendor_collection.find_one(
        {},
        sort=[("vendor_id", -1)]
    )

    if not last_vendor:
        return "TIAPL/SC/001"

    last_id = last_vendor["vendor_id"]   # e.g. VEND1014

    # ✅ extract number part
    number = int(last_id.replace("VEND", ""))

    new_number = number 

    return f"TIAPL/VC/{str(new_number).zfill(3)}"