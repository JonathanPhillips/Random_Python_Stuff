def extract_pid(LogLine):
    x = re.search(r"\[(\d+)\]", LogLine)
    if x is None:
        return "no ID"
    return x[1]
