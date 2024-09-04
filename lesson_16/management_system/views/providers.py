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
    name = input("Enter a last name to delete: ")
    session.query(Provider).filter_by(name=name).delete(synchronize_session="fetch")
