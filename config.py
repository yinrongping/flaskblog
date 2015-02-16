#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

# 获取项目路径
basedir = os.path.abspath(os.path.dirname(__file__))

# sqlite数据库文件路径
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(basedir, 'app.db')

# migrate文件路径
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# 表示启用了跨站请求攻击保护 Flask-WTF的设置
CSRF_ENABLED = True

# 当CSRF_ENABLED启动时此配置有效，生成一个加密的token供表单验证使用
SECRET_KEY = 'helloflask'


OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5

# email server
MAIL_SERVER = 'your.mailserver.com'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = 'you'
MAIL_PASSWORD = 'your-password'

# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = ''  # enter your MS translator app id here
MS_TRANSLATOR_CLIENT_SECRET = ''  # enter your MS translator app secret here

# administrator list
ADMINS = ['you@example.com']

# pagination
POSTS_PER_PAGE = 50
MAX_SEARCH_RESULTS = 50
