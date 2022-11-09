#include<iostream>
using namespace std;
class stack
{
    int ar[30],top,n;
    public:
    stack()
    {   n=30;
        top=-1;
    }
    
    void push()
    {
        int val;
        cout<<"enter the value to be pushed "<<endl;
        cin>>val;
        if(top==n-1)
        {
             cout<<"stack is overflow "<<endl;
        }
        else{
            top++;
            ar[top]=val;
        }
    }
    int pop()
    {
        if(top==-1)
        {
            cout<<"stack is underflow "<<endl;
            return 0;
        }
        else
        {
           
           
           return (ar[--top]);
           cout<<"the poped element is ";

        }
    }
    int peek()
    {
        cout<<"the peek(top) value is :"<<ar[top]<<endl;
        return 1;
    }
    
    void display()
    {
       if (top==-1)
       {
        cout<<"no element in stack "<<endl;
       }
       else
       {
           for(int i=top;i>=0;i--)
           {
              cout<<"the values are :"<<ar[i]<<endl;

           }
       }
    
    }

};
int main()
{
    stack s1;
    s1.push();
    s1.push();
    s1.push();
    s1.peek();
    s1.display();
    s1.pop();
    s1.display();
    s1.peek();
    return 0;
}