from django.core.validators import RegexValidator

nat_ins_validator = RegexValidator(regex=r'[A-Za-z]{2}\d{6}[A-Za-z ]{1}', message="This must be two letters, six digits, and a final letter, or a space")

