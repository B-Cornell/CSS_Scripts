#ifndef UNIQUE_PAIRS_H
#define UNIQUE_PAIRS_H

#include <iostream>
#include <math.h>
#include <string>
#include <fstream>
#include <ostream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <string>

#define N_HEADER_LINES 3
#define HUBBLE_CONST 0.688062
#define N_HALO_ATTR 12
#define PI 3.14159265359


struct cart_t{
  double x;
  double y;
  double z;
};

struct sph_t{
  double theta; // polar angle
  double phi; // azimuthal angle
  double rho; // radius, this isn't really used
};

struct halo_t{
  cart_t pos,vel;
  long index;
  double mvir;
  double r200b;
  int snapnum;
  long mainleaf;
  long depthfirst;
};

struct bounds_t{
  double up;
  double low;
};

struct pair_t{
  int id;
  halo_t a;
  halo_t b;
  double prob; //probability
};

double probability(std::string type, double mean, double sigma, double value);
double magnitude(cart_t cart);
cart_t projection(cart_t a, cart_t b);
cart_t sep_projection(cart_t a, cart_t b);
cart_t sph_to_cart(sph_t sph);
pair_t  temp_halo(pair_t old_pair);
sph_t cart_to_sph(cart_t cart);
cart_t get_rel_v(halo_t halo_a, halo_t halo_b);
cart_t get_rel_p(halo_t halo_a, halo_t halo_b);
halo_t halo_t_parser(std::string str_input);
bounds_t get_range_input(std::string type);
void print_halo(halo_t halo);
void save_halo(halo_t halo, std::ofstream& data);


#endif
