#include <iostream>

using namespace std;

class Queue {
private:
  int front;
  int rear;
  int arr[5];

public:
  Queue() {
    front = -1;
    rear = -1;
    for (int i = 0; i < 5; i++) {
      arr[i] = 0;
    }
  }

  bool isEmpty() {
    if (front == -1 && rear == -1)
      return true;
    return false;
  }

  bool isFull() {
    // size of array: 5
    if (rear == 4)
      return true;
    return false;
  }

  void enqueue(int val) {
    if (isFull()) {
      cout << "Queue is full. Cannot insert any values" << endl;
      return;
    } else if (isEmpty()) {
      rear = 0;
      front = 0;
      arr[rear] = val;
    } else {
      rear++;
      arr[rear] = val;
    }
  }

  int dequeue() {
    int x = 0;
    if (isEmpty()) {
      cout << "Queue is Empty" << endl;
      return x;
    } else if (rear == front) {
      x = arr[rear];
      rear = -1;
      front = -1;
      return x;
    } else {
      cout << "front value: " << front << endl;
      x = arr[front];
      arr[front] = 0;
      front++;
      return x;
    }
  }

  int count() {
    return (rear - front + 1);
  }

  void print() {
    cout << "All values in the Queue are - " << endl;
    for (int i = 0; i < 5; i++) {
      cout << arr[i] << "  ";
    }
  }
};

int main() {
  Queue queue;
  int option;
  do {
    cout << "What operation do you want to perform? Select option number. Enter 0 to exit." << endl;
    cout << "1. enqueue()" << endl;
    cout << "2. dequeue()" << endl;
    cout << "3. isEmpty()" << endl;
    cout << "4. isFull()" << endl;
    cout << "5. count()" << endl;
    cout << "6. print()" << endl;
    cout << "7. Clear screen" << endl;

    cin >> option;

    switch (option) {
      case 0:
        break;
      case 1:
        break;
      case 2:
        break;
      case 3:
        break;
      case 4:
        break;
      case 5:
        break;
      case 6:
        break;
      case 7:
        break;
      default:
        cout << "Enter Proper Option number " << endl;
    }
  } while (option != 0);

  return 0;
}