from django import template

register = template.Library()


@register.filter
def to_class_name(value):
    return value.__class__.__name__


@register.filter
def get_icon_for_class(value):
    return {
        "Pill": 'ion-egg',
        "Tool": 'ion-scissors',
        "Syrup": 'ion-ios-flask',
        "Bandage": 'ion-ios-medkit',
    }.get(value.__class__.__name__,'ion-help-circled')
