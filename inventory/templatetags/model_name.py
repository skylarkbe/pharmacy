from django import template

register = template.Library()


@register.filter
def to_class_name(value):
    return value.__class__.__name__


@register.filter
def get_icon_for_class(value):
    ion_mapping = {
        "Pill": 'ion-ios-keypad',
        "Tool": 'ion-scissors',
        "Syrup" : 'ion-ios-flask',
        "Bandage" : 'ion-ios-medkit',
    }
    if value.__class__.__name__ in ion_mapping :
        return ion_mapping[value.__class__.__name__]
    return 'ion-help-circled'
