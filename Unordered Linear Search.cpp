#include<bits/stdc++.h>
using namespace std;

int ULS(int A[],int n,int data)
{
    for(int i=0;i<n;i++)
    {
        if(A[i]==data)
            return i;
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
    cout<<"Enter the elements of array";
    for(int i=0;i<n;i++)
    {
        cin>>A[i];
    }
    cout<<"Enter the data to be searched";
    cin>>data;
    info = ULS(A,n,data);
    if(info==-1)
        cout<<"Element not found";
    else
        cout<<"Element found at position :"<<info;
}
