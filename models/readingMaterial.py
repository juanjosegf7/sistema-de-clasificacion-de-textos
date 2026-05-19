from abc import ABC, abstractmethod


class ReadingMaterial(ABC):
    def __init__(
        self,
        materialId,
        title,
        author,
        country,
        writingYear,
        edition,
        publicationYear,
        isbn,
        formatType,
        owner,
        exchangeCenter,
    ):
        self.__materialId = materialId
        self.__title = title
        self.__author = author
        self.__country = country
        self.__writingYear = writingYear
        self.__edition = edition
        self.__publicationYear = publicationYear
        self.__isbn = isbn
        self.__formatType = formatType
        self.__owner = owner
        self.__exchangeCenter = exchangeCenter
        self.__available = True

    def getMaterialId(self):
        return self.__materialId

    def getTitle(self):
        return self.__title

    def getAuthor(self):
        return self.__author

    def getCountry(self):
        return self.__country

    def getWritingYear(self):
        return self.__writingYear

    def getEdition(self):
        return self.__edition

    def getPublicationYear(self):
        return self.__publicationYear

    def getIsbn(self):
        return self.__isbn

    def getFormatType(self):
        return self.__formatType

    def getOwner(self):
        return self.__owner

    def getExchangeCenter(self):
        return self.__exchangeCenter

    def isAvailable(self):
        return self.__available

    def changeAvailability(self, available):
        self.__available = available

    def getBasicInfo(self):
        return f"{self.__title} - {self.__author} ({self.__publicationYear})"

    def getMaterialInfo(self):
        availability = "Disponible" if self.__available else "No disponible"

        return (
            f"{self.__title} - {self.__author} | "
            f"País: {self.__country} | "
            f"Año escritura: {self.__writingYear} | "
            f"Edición: {self.__edition} | "
            f"Año publicación: {self.__publicationYear} | "
            f"ISBN: {self.__isbn} | "
            f"Formato: {self.__formatType} | "
            f"Estado: {availability}"
        )

    @abstractmethod
    def getMaterialType(self):
        pass

    @abstractmethod
    def classifyMaterial(self):
        pass

    @abstractmethod
    def showDetails(self):
        pass
