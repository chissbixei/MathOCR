import fitz
from pathlib import Path

INPUT_DIR = Path.home() / "Desktop" / "pdf_ocr_projesi" / "split" / "split_input"
OUTPUT_DIR = Path.home() / "Desktop" / "pdf_ocr_projesi" / "split" / "split_output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for pdf_file in INPUT_DIR.glob("*.pdf"):
    print(f"\nİşleniyor: {pdf_file.name}")

    doc = fitz.open(pdf_file)
    total_pages = len(doc)

    for start in range(0, total_pages, 5):      # Sayfa bölünme sayisi
        end = min(start + 5, total_pages)       # Sayfa bölünme sayisi

        new_doc = fitz.open()

        # 5 sayfalık chunk oluştur
        for page_num in range(start, end):
            new_doc.insert_pdf(
                doc,
                from_page=page_num,
                to_page=page_num
            )

        output_name = f"{pdf_file.stem}_{start + 1:03d}_{end:03d}.pdf"
        output_path = OUTPUT_DIR / output_name

        new_doc.save(output_path)
        new_doc.close()

        print(f"Oluşturuldu: {output_name}")

    doc.close()

print("\nTüm PDF'ler bölündü.")