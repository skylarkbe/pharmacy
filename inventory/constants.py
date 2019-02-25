MEDICINE_TO_ICON = {
    "Pill": 'ion-egg',
    "Tool": 'ion-scissors',
    "Syrup": 'ion-ios-flask',
    "Bandage": 'ion-ios-medkit',
}

MEDICINE_DEFAULT_ICON = 'ion-help-circled'

DATE_INPUT_FORMATS = ['%d-%m-%Y']

MEDICINE_TYPE_FILTERS = ['show_syrups', 'show_pills', 'show_bandages', 'show_tools']

MEDICINE_VALIDITY_FILTERS = ['show_not_expired', 'show_expired']

APPLICATION_FILTERS = MEDICINE_TYPE_FILTERS + MEDICINE_VALIDITY_FILTERS
