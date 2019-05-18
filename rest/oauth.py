import hashlib

from flask_oauthlib.provider import OAuth2Provider

from rest.dao.database import db_session
from rest.models.token import Token
from rest.models.user import User


oauth = OAuth2Provider()


@oauth.clientgetter
def get_user(user_id):
    return User.query.get(int(user_id))


@oauth.grantgetter
def get_grant(client_id, code):
    # return Grant.query.filter_by(client_id=client_id, code=code).first() TODO ARIEL
    return None


@oauth.tokengetter
def get_token(access_token=None, refresh_token=None):
    if access_token:
        return Token.query.filter_by(access_token=access_token).first()


@oauth.grantsetter
def set_grant(client_id, code, request, *args, **kwargs):
    # expires = datetime.utcnow() + timedelta(seconds=100)
    # grant = Grant(
    #     client_id=client_id,
    #     code=code['code'],
    #     redirect_uri=request.redirect_uri,
    #     scope=' '.join(request.scopes),
    #     user_id=g.user.id,
    #     expires=expires,
    # )
    # db.session.add(grant)
    # db.session.commit()
    pass


@oauth.tokensetter
def set_token(token, request, *args, **kwargs):
    tok = Token(**token)
    tok.user_id = request.user.id

    # tok.client_id = request.client.client_id
    session = db_session()
    session.add(tok)
    session.commit()


@oauth.usergetter
def get_user(username, password, *args, **kwargs):
    m = hashlib.sha512()
    m.update(str(password).encode("utf-8"))
    password = str(m.hexdigest())

    return User.query.filter_by(email=username, password=password).first()
