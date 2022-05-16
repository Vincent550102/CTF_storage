var 交互秘術 = new function () {
    var 正閱 = this.正閱 = "data";
    var 已閱 = this.已閱 = "end";
    const _ans1 = require("readline").createInterface(process.stdin, process.stdout);
    var 讀行 = _ans1;
    var 化言 = this.化言 = _ => { };
    化言 = this.化言 = 甲 => {
        const _ans2 = 甲.toString();
        return _ans2;
    };
    var 發生 = this.發生 = _ => { };
    發生 = this.發生 = 事 => {
        const _ans3 = ((event) => process.stdin.emit(event))(事);
    };
    var 監聽 = this.監聽 = _ => { };
    監聽 = this.監聽 = 事件 => 響應 => {
        const _ans4 = ((event) => ((func) => process.stdin.on(event, func)))(事件)(響應);
    };
    var 聽寫 = this.聽寫 = _ => { };
    聽寫 = this.聽寫 = 事件 => 響應 => {
        const _ans5 = ((event) => ((func) => 讀行.on(event, func)))(事件)(響應);
    };
    var 閱止 = this.閱止 = _ => { };
    閱止 = this.閱止 = () => {
        const _ans6 = (() => process.stdin.end())();
    };
    var 輸出 = this.輸出 = _ => { };
    輸出 = this.輸出 = 文 => {
        const _ans7 = ((s) => process.stdout.write(s))(文);
    };
};
