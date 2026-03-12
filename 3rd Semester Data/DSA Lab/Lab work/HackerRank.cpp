// #include <iostream>
// #include <string>
// using namespace std;

// struct employee
// {
//     char name[20];
//     float salary;
// };

// int main()
// {
    // employee emp[3] = {{"Ali",2000},{"Ayesha",9000},{"Wasay",3000}};

    // // Linear Search
    // for (int i = 0; i < 3; i++)
    // {
    //     if(strcmp(emp[i].name,"Ali") == 0){
    //         cout<<"Found: "<<emp[i].name<<" with Salary "<<emp[i].salary<<endl;
    //     }
    // }

    //Bubble Sort 
    
    // for (int i = 0; i < 3; i++)
    // {
    //     for (int j = 0; j < 2; j++)
    //     {
          
    //     }
    // }
    

    // ------------------------ 1 -------------------------
    // int arr[] = {2,4,6,8,1,9,14};
    // int n = 7;
    // int key, low = 0, high = n-1, mid;
    // cout<<"Enter Number to Search: ";
    // cin>>key;
    // while (low <= high)
    // {
    //     mid = (low + high)/2;
    //     if (arr[mid] == key)
    //     {
    //         cout<<"\nFound at index "<<mid<<endl;
    //         return 0;
    //     }
    //     else if (key < arr[mid])
    //     {
    //         high = mid - 1;
    //     }
    //     else{
    //         low = mid + 1;
    //     }
    // }
    // cout<<"Number not found."<<endl;

    // ------------------------ 2 -------------------------
    // int arr[5] = {3, 1, 5, 2, 4};
    // int n = 5;
    // for (int i = 0; i < n - 1; i++)
    // {
    //     for (int j = 0; j < n - i - 1; j++)
    //     {
    //         if (arr[j] > arr[j + 1])
    //         {
    //             swap(arr[j],arr[j+1]);
    //         }
    //     }
    // }
    // for (int i = 0; i < n; i++)
    // {
    //     cout << arr[i] << " ";
    // }

    // ------------------------ 3 -------------------------

    // int a = 10;
    // int b = 8;
    // cout << "===Simple Value===" << endl;
    // cout << "a = " << a << endl;
    // cout << "b = " << b << endl;
    // int *ptr1 = &a;
    // int *ptr2 = &b;
    // int temp = *ptr1;
    // *ptr1 = *ptr2;
    // *ptr2 = temp;
    // cout << "===After Swap===" << endl;
    // cout << "a = " << a << endl;
    // cout << "b = " << b << endl;
    
    // ------------------------ 4 -------------------------

    // 1st row == 2nd colu

    // int r1 , c1, r2 , c2;
    // bool multi = false;

    // cout<<" ------------------------------------------- "<<endl;
    // cout<<" Check if Multiplication is possible or not? "<<endl;
    // cout<<" ------------------------------------------- "<<endl;
    // cout<<"Enter 1st matrix row and coulmns: ";
    // cin>>r1>>c1;
    // cout<<"\nEnter 2nd matrix row and coulmns: ";
    // cin>>r2>>c2;

    // int arr1[r1][c1];
    // int arr2[r2][c2];

    // if (r1 == c2){
    //     cout<<"Yes, Multiplaciation is Possible."<<endl;
    //     multi = true;
    // }
    // else{
    //     cout<<"No, Multiplaciation isn't Possible."<<endl;
    // }
 
    // if (multi == true){
    // cout<<"Enter Elements: ";
    
    // for (int i = 0; i < r1; i++)
    // {
    //     for (int i = 0; i < c1; i++)
    //     {
                       
    //     }
    // }

    // ------------------------ 5 -------------------------   
    
//     return 0;
// }


#include <bits/stdc++.h>

using namespace std;

class SinglyLinkedListNode {
    public:
        int data;
        SinglyLinkedListNode *next;

        SinglyLinkedListNode(int node_data) {
            this->data = node_data;
            this->next = nullptr;
        }
};

class SinglyLinkedList {
    public:
        SinglyLinkedListNode *head;
        SinglyLinkedListNode *tail;

        SinglyLinkedList() {
            this->head = nullptr;
            this->tail = nullptr;
        }

};

void print_singly_linked_list(SinglyLinkedListNode* node, string sep, ofstream& fout) {
    while (node) {
        fout << node->data;

        node = node->next;

        if (node) {
            fout << sep;
        }
    }
}

void free_singly_linked_list(SinglyLinkedListNode* node) {
    while (node) {
        SinglyLinkedListNode* temp = node;
        node = node->next;

        free(temp);
    }
}

SinglyLinkedListNode {
      int data;
      SinglyLinkedListNode* next;
  };
 
SinglyLinkedListNode* insertNodeAtHead(SinglyLinkedListNode* llist, int data) {
	SinglyLinkedList* newNode = new SinglyLinkedListNode();
    newNode->data = data;
    
    if(llist == NULL){
        llist = newNode;
        return llist;
    }
    SinglyLinkedList* temp = llist;
        

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    SinglyLinkedList* llist = new SinglyLinkedList();

    int llist_count;
    cin >> llist_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

  
    for (int i = 0; i < llist_count; i++) {
        int llist_item;
        cin >> llist_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

    	SinglyLinkedListNode* llist_head = insertNodeAtHead(llist->head, llist_item);
      	llist->head = llist_head;
    }


    print_singly_linked_list(llist->head, "\n", fout);
    fout << "\n";

    free_singly_linked_list(llist->head);

    fout.close();

    return 0;
}
