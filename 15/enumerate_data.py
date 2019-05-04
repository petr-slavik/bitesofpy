names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    dvojice = zip(names, countries)
    for i, val in enumerate(dvojice, 1):
        name = val[0]
        country = val[1]
        print(f"{i}. {name:<10} {country:<15}")