from django import template
from ..constants import MEDICINE_TO_ICON, MEDICINE_DEFAULT_ICON

register = template.Library()


@register.filter
def to_class_name(value):
    return value.__class__.__name__


@register.filter
def get_icon_for_class(value):
    return MEDICINE_TO_ICON.get(value.__class__.__name__, MEDICINE_DEFAULT_ICON)
