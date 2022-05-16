var 鑿字秘術 = new function () {
    var 正閱 = this.正閱 = "data";
    var 已閱 = this.已閱 = "end";
    var 始碼 = this.始碼 = _ => { };
    始碼 = this.始碼 = 字 => {
        const _ans1 = String.fromCharCode(字);
        return _ans1;
    };
    var 字址 = this.字址 = _ => { };
    字址 = this.字址 = 字 => 址 => {
        const _ans2 = ((target) => ((idx) => target.charCodeAt(idx)))(字)(址);
        return _ans2;
    };
    var 始於 = this.始於 = _ => { };
    始於 = this.始於 = 字 => 符 => {
        const _ans3 = ((target) => ((label) => target.startsWith(label)))(字)(符);
        return _ans3;
    };
    var 字子 = this.字子 = _ => { };
    字子 = this.字子 = 字 => 址 => {
        const _ans4 = ((target) => ((idx) => target.substring(idx)))(字)(址);
        return _ans4;
    };
    var 子字 = this.子字 = _ => { };
    子字 = this.子字 = 字 => 始 => 末 => {
        const _ans5 = ((target) => ((s) => ((e) => target.substring(s, e))))(字)(始)(末);
        return _ans5;
    };
};
