def format_accidental(accidental: str) -> str:
    if accidental == "s":
        return "\u266f"
    elif accidental == "f":
        return "\u266d"
    else:
        raise KeyError("Not an accidental.")


class _Display_(_Key):
    def __repr__(self):
        keyname = self._key.name
        keyname = keyname.replace("s", format_accidental("s"))
        keyname = keyname.replace("s", format_accidental("s"))
        return keyname
