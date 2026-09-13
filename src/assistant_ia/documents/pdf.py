"""Extraction locale et page par page du texte des fichiers PDF."""

from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader
from pypdf.errors import PdfReadError


class PDFExtractionError(RuntimeError):
    """Un fichier PDF ne peut pas être lu ou extrait."""


@dataclass(frozen=True)
class PDFPage:
    """Texte extrait d'une page, avec les métadonnées de source associées."""

    document_path: Path
    page_number: int
    text: str


class PDFExtractor:
    """Extrait le texte d'un PDF local tout en conservant son découpage en pages."""

    def extract(self, path: str | Path) -> list[PDFPage]:
        """Retourne une entrée par page de ``path``.

        La numérotation commence à 1, comme celle affichée par les lecteurs PDF.
        Une page sans texte est conservée avec une chaîne vide : cela permet de
        garder une référence de source fiable pour les étapes de recherche et de
        citation à venir.
        """

        document_path = self._validate_path(path)

        try:
            reader = PdfReader(document_path)
            return [
                PDFPage(
                    document_path=document_path,
                    page_number=page_number,
                    text=page.extract_text() or "",
                )
                for page_number, page in enumerate(reader.pages, start=1)
            ]
        except (OSError, PdfReadError) as exc:
            raise PDFExtractionError(
                f"Impossible d'extraire le PDF « {document_path} »."
            ) from exc

    @staticmethod
    def _validate_path(path: str | Path) -> Path:
        if not isinstance(path, (str, Path)):
            raise PDFExtractionError(
                "Le chemin du document PDF doit être une chaîne ou un Path."
            )

        document_path = Path(path)
        if not document_path.is_file():
            raise PDFExtractionError(
                f"Le document PDF est introuvable : « {document_path} »."
            )
        if document_path.suffix.lower() != ".pdf":
            raise PDFExtractionError(
                f"Le document doit avoir l'extension .pdf : « {document_path} »."
            )
        return document_path
