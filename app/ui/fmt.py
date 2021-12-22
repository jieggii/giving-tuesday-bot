def fmt_child_name(name: str):
    first_name, last_name = name.split()
    return f"{first_name} {last_name[0]}."
