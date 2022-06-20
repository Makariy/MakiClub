from uuid import UUID


def convert_string_to_uuid(uuid: str) -> UUID:
    """Converts uuid of type str to UUID. If param is not valid, returns None"""
    try:
        return UUID(uuid)
    except ValueError:
        return None

