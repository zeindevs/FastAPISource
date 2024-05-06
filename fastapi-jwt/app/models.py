from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        json_schema_extra = {
            'example': {
                'title': "Securing FastAPI application with JWT.",
                'content': 'In this tutorial, you\'ll learn how to secure \
                your application by enabling authentication using JWT. We\'ll \
                be using PyJWT so sign, encode and decode JWT token....'
            }
        }


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            'example': {
                'fullname': 'John Kelly',
                'email': 'john.kelly@gmail.com',
                'password': 'strongpassword'
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            'example': {
                'email': 'john.kelly@gmail.com',
                'password': 'strongpassword'
            }
        }
