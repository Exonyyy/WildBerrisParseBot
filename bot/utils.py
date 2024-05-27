def check_is_in(_dict: dict, text: str) -> bool:
    for key in _dict.keys():
        if text in _dict[key]:
            return True
    else:
        return False
