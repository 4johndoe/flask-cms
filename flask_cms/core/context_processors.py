# -*- coding: utf-8 -*-
"""
    core.context_processors
"""
import os
from settings import BaseConfig
from flask.helpers import url_for
from faker.factory import Factory
from page.context_processors import add_get_button, add_get_icon,get_context, add_get_block,add_urlfor

ROOT_PATH = BaseConfig.ROOT_PATH


def is_list(lst):
    return type(lst) == list


def add_is_list():
    return {'is_list': is_list}


def _get_name():
    factory = Factory()
    faker = factory.create()
    return faker.name()


def is_dir(name):
    return os.path.isdir(os.path.join(ROOT_PATH,name))

def extract_settings(config):
    rtn = []
    for itm in sorted(dir(config)):
        if not itm.startswith('_') and itm == itm.upper():
            rtn.append((itm,getattr(config,itm)))
    return tuple(rtn)

def common_context():
    return {
        'extract_settings':extract_settings,
        'str':str,
        'zip':zip,
        'is_dir':is_dir,
        'my_email': 'kyle@level2designs.com',
        'type': type,
        'dir': dir,
        'get_name': _get_name,
        'use_editor': False,
        'config':BaseConfig,
        'map':map,
    }


def common_forms():
    return {}   


def is_page(obj):
    return obj.__class__.__name__ == 'Page'


def add_is_page():
    return {'is_page': is_page}


#ef add_get_button():
#   return {'get_button': get_button}


def get_model(model, blueprint=None):
    if '_' in model:
        start, end = model.split('_')
        cls = start.title() + end.title()
    else:
        cls = model.title()
    return __import__(blueprint or model.lower() +
                      '.models', globals(), locals(),
                      fromlist=[]).models.__dict__[cls]


def add_get_model():
    return {'get_model': get_model}


def fix_body(txt):
    return txt.replace('.','_')


def add_layouts():
    layouts = BaseConfig.LAYOUT_FILES.copy()
    return dict(layouts=layouts)
            

def layout_menu():
    return '''
    <div class=layout-menu>
        <div class=row>
            <div class=col-md-4>
                <div class=list-group>
                    <a class="list-group-item" href="{{url_for('.blockview',alt_layout=3)}}">3 columns</a>
                </div>
            </div>
            <div class=col-md-4>
                <div class=list-group>
                    <a class="list-group-item" href="{{url_for('.blockview',alt_layout=4)}}">4 columns</a>
                </div>
            </div>
            <div class=col-md-4>
                <div class=list-group>
                    <a class="list-group-item" href="{{url_for('.blockview',alt_layout=5)}}">5 columns</a>
                </div>
            </div>
        </div>
    </div>
    '''

def add_layout_mode():
    return dict(layout_menu=layout_menu)
