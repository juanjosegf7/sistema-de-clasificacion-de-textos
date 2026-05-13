class Interest:
    def __init__(self, interestId: int, name: str, description: str):
        self.__interestId = interestId
        self.__name = name
        self.__description = description

    def createInterest(self):
        return f"Interés '{self.__name}' creado correctamente."

    def updateInterest(self, name=None, description=None):
        if name:
            self.__name = name
        if description:
            self.__description = description
        return "Interés actualizado correctamente."

    def getInterestId(self):
        return self.__interestId

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def getInterestInfo(self):
        return (
            f"ID interés: {self.__interestId} | "
            f"Nombre: {self.__name} | "
            f"Descripción: {self.__description}"
        )
