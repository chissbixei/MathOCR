# MathScan-OCR

## Important Notes

First of all, this project is **not a fully automated system**. You should understand the workflow and follow the instructions in this guide carefully.

The system is designed to run from a specific folder structure located on the desktop. Moving the project to a different location may cause it to stop working correctly.

## Dependencies

Run `pip install.bat` to install all required Python packages.

This process may take some time. Since this was my first major project, there was a lot of experimentation and trial-and-error during development. Some unnecessary packages may have ended up in `requirements_full.txt`.

If you are familiar with Python environments, you may remove any packages you believe are unnecessary.

---

# OCR Processing

## Step 1: Performance Testing

Before processing large PDFs, test the system with a 5-page PDF first.

This allows you to estimate your system's processing speed and determine a safe PDF size for OCR.

If your computer struggles to process a 5-page PDF, that's fine—continue reading.

### Warning

If the system cannot finish processing a PDF within approximately **30–45 minutes**, the process may time out.

### What Should I Do?

For example:

* If a 5-page PDF takes 10 minutes to process, use PDFs of around 15 pages or less.
* Processing significantly larger PDFs may result in timeouts.

If you need to handle larger PDFs, use the PDF splitting feature described below.

---

# PDF Splitting

## Method 1

1. Open the `split` folder.
2. Place the PDFs you want to split into the `split_input` folder.
3. Run `split.bat`.

By default, the system splits PDFs into 5-page chunks and saves them into the `split_output` folder.

Move the generated files into either `input_math` or `input_text` as described in the usage guide.

Manual file placement is currently required because the system cannot automatically determine the PDF content type.

## Method 2

You can change the number of pages per split by editing the instructions on lines 15 and 16 of `split_pdf.py`.

Suggested values:

* Low-end hardware: 1 page per file
* Mid-range hardware: 5–10 pages per file
* High-end hardware: 15–20 pages or more

---

# CPU Usage Reaches 100%

If your CPU usage reaches 100%, follow the instructions inside `ocr math.bat` to apply CPU usage limitations.

---

# Important

To prevent accidental data loss, the system **never deletes PDFs automatically**.

The following folders are not cleaned automatically:

* `input_math`
* `input_text`
* `split_input`

This behavior protects users from losing important files due to:

* Unexpected crashes
* Interrupted OCR jobs
* Closing the command window during processing
* Other unforeseen issues

After verifying that the OCR output is correct, you should manually remove processed PDFs.

If old PDFs remain in these folders, they may be processed again the next time the OCR system is executed.

The responsibility for cleaning up processed files belongs entirely to the user.

---

# Usage Guide

## Mathematical PDFs

If your PDF contains mathematical expressions, place it inside:

`input_math`

## Text-Only PDFs

If your PDF does not contain mathematical expressions, place it inside:

`input_text`

## Start OCR

Run one of the following files depending on the PDF type:

* `ocr math.bat`
* `ocr text.bat`

## OCR Output

Processed files will appear inside:

`output_all`

The most important output file is:

`output_all/<OCR_FOLDER>/hybrid_auto/*.md`

The generated Markdown file contains the final OCR result.

---

# Merging Split PDFs

If you used the PDF splitting feature:

1. Open the `merge` folder.
2. Run `merge_markdowns.bat`.

The system automatically:

* Detects folders with matching names
* Reassembles pages in the correct order
* Merges Markdown outputs

Folders used during the merge process are moved to:

`Processed OCR Folders`

Since the merge process is not perfect, review the output before deleting any files.

---

# Final Collection Step

After merging, run:

`collect.bat`

This gathers all generated files into centralized folders.

If everything was completed successfully:

### All Markdown Files

Stored in:

`All Markdowns`

Including:

* Markdown files directly inside `output_all`
* Markdown files inside OCR output folders
* Markdown files from `merge/Merged Markdowns`

### All Input PDFs

Stored in:

`Processed Inputs`

Including files from:

* `input_math`
* `input_text`
* `split_input`

### All Processed OCR Outputs

Stored in:

`Processed OCR Folders`

---

# Next Step: RAG Pipeline

After OCR processing is complete, you can continue with the `rag_sistemi` project for:

* Chunking
* Embedding generation
* Retrieval
* RAG workflows

Please read the README file included in that project as well.
