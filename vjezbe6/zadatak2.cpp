#include <iostream>
#include <cmath>
void  udaljenost_tocke(int x1,int y1,int x2,int y2,int r)
{
    float x;
    x = pow((x1-x2),2) + pow((y1-y2),2);
    float d;
    d = sqrt(x);
    float epsilon = 0.01;
    if (d<r){
        std::cout << "Točka se nalazi unutar kružnice" << std::endl;
    }
    else if ( r-epsilon < d < r+epsilon){
        std::cout << "Točka se nalazi na kružnici" << std::endl;
    }
    else{
        std::cout << "Točka se nalazi izvan kružnice" << std::endl;
    }
}
int main(){
    udaljenost_tocke(1,2,3,4,5);
    return 0;
}
