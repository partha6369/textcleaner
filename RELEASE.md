# Release Notes for **textcleaner-partha v1.0.0**

**Release Date:** 29 July 2025  
**Version:** `1.1.2`  
**Author:** Dr. Partha Majumdar  
**PyPI:** [textcleaner-partha](https://pypi.org/project/textcleaner-partha/1.0.0/)

---

## 🎯 Highlights

This is the **first stable and production-ready release** of `textcleaner-partha`.  
The library now includes **file-based preprocessing (`preprocess_file`)** and **token extraction from files (`get_tokens_from_file`)**, making it easy to process text from TXT, DOCX, and PDF documents seamlessly.

---

## ✅ What’s Added

- **`preprocess_file()`** – Preprocess entire TXT, DOCX, or PDF files.
- **`get_tokens_from_file()`** – Extract tokens from documents, with optional PDF page-wise processing.

---

## ✅ What’s Enhanced

- Expanded **domain-specific abbreviation mappings**:
  - `medical.json`
  - `legal.json`
  - `telecom.json`
- Expanded **`common.json`** and **`slang.json`** abbreviation files with more entries.

---

## ✅ Installation

```bash
pip install textcleaner-partha
```