#include<bits/stdc++.h>
using namespace std;

// It is similar as binary search but instead of directly searching the mid element
// It searches the nearest element to the number to be searched
// the variable mid helps in finding the closest number
int IS(int A[],int data)
{
    int low=0,mid,high=sizeof(A)-1;
    while(low<=high)
    {
        mid = low + (((data - A[low]) * (high - low))/(A[high]-A[low]));
        if(data == A[mid])
            return mid+1;
        if(data < A[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }
return -1;
}

int main()
{
    int n;
    int data,info;
    cout<<"Enter the number of elements in an array";
    cin>>n;
    int A[n];
    // ELEMENTS INPUT ARE TO BE IN SORTED ORDER
    // OR YOU CAN ADD THE SORT FUNCTION IN IT
    cout<<"Enter the elements of array";
    for(int i=0;i<n;i++)
    {
        cin>>A[i];
    }
    cout<<"Enter the data to be searched";
    cin>>data;
    info = IS(A,data);
    if(info==-1)
        cout<<"Element not found";
    else
        cout<<"Element found at position :"<<info;
}
