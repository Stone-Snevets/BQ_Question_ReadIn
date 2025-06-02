# Version 1.4
### New features:
* Added 'true / happened' to `add_concordance.py` as a search parameter
* 'A conc' now accounts for "one-word" and "1-word" variations of #-word questions
* Questions that end in "named" but aren't Chapter Analysis are now classified as 'mentioned' questions
### Fixed Bugs:
* 'true / happened' was overwriting 'conc fv'
* 'words of' was overwriting 'A conc'
* Occasional whitespace before the actual question was being included in the question