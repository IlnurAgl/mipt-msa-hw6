from pydantic import BaseModel, EmailStr, field_validator


class UserCreate(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, password):
        if len(password) < 6:
            raise ValueError('Small password')
        return password


class UserCreds(BaseModel):
    email: str
    password: str
