# https://jupyterhub.readthedocs.io/en/latest/getting-started.html#configuration-file

c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 443

c.JupyterHub.hub_ip = 'jupyter2.rc.int.colorado.edu'

c.Spawner.env_keep.extend(['LD_LIBRARY_PATH', 'R_LIBS'])

c.JupyterHub.cookie_secret_file = '/opt/jupyterhub/var/jupyterhub_cookie_secret'

c.JupyterHub.db_url = '/opt/jupyterhub/var/jupyterhub.sqlite'

c.JupyterHub.ssl_cert = '/opt/jupyterhub/etc/jupyter.rc.int.colorado.edu.crt'
c.JupyterHub.ssl_key = '/opt/jupyterhub/etc/jupyter.rc.int.colorado.edu.key'

c.PAMAuthenticator.service = 'jupyterhub'

c.Authenticator.admin_users = { 'holtat', 'joan5896' }

c.Spawner.cmd = ['jupyterhub-singleuser-autoinit']
