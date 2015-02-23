/************************************************************

  C151 Spring 2004
  Dana Vrajitoru
  sum_array.cc

  A program that inputs a list of real numbers, stores it 
  in an array, and outputs the sum of these numbers.

*************************************************************/

#include <iostream>
using namespace std;

const int MAX_SIZE = 50;
float numbers[MAX_SIZE];

// Function prototypes
void init_array(int size);
void input_array(int &size);
float compute_sum(int size);

int main()
{
  int size;

  // Input the numbers
  input_array(size);

  // Compute and output the sum
  cout << "The sum of these numbers is " 
       << compute_sum(size) << endl;

  return 0;
}

// A function that assign 0.0 to each element of the array.
void init_array(int size)
{  
  for (int i=0; i<size; i++)
    numbers[i] = 0.0;
}

// A function that inputs the elements of an array and returns the
// number of elements in the reference parameter size.
void input_array(int &size)
{
  cout << "Enter the number of elements, " 
       << "maximum " << MAX_SIZE << endl;
  cin >> size;
  for (int i=0; i<size; i++) {
    cout << "Enter the element number " << i << endl;
    cin >> numbers[i];
  }
}

// A function that computes the sum of the elements of an array.
float compute_sum(int size)
{
  float sum = 0;
  for (int i=0; i<size; i++)
    sum = sum + numbers[i];
  return sum;
}

/******************* Example of program output *************

Enter the number of elements,maximum 50
5
Enter the element number 0
2.15
Enter the element number 1
3.14
Enter the element number 2
60
Enter the element number 3
19.5
Enter the element number 4
2.41
The sum of these numbers is 87.2

*************************************************************/

