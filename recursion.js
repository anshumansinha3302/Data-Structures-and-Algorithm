// Function to calculate factorial using recursion
function factorial(n) {
    if (n === 0 || n === 1) {
        return 1; // Base case
    }
    return n * factorial(n - 1); // Recursive case
}

// Test the factorial function
const num = 5;
console.log(`Factorial of ${num} is ${factorial(num)}`);
