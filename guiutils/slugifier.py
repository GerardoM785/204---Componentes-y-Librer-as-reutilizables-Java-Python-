import unicodedata
import re

def slug(text: str) -> str:
    """
    Convierte una cadena de texto en un slug legible y seguro para URLs.
    Ejemplo: "Hola Mundo!" -> "hola-mundo"
    """
    if not isinstance(text, str):
        return ""
    # Normalizar caracteres unicode (remover acentos)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    # Filtrar caracteres especiales, convertir a minúsculas y quitar espacios extremos
    text = re.sub(r"[^a-zA-Z0-9\s-]", "", text).strip().lower()
    # Reemplazar espacios por guiones y eliminar guiones duplicados
    text = re.sub(r"\s+", "-", text)
    return re.sub(r"-{2,}", "-", text)