from models.readingMaterial import ReadingMaterial


class LiteratureBook(ReadingMaterial):
    def __init__(self, literaryGenre, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__literaryGenre = literaryGenre

    def getLiteraryGenre(self):
        return self.__literaryGenre

    def getMaterialType(self):
        return "Libro de literatura"

    def classifyGenre(self):
        return f"Género literario: {self.__literaryGenre}"

    def classifyMaterial(self):
        return "Clasificación: material literario destinado a lectura narrativa o cultural."

    def showDetails(self):
        return (
            f"{self.getMaterialInfo()} | "
            f"Tipo: {self.getMaterialType()} | "
            f"Género: {self.__literaryGenre}"
        )


class ScientificBook(ReadingMaterial):
    def __init__(self, subject, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__subject = subject

    def getSubject(self):
        return self.__subject

    def getMaterialType(self):
        return "Libro científico"

    def classifySubject(self):
        return f"Materia científica: {self.__subject}"

    def classifyMaterial(self):
        return "Clasificación: material científico organizado por área de conocimiento."

    def showDetails(self):
        return (
            f"{self.getMaterialInfo()} | "
            f"Tipo: {self.getMaterialType()} | "
            f"Materia: {self.__subject}"
        )


class Magazine(ReadingMaterial):
    def __init__(self, issueNumber, periodicity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__issueNumber = issueNumber
        self.__periodicity = periodicity

    def getIssueNumber(self):
        return self.__issueNumber

    def getPeriodicity(self):
        return self.__periodicity

    def getMaterialType(self):
        return "Revista"

    def getIssueInfo(self):
        return (
            f"Número de edición: {self.__issueNumber} | "
            f"Periodicidad: {self.__periodicity}"
        )

    def classifyMaterial(self):
        return "Clasificación: revista de publicación periódica."

    def showDetails(self):
        return (
            f"{self.getMaterialInfo()} | "
            f"Tipo: {self.getMaterialType()} | "
            f"Número de edición: {self.__issueNumber} | "
            f"Periodicidad: {self.__periodicity}"
        )


class Comic(ReadingMaterial):
    def __init__(self, publisher, mainCharacter, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__publisher = publisher
        self.__mainCharacter = mainCharacter

    def getPublisher(self):
        return self.__publisher

    def getMainCharacter(self):
        return self.__mainCharacter

    def getMaterialType(self):
        return "Cómic"

    def getCharacterInfo(self):
        return (
            f"Editorial: {self.__publisher} | "
            f"Personaje principal: {self.__mainCharacter}"
        )

    def classifyMaterial(self):
        return "Clasificación: cómic con contenido gráfico y narrativo."

    def showDetails(self):
        return (
            f"{self.getMaterialInfo()} | "
            f"Tipo: {self.getMaterialType()} | "
            f"Editorial: {self.__publisher} | "
            f"Personaje principal: {self.__mainCharacter}"
        )


class ResearchArticle(ReadingMaterial):
    def __init__(self, researchArea, journalName, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__researchArea = researchArea
        self.__journalName = journalName

    def getResearchAreaValue(self):
        return self.__researchArea

    def getJournalName(self):
        return self.__journalName

    def getMaterialType(self):
        return "Artículo de investigación"

    def getResearchArea(self):
        return (
            f"Área de investigación: {self.__researchArea} | "
            f"Revista: {self.__journalName}"
        )

    def classifyMaterial(self):
        return "Clasificación: artículo académico o de investigación."

    def showDetails(self):
        return (
            f"{self.getMaterialInfo()} | "
            f"Tipo: {self.getMaterialType()} | "
            f"Área: {self.__researchArea} | "
            f"Revista: {self.__journalName}"
        )
