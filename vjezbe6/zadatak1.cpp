#include <iostream>

void pravac(int x1,int y1, int x2, int y2)
{
    float k;
    k = (y2-y1)/(x2-x1);
    std::cout << "jednadzba pravca je: y-" << y1 << "="<< k <<"(x-"<<x1<<")" << std::endl;
}

int main(){
    pravac(1,2,3,4);
}
