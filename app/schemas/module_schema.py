from pydantic import BaseModel, HttpUrl

class ModuleCreate(BaseModel):

    module_name: str

    module_url: str

    department_id: str