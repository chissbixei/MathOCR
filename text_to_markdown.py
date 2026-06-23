import fitz
from pathlib import Path

# Klasör yolları
INPUT_DIR = Path.home() / "Desktop" / "pdf_ocr_projesi" / "input_text"
OUTPUT_DIR = Path.home() / "Desktop" / "pdf_ocr_projesi" / "output_all"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for pdf_file in INPUT_DIR.glob("*.pdf"):
    print(f"İşleniyor: {pdf_file.name}")

    try:
        doc = fitz.open(pdf_file)
        
        output_file = OUTPUT_DIR / f"{pdf_file.stem}.md"
        
        with open(output_file, "w", encoding="utf-8") as md:
            md.write(f"# {pdf_file.stem}\n\n")
            
            for page_num in range(len(doc)):
                page = doc[page_num]
                text = page.get_text()  # Daha iyi format için: page.get_text("text")
                
                if text.strip():  # Boş sayfaları atla
                    md.write(f"## Sayfa {page_num + 1}\n\n")
                    md.write(text)
                    md.write("\n\n")
                else:
                    md.write(f"## Sayfa {page_num + 1}\n\n*(Bu sayfada okunabilir metin bulunamadı)*\n\n")
        
        doc.close()
        print(f"Oluşturuldu: {output_file.name}")
        
    except Exception as e:
        print(f"Hata oluştu ({pdf_file.name}): {e}")

print("\nTüm PDF'ler Markdown'a dönüştürüldü.")