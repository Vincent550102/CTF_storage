#/*___wenyan_module_恆常_start___*/
# encoding: UTF-8
require 'forwardable'
class Ctnr
  extend Forwardable
  attr_accessor :dict, :length, :it
  def initialize()
    @dict = {}
    @length = 0
    @it = -1
  end
  def push(*args)
    args.each do |arg|
      @dict[@length.to_s] = arg
      @length += 1
    end
  end
  def [](i)
    @dict[i.to_s]
  end
  def []=(i,x)
    @dict[i.to_s] = x
  end
  def slice(i)
    result = Ctnr.new;
    i.times {|index| result.push(self[index])}
    return result
  end
  def concat(other)
    other.length.times {|i| push(other[i]) }
    self
  end
  def values
    @dict.values
  end
  def to_s
    "[#{@dict.values.join(", ")}]"
  end
  def_delegators :values, :each
end
module Math
  def self.random(*args)
    rand(*args)
  end
  def self.floor(number)
    number.floor
  end
end
#####
大="輸入「助」以獲得更多幫助"
笆="/+9876543210zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
斯="k5aRmv=="
啟="5KTMx8XKxf=="
魠="kv=="
歷="5KSS"
託="幫助幫助幫助幫助幫助幫助"
師="先帝創業未半而中道崩殂今天下三分益州疲弊此誠危急存亡之秋也然侍衛之臣不懈於內忠誌之士忘身於外者蓋追先帝之殊遇欲報之於陛下也誠宜開張聖聽以光先帝遺德恢弘誌士之氣不宜妄自菲薄引喻失義以塞忠諫之路也宮中府中俱為一體陟罰臧否不宜異同若有作奸犯科及為忠善者宜付有司論其刑賞以昭陛下平明之理不宜偏私使內外異法也侍中侍郎郭攸之費禕董允等此皆良實誌慮忠純是以先帝簡拔以遺陛下愚以為宮中之事事無大小悉以谘之然後施行必能裨補闕漏有所廣益將軍嚮寵性行淑均曉暢軍事試用於昔日先帝稱之曰能是以衆議舉寵為督愚以為營中之事悉以谘之必能使行陣和睦優劣得所親賢臣遠小人此先漢所以興隆也親小人遠賢臣此後漢所以傾頹也先帝在時每與臣論此事未嘗不歎息痛恨於桓靈也侍中尚書長史參軍此悉貞良死節之臣願陛下親之信之則漢室之隆可計日而待也臣本佈衣躬耕於南陽苟全性命於亂世不求聞達於諸侯先帝不以臣卑鄙猥自枉屈三顧臣於草廬之中谘臣以當世之事由是感激遂許先帝以驅馳後值傾覆受任於敗軍之際奉命於危難之間爾來二十有一年矣先帝知臣謹慎故臨崩寄臣以大事也受命以來夙夜憂歎恐托付不效以傷先帝之明故五月渡瀘深入不毛今南方巳定兵甲已足當獎率三軍北碇中原庶竭駑鈍攘除奸兇興複漢室還于舊都此臣所以報先帝而忠陛下之職分也至於斟酌損益進盡忠言則攸之禕允之任也願陛下托臣以討賊興複之效不效則治臣之罪以告先帝之靈若無興德之言則責攸之禕允等之慢以彰其咎陛下亦宜自謀以谘諏善道察納雅言深追先帝遺詔臣不勝受恩感激今當遠離臨錶涕零不知所言"
秘旗="\x1b[38:5:181m獎\x1b[38:5:202m當\x1b[38:5:177m之\x1b[38:5:210m兇\x1b[38:5:191m深\x1b[38:5:170m定\x1b[38:5:189m忠\x1b[38:5:197m忠\x1b[38:5:192m複\x1b[38:5:226m除\x1b[38:5:177m率\x1b[38:5:226m月\x1b[38:5:191m月\x1b[38:5:170m都\x1b[38:5:177m三\x1b[38:5:178m還\x1b[38:5:177m三\x1b[38:5:209m先\x1b[38:5:188m而\x1b[38:5:197m忠\x1b[38:5:192m兇\x1b[38:5:198m故\x1b[38:5:192m複\x1b[38:5:226m巳\x1b[38:5:177m三\x1b[38:5:222m定\x1b[38:5:189m率\x1b[38:5:225m陛\x1b[38:5:194m軍\x1b[38:5:166m除\x1b[38:5:178m軍\x1b[38:5:186m忠\x1b[38:5:181m率\x1b[38:5:226m所\x1b[38:5:177m瀘\x1b[38:5:226m獎\x1b[38:5:181m獎\x1b[38:5:218m除\x1b[38:5:179m當\x1b[38:5:166m鈍\x1b[38:5:178m三\x1b[38:5:170m斟"
# 已': 2,'定': 2 

