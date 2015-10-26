Step 1: Print!
```python
print('Hello Nicole!')
```


Step 2: find events in email
with open, variables, list
```python
def add_email():
    with open('email.txt', 'r') as email:
        lines = email.readlines()

    events = []
    for line in lines:
        if line.startswith('['):
            events.append(line)

    for event in events:
        print(event)


add_email()
```


Step 3: Categorizing events based on Broome credit
if/then
```python
def add_email():
    with open('email.txt', 'r') as email:
        lines = email.readlines()

    events = []
    for line in lines:
        if line.startswith('['):
            events.append(line)

    with open('BroomeCodes.txt', 'w') as output:
        for event in events:
            if 'Stream' in event:
                output.write('Stream, {}'.format(event))
            elif 'FFiR' in event:
                output.write('FFiR, {}'.format(event))
            elif 'BEAST' in event:
                output.write('BEAST, {}'.format(event))
            elif 'Floor' in event:
                output.write('Floor, {}'.format(event))
            elif 'Service' in event:
                output.write('Service, {}'.format(event))
            elif 'All Hall' in event:
                output.write('All Hall, {}'.format(event))
            else:
                output.write('Other, {}'.format(event))


add_email()
```


Step 4: Add log new attendance feature
input
```python
def add_email():
    with open('email.txt', 'r') as email:
        lines = email.readlines()

    events = []
    for line in lines:
        if line.startswith('['):
            events.append(line)

    with open('BroomeCodes.txt', 'w') as output:
        for event in events:
            if 'Stream' in event:
                output.write('Stream, {}'.format(event))
            elif 'FFiR' in event:
                output.write('FFiR, {}'.format(event))
            elif 'BEAST' in event:
                output.write('BEAST, {}'.format(event))
            elif 'Floor' in event:
                output.write('Floor, {}'.format(event))
            elif 'Service' in event:
                output.write('Service, {}'.format(event))
            elif 'All Hall' in event:
                output.write('All Hall, {}'.format(event))
            else:
                output.write('Other, {}'.format(event))


def log_attendance():
    with open('BroomeCodes.txt', 'a+') as events_file:
        events = events_file.readlines()

    for i, event in enumerate(events):
        print('{} - {}'.format(i, event))

    response = input('Please enter the corresponding event number: ')
    event_index = int(response)
    if event_index < len(events):
        event = events[event_index]
        with open('nicole_broome.txt', 'a+') as nicole_stats:
            nicole_stats.write(event)

    else:
        print('Invalid number')


add_email()
log_attendance()
```


Step 6: Putting them together into the menu
while True
```python
def add_email():
    with open('email.txt', 'r') as email:
        lines = email.readlines()
    events = []
    for line in lines:
        if line.startswith('['):
            events.append(line)

    with open('BroomeCodes.txt', 'w') as output:
        for event in events:
            if 'Stream' in event:
                output.write('Stream, {}'.format(event))
            elif 'FFiR' in event:
                output.write('FFiR, {}'.format(event))
            elif 'BEAST' in event:
                output.write('BEAST, {}'.format(event))
            elif 'Floor' in event:
                output.write('Floor, {}'.format(event))
            elif 'Service' in event:
                output.write('Service, {}'.format(event))
            elif 'All Hall' in event:
                output.write('All Hall, {}'.format(event))
            else:
                output.write('Other, {}'.format(event))


def log_attendance():
    with open('BroomeCodes.txt', 'a+') as events_file:
        events = events_file.readlines()

    for i, event in enumerate(events):
        print('{} - {}'.format(i, event))

    response = input('Please enter the corresponding event number: ')
    event_index = int(response)
    if event_index < len(events):
        event = events[event_index]
        with open('nicole_broome.txt', 'a+') as nicole_stats:
            nicole_stats.write(event)
    else:
        print('Invalid number') 


while True:
   print('Broome Main Menu')
   print('1 - Add New Email')
   print('2 - Log New Attendance')
   print('-- enter the corresponding number of the action you wish to perform --')

   response = str(input())
   if response[0] == '1':
       add_email()

   elif response[0] == '2':
       log_attendance()

   else:
       print('Unrecognized Number')
       print('Plase Try Again -- Meow')
```


Step 7: Add stats functionality
import
```python
import collections


def add_email():
    with open('email.txt', 'r') as email:
        lines = email.readlines()
    events = []
    for line in lines:
        if line.startswith('['):
            events.append(line)

    with open('BroomeCodes.txt', 'w') as output:
        for event in events:
            if 'Stream' in event:
                output.write('Stream, {}'.format(event))
            elif 'FFiR' in event:
                output.write('FFiR, {}'.format(event))
            elif 'BEAST' in event:
                output.write('BEAST, {}'.format(event))
            elif 'Floor' in event:
                output.write('Floor, {}'.format(event))
            elif 'Service' in event:
                output.write('Service, {}'.format(event))
            elif 'All Hall' in event:
                output.write('All Hall, {}'.format(event))
            else:
                output.write('Other, {}'.format(event))


def log_attendance():
    with open('BroomeCodes.txt', 'a+') as events_file:
        events = events_file.readlines()

    for i, event in enumerate(events):
        print('{} - {}'.format(i, event))

    response = input('Please enter the corresponding event number: ')
    event_index = int(response)
    if event_index < len(events):
        event = events[event_index]
        with open('nicole_broome.txt', 'a+') as nicole_stats:
            nicole_stats.write(event)
    else:
        print('Invalid number') 


def my_stats():
   stats = collections.defaultdict(int)
   with open('nicole_broome.txt', 'r+') as nicole_stats:
       for line in nicole_stats.readlines():
           stream_type = line.split(',')[0]
           stats[stream_type] += 1

   for event_type, count in stats.items():
       print('{} - {}'.format(event_type, count))


while True:
    print('Broome Main Menu')
    print('1 - Add New Email')
    print('2 - Log New Attendance')
    print('3 - Check my stats')
    print('-- enter the corresponding number of the action you wish to perform --')

    response = str(input())
    if response[0] == '1':
        add_email()

    elif response[0] == '2':
        log_attendance()

    elif response[0] == '3':
        my_stats()

    else:
        print('Unrecognized Number')
        print('Plase Try Again -- Meow')
```

