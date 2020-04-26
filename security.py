from models.user import UserModel
from werkzeug.security import  safe_str_cmp


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(password,user.password):
        return user

def identity(payload):
    userid = payload['identity']
    return UserModel.find_by_userid(userid)


