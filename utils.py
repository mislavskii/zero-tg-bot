MAX_MESSAGE_LENGTH = 4096  # Telegram's limit for message length


def split_message(message):
    """
    Splits a long message into chunks that fit within Telegram's character limit.
    """
    return [message[i:i + MAX_MESSAGE_LENGTH] for i in range(0, len(message), MAX_MESSAGE_LENGTH)]
