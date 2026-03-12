#include <iostream>
#include <string>
using namespace std;

const int MAX = 10;

class AdmissionQueue {
private:
    string queue[MAX];
    int front;
    int rear;
    int count;

public:
    AdmissionQueue() {
        front = 0;
        rear = -1;
        count = 0;
    }

    void enqueue(string student) {
        if (count == MAX) {
            cout << "Queue is full. Cannot add more students.\n";
            return;
        }
        rear = (rear + 1) % MAX;
        queue[rear] = student;
        count++;
        cout << student << " added to the waiting list.\n";
    }

    void dequeue() {
        if (count == 0) {
            cout << "No students to process.\n";
            return;
        }
        cout << "Processing completed for: " << queue[front] << endl;
        front = (front + 1) % MAX;
        count--;
    }

    void currentStudent() {
        if (count == 0) {
            cout << "No student is currently being served.\n";
        } else {
            cout << "Currently being served: " << queue[front] << endl;
        }
    }

    void totalWaiting() {
        cout << "Total students waiting: " << count << endl;
    }
};

int main() {
    AdmissionQueue aq;

    aq.enqueue("Student A");
    aq.enqueue("Student B");
    aq.enqueue("Student C");

    aq.currentStudent();
    aq.dequeue();

    aq.currentStudent();
    aq.totalWaiting();

    return 0;
}
