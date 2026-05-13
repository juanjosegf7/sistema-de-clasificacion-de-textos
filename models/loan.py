from datetime import date
from models.readingMaterial import ReadingMaterial


class Loan:
    def __init__(
        self,
        loanId: int,
        user,
        material: ReadingMaterial,
        loanDate: date,
        expectedReturnDate: date,
    ):
        self.__loanId = loanId
        self.__user = user
        self.__material = material
        self.__loanDate = loanDate
        self.__expectedReturnDate = expectedReturnDate
        self.__actualReturnDate = None
        self.__loanStatus = "Activo"

    def createLoan(self):
        if not self.__material.isAvailable():
            self.__loanStatus = "Rechazado"
            return (
                "No se puede crear el préstamo porque el material no está disponible."
            )

        self.__material.changeAvailability(False)

        return (
            f"Préstamo creado para {self.__user.getFullName()} "
            f"con el material: {self.__material.getTitle()}"
        )

    def closeLoan(self):
        self.__actualReturnDate = date.today()
        self.__loanStatus = "Cerrado"
        self.__material.changeAvailability(True)
        return "Préstamo cerrado correctamente."

    def checkStatus(self):
        return self.__loanStatus

    def calculateDelayDays(self):
        currentDate = (
            self.__actualReturnDate if self.__actualReturnDate else date.today()
        )
        delay = (currentDate - self.__expectedReturnDate).days
        return delay if delay > 0 else 0

    def getLoanInfo(self):
        return (
            f"ID préstamo: {self.__loanId} | "
            f"Usuario: {self.__user.getFullName()} | "
            f"Material: {self.__material.getTitle()} | "
            f"Fecha préstamo: {self.__loanDate} | "
            f"Fecha esperada devolución: {self.__expectedReturnDate} | "
            f"Fecha real devolución: {self.__actualReturnDate} | "
            f"Estado: {self.__loanStatus} | "
            f"Días de retraso: {self.calculateDelayDays()}"
        )
