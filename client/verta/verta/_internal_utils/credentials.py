# -*- coding: utf-8 -*-

import abc
import os

from verta.external import six


def build(email=None, dev_key=None, jwt_token=None, jwt_token_sig=None):
    if email and dev_key:
        return EmailCredentials(email, dev_key)
    elif jwt_token and jwt_token_sig:
        return JWTCredentials(jwt_token, jwt_token_sig)
    else:
        return None


@six.add_metaclass(abc.ABCMeta)
class Credentials(object):

    @abc.abstractmethod
    def export_env_vars_to_os(self):
        raise NotImplementedError

class EmailCredentials:

    EMAIL_ENV = "VERTA_EMAIL"
    DEV_KEY_ENV = "VERTA_DEV_KEY"

    def __init__(self, email, dev_key):
        self.email = email
        self.dev_key = dev_key

    def export_env_vars_to_os(self):
        os.environ[self.EMAIL_ENV] = self.email
        os.environ[self.DEV_KEY_ENV] = self.dev_key

    def __repr__(self):
        return "" # TODO: implement and obscure dev key to avoid printing accidentally

class JWTCredentials:

    JWT_TOKEN_ENV = "VERTA_JWT_TOKEN"
    JWT_TOKEN_SIG_ENV = "VERTA_JWT_TOKEN_SIG"

    def __init__(self, jwt_token, jwt_token_sig):
        self.jwt_token = jwt_token
        self.jwt_token_sig = jwt_token_sig

    def export_env_vars_to_os(self):
        os.environ[self.JWT_TOKEN_ENV] = self.jwt_token
        os.environ[self.JWT_TOKEN_SIG_ENV] = self.jwt_token_sig

    def __repr__(self):
        return "" # TODO: implement and obscure as appropriate to avoid accidentally printing
