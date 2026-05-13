from datetime import date
from models.loan import Loan
from models.interest import Interest
from models.readingMaterial import ReadingMaterial
from models.readingStatistic import ReadingStatistic


class User:
    def __init__(
        self,
        userId: int,
        firstName: str,
        lastName: str,
        documentNumber: str,
        age: int,
        gender: str,
        populationGroup: str,
        address: str,
        phone: str,
        email: str,
        registrationDate: date,
    ):
        self.__userId = userId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__documentNumber = documentNumber
        self.__age = age
        self.__gender = gender
        self.__populationGroup = populationGroup
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__registrationDate = registrationDate
        self.__ownedMaterials = []
        self.__loans = []
        self.__interests = []
        self.__statistics = []

    def registerUser(self):
        return f"Usuario {self.__firstName} {self.__lastName} registrado correctamente."

    def updateInformation(self, address=None, phone=None, email=None):
        if address:
            self.__address = address
        if phone:
            self.__phone = phone
        if email:
            self.__email = email

        return "Información del usuario actualizada correctamente."

    def offerMaterial(self, material: ReadingMaterial):
        self.__ownedMaterials.append(material)
        return f"El usuario ofreció el material: {material.getTitle()}"

    def requestLoan(self, material: ReadingMaterial):
        loan = Loan(
            loanId=len(self.__loans) + 1,
            user=self,
            material=material,
            loanDate=date.today(),
            expectedReturnDate=date(2026, 6, 1),
        )

        result = loan.createLoan()

        if loan.checkStatus() != "Rechazado":
            self.__loans.append(loan)

        return loan, result

    def returnMaterial(self, loan: Loan):
        return loan.closeLoan()

    def viewLoanHistory(self):
        if not self.__loans:
            return "El usuario no tiene préstamos registrados."

        result = "Historial de préstamos:\n"

        for loan in self.__loans:
            result += f"- {loan.getLoanInfo()}\n"

        return result

    def addInterest(self, interest: Interest):
        self.__interests.append(interest)
        return f"Interés agregado: {interest.getName()}"

    def addStatistic(self, statistic: ReadingStatistic):
        self.__statistics.append(statistic)
        return "Estadística asociada al usuario."

    def getFullName(self):
        return f"{self.__firstName} {self.__lastName}"

    def getUserInfo(self):
        return (
            f"ID: {self.__userId} | "
            f"Nombre: {self.__firstName} {self.__lastName} | "
            f"Documento: {self.__documentNumber} | "
            f"Edad: {self.__age} | "
            f"Género: {self.__gender} | "
            f"Grupo poblacional: {self.__populationGroup} | "
            f"Dirección: {self.__address} | "
            f"Teléfono: {self.__phone} | "
            f"Email: {self.__email} | "
            f"Fecha de registro: {self.__registrationDate}"
        )
