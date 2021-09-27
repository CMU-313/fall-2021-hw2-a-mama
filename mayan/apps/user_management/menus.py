from django.utils.translation import ugettext_lazy as _

from mayan.apps.navigation.classes import Menu
from mayan.apps.navigation.utils import get_cascade_condition

from .icons import icon_user_list
from .permissions import permission_user_view, permission_user_edit

menu_reviewers = Menu(
    condition=get_cascade_condition(
        app_label='cabinets', model_name='Cabinet',
        object_permission=permission_user_view,
        view_permission=permission_user_edit,
    ), icon=icon_user_list, label=_('Reviewers'), name='reviewers'
)
