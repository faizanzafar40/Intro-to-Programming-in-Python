def clear_screen():
    print("\n" * 60)


def banner_message(message, total_length=60):
    print("-" * total_length)
    message_length = len(message)
    guard_length_left = (total_length - message_length) // 2
    guard_length_right = (total_length - message_length - guard_length_left)
    print(" " * guard_length_left + str(message) + " " * guard_length_right)
    print("-" * total_length)
    print("")
