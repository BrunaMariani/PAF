#include <iostream>
#include <cmath>
void ispis(int polje[], int a, int b){
    int n = sizeof(polje);
    for (int i = 0; i<21; i++)
    { 
        if (polje[i] >= a){
            if (polje[i] <= b){
            std::cout << polje[i] << std::endl;
            }
        }
        
    }



int main(){
    int polje[20]= {-10,2,34,11,-32,13,56,-23,43,1,0,-5,4,14,-15,16,-17,18,-19,20};
    int a;
    a = -5;
    int b;
    b = 15;
    for (int i = 0; i<21; i++)
    { 
        if (polje[i] >= a){
            if (polje[i] <= b){
            std::cout << polje[i] << std::endl;
            }
        }
        
    }
    return 0;
