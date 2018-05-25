#include "uniquepairs.h"

using namespace std;



int main(int argc, char *argv[]){
  float N_PAIRS = atof(argv[2]);
  string inputfilesnap = argv[1];
  string f_halo_data_string = "reduced_cosmo_pairs_increased_timeframe_" + inputfilesnap + ".txt";
  std::ofstream savefile;

  string savefilestring = "separation_data_increased_timeframe" + inputfilesnap + ".csv";

  savefile.open(savefilestring);
  savefile << "Pair ID, RockstarA, RockstarB, Mass A, Mass B, Radius A, Radius B, Separation, Head On Velocity, Tangential Velocity" << std::endl;
  vector<pair_t> pair(N_PAIRS); // This is our giant vector where we store all the halo pairs in the heap

  pair_t calculation_pair;
  string halo_a_str, halo_b_str, pair_id_str, temp;
  int i,j,k, unique = 1;
  string save_directory = "/home/CosmoSim/";


  cout << "------------------------------------------" << endl;

  ifstream f_halo_data;

  f_halo_data.open(f_halo_data_string);

  if (f_halo_data.is_open()){

    // Skip header
    for(i = 0; i < N_HEADER_LINES; i++){
      getline(f_halo_data,temp);
    }

    // This loop sticks everything into a giant vector of type pair
    for(i=0; i< N_PAIRS; i++){

      getline(f_halo_data,pair_id_str); //halo pair id
      getline(f_halo_data,halo_a_str);  // halo a data
      getline(f_halo_data,halo_b_str);  // halo b data

      pair[i].id = atoi(pair_id_str.c_str());
      pair[i].a = halo_t_parser(halo_a_str); // Parses pair.a data into halo_t retainer
      pair[i].b = halo_t_parser(halo_b_str); // Parses pair.b data into halo_t retainer
      //std::cout << pair[i].a.vel.x << std::endl;
      if (i%100 == 0){
        cout << "Processing... " <<  double(i)/N_PAIRS*100 << "%\r";
        cout.flush();
      }
    }
    cout << "Processing... 100%              \nComplete."<< endl;
  }

  // Iterates over all the pairs
  for(k=0; k < N_PAIRS; k++){
    //std::cout << pair[k].a.vel.x << " " << pair[k].b.vel.x << " " << std::endl;
    // Print progress in percentage
    if (k%1000 == 0){
      cout << "Searching for unique pairs... " << double(k)/double(N_PAIRS)*100 << "%    \r";
      cout.flush();
    }

    unique = 1;
    for (j=0; j < N_PAIRS && unique == 1; j++){

      if (pair[k].a.index == pair[j].a.index or pair[k].a.index == pair[j].b.index or pair[k].b.index == pair[j].a.index or pair[k].b.index == pair[j].b.index ){

        if (k!=j){
          unique = 0;

        }
      }
    }
    if(unique == 1){
      //function rotates pair to make calculations easier
      calculation_pair = temp_halo(pair[k]);


      //writes the pair data to the save file
      savefile << pair[k].id << ", " << pair[k].a.index << ", " << pair[k].b.index << "," << calculation_pair.a.mvir << ", " << calculation_pair.b.mvir << ", " << pair[k].a.r200b << ", " << pair[k].b.r200b << ", " <<  pair[k].a.mainleaf << ", " <<  pair[k].b.mainleaf << ", " <<  pair[k].a.depthfirst << ", " <<  pair[k].b.depthfirst << ", " <<  calculation_pair.b.pos.z << ", " << calculation_pair.b.vel.z << ", " << calculation_pair.b.vel.y << endl;
    }
  }
  f_halo_data.close();

  cout << "100%                                                                \nComplete."<< endl;

//##################################################################

  return 0;
}
