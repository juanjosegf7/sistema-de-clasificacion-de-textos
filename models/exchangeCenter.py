from models.readingMaterial import ReadingMaterial


class ExchangeCenter:
    def __init__(
        self, centerId: int, name: str, address: str, municipality: str, department: str
    ):
        self.__centerId = centerId
        self.__name = name
        self.__address = address
        self.__municipality = municipality
        self.__department = department
        self.__materials = []

    def registerCenter(self):
        return (
            f"Centro de intercambio '{self.__name}' registrado correctamente "
            f"en {self.__municipality}, {self.__department}."
        )

    def updateCenter(self, name=None, address=None):
        if name:
            self.__name = name
        if address:
            self.__address = address
        return "Centro actualizado correctamente."

    def addMaterial(self, material: ReadingMaterial):
        self.__materials.append(material)
        return f"Material '{material.getTitle()}' agregado al centro."

    def listAvailableMaterials(self):
        availableMaterials = [
            material for material in self.__materials if material.isAvailable()
        ]

        if not availableMaterials:
            return "No hay materiales disponibles en este centro."

        result = "Materiales disponibles:\n"
        for material in availableMaterials:
            result += f"- {material.getTitle()} | ISBN: {material.getIsbn()}\n"

        return result

    def getCenterInfo(self):
        return (
            f"ID centro: {self.__centerId} | "
            f"Nombre: {self.__name} | "
            f"Dirección: {self.__address} | "
            f"Municipio: {self.__municipality} | "
            f"Departamento: {self.__department}"
        )
