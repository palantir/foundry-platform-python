from pydantic import BaseModel


class SignInResponse(BaseModel):
    session: dict


class SignOutResponse(BaseModel):
    pass
