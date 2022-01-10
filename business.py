import csv
import pandas as pd


class Business:
    raw_data = {'Name': [],
                'Title': [],
                'Telephone': [],
                'Address': [],
                'Webpage': [],
                'Stars': [],
                'Reviews': []}

    def __init__(self, name: str, title: str, phone: str, address: str, webpage='', stars=0.0, reviews=0):
        # Assign to self object
        self.__name = name
        self.__title = title
        self.__phone = phone
        self.__address = address
        self.__webpage = webpage
        self.__stars = stars
        self.__reviews = reviews

        # Actions to execute
        Business.raw_data['Name'].append(self.name)
        Business.raw_data['Title'].append(self.title)
        Business.raw_data['Telephone'].append(self.phone)
        Business.raw_data['Address'].append(self.address)
        Business.raw_data['Webpage'].append(self.webpage)
        Business.raw_data['Stars'].append(self.stars)
        Business.raw_data['Reviews'].append(self.reviews)

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def webpage(self):
        return self.__webpage

    @webpage.setter
    def webpage(self, value):
        self.__webpage = value

    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self, value):
        self.__stars = value

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, value):
        self.__reviews = value

    @classmethod
    def export_data(cls):
        df = pd.DataFrame(Business.raw_data)
        print(df)
        df.to_csv('business.csv', index=False)
        print('Data has been exported in csv and xlsx format. Check out your project folder.')
        df.to_excel('business.xlsx', index=False)


    @classmethod
    def instantiate_from_csv(cls, rute):
        with open(rute, 'r') as f:
            reader = csv.DictReader(f)  # Lee nuestro contenido como un diccionario
            values = list(reader)

        for value in values:
            print(value)
            Business(
                name=value.get('Name'),
                title=value.get('Title'),
                phone=value.get('Phone'),
                address=value.get('Address'),
                webpage=value.get('Webpage'),
                stars=value.get('Stars'),
                reviews=value.get('Reviews')
            )

    @classmethod
    def instantiate_from_gspread(cls, values):
        for value in values:
            Business(
                name=value.get('Name'),
                title=value.get('Title'),
                phone=value.get('Phone'),
                address=value.get('Address'),
                webpage=value.get('Webpage'),
                stars=value.get('Stars'),
                reviews=value.get('Reviews')
            )
            print(f"We've got data from the business {value.get('Name')}")

    @staticmethod
    def is_new(name):
        if name not in Business.raw_data['Name']:
            return True
        else:
            print(f"The business called {name} it's already registered")
            return False

    def __repr__(self):
        return self.name
