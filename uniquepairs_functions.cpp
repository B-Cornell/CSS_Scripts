//functions used in the unique pairs program

#include "uniquepairs.h"


//reads in halo pairs from the input file and saves them as halo structures
halo_t halo_t_parser(std::string str_input){
  int i;
  halo_t halo;
  std::string str_working[12];

  std::stringstream str_stream(str_input);

  //if we have valid input, we save the file line information to a temporary string
  if (str_stream.good()){
    for( i=0; i<N_HALO_ATTR; i++){
      str_stream >> str_working[i];
    }
  }

  //save all the specific data to the correct piece of the halo structure
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



//just prints the halo to the terminal
void print_halo(halo_t halo){

  std::cout << halo.index << " " << halo.pos.x << " " << halo.pos.y << " " << halo.pos.z << " " << halo.vel.x << " " << halo.vel.y << " " << halo.vel.z << " " << halo.mvir << " " << halo.r200b  << std::endl;

  return;
}






//prints the to the file we want
void save_halo(halo_t halo, std::ofstream& data){

  data << halo.index << " " << halo.pos.x << " " << halo.pos.y << " " << halo.pos.z << " " << halo.vel.x << " " << halo.vel.y << " " << halo.vel.z << " " << halo.mvir << " " << halo.r200b  << std::endl;

  return;
}







//this function takes in a halo pair and does calculations to transform them into an easier to use coordinate system
pair_t  temp_halo(pair_t old_pair){
  double position, velocitynew, Vel_par, Vel_perp;
  pair_t new_pair;

  //this is the magnitude of the 3D separation of the two halos
  position = sqrt((old_pair.a.pos.x-old_pair.b.pos.x)*(old_pair.a.pos.x-old_pair.b.pos.x)+(old_pair.a.pos.y-old_pair.b.pos.y)*(old_pair.a.pos.y-old_pair.b.pos.y)+(old_pair.a.pos.z-old_pair.b.pos.z)*(old_pair.a.pos.z-old_pair.b.pos.z));

  //magnitude of the relative velocity of the two halos
  velocitynew = sqrt((old_pair.a.vel.x-old_pair.b.vel.x)*(old_pair.a.vel.x-old_pair.b.vel.x)+(old_pair.a.vel.y-old_pair.b.vel.y)*(old_pair.a.vel.y-old_pair.b.vel.y)+(old_pair.a.vel.z-old_pair.b.vel.z)*(old_pair.a.vel.z-old_pair.b.vel.z));


  //dot the velocity vector to the sep vector to get the velocity parallel to the separation vector
  Vel_par = ((old_pair.a.vel.x-old_pair.b.vel.x)*(old_pair.a.pos.x-old_pair.b.pos.x)+(old_pair.a.vel.y-old_pair.b.vel.y)*(old_pair.a.pos.y-old_pair.b.pos.y)+(old_pair.a.vel.z-old_pair.b.vel.z)*(old_pair.a.pos.z-old_pair.b.pos.z))/position;

  //the velocity component perpendicular to the separation vector is just the third side of a right triangle that has side=parallel velocity and hypotenuse=total velocity
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
  //the separation is the same, but it is all along one axis to make calculations simpler
  new_pair.b.pos.x = 0;
  new_pair.b.pos.y = 0;
  new_pair.b.pos.z = position;

  //Now we set the relative velocity of the second halo
  new_pair.b.vel.x = 0;
  new_pair.b.vel.y = Vel_perp;//velocity perpendicular to the separation vector
  new_pair.b.vel.z = Vel_par;//velocity along separation vector

  //just assign the old values, these don't change
  new_pair.a.r200b = old_pair.a.r200b; //radii
  new_pair.b.r200b = old_pair.b.r200b;
  new_pair.a.mvir = old_pair.a.mvir; //masses
  new_pair.b.mvir = old_pair.b.mvir;
  new_pair.a.mainleaf = old_pair.a.mainleaf; //system ids
  new_pair.b.mainleaf = old_pair.b.mainleaf;
  new_pair.a.depthfirst = old_pair.a.depthfirst;
  new_pair.b.depthfirst = old_pair.b.depthfirst;
  return new_pair;
}