Step 8: Add return to main menu functionality and quit
```python
import collections


def add_email():
    print('-- to return home type main menu --')
    response = input('say yes to parse events from email.txt')
    if 'main menu' in response.lower():
        return

    if 'y' in response.lower():
        with open('email.txt', 'r') as email:
            lines = email.readlines()

        events = []
        for line in lines:
            if line.startswith('['):
                events.append(line)

        with open('BroomeCodes.txt', 'w') as output:
            for event in events:
                if 'Stream' in event:
                    output.write('Stream, {}'.format(event))
                elif 'FFiR' in event:
                    output.write('FFiR, {}'.format(event))
                elif 'BEAST' in event:
                    output.write('BEAST, {}'.format(event))
                elif 'Floor' in event:
                    output.write('Floor, {}'.format(event))
                elif 'Service' in event:
                    output.write('Service, {}'.format(event))
                elif 'All Hall' in event:
                    output.write('All Hall, {}'.format(event))
                else:
                    output.write('Other, {}'.format(event))


def log_attendance():
    with open('BroomeCodes.txt', 'a+') as events_file:
        events = events_file.readlines()

    for i, event in enumerate(events):
        print('{} - {}'.format(i, event))

    print('-- to return home type main menu --')
    response = input('Please enter the corresponding event number: ')
    if 'main menu' in response.lower():
        return

    event_index = int(response)
    if event_index < len(events):
        event = events[event_index]
        with open('nicole_broome.txt', 'a+') as nicole_stats:
            nicole_stats.write(event)
    else:
        print('Invalid number') 


def my_stats():
    stats = collections.defaultdict(int)
    with open('nicole_broome.txt', 'r+') as nicole_stats:
        for line in nicole_stats.readlines():
            stream_type = line.split(',')[0]
            stats[stream_type] += 1

    for event_type, count in stats.items():
        print('{} - {}'.format(event_type, count))


while True:
    print('Broome Main Menu')
    print('1 - Add New Email')
    print('2 - Log New Attendance')
    print('3 - Check my stats')
    print('4 - Quit')
    print('-- enter the corresponding number of the action you wish to perform --')
    print('-- to return home type main menu --')

    response = input()
    if response[0] == '1':
        add_email()

    elif response[0] == '2':
        log_attendance()

    elif response[0] == '3':
        my_stats()

    elif response[0] == '4':
        print('Thanks Nicole.')
        break

    else:
        print('Unrecognized Number')
        print('Please Try Again -- Meow')
```

Step 9: Minor corrections to make useable beyond today
```python
import collections
import os.path


def add_email():
    print('-- to return home type main menu --')
    if 'main menu' in response.lower():
        continue

    elif 'y' in response.lower():
        with open('email.txt', 'r') as email:
            lines = email.readlines()
        events = []
        for line in lines:
            if line.startswith('['):
                events.append(line)

        with open('BroomeCodes.txt', 'a+') as output:
            for event in events:
                if 'Stream' in event:
                    output.write('Stream, {}'.format(event))
                elif 'FFiR' in event:
                    output.write('FFiR, {}'.format(event))
                elif 'BEAST' in event:
                    output.write('BEAST, {}'.format(event))
                elif 'Floor' in event:
                    output.write('Floor, {}'.format(event))
                elif 'Service' in event:
                    output.write('Service, {}'.format(event))
                elif 'All Hall' in event:
                    output.write('All Hall, {}'.format(event))
                else:
                    output.write('Other, {}'.format(event))

        with open('BroomeCodes.txt', 'r') as infile:
            events = infile.readlines()


def log_attendance():
    with open('BroomeCodes.txt', 'a+') as events_file:
        events = events_file.readlines()

    for i, event in enumerate(events):
        print('{} - {}'.format(i, event))

    print('-- to return home type main menu --')
    response = input('Please enter the corresponding event number: ')
    if 'main menu' in response.lower():
        continue

    event_index = int(response)
    if event_index < len(events):
        event = events[event_index]
        with open('nicole_broome.txt', 'a+') as nicole_stats:
            nicole_stats.write(event)
    else:
        print('Invalid number') 


def my_stats():
    stats = collections.defaultdict(int)
    if not os.path.isfile('nicole_broome.txt'):
        print('No events logged yet. Please log an event first')
        continue

    with open('nicole_broome.txt', 'r+') as nicole_stats:
        for line in nicole_stats.readlines():
            stream_type = line.split(',')[0]
            stats[stream_type] += 1

    for event_type, count in stats.items():
        print('{} - {}'.format(event_type, count))


while True:
    print('Broome Main Menu')
    print('1 - Add New Email')
    print('2 - Log New Attendance')
    print('3 - Check my stats')
    print('4 - Quit')
    print('-- enter the corresponding number of the action you wish to perform --')
    print('-- to return home type main menu --')

    response = input()
    if response[0] == '1':
        add_email()

    elif response[0] == '2':
        log_attendance()

    elif response[0] == '3':
        my_stats()

    elif response[0] == '4':
        print('Thanks Nicole.')
        break

    else:
        print('Unrecognized Number')
        print('Please Try Again -- Meow')
```
