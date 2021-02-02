

def why_text() -> dict:
    list_text = []
    text = "The bottom line is that no matter how old we are, we all need to know we have something to offer, that we are valued and appreciated, that our voices count. The Three Plagues of loneliness, helplessness, and boredom exist, in part, due to ageism in our society. When people resort to snap judgments, don’t take the time to know us well as individuals, and write us off as either “too young” or “too old,” we never have the opportunity to share our talents, our gifts, or our generosity. Pigeon-holed by our age, we become ripe for boredom. Take the recent tragedy involving the random shooting in Oklahoma of an Australian baseball player by youth claiming to be “bored,”. While an extreme example, it’s a painful reminder that the Three Plagues, gone unchecked, are indeed deadly. When youth aren’t invited to give back, or to contribute somehow, some way, they are going to give up… just like an Elder, who gives up talking, walking, or eating in an impersonal care environment."
    tmp = ""
    for i in text:
        if i == ".":
            tmp += i
            list_text.append(tmp)
            tmp = ""
        else:
            tmp += i
    source = "https://changingaging.org/culture-change/ageism-not-just-for-grown-ups/"
    return {"text": list_text, "source": source}
