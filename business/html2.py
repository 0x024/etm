from lxml import etree
import os,re

html=""<b>尊敬的张文先生：
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;您好！
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;您于2015年01月05日在中国铁路客户服务中心网站（<a href="http://www.12306.cn">www.12306.cn</a>)成功购买了1张车票，票款共计8.50元，订单号码E785904270。所购车票信息如下：


<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.张文,2015年01月07日14:32开,安阳—新乡,K817次列车,14车011号,硬座,票价8.50元。


<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了确保列车运行秩序和旅客人身安全，车站将在开车时间之前提前停止检票，请合理安排出行时间，提前到乘车站办理安检、验证并到指定场所
候车，以免耽误乘车。


<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size:19px;color:blue;"><em>温馨提示：</em></span>
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;（1）请牢记网站<a href="http://www.12306.cn">http://www.12306.cn</a>提供的订单号码E785904270，并妥善保管，以确保您的购票信息安全。
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;（2）选择车票快递服务的，请准备有效身份证件原件。您可在“已完成订单”-> “订单详情”-> “快递详情”中查看你的快递状态。当车票处于“待制票”状态时，用户可进行以下变更操作：
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1>取消车票快递服务：客户可单独选择取消车票快递服务，系统自动退还快递服务费。车票快递服务一经取消，同一订单无法再次提供车票快递服务。
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2>改签、退票及换取纸质车票：客户可自行办理车票的改签、退票、换取纸质车票等业务。变更后符合快递服务条件的车票将按照原约定继续提供快递服务；变更后整件不符合快递服务条件的车票将取消快递服务，同时系统自动退还快递服务费。
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当车票处于“已制票”、 “派件中”状态时，客户不能在网站办理取消车票快递服务及办理车票的改签、退票、换票等业务，如有特殊情况可联系快递（物流）企业客户代表。 
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;（3）根据铁路实名制购票、乘车有关要求，乘车人有效身份证件的姓名、号码需与在网站<a href="http://www.12306.cn">http://www.12306.cn</a>填写的内容（因姓名超长、有生僻字、繁体字等除外）完全一致方可办理换票和实名制验证；否则，不予换票，车站拒绝进站乘车，列车按无票处理。同时，网站<a href="http://www.12306.cn">http://www.12306.cn</a>对注册用户和常用联系人（乘车人）进行身份信息核验。如您的身份信息核验状态为“待核验”时，请携带购票时所使用的有效身份证件原件到车站售票窗口或者铁路客票代售点办理身份信息核验；为“未通过”（限二代居民身份证）、“请报验”时，请携带购票时所使用的有效身份证件原件到车站售票窗口办理。如果您拟委托他人办理时，请同时携带代办人和您的有效身份证件原件。办理时，如果您的二代居民身份证不能通过二代证自动识读设备自动读取的，不能办理，请到发证机关换证后再予办理。核验通过的，可以在车站售票窗口对已购车票办理换票、改签、退票；未通过的，在车站售票窗口对已购车票只能办理退票，不能办理换票、改签。您也可在网站<a href="http://www.12306.cn">http://www.12306.cn</a>对已购车票正常办理退票。
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;（4）使用乘车人本人的二代居民身份证在网站<a href="http://www.12306.cn">http://www.12306.cn</a>购票，且乘车站和下车站均具备二代居民身份证自动识读检票条件的，可以通过自动检票机（闸机）自动识读二代居民身份证的方式办理进、出站检票手续，无需提前换取纸质车票；因此乘车至到站后，需报销凭证时，请不晚于自乘车日期之日起31日，凭购票时所使用的二代居民身份证原件到车站售票窗口索取，逾期不予办理。
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;（5）其他情形均需换取纸质车票后进站乘车。自网站<a href="http://www.12306.cn">http://www.12306.cn</a>购票交易成功之时起，您即可到中国铁路总公司所属铁路运输企业辖下任何一个铁路客票代售点、办理客运售票业务的车站售票窗口或自动售（取）机换取纸质车票。如您拟于乘车前到乘车站换票，请合理安排出行时间，以避免因窗口排队人数多、来不及换票而耽误乘车。在自动售（取）票机，只能使用二代居民身份证原件，且姓名、身份证号码与在网站<a href="http://www.12306.cn">http://www.12306.cn</a>填写的完全一致，方可换票。学生票、残疾军人（伤残人民警察）票需凭购票时所使用的有效身份证件和附有学生火车票优惠卡的学生证、“中华人民共和国残疾军人证”、“中华人民共和国伤残人民警察证”（均为原件），并符合规定条件。换票时，按规定核收异地售票手续费或铁路客票销售服务费。换票后，请妥善保管纸质车票，保持票面信息清晰、可识读，以便您顺利乘车。请注意妥善保护票面身份信息。 
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;（6）如果您换票后丢失车票时，请不晚于票面乘车站停止检票时间前20分钟到车站售票窗口办理挂失补办。办理时，需提供购票时所使用的乘车人有效身份证件原件、原车票乘车日期和购票地车站名称等，经车站确认无误后，需按原车票车次、席位、票价重新购买一张新车票。您持新车票乘车时，请向列车工作人员声明；到站前列车长经确认该席位使用正常的，将开具客运记录交给您；请您在到站后24小时内，凭客运记录、新车票和购票时所使用的有效身份证件原件，至到站退票窗口办理新车票退票。办理时，车站按规定核收补票的手续费。如您超过规定时间或者原车票已经退票、挂失补办的，不予办理挂失补办。原车票已经改签的按改签后的车票办理挂失补办。
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;（7）如果您改变行程或取消旅行，没有换取纸质车票且不晚于开车前2小时的，可登录网站<a href="http://www.12306.cn">http://www.12306.cn</a>，也可到中国铁路总公司所属铁路运输企业辖下任何一个办理客运售票业务的车站售票窗口办理改签或者退票；已经换取纸质车票或者开车时间前2小时之内的，只能在车站售票窗口办理。开车前48小时（不含）以上，可改签预售期内的其他列车；开车前48小时以内，可改签开车前的其他列车，也可改签开车后至票面日期当日24:00之间的其他列车，不办理票面日期次日及以后的改签；开车之后，旅客仍可改签当日其他列车，但只能在票面发站办理改签。在车站售票窗口办理时，请携带二代居民身份证原件；如果使用护照、港澳居民来往内地通行证、台湾居民来往大陆通行证购票或者所使用的二代居民身份证不能识读的，请携带该有效身份证件原件和订单号码E785904270。改签只能办理一次，且不能改变原车票的乘车站和到站。改签时，由于新、原车票可能有票价差额，如果新票票价高于原票时，需使用银行卡支付新票全额票款，原票款将在规定时间内退回至购票时所使用的网上支付帐户，因此，请携带银行卡（可以是购票时所使用的银行卡，也可以是其他银行卡，但余额应不小于新票全额票款）。
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;（8）在车站售票处（厅）办理换票、改签、退票、挂失补办、身份信息核验、索取报销凭证时，请注意车站公告或售票窗口标识。
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;（9）未尽事项，请关注网站<a href="http://www.12306.cn">http://www.12306.cn</a>或车站公告。


<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;感谢您使用中国铁路客户服务中心网站<a href="http://www.12306.cn">http://www.12306.cn</a>！ 本邮件由系统自动发出，请勿回复。
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;祝您旅途愉快！

<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;中国铁路客户服务中心
<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2015年01月05日<br/>
</b>""
content.replace('&nbsp;','')
content.replace('（<a href="http://www.12306.cn">www.12306.cn</a>)','')
html =etree.html(content)
cotents=html.xpath('text()')
#print (br_tags)
line_chick=cotents[2].replace("\n",'')
line_detail=cotents[3].replace("\n",'')
print (line_detail)