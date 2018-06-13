//Unique pair finder header file
#ifndef UNIQUE_PAIRS_H
#define UNIQUE_PAIRS_H


// C++ packages used
#include <iostream>
#include <math.h>
#include <string>
#include <fstream>
#include <ostream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <string>

//definitions
#define N_HEADER_LINES 3
#define HUBBLE_CONST 0.688062
#define N_HALO_ATTR 12
#define PI 3.14159265359

//we work in a cartesian coordinate system
struct cart_t{
  double x;
  double y;
  double z;
};

struct halo_t{ //single halo structure
  cart_t pos,vel; //cartesian position and velocity
  long index;
  double mvir; //mass
  double r200b; //radius
  int snapnum; //snapshot within simulation
  long mainleaf; //mainleaf depthfirst id given by simulation
  long depthfirst; // depthfirst id given by simulation
};

struct pair_t{ //halo pair structure
  int id;
  halo_t a; //first halo in pair
  halo_t b; //second halo in pair
  double prob; //probability
};

//declaring functions
pair_t  temp_halo(pair_t old_pair);
halo_t halo_t_parser(std::string str_input);
void print_halo(halo_t halo);
void save_halo(halo_t halo, std::ofstream& data);


#endif
