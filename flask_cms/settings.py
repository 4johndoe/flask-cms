# -*- coding: utf-8 -*-

"""
    settings
    ~~~~~~~~

    Global settings for project.
"""
import os
from local_settings import LocalConfig

class BaseConfig(LocalConfig):
    ADMIN_PER_PAGE = 5
    CODEMIRROR_LANGUAGES = ['python','python2','python3','php','javascript','xml']
    CODEMIRROR_THEME = '3024-day'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    CSRF_ENABLED = True
    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

    URL_ROUTE_MODULES = [
            'core.urls.routes',
    ]

    BLUEPRINTS = [
            'core.core',
            'member.member',
            'admin.admin',
            'menu.menu',
            'blog.blog',
            'page.page',
            'auth.auth',
                                        
    ]

    EXTENSIONS = [
            'ext.db',
            'ext.toolbar',
            'ext.pagedown',
            'ext.codemirror',
            'ext.manager',
            'ext.alembic',
    ]

    CONTEXT_PROCESSORS = [
            'core.context_processors.common_context',                      
            'core.context_processors.common_forms',
            'menu.context_processors.frontend_nav',
            'menu.context_processors.admin_nav',
            'auth.context_processors.user_context',
            'core.context_processors.add_is_page',
    ]

    TEMPLATE_FILTERS = [
            'core.filters.date',
            'core.filters.date_pretty',
            'core.filters.datetime',
            'core.filters.pluralize',
            'core.filters.month_name',
            'core.filters.markdown',
    ]
    
    CONTACT_FORM_SETTINGS = {
    'HEADING':'Send Us a message',
    'SUBHEADING':'Or a Comment',
    'OPTIONS':(
        ('test','opt1'),
        ('test2','opt2'),
        ('test3','opt3'),
        ('test4','opt4'),
        ('test5','opt5'),
        ('test6','opt6'),
    ),
    'SUBMIT_TEXT':'Send to Us',
    'COMPANY_TITLE':'Level2designs',
    'COMPANY_ADDRESS':{
        'NAME':'level2designs',
        'STREET':'1045 w katella',
        'CITY':'Orange',
        'STATE':'CA',
        'ZIP':'92804',
    },
    'COMPANY_PHONE':'714-783-6369',
    'CONTACT_NAME':'Kyle Roux',
    'CONTACT_EMAIL':'kyle@level2designs.com',
    }

def get_choices():
    return BaseConfig.CONTACT_FORM_SETTINGS['OPTIONS']


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig(BaseConfig):
    TESTING = True
    
