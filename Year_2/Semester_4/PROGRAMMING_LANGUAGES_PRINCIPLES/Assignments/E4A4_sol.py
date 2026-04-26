import datetime

class Document:
    """
    Represents a generic document with authors and a creation date.

    - __init__: Initializes creation date and author list.
    - addAuthor: Adds a new author to the document.
    - __str__: Returns basic document details.
    """

    def __init__(self, creation_date: datetime.datetime):
        """
        Initializes a Document instance.
        Args:
            creation_date (datetime): The timestamp when the document was created.
        """
        self.creation_date = creation_date
        self.authors = []

    def addAuthor(self, name: str):
        """
        Adds an author to the list of authors.
        Args:
            name (str): The name of the author.
        """
        # Stores authors in a list to maintain the order of addition.
        self.authors.append(name)

    def __str__(self) -> str:
        """
        Returns a string representation of the document.
        Returns:
            str: Creation date and comma-separated authors.
        """
        authors_str = ", ".join(self.authors)
        return f"Document created at {self.creation_date} authors={authors_str}"


class Book(Document):
    """
    A specific type of document representing a book.

    - __init__: Initializes with title in addition to base document attributes.
    - __str__: Appends title and BOOK type to the base string.
    """

    def __init__(self, creation_date: datetime.datetime, title: str):
        """
        Initializes a Book instance.
        Args:
            creation_date (datetime): The creation timestamp.
            title (str): The title of the book.
        """
        super().__init__(creation_date)
        self.title = title

    def __str__(self) -> str:
        """
        Returns a string representation of the book.
        Returns:
            str: Base document details plus title and type.
        """
        # Reuses the base document string to avoid redundant logic.
        base_str = super().__str__()
        return f"{base_str} title={self.title} type=BOOK"


class Email(Document):
    """
    A specific type of document representing an email.

    - __init__: Initializes with sender and subject.
    - addRecipient: Adds a recipient to the email.
    - __str__: Appends sender, subject, recipients, and EMAIL type.
    """

    def __init__(self, creation_date: datetime.datetime, sender: str, subject: str):
        """
        Initializes an Email instance.
        Args:
            creation_date (datetime): The creation timestamp.
            sender (str): The sender's name.
            subject (str): The email subject.
        """
        super().__init__(creation_date)
        self.sender = sender
        self.subject = subject
        self.recipients = []

    def addRecipient(self, name: str):
        """
        Adds a recipient to the recipient list.
        Args:
            name (str): The name of the recipient.
        """
        # Appends recipient names to track all intended readers.
        self.recipients.append(name)

    def __str__(self) -> str:
        """
        Returns a string representation of the email.
        Returns:
            str: Detailed email info including sender and recipients.
        """
        base_str = super().__str__()
        recipients_str = ", ".join(self.recipients)
        return f"{base_str} sender={self.sender} subject={self.subject} recipients={recipients_str} type=EMAIL"


def runExercise():
    """
    Creates various documents and displays them sorted by creation date.
    """
    documents = []
    
    d1 = Document(datetime.datetime(2022, 3, 24, 9, 30))
    d1.addAuthor("Nikos")
    
    d2 = Document(datetime.datetime(2022, 3, 24, 10, 20))
    d2.addAuthor("Petros")
    d2.addAuthor("Maria")

    d3 = Book(datetime.datetime(2021, 1, 1, 0, 0), "Philosophy 101")
    d3.addAuthor("Socrates")
    d3.addAuthor("Descartes")
    d3.addAuthor("Nietschie")

    d4 = Email(datetime.datetime(2022, 3, 26, 10, 30), "Panayiotis", "Important notice")
    d4.addAuthor("Panayiotis")
    d4.addRecipient("Maria")

    d5 = Email(datetime.datetime(2022, 3, 21, 22, 45), "Marianthi", "SPAM")
    d5.addAuthor("Marianthi")
    d5.addAuthor("Vasilis")
    d5.addRecipient("Maria")
    d5.addRecipient("Christos")
    d5.addRecipient("Vasilis")
    d5.addRecipient("Sofia")

    documents.append(d1)
    documents.append(d2)
    documents.append(d3)
    documents.append(d4)
    documents.append(d5)

    # Sorts documents chronologically based on their creation timestamp.
    documents.sort(key=lambda doc: doc.creation_date)
    
    for doc in documents:
        print(doc)

if __name__ == "__main__":
    runExercise()
