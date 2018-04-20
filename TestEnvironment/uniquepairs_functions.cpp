#include "uniquepairs.h"

double magnitude(cart_t cart){
  double mag;

  mag = sqrt(cart.x*cart.x + cart.y*cart.y + cart.z*cart.z);

  return mag;
}

//Projection of a onto b
cart_t projection(cart_t a, cart_t b){

  cart_t proj;

  proj.x = ( (a.x*b.x) + (a.y*b.y) + (a.z*b.z) ) / ( magnitude(b)*magnitude(b) ) * b.x;
  proj.y = ( (a.x*b.x) + (a.y*b.y) + (a.z*b.z) ) / ( magnitude(b)*magnitude(b) ) * b.y;
  proj.z = ( (a.x*b.x) + (a.y*b.y) + (a.z*b.z) ) / ( magnitude(b)*magnitude(b) ) * b.z;

  return proj;
}

cart_t sep_projection(cart_t a, cart_t b){

  cart_t p_sep, norm_comp;

  norm_comp = projection(a,b);

  p_sep.x = a.x - norm_comp.x;
  p_sep.y = a.y - norm_comp.y;
  p_sep.z = a.z - norm_comp.z;

  return p_sep;
}

cart_t sph_to_cart(sph_t sph){

  cart_t cart;

  cart.x = sin(sph.theta)*cos(sph.phi);
  cart.y = sin(sph.theta)*sin(sph.phi);
  cart.z = cos(sph.theta);

  return cart;
}

sph_t cart_to_sph(cart_t cart){

  sph_t sph;

  sph.theta = atan(sqrt(cart.x*cart.x + cart.y*cart.y)/cart.z);
  sph.phi = atan(cart.y/cart.x);

  return sph;
}

//relative velocity of a from b
cart_t get_rel_v(halo_t halo_a, halo_t halo_b){

  cart_t v;

  v.x = halo_a.vel.x - halo_b.vel.x;
  v.y = halo_a.vel.y - halo_b.vel.y;
  v.z = halo_a.vel.z - halo_b.vel.z;

  return v;
}

//relative position of a from b
cart_t get_rel_p(halo_t halo_a, halo_t halo_b){

  cart_t p;

  p.x = halo_a.pos.x - halo_b.pos.x;
  p.y = halo_a.pos.y - halo_b.pos.y;
  p.z = halo_a.pos.z - halo_b.pos.z;

  return p;
}

halo_t halo_t_parser(std::string str_input){
  int i;
  halo_t halo;
  std::string str_working[12];

  std::stringstream str_stream(str_input);
  //std::cout << str_input << std::endl;
  if (str_stream.good()){
    for( i=0; i<N_HALO_ATTR; i++){
      str_stream >> str_working[i];
    }
  }
  //std::cout << atof(str_working[0].c_str()) << ", " << atof(str_working[1].c_str()) << ", " << atof(str_working[2].c_str()) << ", " << atof(str_working[3].c_str()) << ", " << atof(str_working[4].c_str()) << ", " << atof(str_working[5].c_str()) << ", " << atof(str_working[6].c_str()) << ", " << atof(str_working[7].c_str()) << ", " << atof(str_working[8].c_str()) << ", " << atof(str_working[9].c_str()) << ", " << atof(str_working[10].c_str()) << ", " << atof(str_working[11].c_str()) << std::endl;

  halo.index = std::stoll(str_working[0].c_str());
  halo.snapnum = atof(str_working[1].c_str());
  halo.mvir = atof(str_working[2].c_str());
  halo.r200b = atof(str_working[3].c_str());
  halo.depthfirst = atof(str_working[4].c_str());
  halo.mainleaf = atof(str_working[5].c_str());
  halo.pos.x = atof(str_working[6].c_str());
  halo.pos.y = atof(str_working[7].c_str());
  halo.pos.z = atof(str_working[8].c_str());
  halo.vel.x = atof(str_working[9].c_str());
  halo.vel.y = atof(str_working[10].c_str());
  halo.vel.z = atof(str_working[11].c_str());


  return halo;
}

