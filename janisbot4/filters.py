

def filter_lorrem(text):
    return str.startswith(text, "[LÖR]")


def filter_quote_message(text):
    return str.endswith(text, ":")
