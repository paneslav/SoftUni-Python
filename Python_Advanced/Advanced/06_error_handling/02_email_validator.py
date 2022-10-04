class NameTooShortError(Exception):
    """Name must be more than 4 characters"""


class MustContainAtSymbolError(Exception):
    """Email must contain @"""


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""


allowed_domains = ['com', 'bg', 'org', 'net']

while True:
    command = input()
    if command == 'End':
        break

    e_mail = command

    if '@' not in e_mail:
        raise MustContainAtSymbolError("Email must contain @")

    e_mail_parts = e_mail.split('@')

    if len(e_mail_parts[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain_split = e_mail_parts[-1].split('.')

    if '.' not in domain_split[-1]:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if domain_split[-1] not in allowed_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print('Email is valid')
