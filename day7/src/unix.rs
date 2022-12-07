// Definitely not just a tree structure ;)
mod unix {
    #[derive(Debug)]
    pub struct Folder<'a> {
        files: Vec<i32>,
        folders: Vec<&'a Folder<'a>>,
    }
    
    pub fn process_line() {
        
    } 
}