#/*___wenyan_module_恆常_end___*/
#/*___wenyan_module_鑿字秘術_start___*/
# encoding: UTF-8
require 'forwardable'
class Ctnr
  extend Forwardable
  attr_accessor :dict, :length, :it
  def initialize()
    @dict = {}
    @length = 0
    @it = -1
  end
  def push(*args)
    args.each do |arg|
      @dict[@length.to_s] = arg
      @length += 1
    end
  end
  def [](i)
    @dict[i.to_s]
  end
  def []=(i,x)
    @dict[i.to_s] = x
  end
  def slice(i)
    result = Ctnr.new;
    i.times {|index| result.push(self[index])}
    return result
  end
  def concat(other)
    other.length.times {|i| push(other[i]) }
    self
  end
  def values
    @dict.values
  end
  def to_s
    "[#{@dict.values.join(", ")}]"
  end
  def_delegators :values, :each
end
module Math
  def self.random(*args)
    rand(*args)
  end
  def self.floor(number)
    number.floor
  end
end
#####
正閱="data"
已閱="end"
def 始碼(字)
	_ans1=string.fromcharcode(字);	return _ans1
end

def 字址(字,址)
	_ans2=((target) => ((idx) => target.charcodeat(idx)))(字)(址);	return _ans2
end

def 始於(字,符)
	_ans3=((target) => ((label) => target.startswith(label)))(字)(符);	return _ans3
end

def 字子(字,址)
	_ans4=((target) => ((idx) => target.substring(idx)))(字)(址);	return _ans4
end

def 子字(字,始,末)
	_ans5=((target) => ((s) => ((e) => target.substring(s, e))))(字)(始)(末);	return _ans5
end


#/*___wenyan_module_鑿字秘術_end___*/
#/*___wenyan_module_交互秘術_start___*/
# encoding: UTF-8
require 'forwardable'
class Ctnr
  extend Forwardable
  attr_accessor :dict, :length, :it
  def initialize()
    @dict = {}
    @length = 0
    @it = -1
  end
  def push(*args)
    args.each do |arg|
      @dict[@length.to_s] = arg
      @length += 1
    end
  end
  def [](i)
    @dict[i.to_s]
  end
  def []=(i,x)
    @dict[i.to_s] = x
  end
  def slice(i)
    result = Ctnr.new;
    i.times {|index| result.push(self[index])}
    return result
  end
  def concat(other)
    other.length.times {|i| push(other[i]) }
    self
  end
  def values
    @dict.values
  end
  def to_s
    "[#{@dict.values.join(", ")}]"
  end
  def_delegators :values, :each
end
module Math
  def self.random(*args)
    rand(*args)
  end
  def self.floor(number)
    number.floor
  end
end
#####
正閱="data"
已閱="end"
_ans1=require("readline").createInterface(process.stdin, process.stdout);
讀行=_ans1;def 化言(甲)
	_ans2=甲.tostring();	return _ans2
end

def 發生(事)
	_ans3=((event) => process.stdin.emit(event))(事);end

def 監聽(事件,響應)
	_ans4=((event) => ((func) => process.stdin.on(event, func)))(事件)(響應);end

def 聽寫(事件,響應)
	_ans5=((event) => ((func) => 讀行.on(event, func)))(事件)(響應);end

def 閱止()
	_ans6=(() => process.stdin.end())();end

def 輸出(文)
	_ans7=((s) => process.stdout.write(s))(文);end


#/*___wenyan_module_交互秘術_end___*/
# encoding: UTF-8
require 'forwardable'
class Ctnr
  extend Forwardable
  attr_accessor :dict, :length, :it
  def initialize()
    @dict = {}
    @length = 0
    @it = -1
  end
  def push(*args)
    args.each do |arg|
      @dict[@length.to_s] = arg
      @length += 1
    end
  end
  def [](i)
    @dict[i.to_s]
  end
  def []=(i,x)
    @dict[i.to_s] = x
  end
  def slice(i)
    result = Ctnr.new;
    i.times {|index| result.push(self[index])}
    return result
  end
  def concat(other)
    other.length.times {|i| push(other[i]) }
    self
  end
  def values
    @dict.values
  end
  def to_s
    "[#{@dict.values.join(", ")}]"
  end
  def_delegators :values, :each
