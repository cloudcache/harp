from mesh.standard import *
from scheme import *

from harp.constants import RULES

class Configuration(Resource):
    name = 'configuration'
    version = 1

    class schema:
        id = Token(segments=1, nonempty=True, oncreate=True, operators='equal')
        filepath = Text(nonempty=True)
        pidfile = Text()
        chroot = Text()
        daemon = Boolean()
        group = Text()
        log_tag = Text()
        user = Text()
        default_mode = Enumeration('http tcp')
        default_connect_timeout = Text()
        default_client_timeout = Text()
        default_server_timeout = Text()
        include_globals = Boolean(default=True)
        include_defaults = Boolean(default=True)

    class update(Resource.update):
        fields = {
            'commit': Boolean(default=False),
        }

class Proxy(Resource):
    class schema:
        name = Token(segments=1, readonly=True)
        mode = Enumeration('http tcp')
        connect_timeout = Text()
        client_timeout = Text()
        server_timeout = Text()
        forwardfor = Boolean()
        forwardfor_header = Text()
        http_close = Boolean()
        http_server_close = Boolean()
        http_log = Boolean()
        log_global = Boolean()

class Backend(Proxy):
    name = 'backend'
    version = 1

    class schema:
        id = Token(segments=2, nonempty=True, oncreate=True, operators='equal')

class Frontend(Proxy):
    name = 'frontend'
    version = 1

    class schema:
        id = Token(segments=2, nonempty=True, oncreate=True, operators='equal')
        bind = Text(nonempty=True)
        default_backend = Text()

class ACL(Resource):
    name = 'acl'
    version = 1

    class schema:
        id = Token(segments=3, nonempty=True, oncreate=True, operators='equal')
        name = Token(segments=1, readonly=True)
        acls = Sequence(Text(nonempty=True), nonempty=True, unique=True)

class Rule(Resource):
    name = 'rule'
    version = 1

    class schema:
        id = Token(segments=3, nonempty=True, oncreate=True, operators='equal')
        name = Token(segments=1, readonly=True)
        rule = Enumeration(RULES, nonempty=True)
        content = Text(nonempty=True)

class Server(Resource):
    name = 'server'
    version = 1

    class schema:
        id = Token(segments=3, nonempty=True, oncreate=True, operators='equal')
        name = Token(segments=1, readonly=True)
        address = Text(nonempty=True)
        addr = Text()
        backup = Boolean()
        check = Boolean()
        cookie = Text()
        disabled = Boolean()
        error_limit = Integer()
        fall = Integer()
        inter = Integer()
        fastinter = Integer()
        downinter = Integer()
        maxconn = Integer()
        maxqueue = Integer()
        minconn = Integer()
        observe = Text()
        on_error = Text()
        port = Integer()
        redir = Text()
        rise = Integer()
        slowstart = Integer()
        track = Text()
        weight = Integer()
