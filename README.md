#  **D.N.A** 

####  **介绍** 

1.  全称：安卓一般固件解包打包助手【 **Droid Normal Assistant** 】 简称： **D.N.A** 

     **如需在WIN10系统中（无需WSL子系统）对安卓11及动态分区ROM进行解包打包工具请戳这里：** [ **R.N.A** ](https://gitee.com/sharpeter/rna)

2.  支持常见格式【 _*.zip, *.br, *.dat, *.dat.1~20, ext4/2 *.img, payload.bin, *.win000-004_ 】,只认后缀，任意名称！

3.  支持安卓5.0+解包，支持安卓11 vendor.img 解包
    - 测试包Mi10Pro：[ _miui_CMI_20.11.19_a7ff2a5b4e_11.0.zip_ ](https://hugeota.d.miui.com/20.11.19/miui_CMI_20.11.19_a7ff2a5b4e_11.0.zip)

4.  支持安卓 [5.0+]  **【非动态分区、动态分区】** 打包，_由于没有动态机子，未进行刷入测试_    ----2020.12.20
    - 安卓 [5.0~8.1] 使用[ _make_ext4fs_ ]打包img !!!
    - 安卓 [9.0+] 使用[ _mke2fs + e2fsdroid_ ]打包img !!!
    - 测试包Mi10Pro：[ _miui_CMI_20.12.10_a0bb9661ec_11.0.zip_ ](https://hugeota.d.miui.com/20.12.10/miui_CMI_20.12.10_a0bb9661ec_11.0.zip)   ----2020.12.20

5.  支持合并分段*.dat.*，最大支持20个(1～20 看了几个vivo rom，通常为15个分段文件，多了影响解包速度)
    - 测试包vivo Y9s：[ _PD1945_A_1.10.7-update-full_1589940104.zip_ ](http://sysupwrdl.vivo.com.cn/upgrade/official/officialFiles/PD1945_A_1.10.7-update-full_1589940104.zip)   ----2020.11.22

6.  支持分解payload.bin，解开bin后自动查找所有ext2/4镜像再次进行分解，一步到位 !!!
    - 测试包OnePlus8Pro：[ _OnePlus8ProHydrogen_15.Y.14_OTA_0140_all_2010200027_1bc1714063af44ff.zip_ ](https://download.h2os.com/OnePlus8Pro/OBT/OnePlus8ProHydrogen_15.Y.14_OTA_0140_all_2010200027_1bc1714063af44ff.zip)   ----2020.11.22

7.  支持分解TWRP备份文件（data除外），最大支持4个( _*.win000~004_ )   ----2020.11.24

8.  电脑Linux版公测      ----2020.11.30

9.  加入插件功能，插件在工具中的相对路径：DNA/Insides/Errors/submodules文件夹   公测      ----2020.12.21

10.  加入AIK(Android-Image-Kitchen)分解合成[boot|exaid|recovery/etc].img, 需要java支持，已安装过的重新执行第6条教程    公测      ----2021.01.09

11.  支持分解部分super.img(不支持动态AB双系统)，最新小米11super.img测试不支持    公测      ----2021.01.09

12.  修复部分动态分区size识别不准确问题！      ----2021.01.09

13.  修复使用[ _make_ext4fs_ ]打包错误问题!      ----2021.01.21

14.  打包过程加入静默模式(不询问，自动打包工程目录中所有可打包内容)      ----2021.01.21


####  **软件架构  同时支持** 

1. 手机 Termux Proot Ubuntu 20.04 Arm64[aarch64]

2. 电脑 Win10 Wsl2 Ubuntu 20.04 x86_64[x64]  WSL2效率较低，不推荐，除非你电脑配置很高！

3. 虚拟机或实体机 Ubuntu 20.04 x86_64[x64]  推荐！！！


####  **安装教程【PC版教程从第6条开始】以下每一行均为一条完整命令** 

1.  手机安装原版[Termux.apk](https://f-droid.org/repo/com.termux_103.apk)  运行Termux 获取存储权限
    - `termux-setup-storage`

2.  下载git、tar、proot【复制下面命令，在Termux中输入，回车】
    - `pkg install git tar proot -y`

3.  下载ubuntu.tar.xz及安装脚本【复制下面命令，在Termux中输入，回车】    ---20201215 优先使用gitee，代替tsinghua镜像源，解决下载慢、出错等问题
    - `git clone https://gitee.com/sharpeter/proot-ubuntu`

4.  执行【复制下面命令，在Termux中输入，回车】
    - `bash proot-ubuntu/install_ubuntu.sh`
    - 【 **注意** 】等待下载、解压完成

5.  执行启动ubuntu 20.04【复制下面命令，在Termux中输入，回车】
    - `ubuntu`
    - 【 **注意** 】  很多人说这里输进去没反应，注意看  ~ 变成 root@localhost 就说明 ubuntu 已经启动了 ，如果报错了就 【 `rm -rf ubnutu` 】 再从第3步开始！！！

6.  执行第5条后进入ubuntu系统   【 **PC版教程从此开始，手机端继续往下** 】    【复制下面命令，终端中执行】
    - `sudo apt update && sudo apt upgrade -y`        【 _必须执行_ 】
    - `sudo apt install git cpio aria2 brotli android-sdk-libsparse-utils openjdk-14-jdk -y`     【 _必须执行，使用新版本前建议重新安装一次_ 】

    - ~`sudo apt install p7zip-full zip unzip gawk sed curl wget -y`~        [可选，非必需]

7.  下载此工具【复制下面命令，终端中执行】
    - `git clone https://gitee.com/sharpeter/DNA.git`      【 **开放下载，所有可用功能完全免费** 】

8.  下载完成后执行【复制下面命令，终端中执行】
    - `cd DNA && python3 run.py`

9.  至此你已启动此工具，教程结束 !
    - 1.  今后每次启动只需打开Termux 输入【 `ubuntu` 】就可直接启动工具（工具存在时）
    - 2.  如果你想打开Termux就直接启动工具： 在Termux(不是在proot ubuntu中，建议重启termux再执行)中执行【  _`echo -e "if [ -d ubuntu ] && [ $(command -v ubuntu) ]; then\n\tubuntu\nfi" >> .bashrc`_  】
           然后重新启动Termux就可以直接启动工具（工具存在时）


####  **使用说明** 

1.  Termux内所有操作尽量【 **不要使用系统root功能** 】， PC端需要root权限(sudo) 且最好不要在【root用户登录状态下】运行此工具，以免打包后刷入手机出现权限问题 ！

2.  工具每次启动都要联网进行版本检测，所以会有点慢；如果经常使用，切记不要退出工具

3.   **关于手机解压zip** 
    - 请将zip文件放置在【 **内置存储 /sdcard/Download** 】工具会自动查找，如果没找到就放在工具目录下

4.  手机端termux proot ubuntu下工具目录： 【**/data/data/com.termux/files/home/ubuntu/root/DNA** 】

5.  **请勿删除【工程目录/configs文件夹】，打包时所需的文件信息都在此处，若你想修改打包img大小，可以打开 【工程目录/configs/*_size.txt】把里面数值改成你想要的大小，该数值必须是字节大小**，动态分区打包超出大小可以同时修改【工程目录/configs/*_size.txt】和【dynamic_partitions_op_list】 中例如【resize vendor ~2016763904~】 ，因为我没有动态分区的机子，不保证打包后能正常开机！

6.  由于手机性能、proot效率以及工具工作方式( **比如每次打包img前都要自动比对获取新增文件的fs_config，不会立刻询问是否打包** )等原因，工具会出现像是卡住不动，不必担心，保持耐心，等待片刻即可

7.  删除文件尽量在【Termux或proot ubuntu】执行 【rm -rf 文件、文件夹】 【 **不要使用系统root功能** 】

8.   **不要放在含有中文名文件夹下运行，不要选择带有空格的文件进行解包，工程文件夹不得有空格或其他特殊符号 ！！！** 

9.  更新说明: 在proot ubuntu下删除原 DNA文件夹（记得提前备份DNA文件夹内的重要文件/插件），重新【 _`git clone https://gitee.com/sharpeter/DNA.git`_  】

10.   **动态分区必须打包成原官方卡刷包格式[zip]（即打包成.new.dat.br或.new.dat，同时必须使用工程文件夹下的dynamic_partitions_op_list，一块压缩成zip卡刷包），不允许单刷.img** 

11.  手机上使用工具时如果使用 **系统ROOT** 对工程目录下进行了操作(比如： **添加文件，修改文件**等。。。 )，请记得给操作过的文件或文件夹  **777**  满权！！！

####  **参与贡献** 

Credit:
1.  aarch64 [mke2fs & e2fsdroid from 小新大大](https://github.com/xiaoxindada/SGSI-build-tool)
2.  x86_64 [mke2fs & e2fsdroid from Erfan Abdi](https://github.com/erfanoabdi/ErfanGSIs)
3.  osm0sis @ Github: [Android-Image-Kitchen](https://github.com/osm0sis/Android-Image-Kitchen)
4.  ~xiliuya @ Github: [termux-linux](https://github.com/xiliuya/termux-linux)~

5.  xpirt   @ Github: [sdat2img.py](https://github.com/xpirt/sdat2img) & [img2sdat.py](https://github.com/xpirt/img2sdat)
6.  Cubi    @ Github: [ext4.py](https://github.com/cubinator/ext4)
7.  Gregory @ Github: [extract_android_ota_payload.py & update_metadata_pb2.py](https://github.com/cyxx/extract_android_ota_payload)
8.  Sergey  @ Github (unix3dgforce@MiuiPro.by DEV Team): [BatchApkTool UnpackerFirmware](https://github.com/unix3dgforce) & [lpunpack.py](https://github.com/unix3dgforce/lpunpack)


####  **工具预览** 

1.  手机 Termux Proot Ubuntu 20.04 Arm64[aarch64]

![Image text](https://gitee.com/wenrou2554/dna_gitee/raw/master/views/view_aarch64.jpg)

2.  虚拟机或实体机 Ubuntu 20.04 x86_64[x64]

![Image text](https://gitee.com/wenrou2554/dna_gitee/raw/master/views/0_view_x86_64.png)
![Image text](https://gitee.com/wenrou2554/dna_gitee/raw/master/views/1_view_x86_64.png)

3.  电脑 Win10 Wsl2 Ubuntu 20.04 x86_64[x64]

![Image text](https://gitee.com/wenrou2554/dna_gitee/raw/master/views/2_view_x86_64.png)
![Image text](https://gitee.com/wenrou2554/dna_gitee/raw/master/views/3_view_x86_64.png)
![Image text](https://gitee.com/wenrou2554/dna_gitee/raw/master/views/4_view_x86_64.png)


####  **交流反馈** 

1.  QQ群1：[578517063](https://jq.qq.com/?_wv=1027&k=3A2CRDjT)

    ~QQ群2：[904865456](https://jq.qq.com/?_wv=1027&k=9izS4Ooz)~

    

2.  [酷安](https://www.coolapk.com/feed/23098694?shareKey=N2NjNjcwZWY5MDdmNWZiZjhhZmQ~&shareUid=1403335&shareFrom=com.coolapk.market_10.5.3
)：[Errors](http://www.coolapk.com/u/1403335)


####  **免责声明** 

1.  本工具在Termux proot环境中运行，不需要root权限， 【 **请不要在Termux中使用系统root功能** 】 ！！！

2.  此工具不含任何【破坏系统、获取数据】等其他不法代码 ！！！

3.   **如果由于用户利用root权限对工具中的工程目录进行操作导致的数据丢失、损毁，本人不承担任何责任 ！！！** 
