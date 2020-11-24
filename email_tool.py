import imaplib, email, time
from email.header import decode_header

def email_login(login, password, mail):
    counter = 0
    try:
        mail.login(login, password)
        print('Successful authorization')
        return mail
    except:
        print('Authorization is failed. Waiting for 1 minute')
        counter +=1
        if counter > 3:
            raise Exception(f"Can't log in {login}. Wrong password or IMAP is disabled")
        time.sleep(60)
        return False


def get_insta_code(login, password):

    server = login.split('@')[1]
    mail = imaplib.IMAP4_SSL(f'imap.{server}')

    while email_login(login, password, mail) is False:
        email_login(login, password, mail)

    mail.select('INBOX')

    search_params = '(FROM "Instagram")'
    result, data = mail.search("utf-8", search_params.encode("utf-8"))
    find_email = bool(data[0])
    while find_email is False:
        result, data = mail.search("utf-8", search_params.encode("utf-8"))
        find_email = bool(data[0])
        print("Can't find email from Instagram. Waiting for 15 seconds")
        time.sleep(15)

    print('Email from Instagram is found')

    ids = data[0] # b'1 2 3 4 5 6 7 8 9 10 11'
    id_list = ids.split() # [b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9', b'10', b'11']
    latest_email_id = id_list[-1] # b'11'
    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf8')
    email_message = email.message_from_string(raw_email_string)
    subject = email_message['Subject']
    bytes, encoding = decode_header(subject)[0]
    try:
        decoded_subject = bytes.decode(encoding)
    except AttributeError:
        decoded_subject = bytes
    mail.logout()

    code = ''.join(i for i in decoded_subject if i.isdigit())

    return code