

def why_text() -> dict:
    text = "The bottom line is that no matter how old we are, we all need to know we have something to offer, that we are valued and appreciated, that our voices count. The Three Plagues of loneliness, helplessness, and boredom exist, in part, due to ageism in our society. When people resort to snap judgments, don’t take the time to know us well as individuals, and write us off as either “too young” or “too old,” we never have the opportunity to share our talents, our gifts, or our generosity. Pigeon-holed by our age, we become ripe for boredom. Take the recent tragedy involving the random shooting in Oklahoma of an Australian baseball player by youth claiming to be “bored,”. While an extreme example, it’s a painful reminder that the Three Plagues, gone unchecked, are indeed deadly. When youth aren’t invited to give back, or to contribute somehow, some way, they are going to give up… just like an Elder, who gives up talking, walking, or eating in an impersonal care environment."
    text = seperate(text)
    source = "https://changingaging.org/culture-change/ageism-not-just-for-grown-ups/"
    return {"text": text, "source": source}


def what_text() -> dict:
    text = """Ageism, also spelled agism, or often refered to as agecism, is stereotyping and/or discrimination against individuals or groups on the basis of their age. This may be casual or systematic. The term was coined in 1969 by Robert Neil Butler to describe discrimination against seniors, and patterned on sexism and racism.[3] Butler defined "ageism" as a combination of three connected elements"""
    text = seperate(text)
    source = "https://en.wikipedia.org/wiki/Ageism"
    return {"text": text, "source": source}


def how_text() -> dict:
    text = """If nothing else, this is clear: For every step we take to fight ageism against Elders, we need to take an equivalent one for youth. For every Elder’s story that you listen to, take some time to get to know a young person. Ageism against any age group will never truly be defeated, unless we simultaneously deal with how it affects young and old alike. Doing so also builds a much-needed bridge between Elders and young people. As natural allies, they need each other, perhaps now more than ever."""
    text = seperate(text)
    source = "https://changingaging.org/culture-change/ageism-not-just-for-grown-ups/"
    return {"text": text, "source": source}


def seperate(text: str) -> list:
    tmp = ""
    list_text = []
    for i in text:
        if i == ".":
            tmp += i
            list_text.append(tmp)
            tmp = ""
        else:
            tmp += i
    return list_text