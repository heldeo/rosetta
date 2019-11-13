
use std::fmt;
use std::env;
//Implementing type debugging/cout for TuplesFromUserInput



impl fmt::Display for TuplesFromUserInput{

    fn fmt(&self, f:    &mut fmt::Formatter)-> fmt::Result{

        write!(f,"{:?} ",self.string_tuples )

        }

    }
struct TuplesFromUserInput{
    string_tuples: Option<Vec<String>>,
}

impl  TuplesFromUserInput{
    
    fn make_without_first_arg(self: &mut Self,raw_input_vector: &mut Vec<String>){
    raw_input_vector.remove(0); //remove first element [debug . .. ] string
    self.string_tuples = Some(raw_input_vector.clone());
    }
}
fn main() {

    let mut args: Vec<String> = env::args().collect();
    let mut  processed_tuples =  TuplesFromUserInput{string_tuples: None,};
    processed_tuples.make_without_first_arg(&mut args);
    println!("Args!{:?}",args);
    
}
