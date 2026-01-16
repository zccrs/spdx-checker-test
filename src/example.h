// SPDX-FileCopyrightText: 2026 zccrs
// SPDX-License-Identifier: GPL-3.0-or-later

#ifndef EXAMPLE_H
#define EXAMPLE_H

/**
 * Example C/C++ header file for testing SPDX checker.
 * 
 * This file demonstrates proper SPDX header formatting for header files.
 */

#ifdef __cplusplus
extern "C" {
#endif

/**
 * Print a message to stdout.
 */
void printMessage();

/**
 * Multiply two integers.
 * 
 * @param a First integer
 * @param b Second integer
 * @return Product of a and b
 */
int multiply(int a, int b);

#ifdef __cplusplus
}
#endif

#endif // EXAMPLE_H
