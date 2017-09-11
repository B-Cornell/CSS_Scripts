#include "pair_search_functions.h"

using namespace std;

int main(int argc, char *argv[]){

 

  vector<pair_t> pair(N_PAIRS); // This is our giant vector where we store all the halo pairs in the heap

  pair_t calculation_pair;
  string halo_a_str, halo_b_str, pair_id_str, temp;
  int i,j,k, unique = 1;
  string save_directory = "/home/DSS_Scripts/";


  cout << "------------------------------------------" << endl;

  ifstream f_halo_data;
  f_halo_data.open("reduced_cosmo_pairs_5mpc.txt");

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

      if (i%100 == 0){
        cout << "Processing... " <<  double(i)/double(N_PAIRS)*100 << "%\r";
        cout.flush();
      }
    }
    cout << "Processing... 100%          \nComplete."<< endl;
  }

  else {
    cout << "Error: Cannot open file." << endl;
    return 1;
  }


  
  std::ofstream savefile;
  savefile.open("data.csv");
 

  // Iterates over all the pairs
  for(k=0; k < N_PAIRS; k++){
  
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
        savefile << pair[k].id << ", " << pair[k].a.index << ", " << pair[k].b.index << ", " << calculation_pair.a.mvir << ", " << calculation_pair.b.mvir << ", " << pair[k].a.r200b << ", " << pair[k].b.r200b << ", " << calculation_pair.b.pos.z << ", " << calculation_pair.b.vel.z << ", " << calculation_pair.b.vel.y << endl;
    }
  }
         

  savefile.close();

  cout << "100%                                                                \nComplete."<< endl;

//##################################################################

  return 0;
}
