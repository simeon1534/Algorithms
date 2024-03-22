/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <list>
using namespace std;

void printArray(int arr[], int arrLen) {
  cout << "\n";
  for (int i =0; i <arrLen; i++) {
        cout << arr[i] << " ";
    }
}

int main()
{
    int myunsortedlist[]={3,8,2,9,1,0,12};
    int getArrayLength = sizeof(myunsortedlist) / sizeof(myunsortedlist[0]);

    printArray(myunsortedlist,getArrayLength);


    while (true) {
        
        bool swap = false;
        for (int i =0; i <getArrayLength; i++) {
            
            // last element doesnt need to check for swap
            if (i == getArrayLength - 1) {
                break;
            }
            if (myunsortedlist[i] > myunsortedlist[i+1]) {
                // swap
                int temp = myunsortedlist[i];
                myunsortedlist[i] = myunsortedlist[i+1];
                myunsortedlist[i+1] = temp;
                swap = true;
            } 
            
        }
        printArray(myunsortedlist,getArrayLength);
        // if for loop didnt swap then the array is sorted already

        if (swap == false) {
            break;
        }
    
    }
    

    
    return 0;
}