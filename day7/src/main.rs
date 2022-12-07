use std::fs::File;
use std::io::{prelude::*, BufReader};
use std::path::Path;
mod unix;

fn main() {
    // Create path to input file
    let path = Path::new("example");
    let display = path.display();

    // Open the path in read-only mode
    let file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why),
        Ok(file) => file,
    };

    let reader = BufReader::new(file);
    // Root folder/head of the tree
    let mut root = unix::Folder{parent: None, files: Vec::new(), folders: Vec::new()};
    let mut current_dir = &root;
    // Read the file line by line
    for line in reader.lines() {
        // read in the line
        let line = match line {
            Err(why) => panic!("couldn't read line {}: {}", display, why),
            Ok(line) => line,
        };

        let line = line.trim();
        let line_arr: Vec<&str> = line.split_whitespace().collect();
        println!("{:?}", line_arr);
    }
}
