#include <iostream>
using namespace std;

struct Node
{
    string names;
    Node *next;
};

void insertion_beg(Node *&head, string name)
{
    Node *newNode = new Node();
    newNode->names = name;

    if (head == NULL)
    {
        head = newNode;
        return;
    }
    newNode->next = head;
    head = newNode;
}

void insertion_End(Node *&head, string name)
{
    Node *newNode = new Node();
    newNode->names = name;
    newNode->next = NULL;

    if (head == NULL)
    {
        insertion_beg(head, name);
        return;
    }
    Node *temp = head;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = newNode;
}

void insertion_pos(Node *&head, string name, int pos)
{
    Node *newNode = new Node();
    newNode->names = name;
    if (pos == 1)
    {
        insertion_beg(head, name);
        return;
    }
    Node *temp = head;
    for (int i = 0; i < pos - 1; i++)
    {
        temp = temp->next;
    }
    newNode->next = temp->next;
    temp->next = newNode;
}

void display(Node *head)
{
    if (head == NULL)
    {
        cout << "List is Empty." << endl;
        return;
    }
    Node *temp = head;
    while (temp != NULL)
    {
        cout << temp->names << " -> ";
        temp = temp->next;
    }
    cout<<"NULL";
}

int main()
{
    // ----------------------------Task # 04 ----------------------------
    Node *head = NULL;
    int choice = 0;
    string name;

    while (choice != 5)
    {
        cout << "\n1: Insertion at beg: " << endl;
        cout << "2: Insertion at End: " << endl;
        cout << "3: Insertion at Pos: " << endl;
        cout << "4: Display: " << endl;
        cout << "5: Exit: " << endl;
        cout << "Enter your Choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            cout << "Enter Name: ";
            cin >> name;
            insertion_beg(head, name);
            break;
        case 2:
            cout << "Enter Name: ";
            cin >> name;
            insertion_End(head, name);
            break;
        case 3:
            int pos;
            cout << "Enter Name: ";
            cin >> name;
            cout << "Enter Position: ";
            cin >> pos;
            insertion_pos(head, name, pos);
            break;
        case 4:
            display(head);
            break;
        case 5:
            cout << "Exiting..." << endl;
            break;
        default:
            cout << "Wrong Choice." << endl;
            break;
        }
    }

    return 0;
}
