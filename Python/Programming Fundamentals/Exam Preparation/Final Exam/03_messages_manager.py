def add_username(msg_info, username, sent_msgs, received_msgs):
    msg_info[username] = msg_info.get(username, {'sent' : sent_msgs, 'received': received_msgs})


def send_message(msg_info, sender, receiver):
    if sender in msg_info and receiver in msg_info:
        msg_info[sender]['sent'] += 1
        msg_info[receiver]['received'] += 1

        if msg_info[sender]['sent'] + msg_info[sender]['received'] >= capacity:
            del msg_info[sender]
            print(f"{sender} reached the capacity!")
        if msg_info[receiver]['sent'] + msg_info[receiver]['received'] >= capacity:
            del msg_info[receiver]
            print(f"{receiver} reached the capacity!")


def empty_records(msg_info, username):
    if username in msg_info:
        del msg_info[username]
    elif username == 'All':
        msg_info.clear()


capacity = int(input())

msg_info = {}

while True:
    command = input().split('=')
    action = command[0]
    if action == 'Statistics':
        break

    if action == 'Add':
        username = command[1]
        sent_msgs = int(command[2])
        received_msgs = int(command[-1])

        add_username(msg_info, username, sent_msgs, received_msgs)
    elif action == 'Message':
        sender = command[1]
        receiver = command[-1]

        send_message(msg_info, sender, receiver)
    elif action == 'Empty':
        username = command[1]
        empty_records(msg_info, username)


print(f"Users count: {len(msg_info)}")
for item in msg_info:
    total_msgs = msg_info[item]['sent'] + msg_info[item]['received']
    print(f"{item} - {total_msgs}")