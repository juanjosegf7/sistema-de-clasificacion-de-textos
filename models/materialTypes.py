from models.readingMaterial import ReadingMaterial


class LiteratureBook(ReadingMaterial):
    def __init__(self, literaryGenre: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__literaryGenre = literaryGenre

    def classifyGenre(self):
        return f"Género literario: {self.__literaryGenre}"

    def classifyMaterial(self):
        return "Clasificación: libro de literatura."


class ScientificBook(ReadingMaterial):
    def __init__(self, subject: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__subject = subject

    def classifySubject(self):
        return f"Materia científica: {self.__subject}"

    def classifyMaterial(self):
        return "Clasificación: libro científico."


class Magazine(ReadingMaterial):
    def __init__(self, issueNumber: str, periodicity: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__issueNumber = issueNumber
        self.__periodicity = periodicity

    def getIssueInfo(self):
        return f"Número de edición: {self.__issueNumber} | Periodicidad: {self.__periodicity}"

    def classifyMaterial(self):
        return "Clasificación: revista."


class Comic(ReadingMaterial):
    def __init__(self, publisher: str, mainCharacter: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__publisher = publisher
        self.__mainCharacter = mainCharacter

    def getCharacterInfo(self):
        return f"Editorial: {self.__publisher} | Personaje principal: {self.__mainCharacter}"

    def classifyMaterial(self):
        return "Clasificación: cómic."


class ResearchArticle(ReadingMaterial):
    def __init__(self, researchArea: str, journalName: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__researchArea = researchArea
        self.__journalName = journalName

    def getResearchArea(self):
        return f"Área de investigación: {self.__researchArea} | Revista: {self.__journalName}"

    def classifyMaterial(self):
        return "Clasificación: artículo de investigación."
