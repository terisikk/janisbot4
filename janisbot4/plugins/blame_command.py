from janisbot4.api.quote_api import get_quote_metadata

COMMANDS = ["blame"]


async def index(message):
    """
    Get metadata for the message replied to.
    """
    reply = message.reply_to_message
    if not reply:
        return

    metadata = get_quote_metadata(reply.text)

    print(metadata)

    user = _parse_nested_name_value(metadata, "user")
    adder = _parse_nested_name_value(metadata, "adder")
    channel = _parse_nested_name_value(metadata, "channel")

    timestamp = metadata.get("timestamp", "unknown date")

    meta_reply = f"{user} at {channel} by {adder}, {timestamp}"

    await message.reply(meta_reply, reply=False)


def _parse_nested_name_value(metadata, field):
    unknown_response = "unknown " + field

    if metadata.get(field, None) is None:
        return unknown_response
    else:
        return metadata[field].get("name", unknown_response)
