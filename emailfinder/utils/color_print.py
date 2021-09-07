from prompt_toolkit import print_formatted_text, HTML


def print_error(msg, start="", end=""):
    print_formatted_text(HTML(f"<red>{start}[!] </red> {msg}{end}"))

def print_ok(msg, start="", end=""):
    print_formatted_text(HTML(f"<green>{start}[+] </green>{msg}{end}"))

def print_info(msg, start="", end=""):
    print_formatted_text(HTML(f"<yellow>{start}[i] </yellow>{msg}{end}"))