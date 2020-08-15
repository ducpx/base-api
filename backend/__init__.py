import logging

import click

from backend.common.utils import log


@click.group()
def cli():
    pass


@cli.command(short_help='Run an api')
@click.option('--enable-gunicorn', default='false')
@click.option('--port', default='5000')
@click.option('--processes', default='5')
@click.option('--api-file', default='public_api')
@click.option('--host')
def api(**kwargs):
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s] - %(message)s'))
    log.setLevel(5)
    log.addHandler(console_handler)

    gunicorn_enabled = False if kwargs.get('enable_gunicorn') == 'false' else True
    host = kwargs.get('host')
    try:
        port = int(kwargs.get('port'))
    except Exception as e:
        raise e

    api_file = kwargs.get('api_file')

    if not gunicorn_enabled:
        if api_file == 'dashboard_api':
            pass
        else:
            from backend.api.pool.public import app

        params = dict(port=port)
        if host:
            params['host'] = host

        return app.run(**params)
