class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


information = []

while True:
    command = input().split()
    if command[0] == 'Stop':
        break

    sender = command[0]
    receiver = command[1]
    content = command[2]
    email = Email(sender, receiver, content)
    information.append(email)

mails_to_send = list(map(int, input().split(', ')))

for i in mails_to_send:
    information[i].send()

for mail in information:
    print(mail.get_info())



