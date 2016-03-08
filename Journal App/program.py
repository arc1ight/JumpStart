def main():
    print_header()
    run_event_loop()


def print_header():
    print('-------------------------------')
    print('         JOURNAL APP')
    print('-------------------------------')


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = None
    journal_data = []

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, or E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("Sorry, I didn't understand '{}'.".format(cmd))

    print('Done, goodbye.')


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, item in enumerate(entries):
        print('[{}] {}'.format(idx + 1, item))


def add_entry(data):
    item = input('Add journal entry: <enter> to exit ')
    data.append(item)


main()
