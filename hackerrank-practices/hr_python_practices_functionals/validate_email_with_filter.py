import re


def fun(s):
    if '@' in s:
        ind = s.index('@')
        username = s[:ind]
        post_name = s[ind + 1:]

        if len(post_name.split('.')) != 2:
            return False
        elif (len(post_name.split('.')[1])) > 3:
            return False
        elif not post_name.split('.')[0].isalnum():
            return False
        elif username.strip() == "":
            return False
        elif re.fullmatch(r"^[a-zA-Z0-9_-]*", username) is None:
            return False
    else:
        return False
    return True
    # return True if s is a valid email, else return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
