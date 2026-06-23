First of all, this project is not a fully automated system. You should be familiar with the information provided here and use the project by following the user guide.

The system is designed to work while being located in a folder on the desktop. If you move it to a different location, it may stop working.

PIPS: If you run the `pip install.bat` file, all required pip packages for using the project will be installed. This process may take some time. Since this is my first project, I went through a lot of trial and error and reset the pip environment several times, so some unnecessary packages may have ended up included. If you know what you're doing, you can remove unnecessary packages from `requirements_full.txt`.

OCR STAGE - FIRST STEP: Before starting, test the system using 5-page PDFs. Here we are testing your system and determining how large the PDFs you process should be based on the processing time of a 5-page PDF. (If your system is too weak to process even a 5-page PDF, that's okay, keep reading.)

WARNING: If the system cannot finish processing a PDF within 30–45 minutes, it will time out.

SO WHAT SHOULD I DO?: For example, if the system processes a 5-page PDF in 10 minutes, then work with PDFs of at most 15 pages. Otherwise, the system may time out. If you need to split large PDFs, read the next section.

PDF SPLITTING 1: Enter the `split` folder, place the PDFs you want to split into the `split_input` folder, and run the `split.bat` file. By default, this process will split PDFs into groups of 5 pages and place them into the `split_output` folder. Take them from there and place them into the `input_math` or `input_text` folders as described in the user guide, then follow the guide instructions. The reason for this manual transfer is that the system does not yet know the content type of the files.

PDF SPLITTING 2: Depending on your hardware, you can change the number of pages per split by following the instructions on lines 15 and 16 inside the `split_pdf.py` file. For a low-end computer, this can be reduced to 1 page. For a high-end computer, values such as 15–20 or even larger may be used.

CPU USAGE 100%!!!: If your CPU usage reaches 100%, you can follow the instructions inside the `ocr math.bat` file and apply a CPU usage limitation.

IMPORTANT: PDFs that are added before OCR scanning begins, PDFs added during splitting, unexpected crashes, closing the command window before the process is completed, and similar situations may prevent output generation. For this reason, PDFs inside the `input_math`, `input_text`, and `split_input` folders are never deleted. The user may, and should, delete them after confirming that the outputs are correct.

Because if the PDFs inside these folders are not removed, adding new files and running the system again will cause the old PDFs to be OCR processed AGAIN. In order to prevent users from losing important files, all cleanup and deletion operations are left entirely to the user. The system will never delete your files under any circumstances.

---------------------------------------------- USER GUIDE ----------------------------------------------

If the PDF you want to scan contains mathematical expressions, place it inside the `input_math` folder.

If the PDF you want to scan does not contain mathematical expressions, place it inside the `input_text` folder.

Depending on the type of file you uploaded, run either `ocr math.bat` or `ocr text.bat`.

The OCR processed files will appear in the `output_all` folder.

The important file for us is the Markdown file with the `.md` extension located inside:

`output_all\%OCR Processed File%\hybrid_auto`

If you performed PDF splitting, simply go to the `merge` folder and run `merge_markdowns.bat`. The system will automatically detect folders with the same name and merge them back together according to page order. Files used during the merge process will be moved into the `Processed OCR Folders` folder. Since this process is not extremely strict, files may be deleted after user verification.

When you complete the merge stage, the `output_all` folder will still contain outputs from non-split PDFs and text-based OCR outputs. To gather all Markdown files, OCR output folders, and old input folders into a single location, run `collect.bat` as the final step.

If you performed all steps correctly...

All Markdown files will be collected into the `All Markdowns` folder.
(output_all root .md files ----- output_all***** contained .md files ----- merge\Merged Markdowns .md files)

All input PDFs will be collected into the `Processed Inputs` folder.
(input_math - input_text - split_input)

All processed outputs will be collected into the `Processed OCR Folders` folder.
(folders remaining inside output_all)

After completing the OCR process, you can continue with chunking, embedding, and related operations using the other project called `rag_sistemi`. `Still in development`

Please read the `README.md` file belonging to that project as well.
