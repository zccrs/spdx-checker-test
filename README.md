# SPDX Checker Test Repository

This is a test repository for validating the functionality of the [@zccrs/github-actions-spdx-checker](https://github.com/zccrs/github-actions-spdx-checker) GitHub Action.

## Purpose

This repository contains various source files with SPDX license headers to test different scenarios and validate that the SPDX checker action correctly identifies and validates license headers across multiple file types and formats.

## Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── spdx-check.yml          # GitHub Actions workflow for SPDX checking
├── src/
│   ├── example.py                  # Python file with correct SPDX header (2026)
│   ├── example.cpp                 # C++ file with correct SPDX header (2026)
│   ├── example.h                   # C header file with correct SPDX header (2026)
│   ├── example.js                  # JavaScript file with correct SPDX header (2026)
│   └── legacy.py                   # Python file with year range (2023-2026)
├── tests/
│   └── test_example.py             # Test file with correct SPDX header (2026)
├── .editorconfig                   # Code style configuration
└── README.md                       # This file
```

## SPDX Header Format

All source files in this repository follow the REUSE specification for SPDX headers.

### For Python files (# comment style):
```python
# SPDX-FileCopyrightText: 2026 zccrs
# SPDX-License-Identifier: GPL-3.0-or-later
```

### For C/C++ files (// comment style):
```cpp
// SPDX-FileCopyrightText: 2026 zccrs
// SPDX-License-Identifier: GPL-3.0-or-later
```

### For legacy files with year ranges:
```python
# SPDX-FileCopyrightText: 2023-2026 zccrs
# SPDX-License-Identifier: GPL-3.0-or-later
```

## Testing the SPDX Checker

### Automated Testing via GitHub Actions

The SPDX checker runs automatically on:
- Pull requests to `main` or `master` branches
- Pushes to `main` or `master` branches

The workflow checks all source files in `src/` and `tests/` directories for proper SPDX headers.

### Manual Testing

You can also test the SPDX checker locally or in your own fork:

1. Fork this repository
2. Create a new branch
3. Make changes to test files (e.g., add files without SPDX headers, modify existing headers)
4. Create a pull request
5. Observe the SPDX checker action results

## Test Scenarios Covered

This repository tests the following scenarios:

1. **Python files** - Tests SPDX headers in `.py` files with `#` comment style
2. **C++ files** - Tests SPDX headers in `.cpp` files with `//` comment style
3. **C header files** - Tests SPDX headers in `.h` files with `//` comment style
4. **JavaScript files** - Tests SPDX headers in `.js` files with `//` comment style
5. **Year ranges** - Tests SPDX headers with copyright year ranges (2023-2026)
6. **Test files** - Ensures test files also maintain proper SPDX headers

## Expected Results

When the SPDX checker runs successfully, all files should:
- ✅ Contain valid SPDX-FileCopyrightText headers
- ✅ Contain valid SPDX-License-Identifier headers
- ✅ Use the correct comment style for their file type
- ✅ Follow the GPL-3.0-or-later license as specified

## Running the Example Code

### Python Examples
```bash
# Run the example module
python src/example.py

# Run the legacy module
python src/legacy.py

# Run tests
python tests/test_example.py
```

### C++ Example
```bash
# Compile and run the C++ example
g++ -o example src/example.cpp
./example
```

### JavaScript Example
```bash
# Run the JavaScript example
node src/example.js
```

## License

All code in this repository is licensed under GPL-3.0-or-later as indicated in the SPDX headers.

## Contributing

This is a test repository. If you'd like to contribute test cases or improve the examples:

1. Ensure all new files include proper SPDX headers
2. Follow the existing code style (see `.editorconfig`)
3. Test that the SPDX checker passes on your changes
4. Submit a pull request

## More Information

- [SPDX Specification](https://spdx.org/)
- [REUSE Software](https://reuse.software/)
- [@zccrs/github-actions-spdx-checker](https://github.com/zccrs/github-actions-spdx-checker)
