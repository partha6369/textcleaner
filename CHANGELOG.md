# Changelog


## [v0.1.6] - 2025-07-11

### Changed Parameter Names
- Replaced **correct_spellings** with **correct_spelling**.

---

## [v0.1.5] - 2025-07-11

### Changed Parameter Names
- Replaced **expand** with **expand_contraction**.
- Replaced **correct** with **correct_spellings**.
- Replaced **lemmatize** with **lemmatise**.

## [v0.1.4] - 2025-07-11
### Fixed
- Replaced deprecated `Speller().correction()` call with function-style usage `Speller(word)` for full compatibility with `autocorrect>=0.4.4`.
- Eliminated runtime errors caused by incorrect version locking in previous releases.

### Added
- `verbose` parameter in `preprocess()` to optionally log warning messages during fallback or skipped preprocessing stages.

### Improved
- More robust error handling in `correct_spelling()` to gracefully bypass issues without silent failure.
- Lazy loading retained for both `spaCy` and `autocorrect` components to improve performance.

### Verified
- Full test pass with clean environment.
- Uploaded and installed from PyPI as working version `textcleaner-partha==0.1.4`.

## [v0.1.3] - 2025-07-11
- Locked `autocorrect==0.4.4` to prevent incompatibility with `.correction()` method.
- Added clear spaCy model error message and instructions.
- Improved test coverage.

## [v0.1.2] - (Unreleased)
- Initial public release. Known issue: `Speller().correction()` fails with newer `autocorrect`.