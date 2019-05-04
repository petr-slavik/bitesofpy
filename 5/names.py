NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    dup = []
    for jmeno in names:
        one_name = [x.capitalize() for x in jmeno.split()]
        one_name = " ".join(one_name)
        if one_name not in dup:
            dup.append(one_name)
    return dup


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    dup = []
    for jmeno in names:
        one_name = [x for x in jmeno.split()]
        #one_name = " ".join(one_name)
        dup.append(one_name)
    sorted_dup = sorted(dup, key = lambda x: x[1], reverse=True)
    dup = []
    for jmeno in sorted_dup:
        one_name = " ".join(jmeno)
        dup.append(one_name)
    return dup
    


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    dup = []
    for jmeno in names:
        one_name = [x for x in jmeno.split()]
        #one_name = " ".join(one_name)
        dup.append(one_name)
    sorted_dup = sorted(dup, key = lambda x: len(x[0]))
    dup = []
    for jmeno in sorted_dup:
        dup.append(jmeno[0])
    return dup[0]

print(dedup_and_title_case_names(NAMES))
print(sort_by_surname_desc(NAMES))
print(shortest_first_name(NAMES))