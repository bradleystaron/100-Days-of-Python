#include <stdio.h>
#include <string.h> // Required for strlen()

int main() {
    
    // Creates an array to store a String of the User
    char inputString[100];
    
    // Prompts the user to enter their name
    printf("What is your name? ");

    // Read the user input using fgets
    // fgets(buffer, size, stream)
    // buffer: The character array to store the input
    // size: The maximum number of characters to read (including the null terminator)
    // stream: The input stream, stdin for standard input (keyboard)
    fgets(inputString, sizeof(inputString), stdin);

    size_t length;
    // Calculate the length of the string
    length = strlen(inputString);

    // Print the length + 1 because it includes the null terminator at the end of the string
    printf("The length of the string is: %zu\n", length);

    return 0;
}