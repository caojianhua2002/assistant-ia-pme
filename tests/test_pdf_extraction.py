from pathlib import Path

import pytest
from pypdf import PdfWriter
from pypdf.generic import DecodedStreamObject, DictionaryObject, NameObject

from src.assistant_ia.documents import PDFExtractionError, PDFExtractor


def _create_pdf_with_pages(path: Path, page_texts: list[str]) -> None:
    """Crée un vrai PDF minimal avec du texte extractible pour le test."""

    writer = PdfWriter()
    for text in page_texts:
        page = writer.add_blank_page(width=595, height=842)
        font = DictionaryObject(
            {
                NameObject("/Type"): NameObject("/Font"),
                NameObject("/Subtype"): NameObject("/Type1"),
                NameObject("/BaseFont"): NameObject("/Helvetica"),
            }
        )
        page[NameObject("/Resources")] = DictionaryObject(
            {
                NameObject("/Font"): DictionaryObject(
                    {NameObject("/F1"): font}
                )
            }
        )
        content = DecodedStreamObject()
        content.set_data(
            f"BT /F1 12 Tf 72 760 Td ({text}) Tj ET".encode("ascii")
        )
        page.replace_contents(content)

    with path.open("wb") as output:
        writer.write(output)


def test_extract_returns_text_and_page_sources_for_a_multi_page_pdf():
    pdf_path = Path(__file__).parent / "fixtures" / "contrat-martin.pdf"
    _create_pdf_with_pages(
        pdf_path,
        ["Contrat Martin - page 1", "Delai de paiement : 30 jours fin de mois"],
    )

    try:
        pages = PDFExtractor().extract(pdf_path)
    finally:
        pdf_path.unlink(missing_ok=True)

    assert [(page.page_number, page.text.strip()) for page in pages] == [
        (1, "Contrat Martin - page 1"),
        (2, "Delai de paiement : 30 jours fin de mois"),
    ]
    assert all(page.document_path == pdf_path for page in pages)


def test_extract_rejects_a_missing_document():
    with pytest.raises(PDFExtractionError, match="introuvable"):
        PDFExtractor().extract("tests/fixtures/absent.pdf")


def test_extract_rejects_a_non_pdf_extension():
    with pytest.raises(PDFExtractionError, match="extension .pdf"):
        PDFExtractor().extract("tests/fixtures/.gitkeep")
