#include <iostream>
#include <math.h>

class Particle{
    public:
        Particle(){
        float brzina;
        float kut;
        float xkoor;
        float ykoor;
        float pi = 3.14159265;
        float g = 9.81;
        float kut = kut*pi/180;
        }

        float range(brzina, kut, xkoor, ykoor, float dt){
            float pi = 3.14159265;
            float g = 9.81;
            float kut = kut*pi/180;
            float vx;
            float vy0;
            vy0 = brzina*sin(kut);
            vx = brzina*cos(kut);
            float vy;
            vy = vy0;
            float y = ykoor;
            float x = xkoor;
            vy = vy0;
            while (y>=0){
            x =x + vx*dt;
            vy = vy - g*dt;
            y = y + vy*dt;
            }

            cout << x-xkoor ;
            
        }













};

