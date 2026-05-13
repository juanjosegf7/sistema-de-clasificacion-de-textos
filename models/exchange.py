from datetime import date
from models.readingMaterial import ReadingMaterial


class Exchange:
    def __init__(
        self,
        exchangeId: int,
        userOne,
        userTwo,
        offeredMaterial: ReadingMaterial,
        requestedMaterial: ReadingMaterial,
        exchangeDate: date,
    ):
        self.__exchangeId = exchangeId
        self.__userOne = userOne
        self.__userTwo = userTwo
        self.__offeredMaterial = offeredMaterial
        self.__requestedMaterial = requestedMaterial
        self.__exchangeDate = exchangeDate
        self.__exchangeStatus = "Pendiente"

    def createExchange(self):
        return (
            f"Intercambio creado entre {self.__userOne.getFullName()} "
            f"y {self.__userTwo.getFullName()} con estado: {self.__exchangeStatus}"
        )

    def confirmExchange(self):
        self.__exchangeStatus = "Confirmado"
        return (
            f"Intercambio confirmado entre {self.__userOne.getFullName()} "
            f"y {self.__userTwo.getFullName()}."
        )

    def cancelExchange(self):
        self.__exchangeStatus = "Cancelado"
        return (
            f"Intercambio cancelado entre {self.__userOne.getFullName()} "
            f"y {self.__userTwo.getFullName()}."
        )

    def getExchangeInfo(self):
        return (
            f"ID intercambio: {self.__exchangeId} | "
            f"Usuario 1: {self.__userOne.getFullName()} | "
            f"Usuario 2: {self.__userTwo.getFullName()} | "
            f"Material ofrecido: {self.__offeredMaterial.getTitle()} | "
            f"Material solicitado: {self.__requestedMaterial.getTitle()} | "
            f"Fecha: {self.__exchangeDate} | "
            f"Estado: {self.__exchangeStatus}"
        )
