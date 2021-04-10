# coding=utf8
"""开发环境配置"""
import os

DATABASES = {
    'default': {
        "ENGINE": 'django.db.backends.mysql',
        "USER": "root",
        "DATABASE_CHARSET": "utf8",
        "NAME": "risk_control",
    },
}

DEBUG = True
