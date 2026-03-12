#include <iostream>
#include <ctime>
using namespace std;

int main(){
    
    srand(time(0));
    int arr[100], s, k=0;

    for (int i = 0; i < 100; i++)
    {
        arr[i] = rand() % 100;
        cout<<"array["<<i<<"] = "<<arr[i]<<endl;
    }

    cout<<"Enter the Value to search in array: ";
    cin>>s;

    for (int i = 0; i < 100; i++)
    {
        if (s == arr[i]){
            cout<<"Number Founded: "<<arr[i]<<" at: "<<i<<endl;
            k = 1;
        }
    }
    
    if ( k == 0 ){
        cout<<"Number don't found."<<endl;
    }

// -------------------------------------------------------

    srand(time(0));
    int arr[20];
    int max , min;
    for (int i = 0; i < 20; i++)
    {
        arr[i] = rand()%100;
        cout<<"Arr["<<i<<"] = "<<arr[i]<<endl;
    }
     max = arr[0];
     min = arr[0];
    for (int i = 0; i < 20; i++)
    {
        if (max < arr[i]){
            max = arr[i];
        }
        if (min > arr[i]){
            min = arr[i];
        }
    }
    cout<<"Max is: "<<max<<endl;
    cout<<"Min is: "<<min<<endl;

// ------------------------------------------------------------------

    int arr[10], size, pos;
    cout<<"Enter Size: ";
    cin>>size;
    for(int i = 0; i < size; i++)
    {
       cin>>arr[i];
    }
    cout<<"Enter Position where you want to Delete: ";
    cin>>pos;
    for (int i = pos; i < size; i++)
    {
        arr[i] = arr[i+1];
    }
    size--;
    for (int i = 0; i < size; i++)
    {
        cout<<arr[i]<<" ";
    }

    

// -------------------------------------------------------
// Task 1
    int n; 
    cout << "Enter number of students: ";
    cin >> n;
    int marks[100]; 
    cout << "\nEnter marks of " << n << " students:\n";
    for (int i = 0; i < n; i++) {
        cout << "Mark " << i + 1 << ": ";
        cin >> marks[i];
    }
    int searchMark;
    cout << "\nEnter mark to search: ";
    cin >> searchMark;

    bool found = false;
    for (int i = 0; i < n; i++) {
        if (marks[i] == searchMark) {
            cout << "Mark " << searchMark << " found at position " << i + 1 << ".\n";
            found = true;
            break;
        }
    }
    if (!found)
        cout << "Mark " << searchMark << " not found.\n";

    int delMark;
    cout << "\nEnter mark to delete: ";
    cin >> delMark;

    found = false;
    for (int i = 0; i < n; i++) {
        if (marks[i] == delMark) {
            found = true;
            
            for (int j = i; j < n - 1; j++) {
                marks[j] = marks[j + 1];
            }
            n--; 
            cout << "Mark " << delMark << " deleted successfully.\n";
            break;
        }
    }
    if (!found)
        cout << "Mark " << delMark << " not found. Cannot delete.\n";

    cout << "\n--- Array Information ---"<<endl;
    cout << "Total memory used by array: " << sizeof(marks) << " bytes\n";
    cout << "Number of elements currently stored: " << n << "\n";

    cout << "\nFinal list of marks: " <<endl;
    for (int i = 0; i < n; i++) {
        cout << marks[i] << " ";
    }
    cout << endl;
 
// -----------------------------------------------------------------
// TAsk 2

    int n;
    cout << "Enter the number of products in inventory: ";
    cin >> n;
    int quantities[100]; 
    cout << "\nEnter product quantities:\n";
    for (int i = 0; i < n; i++) {
        cout << "Quantity of product " << i + 1 << ": ";
        cin >> quantities[i];
    }
    int searchQty;
    cout << "\nEnter product quantity to search for: ";
    cin >> searchQty;

    bool found = false;
    for (int i = 0; i < n; i++) {
        if (quantities[i] == searchQty) {
            cout << "Quantity " << searchQty << " found at position " << i + 1 << ".\n";
            found = true;
            break;
        }
    }
    if (!found)
        cout << "Quantity " << searchQty << " not found in inventory.\n";

    for (int i = 0; i < n; i++) {
        if (quantities[i] <= 0) {
            cout << "\nProduct with quantity " << quantities[i] << " (out of stock) deleted.\n";
            for (int j = i; j < n - 1; j++) {
                quantities[j] = quantities[j + 1];
            }
            n--;  
            i--;  
        }
    }

    cout << "\n--- Inventory Information ---\n";
    cout << "Total memory allocated for array: " << sizeof(quantities) << " bytes\n";
    cout << "Number of products currently stored: " << n << "\n";

    cout << "\nUpdated inventory quantities:\n";
    for (int i = 0; i < n; i++) {
        cout << quantities[i] << " ";
    }
    cout << endl;

    return 0;
}
