#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<math.h>
#include<iomanip>

using namespace std;

int main(){
	float a,area,pi = 3.14159;
	cin>>a;
	area = pi * pow(a,2);
	std::cout<<std::fixed;
	std::cout<<std::setprecision(4);
	std::cout<<"A="<<area<<endl;
	return 0;
}
