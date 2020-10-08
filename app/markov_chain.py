import markovify


def tech_markov():
    # Get raw text as string.
    with open("corpus/tech._quotes.txt", encoding="utf8") as f:
        text = f.read()
    # Build the model.
    text_model = markovify.Text(text, state_size=1)
    # Print three randomly-generated sentences of no more than 280 characters
    for i in range(1):
        return text_model.make_short_sentence(280, max_overlap_ratio=0.5, tries=100)


def news_abstract():
    # Get raw text as string.
    with open("corpus/abstracts.txt") as f:
        text = f.read()
    # Build the model.
    text_model = markovify.NewlineText(text, state_size=1, well_formed="false")
    # Print three randomly-generated sentences of no more than 280 characters
    for i in range(1):
        return str(text_model.make_short_sentence(280, max_overlap_ratio=0.5, tries=100)).title()


def news_headline():
    with open("corpus/headlines.txt") as f:
        text = f.read()
    # Build the model.
    text_model = markovify.NewlineText(text, state_size=1, well_formed="false")
    # Print three randomly-generated sentences of no more than 280 characters
    for i in range(1):
        return str(text_model.make_short_sentence(200, max_overlap_ratio=0.5, tries=100)).title()
