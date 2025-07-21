import phonenumbers
from django import template

register = template.Library()

@register.filter
def phone_number_format(value):
    try:
        phone_number = phonenumbers.parse(value, "BR")
        return phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    except:
        return value
