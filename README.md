# SPDX Checker Test Repository

This is a test repository for testing the [github-actions-spdx-checker](https://github.com/zccrs/github-actions-spdx-checker) action.

## Purpose

This repository demonstrates the SPDX header checker GitHub Action functionality by:
- Including a GitHub Actions workflow that validates SPDX headers on pull requests
- Providing example source files with proper SPDX headers
- Testing the action's capability to detect missing or incorrect SPDX headers

## Files

- `hello.py` - Python example with SPDX header
- `greet.js` - JavaScript example with SPDX header
- `main.cpp` - C++ example with SPDX header

## SPDX Header Format

All source files in this repository include SPDX headers in the format:

```
# SPDX-FileCopyrightText: 2026 Test Project
# SPDX-License-Identifier: GPL-3.0-or-later
```

or for C-style comments:

```
// SPDX-FileCopyrightText: 2026 Test Project
// SPDX-License-Identifier: GPL-3.0-or-later
```

## GitHub Action

The SPDX checker runs automatically on pull requests to ensure all new and modified files have correct SPDX headers.