end
module Math
  def self.random(*args)
    rand(*args)
  end
  def self.floor(number)
    number.floor
  end
end
#####
輸出=交互秘術.輸出;聽寫=交互秘術.聽寫;始碼=鑿字秘術.始碼;字址=鑿字秘術.字址;子字=鑿字秘術.子字;始於=鑿字秘術.始於;字子=鑿字秘術.字子;啟=恆常.啟;歷=恆常.歷;託=恆常.託;師=恆常.師;大=恆常.大;笆=恆常.笆;斯=恆常.斯;魠=恆常.魠;秘旗=恆常.秘旗;def 獲取(對象,域)
	return 對象[域]

end

# "============"
def 營(日,鑫)
	_ans1=日%鑫;	_ans2=日-_ans1;
	戌卯=_ans2;	_ans3=戌卯/鑫;
	庚巳=_ans3;	return 庚巳
end

def 削(日,鑫)
	命=0
	恩=1
	while true do
		戊乙=false
		if 日>0
			戊乙=true
		end 
		午酉=false
		if 鑫>0
			午酉=true
		end 
		_ans4=戊乙&&午酉;
		酉癸=_ans4;		if 酉癸==0
			break
		end 
		_ans5=日%2;
		辛甲=_ans5;		甲二=false
		if 辛甲==1
			甲二=true
		end 
		_ans6=鑫%2;
		二辛=_ans6;		午庚=false
		if 二辛==1
			午庚=true
		end 
		_ans7=甲二&&午庚;
		巳己=_ans7;		if 巳己
			_ans8=命+恩;			命=_ans8
		end 
		_ans9=營(日)(2);		日=_ans9
		_ans10=營(鑫)(2);		鑫=_ans10
		_ans11=恩*2;		恩=_ans11
	end 
	return 命
end

def 斐(竺)
	呼=0
	while true do
_ans12=笆.length;		巳酉=false
		if 呼<undefined
			巳酉=true
		end 
		if 巳酉==0
			break
		end 
		_ans13=獲取(笆)(呼);
		乙丁=_ans13;		if 乙丁==竺
			return 呼
		end 
		_ans14=呼+1;		呼=_ans14
	end 
	return 0
end

def 天(食)
	返=Ctnr.new
	呼=0
	while true do
_ans15=食.length;		寅二=false
		if 呼<undefined
			寅二=true
		end 
		if 寅二==0
			break
		end 
		表=Ctnr.new
		_ans16=獲取(食)(呼);
		辰丁=_ans16;		_ans17=斐(辰丁);
		丙戊=_ans17;		_ans18=呼+1;
		丙甲=_ans18;		_ans19=獲取(食)(丙甲);
		丁申=_ans19;		_ans20=斐(丁申);
		午申=_ans20;		_ans21=呼+2;
		乙庚=_ans21;		_ans22=獲取(食)(乙庚);
		地戌=_ans22;		_ans23=斐(地戌);
		丁亥=_ans23;		_ans24=呼+3;
		二卯=_ans24;		_ans25=獲取(食)(二卯);
		寅酉=_ans25;		_ans26=斐(寅酉);
		支丙=_ans26;		表.push(丙戊,午申,丁亥,支丙)
_ans27=表[1-1];
		己辛=_ans27;		_ans28=己辛*4;
		酉支=_ans28;_ans29=表[2-1];
		乙酉=_ans29;		_ans30=營(乙酉)(16);		_ans31=酉支+_ans30;
		丁壬=_ans31;		返.push(丁壬)
_ans32=表[2-1];
		子甲=_ans32;		_ans33=削(子甲)(15);
		丁巳=_ans33;		_ans34=丁巳*16;
		壬己=_ans34;_ans35=表[3-1];
		辛辛=_ans35;		_ans36=營(辛辛)(4);		_ans37=壬己+_ans36;
		支己=_ans37;		返.push(支己)
