from airtest.core.api import *
from airtest.report.report import simple_report
import sys
sys.path.append(r"D:\PiaoFang_Test\core_gameplay")
from common import check_image1,check_image2,check_zhujiemian,chonglian,click_template_if_exists

dev = connect_device("Android:///Q2NVB21806000861")
os.path.dirname(os.path.abspath(__file__))

log_dir = r"D:\PiaoFang_Test\core_gameplay\huodong_log"
os.makedirs(log_dir, exist_ok=True)  # 确保目录存在
set_logdir(log_dir)  # 强制指定日志位置


check_image1(r"tpl1750143420095.png")
#检查超偶奖励
chaoou=click_template_if_exists(r"tpl1750143981388.png")
sleep(5)
if chaoou:
    if exists(Template(r"tpl1750144508786.png")):
        check_image2(r"tpl1750145054142.png")
        sleep(3)
        touch(Template(r"tpl1750145108346.png", record_pos=(0.017, -0.253), resolution=(1080, 2400)))
        sleep(3)
        check_image2(r"tpl1750145139525.png")
        sleep(3)
        touch(Template(r"tpl1750145183740.png", record_pos=(0.329, -0.259), resolution=(1080, 2400)))
        sleep(3)
        check_image2(r"tpl1750145379356.png")
        sleep(3)
        swipe((545,1965),(545,786))
        sleep(3)
        swipe((545,1965),(545,786))
        sleep(5)
        check_image2(r"tpl1750146083478.png")
        touch(Template(r"tpl1750146482508.png", record_pos=(-0.456, -0.867), resolution=(1080, 2400)))

check_zhujiemian()
touch(Template(r"tpl1750150481224.png", record_pos=(0.328, -0.592), resolution=(1080, 2400)))
sleep(5)
if exists(Template(r"tpl1750150567564.png")):
    touch(Template(r"tpl1750150641232.png", record_pos=(-0.371, 0.706), resolution=(1080, 2400)))
    sleep(5)
    #练习生礼包奖励检查
    if exists(Template(r"tpl1750150752685.png")):
        check_image2(r"tpl1750150894942.png")
        sleep(5)
        swipe((663,1788),(663,911))
        sleep(3)
        check_image2(r"tpl1750151080867.png")
        sleep(3)
        touch(Template(r"tpl1750151129359.png", record_pos=(-0.432, -0.601), resolution=(1080, 2400)))
    else:
        touch(Template(r"tpl1750151129359.png", record_pos=(-0.432, -0.601), resolution=(1080, 2400)))
check_zhujiemian()
sleep(3)
touch(Template(r"tpl1750152458184.png", record_pos=(0.328, -0.697), resolution=(1080, 2400)))
sleep(3)
if exists(Template(r"tpl1750153163628.png", rgb=True)):
    touch(Template(r"tpl1750153196217.png", rgb=True, record_pos=(-0.145, -0.497), resolution=(1080, 2400)))
    check_image2(r"tpl1750154067296.png")
    sleep(5)
else:
    swipe((926,663),(83,663))
    sleep(5)
    if exists(Template(r"tpl1750153196217.png", rgb=True)):
        touch(Template(r"tpl1750153196217.png", rgb=True, record_pos=(-0.145, -0.497), resolution=(1080, 2400)))
        sleep(5)
        check_image2(r"tpl1750231129006.png")
check_zhujiemian()

yingyelianmeng=click_template_if_exists(r"tpl1750232051691.png")
if yingyelianmeng:
    sleep(5)
    touch(Template(r"tpl1750232356251.png", record_pos=(0.409, 0.976), resolution=(1080, 2400)))
    check_image2(r"tpl1750232382887.png")
    touch(Template(r"tpl1750232419891.png", record_pos=(-0.431, -0.858), resolution=(1080, 2400)))
    sleep(5)
    touch(Template(r"tpl1750232449217.png", record_pos=(-0.454, -0.863), resolution=(1080, 2400)))
check_zhujiemian()

