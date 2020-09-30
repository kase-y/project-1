import markovify


def tech_markov():
    # Get raw text as string.
    with open("corpus/tech._quotes.txt", encoding="utf8") as f:
        text = f.read()
    # Build the model.
    text_model = markovify.Text(text, state_size=2)
    # Print three randomly-generated sentences of no more than 280 characters
    for i in range(1):
        return text_model.make_short_sentence(240, tries=100)


def breaking_news():
    # Get raw text as string.
    with open("corpus/headlines.txt") as f:
        text = f.read()
    # Build the model.
    text_model = markovify.NewlineText(text, state_size=1, well_formed="false")
    # Print three randomly-generated sentences of no more than 280 characters
    for i in range(1):
        return str(text_model.make_short_sentence(140, tries=100)).title()
