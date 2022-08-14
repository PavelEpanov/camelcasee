def solution(s):
    result = ""
    result += s[0].lower()
    for slot in s[1:]:
        if slot.isupper():
            result += f" {slot}"
        else:
            result += slot
    return result