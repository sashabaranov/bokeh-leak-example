from collections import namedtuple


Bin2D = namedtuple('Bin2D', ["value", "top", "bottom", "left", "right", "color"])
bins = [
    Bin2D(value=12097.0, top=0.004000000000000001, bottom=0.0038000000000000004, left=4.39822971502571, right=4.71238898038469, color='#d1f200') ,
    Bin2D(value=11893.0, top=0.0042, bottom=0.004000000000000001, left=4.39822971502571, right=4.71238898038469, color='#bff200') ,
    Bin2D(value=11803.0, top=0.0044, bottom=0.0042, left=4.39822971502571, right=4.71238898038469, color='#b8f200') ,
    Bin2D(value=11566.0, top=0.004600000000000001, bottom=0.0044, left=4.39822971502571, right=4.71238898038469, color='#a3f200') ,
    Bin2D(value=11489.0, top=0.0048, bottom=0.004600000000000001, left=4.39822971502571, right=4.71238898038469, color='#9cf200') ,
    Bin2D(value=11477.0, top=0.005, bottom=0.0048, left=4.39822971502571, right=4.71238898038469, color='#9bf200') ,
    Bin2D(value=9704.0, top=-0.0048000000000000004, bottom=-0.005, left=4.71238898038469, right=5.026548245743669, color='#00f200') ,
    Bin2D(value=9782.0, top=-0.0046, bottom=-0.0048000000000000004, left=4.71238898038469, right=5.026548245743669, color='#06f200') ,
    Bin2D(value=9955.0, top=-0.0044, bottom=-0.0046, left=4.71238898038469, right=5.026548245743669, color='#15f200') ,
    Bin2D(value=10467.0, top=-0.0042, bottom=-0.0044, left=4.71238898038469, right=5.026548245743669, color='#42f200') ,
    Bin2D(value=10441.0, top=-0.004, bottom=-0.0042, left=4.71238898038469, right=5.026548245743669, color='#40f200') ,
    Bin2D(value=10444.0, top=-0.0038, bottom=-0.004, left=4.71238898038469, right=5.026548245743669, color='#40f200') ,
    Bin2D(value=10642.0, top=-0.0036, bottom=-0.0038, left=4.71238898038469, right=5.026548245743669, color='#51f200') ,
    Bin2D(value=10872.0, top=-0.0034000000000000002, bottom=-0.0036, left=4.71238898038469, right=5.026548245743669, color='#66f200') ,
    Bin2D(value=10914.0, top=-0.0031999999999999997, bottom=-0.0034000000000000002, left=4.71238898038469, right=5.026548245743669, color='#69f200') ,
    Bin2D(value=11209.0, top=-0.003, bottom=-0.0031999999999999997, left=4.71238898038469, right=5.026548245743669, color='#83f200') ,
    Bin2D(value=11562.0, top=-0.0028, bottom=-0.003, left=4.71238898038469, right=5.026548245743669, color='#a2f200') ,
    Bin2D(value=11791.0, top=-0.0026, bottom=-0.0028, left=4.71238898038469, right=5.026548245743669, color='#b6f200') ,
    Bin2D(value=12202.0, top=-0.0024, bottom=-0.0026, left=4.71238898038469, right=5.026548245743669, color='#dbf200') ,
    Bin2D(value=12676.0, top=-0.0022, bottom=-0.0024, left=4.71238898038469, right=5.026548245743669, color='#f2df00') ,
    Bin2D(value=12646.0, top=-0.002, bottom=-0.0022, left=4.71238898038469, right=5.026548245743669, color='#f2e200') ,
    Bin2D(value=12927.0, top=-0.0018, bottom=-0.002, left=4.71238898038469, right=5.026548245743669, color='#f2c900') ,
    Bin2D(value=13110.0, top=-0.0015999999999999999, bottom=-0.0018, left=4.71238898038469, right=5.026548245743669, color='#f2b900') ,
    Bin2D(value=13317.0, top=-0.0013999999999999998, bottom=-0.0015999999999999999, left=4.71238898038469, right=5.026548245743669, color='#f2a700') ,
    Bin2D(value=13121.0, top=-0.0012000000000000001, bottom=-0.0013999999999999998, left=4.71238898038469, right=5.026548245743669, color='#f2b800') ,
    Bin2D(value=13352.0, top=-0.001, bottom=-0.0012000000000000001, left=4.71238898038469, right=5.026548245743669, color='#f2a400') ,
    Bin2D(value=13669.0, top=-0.0007999999999999995, bottom=-0.001, left=4.71238898038469, right=5.026548245743669, color='#f28800') ,
    Bin2D(value=13568.0, top=-0.0005999999999999998, bottom=-0.0007999999999999995, left=4.71238898038469, right=5.026548245743669, color='#f29100') ,
    Bin2D(value=13661.0, top=-0.0004000000000000002, bottom=-0.0005999999999999998, left=4.71238898038469, right=5.026548245743669, color='#f28800') ,
    Bin2D(value=14049.0, top=-0.00019999999999999966, bottom=-0.0004000000000000002, left=4.71238898038469, right=5.026548245743669, color='#f26600') ,
    Bin2D(value=13810.0, top=0.0, bottom=-0.00019999999999999966, left=4.71238898038469, right=5.026548245743669, color='#f27b00') ,
    Bin2D(value=13574.0, top=0.00020000000000000052, bottom=0.0, left=4.71238898038469, right=5.026548245743669, color='#f29000') ,
    Bin2D(value=13642.0, top=0.0004000000000000002, bottom=0.00020000000000000052, left=4.71238898038469, right=5.026548245743669, color='#f28a00') ,
    Bin2D(value=13515.0, top=0.0005999999999999998, bottom=0.0004000000000000002, left=4.71238898038469, right=5.026548245743669, color='#f29500') ,
    Bin2D(value=13356.0, top=0.0008000000000000004, bottom=0.0005999999999999998, left=4.71238898038469, right=5.026548245743669, color='#f2a300') ,
    Bin2D(value=13325.0, top=0.001, bottom=0.0008000000000000004, left=4.71238898038469, right=5.026548245743669, color='#f2a600') ,
    Bin2D(value=12994.0, top=0.0012000000000000005, bottom=0.001, left=4.71238898038469, right=5.026548245743669, color='#f2c300') ,
    Bin2D(value=13249.0, top=0.0014000000000000002, bottom=0.0012000000000000005, left=4.71238898038469, right=5.026548245743669, color='#f2ad00') ,
    Bin2D(value=13019.0, top=0.0015999999999999999, bottom=0.0014000000000000002, left=4.71238898038469, right=5.026548245743669, color='#f2c100') ,
    Bin2D(value=12765.0, top=0.0018000000000000004, bottom=0.0015999999999999999, left=4.71238898038469, right=5.026548245743669, color='#f2d700') ,
    Bin2D(value=12597.0, top=0.002, bottom=0.0018000000000000004, left=4.71238898038469, right=5.026548245743669, color='#f2e600') ,
    Bin2D(value=12305.0, top=0.0022000000000000006, bottom=0.002, left=4.71238898038469, right=5.026548245743669, color='#e4f200') ,
    Bin2D(value=12015.0, top=0.0024000000000000002, bottom=0.0022000000000000006, left=4.71238898038469, right=5.026548245743669, color='#caf200') ,
    Bin2D(value=12018.0, top=0.0026, bottom=0.0024000000000000002, left=4.71238898038469, right=5.026548245743669, color='#caf200') ,
    Bin2D(value=11688.0, top=0.0028000000000000004, bottom=0.0026, left=4.71238898038469, right=5.026548245743669, color='#adf200') ,
    Bin2D(value=11538.0, top=0.003, bottom=0.0028000000000000004, left=4.71238898038469, right=5.026548245743669, color='#a0f200') ,
    Bin2D(value=11437.0, top=0.0032000000000000006, bottom=0.003, left=4.71238898038469, right=5.026548245743669, color='#97f200') ,
    Bin2D(value=11143.0, top=0.003400000000000001, bottom=0.0032000000000000006, left=4.71238898038469, right=5.026548245743669, color='#7df200') ,
    Bin2D(value=11001.0, top=0.0036, bottom=0.003400000000000001, left=4.71238898038469, right=5.026548245743669, color='#71f200') ,
    Bin2D(value=10929.0, top=0.0038000000000000004, bottom=0.0036, left=4.71238898038469, right=5.026548245743669, color='#6bf200') ,
    Bin2D(value=10834.0, top=0.004000000000000001, bottom=0.0038000000000000004, left=4.71238898038469, right=5.026548245743669, color='#62f200') ,
    Bin2D(value=10620.0, top=0.0042, bottom=0.004000000000000001, left=4.71238898038469, right=5.026548245743669, color='#4ff200') ,
    Bin2D(value=10381.0, top=0.0044, bottom=0.0042, left=4.71238898038469, right=5.026548245743669, color='#3af200') ,
    Bin2D(value=10097.0, top=0.004600000000000001, bottom=0.0044, left=4.71238898038469, right=5.026548245743669, color='#21f200') ,
    Bin2D(value=10252.0, top=0.0048, bottom=0.004600000000000001, left=4.71238898038469, right=5.026548245743669, color='#2ff200') ,
    Bin2D(value=9646.0, top=0.005, bottom=0.0048, left=4.71238898038469, right=5.026548245743669, color='#00f205') ,
    Bin2D(value=8812.0, top=-0.0048000000000000004, bottom=-0.005, left=5.026548245743669, right=5.340707511102648, color='#00f24f') ,
    Bin2D(value=8934.0, top=-0.0046, bottom=-0.0048000000000000004, left=5.026548245743669, right=5.340707511102648, color='#00f244') ,
    Bin2D(value=9071.0, top=-0.0044, bottom=-0.0046, left=5.026548245743669, right=5.340707511102648, color='#00f238') ,
    Bin2D(value=8905.0, top=-0.0042, bottom=-0.0044, left=5.026548245743669, right=5.340707511102648, color='#00f247') ,
    Bin2D(value=9118.0, top=-0.004, bottom=-0.0042, left=5.026548245743669, right=5.340707511102648, color='#00f234') ,
    Bin2D(value=9232.0, top=-0.0038, bottom=-0.004, left=5.026548245743669, right=5.340707511102648, color='#00f22a') ,
    Bin2D(value=9479.0, top=-0.0036, bottom=-0.0038, left=5.026548245743669, right=5.340707511102648, color='#00f214') ,
    Bin2D(value=9685.0, top=-0.0034000000000000002, bottom=-0.0036, left=5.026548245743669, right=5.340707511102648, color='#00f202') ,
    Bin2D(value=9728.0, top=-0.0031999999999999997, bottom=-0.0034000000000000002, left=5.026548245743669, right=5.340707511102648, color='#01f200') ,
    Bin2D(value=10045.0, top=-0.003, bottom=-0.0031999999999999997, left=5.026548245743669, right=5.340707511102648, color='#1df200') ,
    Bin2D(value=10466.0, top=-0.0028, bottom=-0.003, left=5.026548245743669, right=5.340707511102648, color='#42f200') ,
    Bin2D(value=10709.0, top=-0.0026, bottom=-0.0028, left=5.026548245743669, right=5.340707511102648, color='#57f200') ,
    Bin2D(value=11105.0, top=-0.0024, bottom=-0.0026, left=5.026548245743669, right=5.340707511102648, color='#7af200') ,
    Bin2D(value=11093.0, top=-0.0022, bottom=-0.0024, left=5.026548245743669, right=5.340707511102648, color='#79f200') ,
    Bin2D(value=11521.0, top=-0.002, bottom=-0.0022, left=5.026548245743669, right=5.340707511102648, color='#9ff200') ,
    Bin2D(value=11881.0, top=-0.0018, bottom=-0.002, left=5.026548245743669, right=5.340707511102648, color='#bef200') ,
    Bin2D(value=12060.0, top=-0.0015999999999999999, bottom=-0.0018, left=5.026548245743669, right=5.340707511102648, color='#cef200') ,
    Bin2D(value=12209.0, top=-0.0013999999999999998, bottom=-0.0015999999999999999, left=5.026548245743669, right=5.340707511102648, color='#dbf200') ,
    Bin2D(value=12474.0, top=-0.0012000000000000001, bottom=-0.0013999999999999998, left=5.026548245743669, right=5.340707511102648, color='#f2f100') ,
    Bin2D(value=12517.0, top=-0.001, bottom=-0.0012000000000000001, left=5.026548245743669, right=5.340707511102648, color='#f2ed00') ,
    Bin2D(value=12871.0, top=-0.0007999999999999995, bottom=-0.001, left=5.026548245743669, right=5.340707511102648, color='#f2ce00') ,
    Bin2D(value=12964.0, top=-0.0005999999999999998, bottom=-0.0007999999999999995, left=5.026548245743669, right=5.340707511102648, color='#f2c600') ,
    Bin2D(value=12970.0, top=-0.0004000000000000002, bottom=-0.0005999999999999998, left=5.026548245743669, right=5.340707511102648, color='#f2c500') ,
    Bin2D(value=13288.0, top=-0.00019999999999999966, bottom=-0.0004000000000000002, left=5.026548245743669, right=5.340707511102648, color='#f2a900') ,
    Bin2D(value=13148.0, top=0.0, bottom=-0.00019999999999999966, left=5.026548245743669, right=5.340707511102648, color='#f2b600') ,
    Bin2D(value=12988.0, top=0.00020000000000000052, bottom=0.0, left=5.026548245743669, right=5.340707511102648, color='#f2c400') ,
    Bin2D(value=13250.0, top=0.0004000000000000002, bottom=0.00020000000000000052, left=5.026548245743669, right=5.340707511102648, color='#f2ad00') ,
    Bin2D(value=13145.0, top=0.0005999999999999998, bottom=0.0004000000000000002, left=5.026548245743669, right=5.340707511102648, color='#f2b600') ,
    Bin2D(value=13000.0, top=0.0008000000000000004, bottom=0.0005999999999999998, left=5.026548245743669, right=5.340707511102648, color='#f2c300') ,
    Bin2D(value=12914.0, top=0.001, bottom=0.0008000000000000004, left=5.026548245743669, right=5.340707511102648, color='#f2ca00') ,
    Bin2D(value=12699.0, top=0.0012000000000000005, bottom=0.001, left=5.026548245743669, right=5.340707511102648, color='#f2dd00') ,
    Bin2D(value=12511.0, top=0.0014000000000000002, bottom=0.0012000000000000005, left=5.026548245743669, right=5.340707511102648, color='#f2ee00') ,
    Bin2D(value=12294.0, top=0.0015999999999999999, bottom=0.0014000000000000002, left=5.026548245743669, right=5.340707511102648, color='#e3f200') ,
    Bin2D(value=12404.0, top=0.0018000000000000004, bottom=0.0015999999999999999, left=5.026548245743669, right=5.340707511102648, color='#ecf200') ,
    Bin2D(value=11831.0, top=0.002, bottom=0.0018000000000000004, left=5.026548245743669, right=5.340707511102648, color='#baf200') ,
    Bin2D(value=11807.0, top=0.0022000000000000006, bottom=0.002, left=5.026548245743669, right=5.340707511102648, color='#b8f200') ,
    Bin2D(value=11828.0, top=0.0024000000000000002, bottom=0.0022000000000000006, left=5.026548245743669, right=5.340707511102648, color='#baf200') ,
    Bin2D(value=11337.0, top=0.0026, bottom=0.0024000000000000002, left=5.026548245743669, right=5.340707511102648, color='#8ff200') ,
    Bin2D(value=11064.0, top=0.0028000000000000004, bottom=0.0026, left=5.026548245743669, right=5.340707511102648, color='#76f200') ,
    Bin2D(value=10952.0, top=0.003, bottom=0.0028000000000000004, left=5.026548245743669, right=5.340707511102648, color='#6df200') ,
    Bin2D(value=10728.0, top=0.0032000000000000006, bottom=0.003, left=5.026548245743669, right=5.340707511102648, color='#59f200') ,
    Bin2D(value=10329.0, top=0.003400000000000001, bottom=0.0032000000000000006, left=5.026548245743669, right=5.340707511102648, color='#36f200') ,
    Bin2D(value=10319.0, top=0.0036, bottom=0.003400000000000001, left=5.026548245743669, right=5.340707511102648, color='#35f200') ,
    Bin2D(value=10302.0, top=0.0038000000000000004, bottom=0.0036, left=5.026548245743669, right=5.340707511102648, color='#33f200') ,
    Bin2D(value=10111.0, top=0.004000000000000001, bottom=0.0038000000000000004, left=5.026548245743669, right=5.340707511102648, color='#23f200') ,
    Bin2D(value=10254.0, top=0.0042, bottom=0.004000000000000001, left=5.026548245743669, right=5.340707511102648, color='#2ff200') ,
    Bin2D(value=9796.0, top=0.0044, bottom=0.0042, left=5.026548245743669, right=5.340707511102648, color='#07f200') ,
    Bin2D(value=9721.0, top=0.004600000000000001, bottom=0.0044, left=5.026548245743669, right=5.340707511102648, color='#00f200') ,
    Bin2D(value=9559.0, top=0.0048, bottom=0.004600000000000001, left=5.026548245743669, right=5.340707511102648, color='#00f20d') ,
    Bin2D(value=9072.0, top=0.005, bottom=0.0048, left=5.026548245743669, right=5.340707511102648, color='#00f238') ,
    Bin2D(value=8225.0, top=-0.0048000000000000004, bottom=-0.005, left=5.340707511102648, right=5.654866776461628, color='#00f283') ,
    Bin2D(value=8094.0, top=-0.0046, bottom=-0.0048000000000000004, left=5.340707511102648, right=5.654866776461628, color='#00f28e') ,
    Bin2D(value=8209.0, top=-0.0044, bottom=-0.0046, left=5.340707511102648, right=5.654866776461628, color='#00f284') ,
    Bin2D(value=8199.0, top=-0.0042, bottom=-0.0044, left=5.340707511102648, right=5.654866776461628, color='#00f285') ,
    Bin2D(value=8384.0, top=-0.004, bottom=-0.0042, left=5.340707511102648, right=5.654866776461628, color='#00f275') ,
    Bin2D(value=8251.0, top=-0.0038, bottom=-0.004, left=5.340707511102648, right=5.654866776461628, color='#00f280') ,
    Bin2D(value=8592.0, top=-0.0036, bottom=-0.0038, left=5.340707511102648, right=5.654866776461628, color='#00f262') ,
    Bin2D(value=8951.0, top=-0.0034000000000000002, bottom=-0.0036, left=5.340707511102648, right=5.654866776461628, color='#00f243') ,
    Bin2D(value=8983.0, top=-0.0031999999999999997, bottom=-0.0034000000000000002, left=5.340707511102648, right=5.654866776461628, color='#00f240') ,
    Bin2D(value=9238.0, top=-0.003, bottom=-0.0031999999999999997, left=5.340707511102648, right=5.654866776461628, color='#00f229') ,
    Bin2D(value=9318.0, top=-0.0028, bottom=-0.003, left=5.340707511102648, right=5.654866776461628, color='#00f222') ,
    Bin2D(value=9593.0, top=-0.0026, bottom=-0.0028, left=5.340707511102648, right=5.654866776461628, color='#00f20a') ,
    Bin2D(value=9883.0, top=-0.0024, bottom=-0.0026, left=5.340707511102648, right=5.654866776461628, color='#0ef200') ,
    Bin2D(value=10269.0, top=-0.0022, bottom=-0.0024, left=5.340707511102648, right=5.654866776461628, color='#30f200') ,
    Bin2D(value=10613.0, top=-0.002, bottom=-0.0022, left=5.340707511102648, right=5.654866776461628, color='#4ff200') ,
    Bin2D(value=11000.0, top=-0.0018, bottom=-0.002, left=5.340707511102648, right=5.654866776461628, color='#71f200') ,
    Bin2D(value=11494.0, top=-0.0015999999999999999, bottom=-0.0018, left=5.340707511102648, right=5.654866776461628, color='#9cf200') ,
    Bin2D(value=11587.0, top=-0.0013999999999999998, bottom=-0.0015999999999999999, left=5.340707511102648, right=5.654866776461628, color='#a5f200') ,
    Bin2D(value=11788.0, top=-0.0012000000000000001, bottom=-0.0013999999999999998, left=5.340707511102648, right=5.654866776461628, color='#b6f200') ,
    Bin2D(value=12213.0, top=-0.001, bottom=-0.0012000000000000001, left=5.340707511102648, right=5.654866776461628, color='#dcf200') ,
    Bin2D(value=12472.0, top=-0.0007999999999999995, bottom=-0.001, left=5.340707511102648, right=5.654866776461628, color='#f2f100') ,
    Bin2D(value=12570.0, top=-0.0005999999999999998, bottom=-0.0007999999999999995, left=5.340707511102648, right=5.654866776461628, color='#f2e800') ,
    Bin2D(value=12963.0, top=-0.0004000000000000002, bottom=-0.0005999999999999998, left=5.340707511102648, right=5.654866776461628, color='#f2c600') ,
    Bin2D(value=13078.0, top=-0.00019999999999999966, bottom=-0.0004000000000000002, left=5.340707511102648, right=5.654866776461628, color='#f2bc00') ,
    Bin2D(value=13244.0, top=0.0, bottom=-0.00019999999999999966, left=5.340707511102648, right=5.654866776461628, color='#f2ad00') ,
    Bin2D(value=13130.0, top=0.00020000000000000052, bottom=0.0, left=5.340707511102648, right=5.654866776461628, color='#f2b700') ,
    Bin2D(value=13007.0, top=0.0004000000000000002, bottom=0.00020000000000000052, left=5.340707511102648, right=5.654866776461628, color='#f2c200') ,
    Bin2D(value=12786.0, top=0.0005999999999999998, bottom=0.0004000000000000002, left=5.340707511102648, right=5.654866776461628, color='#f2d500') ,
    Bin2D(value=12872.0, top=0.0008000000000000004, bottom=0.0005999999999999998, left=5.340707511102648, right=5.654866776461628, color='#f2ce00') ,
    Bin2D(value=12503.0, top=0.001, bottom=0.0008000000000000004, left=5.340707511102648, right=5.654866776461628, color='#f2ee00') ,
    Bin2D(value=12277.0, top=0.0012000000000000005, bottom=0.001, left=5.340707511102648, right=5.654866776461628, color='#e1f200') ,
    Bin2D(value=12123.0, top=0.0014000000000000002, bottom=0.0012000000000000005, left=5.340707511102648, right=5.654866776461628, color='#d4f200') ,
    Bin2D(value=11815.0, top=0.0015999999999999999, bottom=0.0014000000000000002, left=5.340707511102648, right=5.654866776461628, color='#b9f200') ,
    Bin2D(value=11216.0, top=0.0018000000000000004, bottom=0.0015999999999999999, left=5.340707511102648, right=5.654866776461628, color='#84f200') ,
    Bin2D(value=11332.0, top=0.002, bottom=0.0018000000000000004, left=5.340707511102648, right=5.654866776461628, color='#8ef200') ,
    Bin2D(value=10756.0, top=0.0022000000000000006, bottom=0.002, left=5.340707511102648, right=5.654866776461628, color='#5bf200') ,
    Bin2D(value=10542.0, top=0.0024000000000000002, bottom=0.0022000000000000006, left=5.340707511102648, right=5.654866776461628, color='#48f200') ,
    Bin2D(value=10209.0, top=0.0026, bottom=0.0024000000000000002, left=5.340707511102648, right=5.654866776461628, color='#2bf200') ,
    Bin2D(value=10082.0, top=0.0028000000000000004, bottom=0.0026, left=5.340707511102648, right=5.654866776461628, color='#20f200') ,
    Bin2D(value=10019.0, top=0.003, bottom=0.0028000000000000004, left=5.340707511102648, right=5.654866776461628, color='#1af200') ,
    Bin2D(value=9914.0, top=0.0032000000000000006, bottom=0.003, left=5.340707511102648, right=5.654866776461628, color='#11f200') ,
    Bin2D(value=9547.0, top=0.003400000000000001, bottom=0.0032000000000000006, left=5.340707511102648, right=5.654866776461628, color='#00f20e') ,
    Bin2D(value=9449.0, top=0.0036, bottom=0.003400000000000001, left=5.340707511102648, right=5.654866776461628, color='#00f217') ,
    Bin2D(value=9493.0, top=0.0038000000000000004, bottom=0.0036, left=5.340707511102648, right=5.654866776461628, color='#00f213') ,
    Bin2D(value=9229.0, top=0.004000000000000001, bottom=0.0038000000000000004, left=5.340707511102648, right=5.654866776461628, color='#00f22a') ,
    Bin2D(value=9148.0, top=0.0042, bottom=0.004000000000000001, left=5.340707511102648, right=5.654866776461628, color='#00f231') ,
    Bin2D(value=9124.0, top=0.0044, bottom=0.0042, left=5.340707511102648, right=5.654866776461628, color='#00f233') ,
    Bin2D(value=8799.0, top=0.004600000000000001, bottom=0.0044, left=5.340707511102648, right=5.654866776461628, color='#00f250') ,
    Bin2D(value=8700.0, top=0.0048, bottom=0.004600000000000001, left=5.340707511102648, right=5.654866776461628, color='#00f259') ,
    Bin2D(value=8371.0, top=0.005, bottom=0.0048, left=5.340707511102648, right=5.654866776461628, color='#00f276') ,
    Bin2D(value=6659.0, top=-0.0048000000000000004, bottom=-0.005, left=5.654866776461628, right=5.969026041820607, color='#00d7f2') ,
    Bin2D(value=6527.0, top=-0.0046, bottom=-0.0048000000000000004, left=5.654866776461628, right=5.969026041820607, color='#00cbf2') ,
    Bin2D(value=6770.0, top=-0.0044, bottom=-0.0046, left=5.654866776461628, right=5.969026041820607, color='#00e1f2') ,
    Bin2D(value=6737.0, top=-0.0042, bottom=-0.0044, left=5.654866776461628, right=5.969026041820607, color='#00def2') ,
    Bin2D(value=6982.0, top=-0.004, bottom=-0.0042, left=5.654866776461628, right=5.969026041820607, color='#00f2f0') ,
    Bin2D(value=7166.0, top=-0.0038, bottom=-0.004, left=5.654866776461628, right=5.969026041820607, color='#00f2e0') ,
    Bin2D(value=7098.0, top=-0.0036, bottom=-0.0038, left=5.654866776461628, right=5.969026041820607, color='#00f2e6') ,
    Bin2D(value=7131.0, top=-0.0034000000000000002, bottom=-0.0036, left=5.654866776461628, right=5.969026041820607, color='#00f2e3') ,
    Bin2D(value=7373.0, top=-0.0031999999999999997, bottom=-0.0034000000000000002, left=5.654866776461628, right=5.969026041820607, color='#00f2ce') ,
    Bin2D(value=7499.0, top=-0.003, bottom=-0.0031999999999999997, left=5.654866776461628, right=5.969026041820607, color='#00f2c2') ,
    Bin2D(value=7757.0, top=-0.0028, bottom=-0.003, left=5.654866776461628, right=5.969026041820607, color='#00f2ac') ,
    Bin2D(value=8041.0, top=-0.0026, bottom=-0.0028, left=5.654866776461628, right=5.969026041820607, color='#00f293') ,
    Bin2D(value=8194.0, top=-0.0024, bottom=-0.0026, left=5.654866776461628, right=5.969026041820607, color='#00f285') ,
    Bin2D(value=8320.0, top=-0.0022, bottom=-0.0024, left=5.654866776461628, right=5.969026041820607, color='#00f27a') ,
    Bin2D(value=8882.0, top=-0.002, bottom=-0.0022, left=5.654866776461628, right=5.969026041820607, color='#00f249') ,
    Bin2D(value=9319.0, top=-0.0018, bottom=-0.002, left=5.654866776461628, right=5.969026041820607, color='#00f222') ,
    Bin2D(value=9666.0, top=-0.0015999999999999999, bottom=-0.0018, left=5.654866776461628, right=5.969026041820607, color='#00f204') ,
    Bin2D(value=10172.0, top=-0.0013999999999999998, bottom=-0.0015999999999999999, left=5.654866776461628, right=5.969026041820607, color='#28f200') ,
    Bin2D(value=10649.0, top=-0.0012000000000000001, bottom=-0.0013999999999999998, left=5.654866776461628, right=5.969026041820607, color='#52f200') ,
    Bin2D(value=11129.0, top=-0.001, bottom=-0.0012000000000000001, left=5.654866776461628, right=5.969026041820607, color='#7cf200') ,
    Bin2D(value=11503.0, top=-0.0007999999999999995, bottom=-0.001, left=5.654866776461628, right=5.969026041820607, color='#9df200') ,
    Bin2D(value=12151.0, top=-0.0005999999999999998, bottom=-0.0007999999999999995, left=5.654866776461628, right=5.969026041820607, color='#d6f200') ,
    Bin2D(value=12162.0, top=-0.0004000000000000002, bottom=-0.0005999999999999998, left=5.654866776461628, right=5.969026041820607, color='#d7f200') ,
    Bin2D(value=12235.0, top=-0.00019999999999999966, bottom=-0.0004000000000000002, left=5.654866776461628, right=5.969026041820607, color='#def200') ,
    Bin2D(value=12573.0, top=0.0, bottom=-0.00019999999999999966, left=5.654866776461628, right=5.969026041820607, color='#f2e800') ,
    Bin2D(value=12356.0, top=0.00020000000000000052, bottom=0.0, left=5.654866776461628, right=5.969026041820607, color='#e8f200') ,
    Bin2D(value=12263.0, top=0.0004000000000000002, bottom=0.00020000000000000052, left=5.654866776461628, right=5.969026041820607, color='#e0f200') ,
    Bin2D(value=12224.0, top=0.0005999999999999998, bottom=0.0004000000000000002, left=5.654866776461628, right=5.969026041820607, color='#ddf200') ,
    Bin2D(value=11918.0, top=0.0008000000000000004, bottom=0.0005999999999999998, left=5.654866776461628, right=5.969026041820607, color='#c2f200') ,
    Bin2D(value=11577.0, top=0.001, bottom=0.0008000000000000004, left=5.654866776461628, right=5.969026041820607, color='#a4f200') ,
    Bin2D(value=11174.0, top=0.0012000000000000005, bottom=0.001, left=5.654866776461628, right=5.969026041820607, color='#80f200') ,
    Bin2D(value=11035.0, top=0.0014000000000000002, bottom=0.0012000000000000005, left=5.654866776461628, right=5.969026041820607, color='#74f200') ,
    Bin2D(value=10699.0, top=0.0015999999999999999, bottom=0.0014000000000000002, left=5.654866776461628, right=5.969026041820607, color='#56f200') ,
    Bin2D(value=10234.0, top=0.0018000000000000004, bottom=0.0015999999999999999, left=5.654866776461628, right=5.969026041820607, color='#2df200') ,
    Bin2D(value=9906.0, top=0.002, bottom=0.0018000000000000004, left=5.654866776461628, right=5.969026041820607, color='#10f200') ,
    Bin2D(value=9591.0, top=0.0022000000000000006, bottom=0.002, left=5.654866776461628, right=5.969026041820607, color='#00f20a') ,
    Bin2D(value=9222.0, top=0.0024000000000000002, bottom=0.0022000000000000006, left=5.654866776461628, right=5.969026041820607, color='#00f22b') ,
    Bin2D(value=9071.0, top=0.0026, bottom=0.0024000000000000002, left=5.654866776461628, right=5.969026041820607, color='#00f238') ,
    Bin2D(value=8723.0, top=0.0028000000000000004, bottom=0.0026, left=5.654866776461628, right=5.969026041820607, color='#00f257') ,
    Bin2D(value=8614.0, top=0.003, bottom=0.0028000000000000004, left=5.654866776461628, right=5.969026041820607, color='#00f260') ,
    Bin2D(value=8651.0, top=0.0032000000000000006, bottom=0.003, left=5.654866776461628, right=5.969026041820607, color='#00f25d') ,
    Bin2D(value=8449.0, top=0.003400000000000001, bottom=0.0032000000000000006, left=5.654866776461628, right=5.969026041820607, color='#00f26f') ,
    Bin2D(value=8312.0, top=0.0036, bottom=0.003400000000000001, left=5.654866776461628, right=5.969026041820607, color='#00f27b') ,
    Bin2D(value=8260.0, top=0.0038000000000000004, bottom=0.0036, left=5.654866776461628, right=5.969026041820607, color='#00f27f') ,
    Bin2D(value=8145.0, top=0.004000000000000001, bottom=0.0038000000000000004, left=5.654866776461628, right=5.969026041820607, color='#00f28a') ,
    Bin2D(value=8001.0, top=0.0042, bottom=0.004000000000000001, left=5.654866776461628, right=5.969026041820607, color='#00f296') ,
    Bin2D(value=8062.0, top=0.0044, bottom=0.0042, left=5.654866776461628, right=5.969026041820607, color='#00f291') ,
    Bin2D(value=8027.0, top=0.004600000000000001, bottom=0.0044, left=5.654866776461628, right=5.969026041820607, color='#00f294') ,
    Bin2D(value=7833.0, top=0.0048, bottom=0.004600000000000001, left=5.654866776461628, right=5.969026041820607, color='#00f2a5') ,
    Bin2D(value=7720.0, top=0.005, bottom=0.0048, left=5.654866776461628, right=5.969026041820607, color='#00f2af') ,
    Bin2D(value=5670.0, top=-0.0048000000000000004, bottom=-0.005, left=5.969026041820607, right=6.283185307179586, color='#0080f2') ,
    Bin2D(value=5751.0, top=-0.0046, bottom=-0.0048000000000000004, left=5.969026041820607, right=6.283185307179586, color='#0087f2') ,
    Bin2D(value=5747.0, top=-0.0044, bottom=-0.0046, left=5.969026041820607, right=6.283185307179586, color='#0087f2') ,
    Bin2D(value=5906.0, top=-0.0042, bottom=-0.0044, left=5.969026041820607, right=6.283185307179586, color='#0095f2') ,
    Bin2D(value=5850.0, top=-0.004, bottom=-0.0042, left=5.969026041820607, right=6.283185307179586, color='#0090f2') ,
    Bin2D(value=6059.0, top=-0.0038, bottom=-0.004, left=5.969026041820607, right=6.283185307179586, color='#00a2f2') ,
    Bin2D(value=5905.0, top=-0.0036, bottom=-0.0038, left=5.969026041820607, right=6.283185307179586, color='#0095f2') ,
    Bin2D(value=6199.0, top=-0.0034000000000000002, bottom=-0.0036, left=5.969026041820607, right=6.283185307179586, color='#00aff2') ,
    Bin2D(value=6128.0, top=-0.0031999999999999997, bottom=-0.0034000000000000002, left=5.969026041820607, right=6.283185307179586, color='#00a8f2') ,
    Bin2D(value=6210.0, top=-0.003, bottom=-0.0031999999999999997, left=5.969026041820607, right=6.283185307179586, color='#00b0f2') ,
    Bin2D(value=6293.0, top=-0.0028, bottom=-0.003, left=5.969026041820607, right=6.283185307179586, color='#00b7f2') ,
    Bin2D(value=6693.0, top=-0.0026, bottom=-0.0028, left=5.969026041820607, right=6.283185307179586, color='#00daf2') ,
    Bin2D(value=6759.0, top=-0.0024, bottom=-0.0026, left=5.969026041820607, right=6.283185307179586, color='#00e0f2') ,
    Bin2D(value=7060.0, top=-0.0022, bottom=-0.0024, left=5.969026041820607, right=6.283185307179586, color='#00f2e9') ,
    Bin2D(value=7484.0, top=-0.002, bottom=-0.0022, left=5.969026041820607, right=6.283185307179586, color='#00f2c4') ,
    Bin2D(value=7712.0, top=-0.0018, bottom=-0.002, left=5.969026041820607, right=6.283185307179586, color='#00f2b0') ,
    Bin2D(value=8377.0, top=-0.0015999999999999999, bottom=-0.0018, left=5.969026041820607, right=6.283185307179586, color='#00f275') ,
    Bin2D(value=8694.0, top=-0.0013999999999999998, bottom=-0.0015999999999999999, left=5.969026041820607, right=6.283185307179586, color='#00f259') ,
    Bin2D(value=9084.0, top=-0.0012000000000000001, bottom=-0.0013999999999999998, left=5.969026041820607, right=6.283185307179586, color='#00f237') ,
    Bin2D(value=9620.0, top=-0.001, bottom=-0.0012000000000000001, left=5.969026041820607, right=6.283185307179586, color='#00f208') ,
    Bin2D(value=9901.0, top=-0.0007999999999999995, bottom=-0.001, left=5.969026041820607, right=6.283185307179586, color='#10f200') ,
    Bin2D(value=10433.0, top=-0.0005999999999999998, bottom=-0.0007999999999999995, left=5.969026041820607, right=6.283185307179586, color='#3ff200') ,
    Bin2D(value=10668.0, top=-0.0004000000000000002, bottom=-0.0005999999999999998, left=5.969026041820607, right=6.283185307179586, color='#54f200') ,
    Bin2D(value=10686.0, top=-0.00019999999999999966, bottom=-0.0004000000000000002, left=5.969026041820607, right=6.283185307179586, color='#55f200') ,
    Bin2D(value=10913.0, top=0.0, bottom=-0.00019999999999999966, left=5.969026041820607, right=6.283185307179586, color='#69f200') ,
    Bin2D(value=10843.0, top=0.00020000000000000052, bottom=0.0, left=5.969026041820607, right=6.283185307179586, color='#63f200') ,
    Bin2D(value=10744.0, top=0.0004000000000000002, bottom=0.00020000000000000052, left=5.969026041820607, right=6.283185307179586, color='#5af200') ,
    Bin2D(value=10389.0, top=0.0005999999999999998, bottom=0.0004000000000000002, left=5.969026041820607, right=6.283185307179586, color='#3bf200') ,
    Bin2D(value=10189.0, top=0.0008000000000000004, bottom=0.0005999999999999998, left=5.969026041820607, right=6.283185307179586, color='#29f200') ,
    Bin2D(value=10090.0, top=0.001, bottom=0.0008000000000000004, left=5.969026041820607, right=6.283185307179586, color='#21f200') ,
    Bin2D(value=9591.0, top=0.0012000000000000005, bottom=0.001, left=5.969026041820607, right=6.283185307179586, color='#00f20a') ,
    Bin2D(value=9382.0, top=0.0014000000000000002, bottom=0.0012000000000000005, left=5.969026041820607, right=6.283185307179586, color='#00f21d') ,
    Bin2D(value=8835.0, top=0.0015999999999999999, bottom=0.0014000000000000002, left=5.969026041820607, right=6.283185307179586, color='#00f24d') ,
    Bin2D(value=8494.0, top=0.0018000000000000004, bottom=0.0015999999999999999, left=5.969026041820607, right=6.283185307179586, color='#00f26b') ,
    Bin2D(value=8199.0, top=0.002, bottom=0.0018000000000000004, left=5.969026041820607, right=6.283185307179586, color='#00f285') ,
    Bin2D(value=7936.0, top=0.0022000000000000006, bottom=0.002, left=5.969026041820607, right=6.283185307179586, color='#00f29c') ,
    Bin2D(value=7484.0, top=0.0024000000000000002, bottom=0.0022000000000000006, left=5.969026041820607, right=6.283185307179586, color='#00f2c4') ,
    Bin2D(value=7170.0, top=0.0026, bottom=0.0024000000000000002, left=5.969026041820607, right=6.283185307179586, color='#00f2df') ,
    Bin2D(value=7103.0, top=0.0028000000000000004, bottom=0.0026, left=5.969026041820607, right=6.283185307179586, color='#00f2e5') ,
    Bin2D(value=6904.0, top=0.003, bottom=0.0028000000000000004, left=5.969026041820607, right=6.283185307179586, color='#00edf2') ,
    Bin2D(value=6953.0, top=0.0032000000000000006, bottom=0.003, left=5.969026041820607, right=6.283185307179586, color='#00f1f2') ,
    Bin2D(value=6719.0, top=0.003400000000000001, bottom=0.0032000000000000006, left=5.969026041820607, right=6.283185307179586, color='#00dcf2') ,
    Bin2D(value=6758.0, top=0.0036, bottom=0.003400000000000001, left=5.969026041820607, right=6.283185307179586, color='#00e0f2') ,
    Bin2D(value=6635.0, top=0.0038000000000000004, bottom=0.0036, left=5.969026041820607, right=6.283185307179586, color='#00d5f2') ,
    Bin2D(value=6606.0, top=0.004000000000000001, bottom=0.0038000000000000004, left=5.969026041820607, right=6.283185307179586, color='#00d2f2') ,
    Bin2D(value=6361.0, top=0.0042, bottom=0.004000000000000001, left=5.969026041820607, right=6.283185307179586, color='#00bdf2') ,
    Bin2D(value=6443.0, top=0.0044, bottom=0.0042, left=5.969026041820607, right=6.283185307179586, color='#00c4f2') ,
    Bin2D(value=6414.0, top=0.004600000000000001, bottom=0.0044, left=5.969026041820607, right=6.283185307179586, color='#00c1f2') ,
    Bin2D(value=6377.0, top=0.0048, bottom=0.004600000000000001, left=5.969026041820607, right=6.283185307179586, color='#00bef2') ,
    Bin2D(value=6456.0, top=0.005, bottom=0.0048, left=5.969026041820607, right=6.283185307179586, color='#00c5f2') ,
]
