/*
 * Create the function factorial here
 */
function factorial(n){
    if (n < 0)
    return -1;
    
    // If the number is 0, its factorial is 1.
    else if (n == 0) 
    return 1;
    
    // Otherwise, call the recursive procedure again
    else {
    return (n * factorial(n - 1));
    }
}
    
