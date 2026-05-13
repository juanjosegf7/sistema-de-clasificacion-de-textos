class ReadingMaterial:
    def __init__(
        self,
        materialId: int,
        title: str,
        author: str,
        country: str,
        writingYear: int,
        edition: str,
        publicationYear: int,
        isbn: str,
        format: str,
        origin: str,
        condition: str,
        available: bool = True,
    ):
        self.__materialId = materialId
        self.__title = title
        self.__author = author
        self.__country = country
        self.__writingYear = writingYear
        self.__edition = edition
        self.__publicationYear = publicationYear
        self.__isbn = isbn
        self.__format = format
        self.__origin = origin
        self.__condition = condition
        self.__available = available

    def registerMaterial(self):
        return f"Material '{self.__title}' registrado correctamente."

    def updateMaterial(self, title=None, condition=None):
        if title:
            self.__title = title
        if condition:
            self.__condition = condition
        return "Material actualizado correctamente."

    def classifyMaterial(self):
        return "Clasificación: material de lectura general."

    def changeAvailability(self, available: bool):
        self.__available = available
        return f"Disponibilidad cambiada a: {self.__available}"

    def getMaterialInfo(self):
        return (
            f"ID: {self.__materialId} | "
            f"Título: {self.__title} | "
            f"Autor: {self.__author} | "
            f"País: {self.__country} | "
            f"Año escritura: {self.__writingYear} | "
            f"Edición: {self.__edition} | "
            f"Año publicación: {self.__publicationYear} | "
            f"ISBN: {self.__isbn} | "
            f"Formato: {self.__format} | "
            f"Origen: {self.__origin} | "
            f"Estado: {self.__condition} | "
            f"Disponible: {self.__available}"
        )

    def getTitle(self):
        return self.__title

    def getIsbn(self):
        return self.__isbn

    def isAvailable(self):
        return self.__available
