#include<stdio.h>
int main(){
    int n,i;scanf("%d",&n);
    for(i=1;i*(i+1)/2<n;i++);
    if(i*i+i==2*n)printf("1");
    else printf("0");
}
​