touch(Template(r"tpl1750152458184.png", record_pos=(0.328, -0.697), resolution=(1080, 2400)))
sleep(3)
if exists(Template(r"tpl1750233150889.png")):
    
    touch(Template(r"tpl1750233150889.png", rgb=True, record_pos=(0.256, -0.488), resolution=(1080, 2400)))
    sleep(3)
    touch(Template(r"tpl1750233467185.png", record_pos=(0.0, 0.654), resolution=(1080, 2400)))
    sleep(5)
    touch(Template(r"tpl1750233509734.png", record_pos=(0.428, 1.008), resolution=(1080, 2400)))
    check_image2(r"tpl1750233528784.png")
    touch(Template(r"tpl1750233582002.png", record_pos=(-0.45, -0.86), resolution=(1080, 2400)))
    sleep(3)
    touch(Template(r"tpl1750233604631.png", record_pos=(-0.094, 1.006), resolution=(1080, 2400)))
    sleep(5)
    check_image2(r"tpl1750233802053.png")
    sleep(3)
    touch(Template(r"tpl1750233985761.png", record_pos=(-0.431, -0.856), resolution=(1080, 2400)))
    sleep(3)
    touch(Template(r"tpl1750234283530.png", record_pos=(-0.434, -0.655), resolution=(1080, 2400)))
    sleep(3)
    touch(Template(r"tpl1750234283530.png", record_pos=(-0.434, -0.655), resolution=(1080, 2400)))
    check_zhujiemian()
    
else:
    swipe((926,663),(83,663))
    sleep(5)
    touch(Template(r"tpl1750233150889.png", rgb=True, record_pos=(0.256, -0.488), resolution=(1080, 2400)))
    sleep(3)
    touch(Template(r"tpl1750233467185.png", record_pos=(0.0, 0.654), resolution=(1080, 2400)))
    sleep(5)
    touch(Template(r"tpl1750233509734.png", record_pos=(0.428, 1.008), resolution=(1080, 2400)))
    check_image2(r"tpl1750233528784.png")
    touch(Template(r"tpl1750233582002.png", record_pos=(-0.45, -0.86), resolution=(1080, 2400)))
    sleep(3)
    touch(Template(r"tpl1750233604631.png", record_pos=(-0.094, 1.006), resolution=(1080, 2400)))
    sleep(5)
    check_image2(r"tpl1750233802053.png")
    sleep(3)
    touch(Template(r"tpl1750233985761.png", record_pos=(-0.431, -0.856), resolution=(1080, 2400)))
    sleep(3)
    touch(Template(r"tpl1750234283530.png", record_pos=(-0.434, -0.655), resolution=(1080, 2400)))
    sleep(3)
    touch(Template(r"tpl1750234283530.png", record_pos=(-0.434, -0.655), resolution=(1080, 2400)))
    check_zhujiemian()


touch(Template(r"tpl1750152458184.png", record_pos=(0.328, -0.697), resolution=(1080, 2400)))
sleep(3)
if exists(Template(r"tpl1750235061235.png")):
    touch(Template(r"tpl1750235061235.png", rgb=True, record_pos=(0.141, -0.484), resolution=(1080, 2400)))
    sleep(5)
    if exists(Template(r"tpl1750235761329.png")):
        
        sleep(5)
        touch(Template(r"tpl1750235241615.png", record_pos=(-0.003, 0.664), resolution=(1080, 2400)))
        sleep(5)
        touch(Template(r"tpl1750235262604.png", record_pos=(-0.371, 0.024), resolution=(1080, 2400)))
        sleep(5)
        check_image2(r"tpl1750235298993.png")
        touch(Template(r"tpl1750236505921.png", record_pos=(-0.436, -0.74), resolution=(1080, 2400)))
        sleep(3)
        touch(Template(r"tpl1750236531600.png", record_pos=(-0.444, -0.854), resolution=(1080, 2400)))
        sleep(3)
        touch(Template(r"tpl1750236553176.png", record_pos=(-0.432, -0.653), resolution=(1080, 2400)))

        check_zhujiemian()

else:
        swipe((926,663),(83,663))
        sleep(5)
        touch(Template(r"tpl1750235061235.png", rgb=True, record_pos=(0.141, -0.484), resolution=(1080, 2400)))
        sleep(5)
        #冒险片
        if exists(Template(r"tpl1750235761329.png")):

            sleep(5)
            touch(Template(r"tpl1750235241615.png", record_pos=(-0.003, 0.664), resolution=(1080, 2400)))
            sleep(5)
            touch(Template(r"tpl1750235262604.png", record_pos=(-0.371, 0.024), resolution=(1080, 2400)))
            sleep(5)
            check_image2(r"tpl1750235298993.png")
            touch(Template(r"tpl1750236505921.png", record_pos=(-0.436, -0.74), resolution=(1080, 2400)))
            sleep(3)
            touch(Template(r"tpl1750236531600.png", record_pos=(-0.444, -0.854), resolution=(1080, 2400)))
            sleep(3)
            touch(Template(r"tpl1750236553176.png", record_pos=(-0.432, -0.653), resolution=(1080, 2400)))          
            check_zhujiemian()


    
    
    
    
    
    
    
       

    
    
    


        
        
        
        
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

simple_report(
    filepath=__file__,
    logpath=log_dir,
    output=os.path.join(log_dir, "report.html")
)
