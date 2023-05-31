from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, APIRouter
from jwt import PyJWT, PyJWTError
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi import status, HTTPException

from config import get_db
from ..schemas import TokenSchema, UtilisateurSchema
from ..routes.utilisateur_router import get_utilisateur_by_username
from config.security import create_access_token
from config.db import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, KEY
from config.hashing import Hasher

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")


def authenticate_user(username: str, password: str, db: Session):
    user: UtilisateurSchema = get_utilisateur_by_username(username, db)
    if not user:
        return False
    if not Hasher.verify_password(password, user.password):
        return False
    return user


@router.post("/token", response_model=TokenSchema)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user_from_token(token: PyJWT = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = PyJWT.decode(token, KEY, algorithms=ALGORITHM)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception
    user = get_utilisateur_by_username(username, db)
    if user is None:
        raise credentials_exception
    return user
