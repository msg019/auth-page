from adapters.db.db import session, User
from domain.utils.auth import Hashear

def addUser(id,username,passwd):
    localSession=session()
    try:
        username=username.lower()
        passwd=Hashear(passwd)
        user=User(id,username,passwd,1)
        localSession.add(user)
        localSession.commit()
    except:
        localSession.rollback()
    finally:
        localSession.close()


# Check if the username is already registered
def searchUser(username):
    localSession=session()
    try:
        username=username.lower()
        query=localSession.query(User).filter_by(username=username).scalar()
        return query
    finally:
        localSession.close()
    

def searchId(id):
    localSession=session()
    try:
        user=localSession.query(User).filter_by(id=id).first()
        return user
    finally:
        localSession.close()