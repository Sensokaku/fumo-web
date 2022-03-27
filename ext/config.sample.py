# -*- coding: utf-8 -*-

# app name
app_name = 'Fumosu!'

# secret key
secret_key = 'changeme'

#hCaptcha settings:
hCaptcha_sitekey = 'changeme'
hCaptcha_secret = 'changeme'

# domain (used for api, avatar, etc)
domain = 'fumosu.pw'

# mysql credentials
mysql = {
    'db': 'gulag',
    'host': 'localhost',
    'user': 'cmyui',
    'password': 'changeme',
}

# path to gulag root (must have leading and following slash)
path_to_gulag = '/path/to/gulag/'

# enable debug (disable when in production to improve performance)
debug = False

# disallowed names (hardcoded banned usernames)
disallowed_names = {
    'cookiezi', 'rrtyui',
    'hvick225', 'qsc20010'
}

# disallowed passwords (hardcoded banned passwords)
disallowed_passwords = {
    'password', 'minilamp'
}

# enable registration
registration = True

# social links (used throughout fumo-web)
github = 'https://github.com/fumosu/fumo-web'
discord_server = 'https://discord.gg/SvE65GsEXE'
twitter = 'https://twitter.com/aochiosu'
