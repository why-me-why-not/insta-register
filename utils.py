import random
import string
import os


def choose_browser():
    browsers = ['Chrome', 'Firefox']
    return random.choice(browsers)


day = str(random.choice(list(range(1,29))))
month = str(random.choice(list(range(1,13))))
year = str(random.choice(list(range(1990,2001))))

def take_email():
    with open(file='emails.txt', mode='r', encoding='utf8') as f:
        login, password = f.readline().replace('\n', '').split(':')
        return [login, password]

def bad_email(email):
    with open(file='bad emails.txt', mode='a', encoding='utf8') as f:
        f.write(':'.join(email) +'\n')

def del_email(email):
    with open(file='emails.txt', mode='r', encoding='utf8') as f:
        lines = f.readlines()

    with open(file='emails.txt', mode='w', encoding='utf8') as f:
        for line in lines:
            if line.strip('\n') != ':'.join(email):
                f.write(line)

def save_accounts(data):
    with open(file='result.txt', mode='a', encoding='utf8') as f:
        f.write(data+'\n')

def randompassword():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(8, 15)
  return ''.join(random.choice(chars) for i in range(size))


def take_name():
    with open(file=os.path.join('name bases', 'names.txt'), mode='r', encoding='utf8') as f:
        lines = f.readlines()
        return random.choice(lines).strip('\n').replace(' ', '').replace('-', '').replace("'", "")

def take_surname():
    with open(file=os.path.join('name bases', 'surnames.txt'), mode='r', encoding='utf8') as f:
        lines = f.readlines()
        return random.choice(lines).strip('\n').replace(' ', '').replace('-', '').replace("'", "")

def simple_login(name, surname):
    symbols = ['_', '.']
    sep = random.choice(symbols)
    username = name + sep + surname
    return username.lower()

def complex_login(name, surname, year):
    user = random.choice([name, surname]).lower()
    symbols = ['_', '.']
    with open(file=os.path.join('name bases', 'adjectives.txt'), mode='r', encoding='utf8') as f:
        lines = f.readlines()
        adjective = random.choice(lines).strip('\n')
    username = ''.join([user,
                       random.choice(symbols),
                       adjective,
                       random.choice(symbols),
                       year]
                       )
    return username


