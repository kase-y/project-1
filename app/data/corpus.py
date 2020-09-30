import random

from pycorpora import words, humans, medicine, objects, governments, societies_and_groups, science, geography, \
    film_tv, books

templates = ["{who} believes \"{who2}s should {action} {object}\".",
             "{action} {preposition}",
             "I heard that {chemical} causes {symptom}.",
             "According to scientist {scientist}, {disease} maybe be related to {chemical}.",
             "Controversial new {media_key_value} sparks protests around parts of {location}.", ]


def template_choice():
    random.choice(templates)


def family_relations():
    family_members = random.choice(humans.familyRelations["familyRelations"])
    return family_members


def diseases():
    disease_list = random.choice(medicine.diseases["diseases"])
    return disease_list


def semi_secret_societies():
    group = random.choice(societies_and_groups.semi_secret)
    return group["name"]


def cities():
    city_state = random.choice(geography.us_cities["cities"])
    return city_state["city"] + "," + city_state["state"]


def book():
    book_choice = random.choice(books.bestsellers["books"])
    return book_choice["title"]


# def random_key_value(dict):
#     random_key = random.choice(list(dict.key()))
#     random_value = random.choice(dict[str(random_key)].value())
#     return random_key + "," + random_value
#
# def random_key_value(dict):
#     key_value = dict.__getitem__(random.choice(list(dict)))
#     key_value_str = str(key_value)
#     return key_value_str

def random_key_value(dict):
    # key_value = dict.__getitem__(random.choice(list(dict)))
    random_key = str(random.choice(list(dict.keys())))
    random_value = str(dict[random_key])
    key_value_str = random_key + ", " + random_value + ", "
    return key_value_str


# who
who_dict = {
    "celebrities": random.choice(humans.celebrities["celebrities"]),
    "occupations": random.choice(humans.occupations["occupations"]),
    "familyRelations": random.choice(list(family_relations().values())),
    "scientists": random.choice(humans.scientists["scientists"]),
    "personal_noun": random.choice(words.personal_nouns["personalNouns"])
}

ages_dict = {
    "man": random.randrange(19, 99),
    "women": random.randrange(19, 99),
    "child": random.randrange(1, 12),
    "kid": random.randrange(1, 12),
    "teenager": random.randrange(13, 18)
}


def random_who():
    return random.choice(list(who_dict.values()))


# what
disease_dict = {
    "cancers": random.choice(medicine.cancer["cancers"]),
    "disease": random.choice(diseases()),
    "symptoms": random.choice(medicine.symptoms["symptoms"])
}

conspiracy_dict = {
    "nsa_project": "project " + random.choice(governments.nsa_projects["codenames"]),
    "toxic_chemicals": random.choice(science.toxic_chemicals["chemicals"]),
    "semi_secret": semi_secret_societies()
}

media_dict = {
    "tv show": random.choice(film_tv.tv_shows["tv_shows"]),
    "movie": random.choice(film_tv.popular_movies["popular-movies"]),
    "book": book()
}

what_dict = {
    "medical": random.choice(list(disease_dict.values())),
    "objects": random.choice(objects.objects["objects"]),
}
# where
where_dict = {
    "city": cities(),
    "country": random.choice(geography.countries["countries"]),

}

action_dict = {
    "infinitive_verbs": random.choice(words.infinitive_verbs)

}

word_dict = {
    "preposition": random.choice(words.prepositions["prepositions"]),
    "adverb": random.choice(words.adverbs["adverbs"]),
    "adjective": random.choice(humans.descriptions["descriptions"]),
}


# template = templates.


def str_template():
    return (str(random.choice(templates)).format(
        who=random_who(),
        who2=random_who(),
        chemical=conspiracy_dict["toxic_chemicals"],
        disease=random.choice(list(disease_dict.values())),
        symptom=disease_dict["symptoms"],
        scientist=who_dict["scientists"],
        location=random.choice(list(where_dict.values())),
        media_key_value=random_key_value(media_dict),
        action=random.choice(list(action_dict.values())),
        object=what_dict["objects"],
        preposition=word_dict["preposition"],
        adverb=word_dict["adverb"],
        person=random.choice([random_key_value(ages_dict), who_dict["occupations"]])

    ).title())
