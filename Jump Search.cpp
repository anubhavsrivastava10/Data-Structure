#include<bits/stdc++.h>
using namespace std;


int JS(int arr[], int x, int n)
{
    int step = sqrt(n);
    int prev = 0;
    while (arr[min(step, n)-1] < x)
    {
        prev = step;
        step += sqrt(n);
        if (prev >= n)
            return -1;
    }
    while (arr[prev] < x)
    {
        prev++;
        if (prev == min(step, n))
            return -1;
    }
    if (arr[prev] == x)
        return prev;
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
    info = JS(A,n,data);
    if(info==-1)
        cout<<"Element not found";
    else
        cout<<"Element found at position :"<<info;
}
