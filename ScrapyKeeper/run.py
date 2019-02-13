import ConfigParser
import logging
import os
from optparse import OptionParser

from ScrapyKeeper.app import app, initialize


def main():
    opts, args = parse_opts(app.config)
    auth_from_file = {}
    if opts.auth_file and os.path.exists(opts.auth_file) and os.path.isfile(opts.auth_file):
        auth_config = ConfigParser.ConfigParser()
        auth_config.read(opts.auth_file)
        auth_from_file['username'] = auth_config.get('auth', 'username', opts.username)
        auth_from_file['password'] = auth_config.get('auth', 'password', opts.password)
    app.config.update(dict(
        SERVER_TYPE=opts.server_type,
        SERVERS=opts.servers or app.config.get('SERVERS'),
        SQLALCHEMY_DATABASE_URI=opts.database_url,
        BASIC_AUTH_USERNAME=auth_from_file.get('username', opts.username),
        BASIC_AUTH_PASSWORD=auth_from_file.get('password', opts.password),
        NO_AUTH=opts.no_auth,
        NO_SENTRY=opts.no_sentry
    ))
    if opts.verbose:
        app.logger.setLevel(logging.DEBUG)
    initialize()
    app.logger.info("ScrapyKeeper startd on %s:%s username:%s/password:%s with %s servers:%s" % (
        opts.host, opts.port, opts.username, opts.password, opts.server_type, ','.join(app.config.get('SERVERS', []))))
    app.run(host=opts.host, port=opts.port, use_reloader=False, threaded=True)


def parse_opts(config):
    parser = OptionParser(usage="%prog [options]",
                          description="Admin ui for scrapy spider service")
    parser.add_option("--host",
                      help="host, default:0.0.0.0",
                      dest='host',
                      default='0.0.0.0')
    parser.add_option("--port",
                      help="port, default:5000",
                      dest='port',
                      type="int",
                      default=5000)
    parser.add_option("--username",
                      help="basic auth username ,default: %s" % config.get('BASIC_AUTH_USERNAME'),
                      dest='username',
                      default=config.get('BASIC_AUTH_USERNAME'))
    parser.add_option("--password",
                      help="basic auth password ,default: %s" % config.get('BASIC_AUTH_PASSWORD'),
                      dest='password',
                      default=config.get('BASIC_AUTH_PASSWORD'))
    parser.add_option("--type",
                      help="access spider server type, default: %s" % config.get('SERVER_TYPE'),
                      dest='server_type',
                      default=config.get('SERVER_TYPE'))
    parser.add_option("--server",
                      help="servers, default: %s" % config.get('SERVERS'),
                      dest='servers',
                      action='append',
                      default=[])
    parser.add_option("--database-url",
                      help='ScrapyKeeper metadata database default: %s' % config.get('SQLALCHEMY_DATABASE_URI'),
                      dest='database_url',
                      default=config.get('SQLALCHEMY_DATABASE_URI'))
    parser.add_option("--auth-file",
                      help="Get the credentials from a file",
                      dest='auth_file')

    parser.add_option("--no-auth",
                      help="disable basic auth",
                      dest='no_auth',
                      action='store_true')
    parser.add_option("--no-sentry",
                      help="disable sentry.io error reporting",
                      dest='no_sentry',
                      action='store_true')
    parser.add_option("-v", "--verbose",
                      help="log level",
                      dest='verbose',
                      action='store_true')
    return parser.parse_args()


if __name__ == '__main__':
    main()
