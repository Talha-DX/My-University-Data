#include<iostream>
using namespace std;

int main(){
    int stock[10] = {5, 15, 22, 35, 40, 55, 65, 70, 85, 95};
    int n = 10;
    // ----------------------------------
    int s;
    cout << "Enter Number to Search: " << endl;
    cin >> s;
    for (int i = 0; i < 10; i++)
    {
        if (s == stock[i])
        {
            cout << "NuMber is founded." << endl;
            break;
        }
    }
    //--------------------------------------
    int p1;
    cout << "Enter Position: " << endl;
    cin >> p1;
    for (int i = n; i > p1; i--)
    {
        stock[i] = stock[i - 1];
    }
    stock[p1] = 66;
    n++;
    for (int i = 0; i < n; i++)
    {
        cout << stock[i] << " ";
    }
    // ----------------------------------------
    int p1;
    cout << "Enter Position: " << endl;
    cin >> p1;
    for (int i = 0; i < p1; i++)
    {
        stock[i] = stock[i + 1];
    }
    n--;
    for (int i = 0; i < n; i++)
    {
        cout << stock[i] << " ";
    }
    // // -------------------------------------------
    // sizeof operator
    int t = sizeof(stock);
    cout << "Total size of operator is: " << t << endl;
    // -------------------------------------------
    int max = stock[0], min = stock[0];
    for (int i = 0; i < n; i++)
    {
        if (max < stock[i])
        {
            max = stock[i];
        }
        if (min > stock[i])
        {
            min = stock[i];
        }
    }
    cout << "Max: " << max << endl;
    cout << "Min: " << min << endl;
    // ----------------------------------------------
}