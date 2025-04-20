from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.schemas import MessageCreate
from app.dependencies import get_db, get_current_user
from app.model import Message


app = FastAPI()


@app.post('/message', status_code=201)
def message(message_create: MessageCreate, db: Session = Depends(get_db), user_id = Depends(get_current_user)):
    db_message = Message(user_id=user_id, message=message_create.message)
    db.add(db_message)
    db.commit()
    return