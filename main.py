def hello(firstname="John", lastname="Doe"):
    if not isinstance(firstname, str) or not isinstance(lastname, str):
        raise TypeError(
            "Les paramètres 'firstname' et 'lastname' "
            " doivent être des chaînes de caractères."
        )
    return f"Hello, {firstname} {lastname}!"
