from flask import Blueprint
print __name__


mainofindex = Blueprint('mainofindex', __name__)

import views, errors
from ..models import Permission


@mainofindex.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


