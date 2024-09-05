from models.providers import Provider


def add_provider(session):
    first_name = input("Enter a first name: ")
    last_name = input("Enter a last name: ")
    email = input("Enter a email: ")
    company_name = input("Enter a company name: ")

    session.add(
        Provider(
            first_name=first_name,
            last_name=last_name,
            email=email,
            company_name=company_name,
        )
    )


def update_provider(session):
    provider_name = input("Enter a last name: ")
    prop_update = input(
        "What to change: 'first_name', 'last_name','email', 'company_name'? "
    )
    new_val = input("Enter a new value: ")
    session.query(Provider).filter(Provider.last_name == provider_name).update(
        {prop_update: new_val}
    )


def delete_provider(session):
    number = int(input("Enter the provider number: "))
    session.query(Provider).filter_by(number=number).delete()


def get_info_provider(session):
    name = input("Enter a provider last name: ")
    provider = session.query(Provider).filter(Provider.last_name == name).first()
    if provider:
        print(
            f"number: {provider.number}\
        \nfirst name: {provider.first_name}\
        \nlast_name: {provider.last_name}\
        \nemail: {provider.email}\
        \ncompany name: {provider.company_name}"
        )
    else:
        print(f"The {name} was not found")


def search_provider(session):
    name = input("Enter part of the name: ")
    providers = (
        session.query(Provider).filter(Provider.first_name.ilike(f"{name}%")).all()
    )
    for provider in providers:
        print(
            f"number: {provider.number}\
            \nfirst name: {provider.first_name}\
            \nlast_name: {provider.last_name}\
            \nemail: {provider.email}\
            \ncompany name: {provider.company_name}"
        )
