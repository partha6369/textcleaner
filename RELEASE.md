# Release Notes for textcleaner-partha v0.1.4

**Release Date:** 11 July 2025  
**Version:** `0.1.4`  
**Author:** Dr. Partha Majumdar  
**PyPI:** [textcleaner-partha](https://pypi.org/project/textcleaner-partha/0.1.4/)

---

## 🎯 Highlights

This release delivers a fully stable and production-ready version of `textcleaner-partha`, resolving the last known issue related to the `autocorrect` package. The library now works reliably in clean environments, and is installable directly from PyPI.

---

## ✅ What’s Fixed

- **Spelling correction compatibility:**  
  Replaced `Speller().correction()` with `Speller(word)`, ensuring full compatibility with modern `autocorrect` versions (>= 0.4.4).
  
- **Autocorrect integration:**  
  Locked dependency to `autocorrect==0.4.4` for consistent results and clean installability.

---

## 🆕 What’s New

- **`verbose=True` flag** in `preprocess()` for optional warning messages during fallback cases (e.g., if autocorrect fails).

- **Clear runtime instructions** if `spaCy` model is missing, with helpful guidance (`python -m spacy download en_core_web_sm`).

---

## 🚀 Improvements

- **Robust error handling:**  
  Ensures graceful fallback without silent failures, while optionally logging helpful debug output.

- **Retained lazy loading:**  
  Efficient memory and performance management with deferred model and tool loading (both `spaCy` and `autocorrect`).

---

## ✅ Installation

```bash
pip install textcleaner-partha