_ans38=表[3-1];
		亥巳=_ans38;		_ans39=削(亥巳)(3);
		地丙=_ans39;		_ans40=地丙*64;
		申戌=_ans40;_ans41=表[4-1];
		乙卯=_ans41;		_ans42=削(乙卯)(63);		_ans43=申戌+_ans42;
		壬寅=_ans43;		返.push(壬寅)
		_ans44=呼+4;		呼=_ans44
	end 
	遣=""
	呼=0
	while true do
_ans45=返.length;		辛未=false
		if 呼<undefined
			辛未=true
		end 
		if 辛未==0
			break
		end 
		_ans46=獲取(返)(呼);
		戊丙=_ans46;		if 戊丙==0
			break
		end 
		_ans47=始碼(戊丙);		_ans48=遣+_ans47;		遣=_ans48
		_ans49=呼+1;		呼=_ans49
	end 
	return 遣
end

_ans50=子字(師)(463)(527);
桐=_ans50;_ans51=天(斯);
系=_ans51;_ans52=天(啟);
啟=_ans52;涅="> "
def 禱(食)
_ans53=食.length;
	連=_ans53;	_ans54=!連;
	未丑=_ans54;	if 未丑
		return ""
	end 
	紀元=""
	呼=0
	while true do
		申壬=false
		if 呼<連
			申壬=true
		end 
		if 申壬==0
			break
		end 
		_ans55=字址(食)(呼);		日=_ans55
		鑫=0
		谷=0
		_ans56=連-呼;
		己酉=_ans56;		if 己酉>=2
			_ans57=呼+1;
			支辛=_ans57;			_ans58=字址(食)(支辛);			鑫=_ans58
		end 
		_ans59=連-呼;
		地巳=_ans59;		if 地巳>2
			_ans60=呼+2;
			乙乙=_ans60;			_ans61=字址(食)(乙乙);			谷=_ans61
		end 
		_ans62=營(日)(4);
		丙癸=_ans62;		_ans63=削(日)(3);
		亥十=_ans63;		_ans64=亥十*16;
		乙己=_ans64;		_ans65=營(鑫)(16);		_ans66=乙己+_ans65;
		卯戌=_ans66;		_ans67=型(丙癸)(卯戌);		_ans68=紀元+_ans67;		紀元=_ans68
		_ans69=削(鑫)(15);
		戌戌=_ans69;		_ans70=戌戌*4;
		乙己七=_ans70;		_ans71=營(谷)(64);		_ans72=乙己七+_ans71;
		戌巳=_ans72;		_ans73=削(谷)(63);
		丁午=_ans73;		_ans74=型(戌巳)(丁午);		_ans75=紀元+_ans74;		紀元=_ans75
		_ans76=呼+3;		呼=_ans76
	end 
	_ans77=連%3;
	辰申=_ans77;	if 辰申==1
		_ans78=紀元+"等於";		紀元=_ans78
	end 
	return 紀元
end

_ans79=天(歷);
歷=_ans79;_ans80=天(魠);
魠=_ans80;def 型(和,宇)
	_ans81=165+和;	_ans82=啟+_ans81;
	巳支=_ans82;	_ans83=巳支+魠;
	申午=_ans83;	_ans84=獲取(桐)(宇);	_ans85=申午+_ans84;
	二酉=_ans85;	return 二酉
end

def 希依(祈)
	_ans86=禱(祈);	命=_ans86
	_ans87="結果"
	_ans88=命
	_ans89=歷
	p([_ans87, _ans88, _ans89].join)
	if 命==秘旗
		_ans90="正解"
		p([_ans90].join)
	end 
end

def 玲瓏()
	_ans91=託
	p([_ans91].join)
end

def 殼(入)
	_ans92=始於(入)("蛵煿 ");
	丁辰=_ans92;	if 丁辰
		_ans93=字子(入)(3);
		地辛=_ans93;		_ans94=希依(地辛);	else
		if 入=="助"
			_ans95=玲瓏();		else
			_ans96="指令「"+入;
			丙丁=_ans96;			_ans97=丙丁+"」不存在\n";
			辛午=_ans97;			_ans98=輸出(辛午);		end 
	end 
	_ans99=輸出(涅);end

def 殼始()
	_ans100=大
	p([_ans100].join)
	_ans101=輸出(涅);end

_ans102=殼始();_ans103=聽寫(系)(殼);