from address_book import AddressBook
from phone_bot import PhoneBot


def main():
    book = AddressBook()
    phone_bot = PhoneBot(book)
    phone_bot.start_bot()


if __name__ == "__main__":
    print("Hello")
    main()
