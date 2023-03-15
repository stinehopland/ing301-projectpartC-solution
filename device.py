from pydantic import BaseModel


class Device (BaseModel):

    serial_no: str
    producer: str
    product_type: str
    nickname: str

