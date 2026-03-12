// #include <iostream>
// using namespace std;

// struct Node {
//     int data;
//     int priority;
//     Node* next;
// };

// Node* head = NULL;

// // Insert
// void insert(int value, int p) {
//     Node* temp = new Node();
//     temp->data = value;
//     temp->priority = p;
//     temp->next = NULL;

//     if (head == NULL || p < head->priority) {
//         temp->next = head;
//         head = temp;
//         return;
//     }

//     Node* curr = head;
//     while (curr->next != NULL && curr->next->priority <= p) {
//         curr = curr->next;
//     }

//     temp->next = curr->next;
//     curr->next = temp;
// }

// // Delete
// void remove() {
//     if (head == NULL) {
//         cout << "Queue is Empty\n";
//         return;
//     }

//     Node* temp = head;
//     cout << "Removed: " << temp->data << endl;
//     head = head->next;
//     delete temp;
// }

// // Display
// void display() {
//     Node* temp = head;
//     while (temp != NULL) {
//         cout << temp->data << "(" << temp->priority << ") ";
//         temp = temp->next;
//     }
//     cout << endl;
// }

// int main() {
//     insert(10, 2);
//     insert(20, 1);
//     insert(30, 3);

//     display();
//     remove();
//     display();

//     return 0;
// }


// #include <iostream>
// using namespace std;

// // Node structure
// struct Node {
//     int data;
//     Node* left;
//     Node* right;
// };

// // Create new node
// Node* createNode(int value) {
//     Node* temp = new Node();
//     temp->data = value;
//     temp->left = NULL;
//     temp->right = NULL;
//     return temp;
// }

// // Insert node in BST (simple logic)
// Node* insert(Node* root, int value) {
//     if (root == NULL) {
//         return createNode(value);
//     }

//     Node* current = root;

//     while (true) {
//         if (value < current->data) {
//             if (current->left == NULL) {
//                 current->left = createNode(value);
//                 break;
//             }
//             current = current->left;
//         } else {
//             if (current->right == NULL) {
//                 current->right = createNode(value);
//                 break;
//             }
//             current = current->right;
//         }
//     }
//     return root;
// }

// // Find minimum value
// int findMin(Node* root) {
//     if (root == NULL) {
//         cout << "Tree is empty\n";
//         return -1;
//     }

//     while (root->left != NULL) {
//         root = root->left;
//     }
//     return root->data;
// }

// // Find maximum value
// int findMax(Node* root) {
//     if (root == NULL) {
//         cout << "Tree is empty\n";
//         return -1;
//     }

//     while (root->right != NULL) {
//         root = root->right;
//     }
//     return root->data;
// }

// int main() {
//     Node* root = NULL;
//     int choice, value;

//     do {
//         cout << "\n--- BST MENU ---\n";
//         cout << "1. Insert\n";
//         cout << "2. Find Minimum\n";
//         cout << "3. Find Maximum\n";
//         cout << "4. Exit\n";
//         cout << "Enter choice: ";
//         cin >> choice;

//         switch (choice) {
//             case 1:
//                 cout << "Enter value: ";
//                 cin >> value;
//                 root = insert(root, value);
//                 break;

//             case 2:
//                 cout << "Minimum value: " << findMin(root) << endl;
//                 break;

//             case 3:
//                 cout << "Maximum value: " << findMax(root) << endl;
//                 break;

//             case 4:
//                 cout << "Exit\n";
//                 break;

//             default:
//                 cout << "Invalid choice\n";
//         }

//     } while (choice != 4);

//     return 0;
// }





// -------------------------------------------------------------



#include <iostream>
using namespace std;

/* ========== PRIORITY QUEUE (LINKED LIST) ========== */

struct Event {
    int id;
    int priority;
    Event* next;
};

Event* front = NULL;

void insertEvent(int id, int priority) {
    Event* n = new Event();
    n->id = id;
    n->priority = priority;
    n->next = NULL;

    if (front == NULL || priority < front->priority) {
        n->next = front;
        front = n;
    } else {
        Event* t = front;
        while (t->next != NULL && t->next->priority <= priority)
            t = t->next;

        n->next = t->next;
        t->next = n;
    }
}

Event* removeEvent() {
    Event* t = front;
    front = front->next;
    return t;
}

/* ========== BINARY SEARCH TREE ========== */

struct Node {
    int data;
    Node* left;
    Node* right;
};

Node* createNode(int v) {
    Node* n = new Node();
    n->data = v;
    n->left = NULL;
    n->right = NULL;
    return n;
}

Node* insertBST(Node* root, int v) {
    if (root == NULL)
        return createNode(v);

    if (v < root->data)
        root->left = insertBST(root->left, v);
    else
        root->right = insertBST(root->right, v);

    return root;
}

int findMin(Node* root) {
    while (root->left != NULL)
        root = root->left;
    return root->data;
}

int findMax(Node* root) {
    while (root->right != NULL)
        root = root->right;
    return root->data;
}

/* ========== MAIN ========== */

int main() {

    Node* root = NULL;

    cout << "RANDOM INPUT\n";

    // Random input (simple values)
    insertEvent(45, 3);
    insertEvent(12, 1);
    insertEvent(78, 4);
    insertEvent(23, 2);
    insertEvent(90, 5);
    insertEvent(34, 3);
    insertEvent(67, 2);
    insertEvent(10, 1);

    while (front != NULL) {
        Event* e = removeEvent();
        cout << "Processed ID: " << e->id << endl;
        root = insertBST(root, e->id);
    }

    cout << "Min ID: " << findMin(root) << endl;
    cout << "Max ID: " << findMax(root) << endl;

    /* -------- SORTED INPUT -------- */

    cout << "\nSORTED INPUT\n";

    front = NULL;
    root = NULL;

    insertEvent(10, 1);
    insertEvent(20, 2);
    insertEvent(30, 3);
    insertEvent(40, 4);
    insertEvent(50, 5);
    insertEvent(60, 6);
    insertEvent(70, 7);
    insertEvent(80, 8);

    while (front != NULL) {
        Event* e = removeEvent();
        cout << "Processed ID: " << e->id << endl;
        root = insertBST(root, e->id);
    }

    cout << "Min ID: " << findMin(root) << endl;
    cout << "Max ID: " << findMax(root) << endl;

    return 0;
}
