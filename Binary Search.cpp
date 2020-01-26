#include<bits/stdc++.h>
using namespace std;

//Iterative Method
int BS(int A[],int n,int data)
{
    int low = 0;
    int high = n-1;
    while(low<=high)
    {
        int mid = low+(high-low)/2;
        if(A[mid] == data)
            return mid;
        else if(A[mid]<data)
            low = mid+1;
        else
            high = mid-1;
    }
return -1;
}

//Recursive Method

int RBS(int A[],int low,int high,int data)
{
    int mid = low+(high-low)/2;
    if(low>high)
        return -1;
    if(A[mid]==data)
        return mid;
    else if(mid<data)
        return RBS(A,mid+1,high,data);
    else
        return RBS(A,low,mid-1,data);
return -1;
}
int main()
{
    int A[]={1,2,3,465,324,5};
    int n = sizeof(A)/sizeof(A[0]);
    int data = 324;
    //Recursive Binary Search Calling
    int result = RBS(A,0,n-1,data);
    //Iterative Binary Search Calling
    int result = BS(A,n,data);
    if(result == -1)
        cout<<"Element is not present";
    else
        cout<<"Element at : "<<result;

}
