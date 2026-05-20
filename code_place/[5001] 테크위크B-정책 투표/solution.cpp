}
#include<stdio.h>
const int NMAX = 1'000'000;
int arr[NMAX];
int main(){
    int n;scanf("%d",&n);
    for(int i = 0;i<n;i++)scanf("%d",arr+i);
​
    int cnt=0, num;
    for(int i = 0;i<n;i++){
        if(cnt==0)num=arr[i],cnt=1;
        else if(num==arr[i])cnt++;
        else cnt--;
    }
    cnt=0;
    for(int i = 0;i<n;i++){
        if(arr[i]==num)cnt++;
    }
​
    if(cnt>n/2)printf("%d",num);
    else printf("-1");
}
​