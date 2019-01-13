class Contact:
    def __init__(self, name, phone_number, email=None, address=None):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def print_info(self):
        print(self.name)
        print(self.phone_number)
        print(self.email)
        print(self.address)


def input_contact():
    name = input("name : ")
    phone_number = input("phone_number : ")
    email = input("email : ")
    address = input("address : ")

    c = Contact(name, phone_number, email, address)
    return c


def print_contacts(contacts):
    print('---------------------')
    for contact in contacts:
        contact.print_info()
        print('---------------------')


def find_contact(contacts, name):
    for contact in contacts:
        if name == contact.name:
            return contact
    return None


# name,phone_number,email,address\n
# ex : 홍길동,01082821001,hong@naver.com,서울시\n
def save_contacts_to_file(file, contacts):
    f = open(file, 'wt')
    for contact in contacts:
        f.write(contact.name + ',' + contact.phone_number + ',' + contact.email + ',' + contact.address + '\n')
    f.close()


def load_contacts_form_file(file):
    contacts = []
    f = open(file)
    lines = f.readlines()
    for line in lines:
        # 끝 '\n' 문자 제거 후, ','로 문자열 분리
        contact_line = line.split('\n')[0].split(',')
        contact = Contact(contact_line[0],  # 이름
                          contact_line[1],  # 전화번호
                          contact_line[2],  # 이메일
                          contact_line[3])  # 주소
        contacts.append(contact)
    return contacts


def run():
    contacts = load_contacts_form_file('./contacts_db.txt')
    while 1:
        print('1. 연락처 입력')
        print('2. 연락처 출력')
        print('3. 연락처 삭제')
        print('4. 종료')
        select_menu = int(input('메뉴선택 : '))

        if select_menu == 4:
            break

        if select_menu == 1:
            contacts.append(input_contact())
            save_contacts_to_file('./contacts_db.txt', contacts)
        if select_menu == 2:
            print_contacts(contacts)
        if select_menu == 3:
            delete_name_of_contact = input("삭제 주소록(이름) :")
            delete_contact = find_contact(contacts, delete_name_of_contact)
            contacts.remove(delete_contact)


if __name__ == "__main__":
    run()
