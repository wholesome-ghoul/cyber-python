import crypt


def crack_pass(pass_hash):
    salt = ""

    if pass_hash[0:3] == "$6$":
        salt = pass_hash[0:3] + pass_hash.split("$")[2]
    else:
        salt = pass_hash[0:2]

    passwords = open("dictionary.txt", 'r')

    for password in passwords.readlines():
        hashed_pass = crypt.crypt(password.strip(), salt)

        if hashed_pass == pass_hash:
            print("[+] Found password: {}".format(password))
            return

    print("[-] Password Not Found\n")
    return


def main():
    pass_file = open("passwords.txt")

    for line in pass_file.readlines():
        if ":" in line:
            user, pass_hash = line.strip().split(":")
            print("[*] Cracking pass for user: {}".format(user))
            crack_pass(pass_hash)


if __name__ == "__main__":
    main()
