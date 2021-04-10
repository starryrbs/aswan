# coding=utf8
"""测试环境配置"""
import os

DATABASES = {
    'default': {
        "ENGINE": 'django.db.backends.mysql',
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "USER": "root",
        "PASSWORD": os.environ.get("MYSQL_PASSWORD", "root"),
        "DATABASE_CHARSET": "utf8mb4",
        "NAME": "risk_control",
        'OPTIONS': {'charset': 'utf8mb4'},
    },
}

DEBUG = True
