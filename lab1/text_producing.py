def make_messages_text(messages: list, variant: str):
    f = open('data/messages_' + variant + '.txt', 'w', encoding='utf-8')
    for message in messages:
        f.write(message + '\n')
    f.close()
