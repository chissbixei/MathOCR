@echo off

:: ================== CPU SINIRLAMALARI ==================
set MINERU_INTRA_OP_NUM_THREADS=6
set MINERU_INTER_OP_NUM_THREADS=6
set MINERU_PDF_RENDER_THREADS=6

:: İstersen daha da azaltabilirsin (örnek: 2)
:: set MINERU_INTRA_OP_NUM_THREADS=2
:: set MINERU_INTER_OP_NUM_THREADS=2
:: set MINERU_PDF_RENDER_THREADS=2

set MINERU_HYBRID_BATCH_RATIO=6

echo CPU kullanimi sinirlandi: %MINERU_INTRA_OP_NUM_THREADS% thread

for %%f in ("%USERPROFILE%\Desktop\pdf_ocr_projesi\input_math\*.pdf") do (
    echo.
    echo ========================================
    echo Isleniyor: %%~nxf
    echo ========================================
    
    mineru -p "%%f" -o "%USERPROFILE%\Desktop\pdf_ocr_projesi\output_all" -b hybrid-engine --formula true
)

echo.
echo Tum islemler tamamlandi.
pause