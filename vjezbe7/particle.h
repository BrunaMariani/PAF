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
        Particle(float v, float kut_, float xkoor_, float ykoor_);
    private:
        float __move(float dt);
    public:
        float range(float dt);
        float vrijeme(float dt);
};