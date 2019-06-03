from flask import session
from flask_oauthlib.provider import OAuth1Provider

from rest.dao.database import db
from rest.models.oauth.access_token import AccessToken
from rest.models.oauth.client import Client
from rest.models.oauth.nonce import Nonce
from rest.models.oauth.request_token import RequestToken
from rest.models.user import User


oauth = OAuth1Provider()


def current_user():
    if 'id' in session:
        uid = session['id']
        return User.query.get(uid)
    return None


@oauth.clientgetter
def load_client(client_key):
    return Client.query.get(client_key)


@oauth.grantgetter
def load_request_token(token):
    return RequestToken.query.filter_by(token=token).first()


@oauth.grantsetter
def save_request_token(token, request):
    if hasattr(oauth, 'realms') and oauth.realms:
        realms = ' '.join(request.realms)
    else:
        realms = None
    grant = RequestToken(
        token=token['oauth_token'],
        secret=token['oauth_token_secret'],
        client=request.client,
        redirect_uri=request.redirect_uri,
        _realms=realms,
    )
    db.session.add(grant)
    db.session.commit()
    return grant


@oauth.verifiergetter
def load_verifier(verifier, token):
    return RequestToken.query.filter_by(
        verifier=verifier, token=token
    ).first()


@oauth.verifiersetter
def save_verifier(token, verifier, *args, **kwargs):
    tok = RequestToken.query.filter_by(token=token).first()
    tok.verifier = verifier['oauth_verifier']
    tok.user = current_user()
    db.session.add(tok)
    db.session.commit()
    return tok


@oauth.noncegetter
def load_nonce(client_key, timestamp, nonce, request_token, access_token):
    return Nonce.query.filter_by(
        client_key=client_key,
        timestamp=timestamp,
        nonce=nonce,
        request_token=request_token,
        access_token=access_token
    ).first()


@oauth.noncesetter
def save_nonce(client_key, timestamp, nonce, request_token, access_token):
    nonce = Nonce(
        client_key=client_key,
        timestamp=timestamp,
        nonce=nonce,
        request_token=request_token,
        access_token=access_token,
    )
    db.session.add(nonce)
    db.session.commit()
    return nonce


@oauth.tokengetter
def load_access_token(client_key, token, *args, **kwargs):
    return AccessToken.query.filter_by(
        client_key=client_key, token=token
    ).first()


@oauth.tokensetter
def save_access_token(token, request):
    tok = AccessToken(
        client=request.client,
        user=request.user,
        token=token['oauth_token'],
        secret=token['oauth_token_secret'],
        _realms=token['oauth_authorized_realms'],
    )
    db.session.add(tok)
    db.session.commit()
