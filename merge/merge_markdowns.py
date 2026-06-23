import re
import shutil
from pathlib import Path
from collections import defaultdict

# ====================== AYARLAR ======================
INPUT_DIR = Path.home() / "Desktop" / "pdf_ocr_projesi" / "output_all"
OUTPUT_DIR = Path.home() / "Desktop" / "pdf_ocr_projesi" / "merge" / "Merged Markdowns"
PROCESSED_DIR = Path.home() / "Desktop" / "pdf_ocr_projesi" / "Processed OCR Folders"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

groups = defaultdict(list)
processed_folders = set()   # ← YENİ: İşlenen klasörleri takip edeceğiz

print("🔍 Markdown dosyaları gruplanıyor...\n")

# ====================== KLASÖRLERİ GRUPLAMA ======================
for folder in INPUT_DIR.iterdir():
    if not folder.is_dir():
        continue

    match = re.match(r"(.+?)_(\d+)_(\d+)$", folder.name)
    if not match:
        print(f"Atlandı: {folder.name}")
        continue

    group_name = match.group(1)
    start_page = int(match.group(2))

    md_files = list(folder.rglob("*.md"))
    if not md_files:
        print(f"MD bulunamadı: {folder.name}")
        continue

    groups[group_name].append((start_page, md_files[0]))
    processed_folders.add(folder)   # ← İşlenen klasörü kaydediyoruz

# ====================== MARKDOWN BİRLEŞTİRME ======================
for group_name, files in groups.items():
    files.sort(key=lambda x: x[0])

    output_file = OUTPUT_DIR / f"{group_name}.md"

    try:
        with open(output_file, "w", encoding="utf-8") as outfile:
            print(f"\n📄 Birleştiriliyor: {group_name} ({len(files)} parça)")

            for _, md_file in files:
                print(f"   ➕ Ekleniyor → {md_file.name}")
                with open(md_file, "r", encoding="utf-8") as infile:
                    content = infile.read().rstrip()
                    outfile.write(content)
                    outfile.write("\n\n")

        print(f"✅ Oluşturuldu: {output_file.name}")

    except Exception as e:
        print(f"❌ Hata oluştu ({group_name}): {e}")

print(f"\n🎉 Tüm markdown'lar birleştirildi! → {OUTPUT_DIR}")

# ====================== SADECE İŞLENEN KLASÖRLERİ TAŞIMA ======================
print("\n📦 İşlenen OCR klasörleri taşınıyor...")

moved_count = 0
for folder in processed_folders:
    try:
        destination = PROCESSED_DIR / folder.name

        if destination.exists():
            shutil.rmtree(destination)

        shutil.move(str(folder), str(destination))
        print(f"   Taşındı → {folder.name}")
        moved_count += 1

    except Exception as e:
        print(f"   ❌ Taşıma hatası ({folder.name}): {e}")

print(f"\n✅ {moved_count} klasör taşındı → {PROCESSED_DIR}")
print("\nİşlem tamamlandı! 🎯")