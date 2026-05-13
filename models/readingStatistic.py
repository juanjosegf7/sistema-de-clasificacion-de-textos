class ReadingStatistic:
    def __init__(
        self,
        statisticId: int,
        weekCount: int = 0,
        monthCount: int = 0,
        yearCount: int = 0,
        preferredMaterialType: str = "Sin definir",
    ):
        self.__statisticId = statisticId
        self.__weekCount = weekCount
        self.__monthCount = monthCount
        self.__yearCount = yearCount
        self.__preferredMaterialType = preferredMaterialType

    def updateStatistic(self, materialType: str):
        self.__weekCount += 1
        self.__monthCount += 1
        self.__yearCount += 1
        self.__preferredMaterialType = materialType
        return "Estadística actualizada correctamente."

    def calculateWeeklyReading(self):
        return self.__weekCount

    def calculateMonthlyReading(self):
        return self.__monthCount

    def calculateYearlyReading(self):
        return self.__yearCount

    def getStatisticInfo(self):
        return (
            f"ID estadística: {self.__statisticId} | "
            f"Lecturas semana: {self.__weekCount} | "
            f"Lecturas mes: {self.__monthCount} | "
            f"Lecturas año: {self.__yearCount} | "
            f"Tipo preferido: {self.__preferredMaterialType}"
        )
