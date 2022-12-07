// Definitely not just a tree structure ;)

/**
 * 
 */
#[derive(Debug)]
pub struct Folder<'a> {
    pub parent: Option<&'a Folder<'a>>,
    pub files: Vec<i32>,
    pub folders: Vec<&'a Folder<'a>>,
}
