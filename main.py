from datetime import date

from models.user import User
from models.interest import Interest
from models.exchange import Exchange
from models.exchangeCenter import ExchangeCenter
from models.readingStatistic import ReadingStatistic
from models.materialTypes import (
    LiteratureBook,
    ScientificBook,
    Magazine,
    Comic,
    ResearchArticle,
)


def showPolymorphismDemo(readingMaterials):
    print("\n*** DEMOSTRACIÓN DE ABSTRACCIÓN Y POLIMORFISMO ***\n")

    print("Todos los materiales se recorren usando la misma estructura.")
    print("Sin embargo, cada clase hija responde diferente al mismo método.\n")

    for material in readingMaterials:
        print(f"Tipo: {material.getMaterialType()}")
        print(material.classifyMaterial())
        print(material.showDetails())
        print("-" * 100)


def main():
    print("*** SISTEMA DE CLASIFICACIÓN E INTERCAMBIO DE TEXTOS ***\n")

    userOne = User(
        userId=1,
        firstName="Juan Jose",
        lastName="Gonzalez Fitzgerald",
        documentNumber="1002456789",
        age=26,
        gender="Masculino",
        populationGroup="Adulto",
        address="Calle 10 # 20-30",
        phone="3001234567",
        email="jjgf@yopmail.com",
        registrationDate=date.today(),
    )

    userTwo = User(
        userId=2,
        firstName="Luisa Fda",
        lastName="Camargo Lopez",
        documentNumber="1098765432",
        age=24,
        gender="Femenino",
        populationGroup="Adulto",
        address="Carrera 15 # 40-21",
        phone="3109876543",
        email="luisa@yopmail.com",
        registrationDate=date.today(),
    )

    print(userOne.registerUser())
    print(userTwo.registerUser())
    print()

    center = ExchangeCenter(
        centerId=1,
        name="Centro Cultural Armenia",
        address="Av. Bolívar # 12-50",
        municipality="Armenia",
        department="Quindío",
    )

    print("*** CENTRO DE INTERCAMBIO ***")
    print(center.registerCenter())
    print(center.getCenterInfo())
    print()

    literatureBook = LiteratureBook(
        literaryGenre="Novela",
        materialId=1,
        title="Cien años de soledad",
        author="Gabriel García Márquez",
        country="Colombia",
        writingYear=1967,
        edition="Primera edición",
        publicationYear=1967,
        isbn="978-0307474728",
        formatType="Impreso",
        owner=userOne,
        exchangeCenter=center,
    )

    scientificBook = ScientificBook(
        subject="Ciencias naturales",
        materialId=2,
        title="Introducción a la Biología",
        author="Helena Curtis",
        country="Argentina",
        writingYear=2000,
        edition="Séptima edición",
        publicationYear=2001,
        isbn="978-9500604477",
        formatType="Impreso",
        owner=userTwo,
        exchangeCenter=center,
    )

    comic = Comic(
        publisher="Marvel",
        mainCharacter="Spider-Man",
        materialId=3,
        title="The Amazing Spider-Man",
        author="Stan Lee",
        country="Estados Unidos",
        writingYear=1963,
        edition="Edición especial",
        publicationYear=1963,
        isbn="978-0785112569",
        formatType="Digital",
        owner=userTwo,
        exchangeCenter=center,
    )

    magazine = Magazine(
        issueNumber="45",
        periodicity="Mensual",
        materialId=4,
        title="Revista Ciencia Hoy",
        author="Varios autores",
        country="Colombia",
        writingYear=2024,
        edition="Edición mensual",
        publicationYear=2024,
        isbn="ISSN-0327-1218",
        formatType="Impreso",
        owner=userOne,
        exchangeCenter=center,
    )

    researchArticle = ResearchArticle(
        researchArea="Educación",
        journalName="Revista de Investigación Académica",
        materialId=5,
        title="Hábitos de lectura en jóvenes",
        author="María Torres",
        country="Colombia",
        writingYear=2023,
        edition="Volumen 12",
        publicationYear=2023,
        isbn="ART-2023-001",
        formatType="Digital",
        owner=userOne,
        exchangeCenter=center,
    )

    readingMaterials = [
        literatureBook,
        scientificBook,
        comic,
        magazine,
        researchArticle,
    ]

    print("*** REGISTRO DE MATERIALES ***")
    for material in readingMaterials:
        print(center.addMaterial(material))
    print()

    showPolymorphismDemo(readingMaterials)

    print("\n*** MÉTODOS ESPECÍFICOS DE CADA SUBCLASE ***")
    print(literatureBook.classifyGenre())
    print(scientificBook.classifySubject())
    print(comic.getCharacterInfo())
    print(magazine.getIssueInfo())
    print(researchArticle.getResearchArea())
    print()

    print("*** MATERIALES DISPONIBLES EN EL CENTRO ***")
    print(center.listAvailableMaterials())
    print()

    print("*** USUARIO OFRECE MATERIAL ***")
    print(userOne.offerMaterial(literatureBook))
    print(userTwo.offerMaterial(comic))
    print()

    print("*** INTERESES DEL USUARIO ***")
    interestOne = Interest(
        interestId=1,
        name="Literatura",
        description="Interés por novelas y cuentos",
    )

    interestTwo = Interest(
        interestId=2,
        name="Cómics",
        description="Interés por historias gráficas",
    )

    print(interestOne.createInterest())
    print(interestOne.getInterestInfo())
    print(userOne.addInterest(interestOne))
    print(userOne.addInterest(interestTwo))
    print()

    print("*** PRÉSTAMO DE MATERIAL ***")
    loan, message = userOne.requestLoan(comic)
    print(message)

    if loan:
        print(loan.getLoanInfo())

    print()
    print(center.listAvailableMaterials())
    print()

    print("*** DEVOLUCIÓN DE MATERIAL ***")
    if loan:
        print(userOne.returnMaterial(loan))
        print(loan.getLoanInfo())

    print()

    print("*** HISTORIAL DE PRÉSTAMOS ***")
    print(userOne.viewLoanHistory())
    print()

    print("*** INTERCAMBIO DE MATERIAL ***")
    exchange = Exchange(
        exchangeId=1,
        userOne=userOne,
        userTwo=userTwo,
        offeredMaterial=literatureBook,
        requestedMaterial=comic,
        exchangeDate=date.today(),
    )

    print(exchange.createExchange())
    print(exchange.getExchangeInfo())
    print(exchange.confirmExchange())
    print(exchange.getExchangeInfo())
    print()

    print("*** ESTADÍSTICAS DE LECTURA ***")
    statistic = ReadingStatistic(statisticId=1)

    print(statistic.updateStatistic("Cómic"))
    print(statistic.updateStatistic("Literatura"))
    print(statistic.getStatisticInfo())
    print(userOne.addStatistic(statistic))
    print()

    print("*** INFORMACIÓN FINAL DEL USUARIO ***")
    print(userOne.getUserInfo())


if __name__ == "__main__":
    main()