bounds_t get_range_input(std::string type){

  bounds_t bound;
  double input, range;

  std::string units;

  if(type=="separation"){
    units = "(Mpc)";
  }

  if(type=="velocity"){
    units = "(km/s)";
  }

  if(type=="mass_a" || type=="mass_b"){
    units = "(Msun)";
  }

  std::cout << "Input projected " << type << " " << units <<": ";
  std::cin >> input;

  std::cout << "Input projected range " << type << " " << units <<": ";
  std::cin >> range;

  bound.up = input + range;
  bound.low = input - range;

  return bound;
}

double probability(std::string type, double mean, double sigma, double value){
	double prob;
	if (type == "tophat"){
		if (value<= mean + sigma and value>= mean - sigma){
			prob = 1;
		}
		else{
			prob = 0;
		}
	}
	if (type == "gaussian"){

		prob = (exp(((mean-value)*(value-mean))/(2*sigma*sigma)));
	}

	return prob;
}
void print_halo(halo_t halo){

  std::cout << halo.index << " " << halo.pos.x << " " << halo.pos.y << " " << halo.pos.z << " " << halo.vel.x << " " << halo.vel.y << " " << halo.vel.z << " " << halo.mvir << " " << halo.r200b  << std::endl;

  return;
}

void save_halo(halo_t halo, std::ofstream& data){

  data << halo.index << " " << halo.pos.x << " " << halo.pos.y << " " << halo.pos.z << " " << halo.vel.x << " " << halo.vel.y << " " << halo.vel.z << " " << halo.mvir << " " << halo.r200b  << std::endl;

  return;
}

pair_t  temp_halo(pair_t old_pair){
double position, velocitynew=0, unitx, unity, unitz, Vel_par, Vel_perp;
pair_t new_pair;

position = sqrt((old_pair.a.pos.x-old_pair.b.pos.x)*(old_pair.a.pos.x-old_pair.b.pos.x)+(old_pair.a.pos.y-old_pair.b.pos.y)*(old_pair.a.pos.y-old_pair.b.pos.y)+(old_pair.a.pos.z-old_pair.b.pos.z)*(old_pair.a.pos.z-old_pair.b.pos.z));

velocitynew = sqrt((old_pair.a.vel.x-old_pair.b.vel.x)*(old_pair.a.vel.x-old_pair.b.vel.x)+(old_pair.a.vel.y-old_pair.b.vel.y)*(old_pair.a.vel.y-old_pair.b.vel.y)+(old_pair.a.vel.z-old_pair.b.vel.z)*(old_pair.a.vel.z-old_pair.b.vel.z));

//find the separation unit vector
unitx = (old_pair.a.pos.x-old_pair.b.pos.x)/position;
unity = (old_pair.a.pos.y-old_pair.b.pos.y)/position;
unitz = (old_pair.a.pos.z-old_pair.b.pos.z)/position;


//dot the velocity vector to the sep vector to get the velocity parallel to the separation vector
Vel_par = ((old_pair.a.vel.x-old_pair.b.vel.x)*(old_pair.a.pos.x-old_pair.b.pos.x)+(old_pair.a.vel.y-old_pair.b.vel.y)*(old_pair.a.pos.y-old_pair.b.pos.y)+(old_pair.a.vel.z-old_pair.b.vel.z)*(old_pair.a.pos.z-old_pair.b.pos.z))/position;

Vel_perp = sqrt((velocitynew*velocitynew)-(Vel_par*Vel_par));

new_pair = old_pair;//Set the new pair values to the old pair values so that it is set up the same, but we can change what we need on it without changing the real pair at all
//Now set the first halo to the origin for easy calculations
new_pair.a.pos.x = 0;
new_pair.a.pos.y = 0;
new_pair.a.pos.z = 0;
//Velocity is relative, so we set one halo to 0 to make the calculations easier
new_pair.a.vel.x = 0;
new_pair.a.vel.y = 0;
new_pair.a.vel.z = 0;

//Now set the second halo along the z axis
new_pair.b.pos.x = 0;
new_pair.b.pos.y = 0;
new_pair.b.pos.z = position;

//Now we set the relative velocity of the second halo
new_pair.b.vel.x = 0;
new_pair.b.vel.y = Vel_perp;//velocity perpendicular this is MagV-vel.z
new_pair.b.vel.z = Vel_par;//velocity along separation vector. This is V_vector dot r-hat
return new_pair;
}
