#include <iostream>
#include <string>

using namespace std;

class Stack {
private:
  int top;
  int arr[5];

public:
  Stack() {
    top = -1;
    for (int i = 0; i < 5; i++) {
      arr[i] = 0;
    }
  }

  bool isEmpty() {
    if (top == -1)
      return true;
    return false;
  }

  bool isFull() {
    if (top == 4)
      return true;
    return false;
  }

  void push(int val) {
    if (isFull()) {
      cout << "Stack is full; stack overflow" << endl;
    } else {
      top++;
      arr[top] = val;
    }
  }

  int pop() {
    if (isEmpty()) {
      cout << "Stack is empty; stack underflow" << endl;
      return 0;
    } else {
      int popval = arr[top];
      arr[top] = 0;
      top--;
      return popval;
    }
  }

  int count() {
    return (top + 1);
  }

  int peek() {
    if (top < 0) {
      cout << "Stack is Empty" << endl;
      return 0;
    } else {
      int x = arr[top];
      return x;
    }
  }

  int getVal(int pos) {
    if (isEmpty()) {
      cout << "Stack is empty; stack underflow" << endl;
      return 0;
    } else {
      return arr[pos];
    }
  }

  void change(int pos, int val) {
    arr[pos] = val;
    cout << "Value changed at the location " << pos << endl;
  }

  void print() {
    cout << "All values in the stack are " << endl;
    for (int i = 4; i >= 0; i--) {
      cout << arr[i] << endl;
    }
  }
};

int main() {
  Stack stack;
  int option;
  int position;
  int value;
  do {
    cout << "What operation do you want to perform? Select Option number. Enter 0 to exit." << endl;
    cout << "1. push()" << endl;
    cout << "2. pop()" << endl;
    cout << "3. isEmpty()" << endl;
    cout << "4. isFull()" << endl;
    cout << "5. peek()" << endl;
    cout << "6. count()" << endl;
    cout << "7. change()" << endl;
    cout << "8. getVal()" << endl;
    cout << "9. print()" << endl;
    cout << "10. Clear Screen" << endl;
    cin >> option;
    switch (option) {
      case 0:
        break;
      case 1:
        cout << "Enter an item to push in the stack" << endl;
        cin >> value;
        stack.push(value);
        break;
      case 2:
        cout << "Poped Value: " << stack.pop() << endl;
        break;
      case 3:
        if (stack.isEmpty())
          cout << "Stack is Empty" << endl;
        else
          cout << "Stack is not Empty" << endl;
        break;
      case 4:
        if (stack.isFull())
          cout << "Stack is Full" << endl;
        else
          cout << "Stack is not Full" << endl;
        break;
      case 5:
        cout << "Peek value is " << stack.peek() << endl;
        break;
      case 6:
        cout << "Number of Items in the Stack are: " << stack.count() << endl;
        break;
      case 7:
        cout << "Enter position of item you want to change : ";
        cin >> position;
        cout << endl;
        cout << "Enter value of item you want to change : ";
        cin >> value;
        stack.change(position, value);
        break;
      case 8:
        cout << "Enter the position you want to see: ";
        cin >> position;
        cout << "The value at the position " << position << " is " << stack.getVal(position) << endl;
      case 9:
        stack.print();
        break;
      case 10:
        system("cls");
        break;
      default:
        cout << "Enter Proper Option number " << endl;
    }
  } while (option != 0);
  return 0;
}
