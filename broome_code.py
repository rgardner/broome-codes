import collections
import os.path


def add_email():
    print('-- to return home type main menu --')
    print('reply yes to read in the email from email.txt')
    response = input()
    if 'main menu' in response.lower():
        return

    elif 'y' in response.lower():
        with open('email.txt', 'r') as email:
            lines = email.readlines()

        events = []
        for line in lines:
            if line.startswith('['):
                events.append(line)

        for event_name in events:
            print(event_name)

        with open('all_events.txt', 'a') as output:
            for event_name in events:
                if 'Stream' in event_name:
                    output.write('Stream, ' + event_name)
                elif 'FFiR' in event_name:
                    output.write('FFiR, ' + event_name)
                elif 'BEAST' in event_name:
                    output.write('BEAST, ' + event_name)
                elif 'Floor' in event_name:
                    output.write('Floor, ' + event_name)
                elif 'Service' in event_name or 'All Hall in' in event_name:
                    output.write('All Hall, ' + event_name)
                else:
                    output.write('Other, ' + event_name)


def log_attendance():
    with open('all_events.txt', 'r') as events_file:
        events = events_file.readlines()

    for i, event_name in enumerate(events):
        print(str(i) + ' - ' + event_name)

    response = input('Please enter the corresponding event number: ')
    if 'main menu' in response:
        return
    event_index  = int(response)
    if event_index < len(events):
        attended_event_name = events[event_index]
        with open('attended_events.txt', 'a') as nicole_stats:
            nicole_stats.write(attended_event_name)
    else:
        print('Invalid number')


def my_stats():
    stats = collections.defaultdict(int)
    with open('attended_events.txt', 'r') as nicole_stats:
        for line in nicole_stats.readlines():
            stream_type = line.split(',')[0]
            stats[stream_type] += 1

    for event_type, count in stats.items():
        print(event_type + ' - ' + str(count))


while True:
    print('Broome Main Menu')
    print('1 - Add New Email')
    print('2 - Log New Attendance')
    print('3 - Check my Stats')
    print('4 - Quit')
    print('-- enter the corresponding number of the action you wish to perform --')
    print('-- to return home type main menu --')

    response = str(input())
    if response.startswith('1'):
        add_email()

    elif response.startswith('2'):
        log_attendance()

    elif response.startswith('3'):
        my_stats()

    elif response.startswith('4'):
        print('Thanks, Nicole!')
        break

    else:
        print('Unrecognized Number')
        print('Please Try Again -- Meow')
