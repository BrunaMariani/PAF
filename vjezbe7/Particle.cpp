#include <iostream>
#include <math.h>
#include "particle.h"
Particle::Particle(float v, float kut_, float xkoor_, float ykoor_){
        brzina=v;
        kut= kut_;
        xkoor =  xkoor_;
        ykoor = ykoor_;
        float kut2_;
        kut2_= kut_*pi/180;
        vx = v*cos(kut2_);
        vy = v*sin(kut2_);

}
float Particle::move(float dt){
    
            xkoor =xkoor + vx*dt;
            vy = vy - g*dt;
            ykoor = ykoor + vy*dt;
            t = t + dt;
            }
float Particle::range(float dt){
    
            
            do{
                __move(dt);
            }
            while (ykoor>=0);
           
            

            std::cout << xkoor << std::endl;
        }
        
float Particle::vrijeme(float dt){
            
            do{
                __move(dt);
            }
            while (ykoor>=0);
            
            std::cout << t << std::endl;
            
        }
