#include <iostream>
using namespace std;

struct student
{
    string name;
    int roll;
    int marks;
};

int main()
{
    // ----------------------------------Task # 03-----------------------------
    int  students[3][3] = {
            {80, 85, 78},
            {88, 82, 90},
            {75, 89, 84}
        };
        // ------------------------------------------------
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                cout<<students[i][j]<<" ";
            }
            cout<<endl;
        }
        // ---------------------------------------------
        int * ptr ;
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                ptr = &students[i][j];
                cout<<"Address is: "<<ptr<<endl;
            }
            cout<<endl;
        }

    // b)

    student s1,s2,s3;
    // -------------------
    s1.name = "Talha";
    s1.marks = 100;
    s1.roll = 900;
    // ------------------
    s2.name = "Hamza";
    s2.marks = 400;
    s2.roll = 8880;
    // ---------------------
    s3.name = "Ali";
    s3.marks = 7600;
    s3.roll = 120;
    cout<<"-------------------------"<<endl;
    cout<<"Student 1 Name: "<<s1.name<<endl;
    cout<<"Student 1 Marks: "<<s1.marks<<endl;
    cout<<"Student 1 Roll:  "<<s1.roll<<endl;
    cout<<"-------------------------"<<endl;
    cout<<"-------------------------"<<endl;
    cout<<"Student 2 Name: "<<s2.name<<endl;
    cout<<"Student 2 Marks: "<<s2.marks<<endl;
    cout<<"Student 2 Roll:  "<<s2.roll<<endl;
    cout<<"-------------------------"<<endl;
    cout<<"-------------------------"<<endl;
    cout<<"Student 3 Name: "<<s3.name<<endl;
    cout<<"Student 3 Marks: "<<s3.marks<<endl;
    cout<<"Student 3 Roll:  "<<s3.roll<<endl;
    cout<<"-------------------------"<<endl;

    int students[3][3] = {
        {80, 85, 78},
        {88, 82, 90},
        {75, 89, 84}};
    int n = 3;
    for (int u = 0; u < 3; u++)
    {
        for (int j = 0; j < n - u - 1; j++)
        {
            if (students[u][j] > students[u][j + 1])
            {
                swap(students[u][j], students[u][j + 1]);
            }
        }
    }
    for (int u = 0; u < 3; u++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << students[u][j] << " ";
        }
        cout << endl;
    }
}
