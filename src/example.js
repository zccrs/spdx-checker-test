// SPDX-FileCopyrightText: 2026 zccrs
// SPDX-License-Identifier: GPL-3.0-or-later

/**
 * Example JavaScript module for testing SPDX checker.
 * 
 * This file demonstrates proper SPDX header formatting for JavaScript files.
 */

/**
 * Print a greeting message to console
 */
function greet() {
    console.log("Hello from JavaScript SPDX checker test!");
}

/**
 * Subtract two numbers
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} Difference of a and b
 */
function subtract(a, b) {
    return a - b;
}

/**
 * Main entry point
 */
function main() {
    greet();
    const result = subtract(10, 4);
    console.log(`10 - 4 = ${result}`);
}

// Run if executed directly
if (require.main === module) {
    main();
}

module.exports = { greet, subtract };
