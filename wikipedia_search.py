import wikipediaapi

def get_nepali_wikipedia_intro(word):
    user_agent = 'Kanchi (swapunil27@gmail.com)'  # id ra email bina kaam gardaina noobde le

    wiki_ne = wikipediaapi.Wikipedia(
        language='ne',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent=user_agent
    )

    page_ne = wiki_ne.page(word)

    if not page_ne.exists():
        return f"'{word}' को लागि पृष्ठ नेपाली विकिपेडियामा अवस्थित छैन।"

    summary = page_ne.summary.split('\n')[0]

    return summary

def search_wikipedia(phrase):
    if phrase.startswith("कान्छी"):
        second_word = extract_second_word(phrase)
        if second_word:
            return get_nepali_wikipedia_intro(second_word)
        else:
            return "दोस्रो शब्द निकाल्न सकिएन।"
    else:
        return "इनपुट 'कान्छी' बाट सुरु हुँदैन।"

def extract_second_word(phrase):
    words = phrase.split()
    if len(words) >= 2:
        return words[1]
    return None
