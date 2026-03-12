#include <iostream>
using namespace std;

int main()
{
    // ------------------------ Task 1 --------------------
    // 1)
    int quantity;
    float price;
    float totalBill;

    cout << "Enter Quantity: ";
    cin >> quantity;
    cout << "\nEnter Price: ";
    cin >> price;
    totalBill = quantity * price;
    cout << "Total : " << totalBill << endl;
    // 2)
    int a, b;
    cout << "Sum: " << a + b << endl;
    cout << "Sub: " << a - b << endl;
    cout << "Multiply: " << a * b << endl;
    cout << "Division: " << a / b << endl;
    cout << "Modulo: " << a % b << endl;
    // 3)
    int marks;
    cout << "Enter marks: ";
    cin >> marks;
    char grade;
    if (marks > 90)
    {
        grade = 'A';
    }
    else if ((marks > 80) && (marks <= 90))
    {
        grade = 'B';
    }
    else if ((marks > 70) && (marks <= 80))
    {
        grade = 'C';
    }
    else
    {
        grade = 'F';
    }
    cout << "Your grade is: " << grade << endl;
    // 4)
    for (int i = 1; i <= 10; i++)
    {
        cout << "Number: " << i << endl;
    }
    // // 5)
    int n, sum = 0;
    cout << "Enter Number: ";
    cin >> n;
    int i = 1;
    while (i <= n)
    {
        sum = sum + i;
        i = i + 1;
    }
    cout << "Sum is: " << sum << endl;
    // // 6)
    int n, sum = 0;
    cout << "Enter Number: ";
    cin >> n;
    int i = 1;
    do
    {
        cout << n << " * " << i << " = " << i * n << endl;
        i++;
    } while (i <= 10);

    return 0;
}