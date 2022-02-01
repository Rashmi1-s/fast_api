from pydantic import BaseModel

# Create ToDo Schema (Pydantic Model)
class CustomerCreate(BaseModel):
    firstname: str
    lastname: str
    email: str
    customer_type: str
    created_on: str
    
# Complete ToDo Schema (Pydantic Model)
class Customer(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str
    customer_type: str
    created_on: str
    
    class Config:
        orm_mode = True

