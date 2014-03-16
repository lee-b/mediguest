from django.core.validators import RegexValidator

postcode_validator = RegexValidator(
    regex=r'[A-Za-z]{1}[A-Za-z0-9]{1,3} \d{1}[A-Za-z]{2}',
    message="This must be one letter, up to three more letters and/or digits, a space, a digit, then two more letters"
)
