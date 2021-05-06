#include <iostream>
#include <math.h>

class Particle{
    public:
        float brzina;
        float kut;
        float xkoor;
        float ykoor;
        float pi = 3.14159265;
        float g = 9.81;
        float kut2; 
        float vx;
        float  vy0;
        //float vx = brzina*cos(kut);
        //float  vy0 = brzina*sin(kut);
        Particle(float v, float kut_, float xkoor_, float ykoor_){
        brzina=v;
        kut= kut_;
        xkoor =  xkoor_;
        ykoor = ykoor_;
        kut2_= kut_*pi/180;
        vx = v*cos(kut2_);
        vy0 = v*sin(kut2_);
        }

        float range(float dt){
            //float pi = 3.14159265;
            //float g = 9.81;
            //float kut = kut*pi/180;
            //float vx;
            //float vy0;
            //vy0 = brzina*sin(kut);
            //vx = brzina*cos(kut);
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

            std::cout << x-xkoor << std::endl;
            
        }













}

