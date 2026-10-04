def clean_text(str):
    stripped = str.strip()
    lower_case = stripped.lower()
    replaced = lower_case.replace("  ", " ")
    return replaced



print(clean_text(" Hello World "))