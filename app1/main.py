from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_user, authenticate_user
from app.schemas import UserCreate, UserCreds
from app.utils import get_password_hash, create_access_token
from app.model import User

app = FastAPI()


@app.post('/register', status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return


@app.post('/auth', status_code=200)
def auth(creds: UserCreds, db: Session = Depends(get_db)):
    user = authenticate_user(db, creds.email, creds.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect email or password',
        )
    access_token = create_access_token(data={"user_id": user.id})
    return {'access_token': access_token,}
