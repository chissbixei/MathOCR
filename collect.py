import shutil
from pathlib import Path

BASE = Path.home() / "Desktop" / "pdf_ocr_projesi"

ALL_MARKDOWNS = BASE / "All Markdowns"
PROCESSED_OCR = BASE / "Processed OCR Folders"
PROCESSED_INPUTS = BASE / "Processed Inputs"

ALL_MARKDOWNS.mkdir(parents=True, exist_ok=True)
PROCESSED_OCR.mkdir(parents=True, exist_ok=True)
PROCESSED_INPUTS.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# 1. Merged Markdowns içindeki md'leri TAŞI
# --------------------------------------------------
MERGED_DIR = BASE / "merge" / "Merged Markdowns"

if MERGED_DIR.exists():
    for md_file in MERGED_DIR.glob("*.md"):
        destination = ALL_MARKDOWNS / md_file.name
        if destination.exists():
            stem = md_file.stem
            suffix = md_file.suffix
            counter = 1
            while destination.exists():
                destination = ALL_MARKDOWNS / f"{stem}_{counter}{suffix}"
                counter += 1
        shutil.move(str(md_file), str(destination))

# --------------------------------------------------
# 2. output_all içindeki tüm md'leri TAŞI (recursive)
# --------------------------------------------------
OUTPUT_ALL = BASE / "output_all"

if OUTPUT_ALL.exists():
    for md_file in OUTPUT_ALL.rglob("*.md"):
        destination = ALL_MARKDOWNS / md_file.name
        if destination.exists():
            stem = md_file.stem
            suffix = md_file.suffix
            counter = 1
            while destination.exists():
                destination = ALL_MARKDOWNS / f"{stem}_{counter}{suffix}"
                counter += 1
        shutil.move(str(md_file), str(destination))

# --------------------------------------------------
# 3. output_all içindeki klasörleri taşı (OCR çıktıları)
# --------------------------------------------------
if OUTPUT_ALL.exists():
    for item in OUTPUT_ALL.iterdir():
        if item.is_dir():
            destination = PROCESSED_OCR / item.name
            if destination.exists():
                shutil.rmtree(destination)
            shutil.move(str(item), str(destination))

# --------------------------------------------------
# 4. input_math, input_text ve split/split_input İÇERİKLERİNİ 
#    doğrudan Processed Inputs içine taşı (düzleştirilmiş)
# --------------------------------------------------
input_sources = [
    BASE / "input_math",
    BASE / "input_text",
    BASE / "split" / "split_input"
]

for source_dir in input_sources:
    if source_dir.exists():
        for item in source_dir.rglob("*"):  # recursive, tüm alt dosyalar ve klasörler
            if item.is_file() or item.is_dir():  # hem dosya hem klasör
                relative_path = item.relative_to(source_dir)
                destination = PROCESSED_INPUTS / relative_path
                
                if destination.exists():
                    if destination.is_dir():
                        shutil.rmtree(destination)
                    else:
                        destination.unlink()
                
                # Hedef klasör yoksa oluştur
                destination.parent.mkdir(parents=True, exist_ok=True)
                
                shutil.move(str(item), str(destination))

print()
print("Tüm markdownlar toplandı.")
print("OCR klasörleri arşivlendi.")
print("Input dosyaları arşivlendi.")
print("İşlem tamamlandı.")