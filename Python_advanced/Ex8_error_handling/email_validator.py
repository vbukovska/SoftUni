class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def email_validator(email):

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, full_domain = email.split("@")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    domain = full_domain.split(".")[1]
    if domain not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(['.' + dom for dom in VALID_DOMAINS])}")


VALID_DOMAINS = ["com", "bg", "org", "net"]
while True:
    email = input()
    if email == "End":
        break
    email_validator(email)
    print("Email is valid")
