// SPDX-FileCopyrightText: 2026 zccrs
// SPDX-License-Identifier: GPL-3.0-or-later

#include <iostream>
#include "example.h"

/**
 * Example C++ implementation for testing SPDX checker.
 * 
 * This file demonstrates proper SPDX header formatting for C++ files.
 */

void printMessage() {
    std::cout << "Hello from C++ SPDX checker test!" << std::endl;
}

int multiply(int a, int b) {
    return a * b;
}

int main() {
    printMessage();
    int result = multiply(6, 7);
    std::cout << "6 * 7 = " << result << std::endl;
    return 0;
}
