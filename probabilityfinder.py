
  for( i = 0; i < 101; i++){
    angleprob[i] = 0.0;
    }

  // Iterates over all the pairs
  for(k=0; k < N_PAIRS; k++){
    
    // Print progress in percentage
    if (k%1000 == 0){
      cout << "Searching for matching pairs... " << double(k)/double(N_PAIRS)*100 << "%    \r";
      cout.flush();
    }

    // Integrating over the sphere
    // The difference between steps in theta are the same as steps in phi
    sph.theta = 0.;
    total_divisor_points = 0.;
    
    // Mass check
    if( ( ((pair[k].a.mvir > b_mass_a.low) && (pair[k].a.mvir <  b_mass_a.up))    &&
          ((pair[k].b.mvir > b_mass_b.low) && (pair[k].b.mvir <  b_mass_b.up)) )  ||
        ( ((pair[k].a.mvir > b_mass_b.low) && (pair[k].a.mvir <  b_mass_b.up))    &&
          ((pair[k].b.mvir > b_mass_a.low) && (pair[k].b.mvir <  b_mass_a.up)) )  ){
    pair_count++;
    
    //function rotates pair to make calculations easier
    calculation_pair = temp_halo(pair[k]);
      
    //add in the if statement to filter out all inbound pairs
    //if (calculation_pair.b.pos.z > 0){ 
      
      
      //find the velocity directions to see if it is inbound or outbound
      if (calculation_pair.b.vel.z < 0.0){
        z_vel = -calculation_pair.b.vel.z;
       
      }
      else {
        z_vel = calculation_pair.b.vel.z;
    
        }
      if (calculation_pair.b.vel.y < 0.0){
        y_vel = -calculation_pair.b.vel.y;
      }
      else {
        y_vel = calculation_pair.b.vel.y;

      }
      rel_vel_angle = atan(y_vel/z_vel) * (180 / PI);

      
    
     
    
    //writes the pair data to the save file
      savefile << pair[k].id << ", " << pair[k].a.index << ", " << pair[k].b.index << ", " << calculation_pair.a.mvir << ", " << calculation_pair.b.mvir << ", " << calculation_pair.b.pos.z << ", " << calculation_pair.b.vel.z << ", " << calculation_pair.b.vel.y << ", " << rel_vel_angle<< ", ";
    
    //starts iterating through the possible viewing angles
    for(i = 0; sph.theta <= double(PI); i++){
      sph.theta = sph.theta + (double(PI)/double(ANGULAR_RES)); // Range for theta is 0 to pi. 
      
      //divisor is the number of points that should go around each viewing angle. This way there are a near even distribution of points we view from 
      divisor = (ANGULAR_RES) * sin(sph.theta);
      total_divisor_points += divisor;
      points = int(divisor);
 
      sph.phi = 0.0;
      angleprobcounter = 0.0;
    
      for( j = 0; sph.phi < double(2*PI) and points>0; j++){
        sph.phi = sph.phi + (double(PI))/points; // Range for phi is 0 to 2pi and the number of points are detirmined above
   
        
        //The math for this section is made easier by the rotation done by the temphalo() function
        obs.x = sin(sph.theta)*cos(sph.phi);
        obs.y = sin(sph.theta)*sin(sph.phi);
        obs.z = cos(sph.theta);
        v_y = calculation_pair.b.vel.y;
        v_z = calculation_pair.b.vel.z;

        obsvel = obs.y*v_y+obs.z*v_z;// Calculate observed velocity
        if(obsvel < 0){obsvel = -obsvel;} //Should always be positive. 
        
        obssep = calculation_pair.b.pos.z*sin(sph.theta); // Calculate observed separation
        if(obssep < 0){obssep = -obssep;}

        //Calculate all of the probabilities

        mass_a_a_prob = probability("gaussian", b_mass_a.up - ((b_mass_a.up - b_mass_a.low)/2.), ((b_mass_a.up - b_mass_a.low)/4.), calculation_pair.a.mvir);//probability that the mass of the first halo in the pair matches the first halo in the musketball

	    mass_a_b_prob = probability("gaussian", b_mass_a.up - ((b_mass_a.up - b_mass_a.low)/2.), ((b_mass_a.up - b_mass_a.low)/4.), calculation_pair.b.mvir);//probability that the mass of the first halo in the pair matches the second halo in the musketball
	
	    mass_b_a_prob = probability("gaussian", b_mass_b.up - ((b_mass_b.up - b_mass_b.low)/2.), ((b_mass_b.up - b_mass_b.low)/4.), calculation_pair.a.mvir);//probability that the mass of the second halo in the pair matches the first halo in the musketball

	    mass_b_b_prob = probability("gaussian", b_mass_b.up - ((b_mass_b.up - b_mass_b.low)/2.), ((b_mass_b.up - b_mass_b.low)/4.), calculation_pair.b.mvir);//probability that the mass of the second halo in the pair matches the second halo in the musketball

        vel_prob = probability("gaussian", b_vel.up - ((b_vel.up - b_vel.low)/2.), ((b_vel.up - b_vel.low)/4.), obsvel);

	    sep_prob = probability("gaussian", b_sep.up - ((b_sep.up - b_sep.low)/2.), ((b_sep.up - b_sep.low)), obssep);
	
	    total_prob = (mass_a_a_prob*mass_b_b_prob+mass_a_b_prob*mass_b_a_prob)*vel_prob*sep_prob;
        
        // Tally to keep track of the probability added together from all viewing angles
        area_counter += double(total_prob);
        angleprob[i] += double(total_prob);
	    
        }
      }
    
    //now that we have gone through all viewing angles, put in the total probability
    
    calculation_pair.prob = area_counter;
    pair[k].prob = area_counter; // Total probability across all viewing angles
    area_counter = 0;
    savefile << calculation_pair.prob << endl;

          
    //Print pair attributes to the terminal screen
    //Prints both original and rotated attributes
    if (VERBOSE == true) {
      cout << pair[k].id << endl;
      print_halo(pair[k].a);
      print_halo(pair[k].b);
      print_halo(calculation_pair.a);
      print_halo(calculation_pair.b);
      cout << "probability: " << pair[k].prob << endl;
      cout << "relative velocity angle: " << rel_vel_angle << endl;
      cout << "------------------------------------------" << endl;
    }
       
//}//This is the bracket for the outbound filter

    } 
  }
         

  savefile.close();

  cout << "100%                                                                \nComplete."<< endl;

//##################################################################

  cout << endl << "Total Pairs: " << pair_count << endl << endl;
  cout << "(id)                  pair_id" << endl;
  cout << "(halo a attributes)   aindex ax ay az avx avy avz amvir ar200b" << endl;
  cout << "(halo b attributes)   bindex bx by bz bvx bvy bvz bmvir br200b" << endl;
  cout << endl << endl << "Angle Probability Histogram" << endl;
  
  for( i = 0; i < 101; i++){
    cout << angleprob[i] << ", ";
    }
  
  return 0;
}
