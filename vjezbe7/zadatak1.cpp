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
        float  vy;
        float t= 0;
        Particle(float v, float kut_, float xkoor_, float ykoor_){
        brzina=v;
        kut= kut_;
        xkoor =  xkoor_;
        ykoor = ykoor_;
        float kut2_;
        kut2_= kut_*pi/180;
        vx = v*cos(kut2_);
        vy = v*sin(kut2_);
        

       
        }
    private: 
        float __move(float dt){
            
           
            xkoor =xkoor + vx*dt;
            vy = vy - g*dt;
            ykoor = ykoor + vy*dt;
            t = t + dt;
            
            }
            
    public:    
        float range(float dt){
            
           
            
            do{
                __move(dt);
            }
            while (ykoor>=0);
           
            

            std::cout << xkoor << std::endl;
        }
        
        float vrijeme(float dt){
            
            do{
                __move(dt);
            }
            while (ykoor>=0);
            
            std::cout << t << std::endl;
            
        }

        

};


int main(){
   Particle p1(20,30,5,5);
   p1.range(0.01);
   p1.vrijeme(0.01);
   Particle p2(10,10,0,0);
   p2.range(0.01);
   p2.vrijeme(0.01);
}
