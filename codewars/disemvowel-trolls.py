def disemvowel(string):
    import re
    return (re.sub('A|a|E|e|I|i|O|o|U|u', "", string))