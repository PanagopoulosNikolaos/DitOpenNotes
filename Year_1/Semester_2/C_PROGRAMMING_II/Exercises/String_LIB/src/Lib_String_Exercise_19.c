// String Expression Evaluator

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

double evaluate(const char *expression);
double parseTerm(const char **expr);
double parseFactor(const char **expr);

int main() {
    char expression[100];
    
    printf("Enter a mathematical expression: ");
    fgets(expression, sizeof(expression), stdin);
    expression[strcspn(expression, "\n")] = '\0';  // Remove trailing newline
    
    printf("Result: %.2f\n", evaluate(expression));
    
    return 0;
}

double evaluate(const char *expression) {
    return parseTerm(&expression);
}

double parseTerm(const char **expr) {
    double left = parseFactor(expr);
    
    while(**expr == '+' || **expr == '-') {
        char op = **expr;
        (*expr)++;
        double right = parseFactor(expr);
        
        if(op == '+')
            left += right;
        else
            left -= right;
    }
    
    return left;
}

double parseFactor(const char **expr) {
    double left = 0;
    
    // Skip whitespace
    while(isspace(**expr))
        (*expr)++;
    
    if(**expr == '(') {
        (*expr)++;
        left = parseTerm(expr);
        if(**expr == ')')
            (*expr)++;
    } else if(isdigit(**expr) || **expr == '.') {
        left = strtod(*expr, (char**)expr);
    } else if(**expr == '-') {
        (*expr)++;
        left = -parseFactor(expr);
    }
    
    // Skip whitespace
    while(isspace(**expr))
        (*expr)++;
    
    // Handle exponents
    if(**expr == '^') {
        (*expr)++;
        double exponent = parseFactor(expr);
        left = pow(left, exponent);
    }
    
    // Handle multiplication and division
    while(**expr == '*' || **expr == '/') {
        char op = **expr;
        (*expr)++;
        double right = parseFactor(expr);
        
        if(op == '*')
            left *= right;
        else
            left /= right;
    }
    
    return left;
}
