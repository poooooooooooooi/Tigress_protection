#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_810870 = ref_278 # MOV operation
ref_911626 = ref_810870 # MOV operation
ref_911632 = (0x1D2C27F0 | ref_911626) # OR operation
ref_962011 = ref_911632 # MOV operation
ref_962025 = ((ref_962011 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1365087 = ref_278 # MOV operation
ref_1465843 = ref_1365087 # MOV operation
ref_1465849 = (0x1D2C27F0 | ref_1465843) # OR operation
ref_1566630 = ref_1465849 # MOV operation
ref_1566638 = (ref_1566630 >> (0x37 & 0x3F)) # SHR operation
ref_1566645 = ref_1566638 # MOV operation
ref_1617027 = ref_962025 # MOV operation
ref_1617031 = ref_1566645 # MOV operation
ref_1617033 = (ref_1617031 | ref_1617027) # OR operation
ref_1667420 = ref_1617033 # MOV operation
ref_2423245 = ref_278 # MOV operation
ref_2876761 = ref_1667420 # MOV operation
ref_2927115 = ref_2876761 # MOV operation
ref_2927129 = ((ref_2927115 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_3330276 = ref_1667420 # MOV operation
ref_3431032 = ref_3330276 # MOV operation
ref_3431040 = (ref_3431032 >> (0x33 & 0x3F)) # SHR operation
ref_3431047 = ref_3431040 # MOV operation
ref_3481429 = ref_2927129 # MOV operation
ref_3481433 = ref_3431047 # MOV operation
ref_3481435 = (ref_3481433 | ref_3481429) # OR operation
ref_3531822 = ref_2423245 # MOV operation
ref_3531826 = ref_3481435 # MOV operation
ref_3531828 = (ref_3531826 | ref_3531822) # OR operation
ref_3582215 = ref_3531828 # MOV operation
ref_4388434 = ref_278 # MOV operation
ref_4438788 = ref_4388434 # MOV operation
ref_4438802 = ((0x6402BE2 + ref_4438788) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_4489190 = ref_4438802 # MOV operation
ref_5245015 = ref_278 # MOV operation
ref_5345771 = ref_5245015 # MOV operation
ref_5345777 = (0x3544223F | ref_5345771) # OR operation
ref_5799318 = ref_4489190 # MOV operation
ref_6202440 = ref_3582215 # MOV operation
ref_6252802 = ref_5799318 # MOV operation
ref_6252806 = ref_6202440 # MOV operation
ref_6252808 = (((sx(0x40, ref_6252806) * sx(0x40, ref_6252802)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6303196 = ref_6252808 # MOV operation
ref_6303198 = (((sx(0x40, ref_6303196) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6353582 = ref_5345777 # MOV operation
ref_6353586 = ref_6303198 # MOV operation
ref_6353588 = (((sx(0x40, ref_6353586) * sx(0x40, ref_6353582)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6403972 = ref_6353588 # MOV operation
ref_7159882 = ref_4489190 # MOV operation
ref_7663792 = ref_6403972 # MOV operation
ref_7714146 = ref_7663792 # MOV operation
ref_7714160 = (0x1F & ref_7714146) # AND operation
ref_7764539 = ref_7714160 # MOV operation
ref_7764553 = ((ref_7764539 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7814940 = ref_7159882 # MOV operation
ref_7814944 = ref_7764553 # MOV operation
ref_7814946 = (ref_7814944 | ref_7814940) # OR operation
ref_7865333 = ref_7814946 # MOV operation
ref_8369231 = ref_3582215 # MOV operation
ref_8469987 = ref_8369231 # MOV operation
ref_8469995 = (ref_8469987 >> (0x1 & 0x3F)) # SHR operation
ref_8470002 = ref_8469995 # MOV operation
ref_8520376 = ref_8470002 # MOV operation
ref_8520390 = (0xF & ref_8520376) # AND operation
ref_8621171 = ref_8520390 # MOV operation
ref_8621177 = (0x1 | ref_8621171) # OR operation
ref_9024324 = ref_1667420 # MOV operation
ref_9074678 = ref_9024324 # MOV operation
ref_9074690 = ref_8621177 # MOV operation
ref_9074692 = ((ref_9074678 << ((ref_9074690 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_9477839 = ref_1667420 # MOV operation
ref_9931355 = ref_3582215 # MOV operation
ref_10032111 = ref_9931355 # MOV operation
ref_10032119 = (ref_10032111 >> (0x1 & 0x3F)) # SHR operation
ref_10032126 = ref_10032119 # MOV operation
ref_10082500 = ref_10032126 # MOV operation
ref_10082514 = (0xF & ref_10082500) # AND operation
ref_10183295 = ref_10082514 # MOV operation
ref_10183301 = (0x1 | ref_10183295) # OR operation
ref_10284086 = ref_10183301 # MOV operation
ref_10284088 = ((0x40 - ref_10284086) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_10284096 = ref_10284088 # MOV operation
ref_10334478 = ref_9477839 # MOV operation
ref_10334482 = ref_10284096 # MOV operation
ref_10334484 = (ref_10334482 & 0xFFFFFFFF) # MOV operation
ref_10334486 = (ref_10334478 >> ((ref_10334484 & 0xFF) & 0x3F)) # SHR operation
ref_10334493 = ref_10334486 # MOV operation
ref_10384875 = ref_9074692 # MOV operation
ref_10384879 = ref_10334493 # MOV operation
ref_10384881 = (ref_10384879 | ref_10384875) # OR operation
ref_10788028 = ref_7865333 # MOV operation
ref_11241544 = ref_6403972 # MOV operation
ref_11342300 = ref_11241544 # MOV operation
ref_11342308 = (ref_11342300 >> (0x3 & 0x3F)) # SHR operation
ref_11342315 = ref_11342308 # MOV operation
ref_11392689 = ref_11342315 # MOV operation
ref_11392703 = (0x7 & ref_11392689) # AND operation
ref_11493484 = ref_11392703 # MOV operation
ref_11493490 = (0x1 | ref_11493484) # OR operation
ref_11543877 = ref_10788028 # MOV operation
ref_11543881 = ref_11493490 # MOV operation
ref_11543883 = (ref_11543881 & 0xFFFFFFFF) # MOV operation
ref_11543885 = (ref_11543877 >> ((ref_11543883 & 0xFF) & 0x3F)) # SHR operation
ref_11543892 = ref_11543885 # MOV operation
ref_11594274 = ref_10384881 # MOV operation
ref_11594278 = ref_11543892 # MOV operation
ref_11594280 = ((ref_11594274 - ref_11594278) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_11594282 = ((((ref_11594274 ^ (ref_11594278 ^ ref_11594280)) ^ ((ref_11594274 ^ ref_11594280) & (ref_11594274 ^ ref_11594278))) >> 63) & 0x1) # Carry flag
ref_11594286 = (0x1 if (ref_11594280 == 0x0) else 0x0) # Zero flag
ref_11594288 = ((((ref_11594278 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if ((ref_11594282 | ref_11594286) == 0x1) else 0x0)) # SETBE operation
ref_11594290 = (ref_11594288 & 0xFF) # MOVZX operation
ref_11644656 = (ref_11594290 & 0xFFFFFFFF) # MOV operation
ref_11644658 = ((ref_11644656 & 0xFFFFFFFF) & (ref_11644656 & 0xFFFFFFFF)) # TEST operation
ref_11644663 = (0x1 if (ref_11644658 == 0x0) else 0x0) # Zero flag
ref_11644665 = (0x186C if (ref_11644663 == 0x1) else 0x184E) # Program Counter


if (ref_11644663 == 0x1):
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_810870 = ref_278 # MOV operation
    ref_911626 = ref_810870 # MOV operation
    ref_911632 = (0x1D2C27F0 | ref_911626) # OR operation
    ref_962011 = ref_911632 # MOV operation
    ref_962025 = ((ref_962011 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_1365087 = ref_278 # MOV operation
    ref_1465843 = ref_1365087 # MOV operation
    ref_1465849 = (0x1D2C27F0 | ref_1465843) # OR operation
    ref_1566630 = ref_1465849 # MOV operation
    ref_1566638 = (ref_1566630 >> (0x37 & 0x3F)) # SHR operation
    ref_1566645 = ref_1566638 # MOV operation
    ref_1617027 = ref_962025 # MOV operation
    ref_1617031 = ref_1566645 # MOV operation
    ref_1617033 = (ref_1617031 | ref_1617027) # OR operation
    ref_1667420 = ref_1617033 # MOV operation
    ref_2423245 = ref_278 # MOV operation
    ref_2876761 = ref_1667420 # MOV operation
    ref_2927115 = ref_2876761 # MOV operation
    ref_2927129 = ((ref_2927115 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_3330276 = ref_1667420 # MOV operation
    ref_3431032 = ref_3330276 # MOV operation
    ref_3431040 = (ref_3431032 >> (0x33 & 0x3F)) # SHR operation
    ref_3431047 = ref_3431040 # MOV operation
    ref_3481429 = ref_2927129 # MOV operation
    ref_3481433 = ref_3431047 # MOV operation
    ref_3481435 = (ref_3481433 | ref_3481429) # OR operation
    ref_3531822 = ref_2423245 # MOV operation
    ref_3531826 = ref_3481435 # MOV operation
    ref_3531828 = (ref_3531826 | ref_3531822) # OR operation
    ref_3582215 = ref_3531828 # MOV operation
    ref_4388434 = ref_278 # MOV operation
    ref_4438788 = ref_4388434 # MOV operation
    ref_4438802 = ((0x6402BE2 + ref_4438788) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_4489190 = ref_4438802 # MOV operation
    ref_5245015 = ref_278 # MOV operation
    ref_5345771 = ref_5245015 # MOV operation
    ref_5345777 = (0x3544223F | ref_5345771) # OR operation
    ref_5799318 = ref_4489190 # MOV operation
    ref_6202440 = ref_3582215 # MOV operation
    ref_6252802 = ref_5799318 # MOV operation
    ref_6252806 = ref_6202440 # MOV operation
    ref_6252808 = (((sx(0x40, ref_6252806) * sx(0x40, ref_6252802)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_6303196 = ref_6252808 # MOV operation
    ref_6303198 = (((sx(0x40, ref_6303196) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_6353582 = ref_5345777 # MOV operation
    ref_6353586 = ref_6303198 # MOV operation
    ref_6353588 = (((sx(0x40, ref_6353586) * sx(0x40, ref_6353582)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_6403972 = ref_6353588 # MOV operation
    ref_7159882 = ref_4489190 # MOV operation
    ref_7663792 = ref_6403972 # MOV operation
    ref_7714146 = ref_7663792 # MOV operation
    ref_7714160 = (0x1F & ref_7714146) # AND operation
    ref_7764539 = ref_7714160 # MOV operation
    ref_7764553 = ((ref_7764539 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_7814940 = ref_7159882 # MOV operation
    ref_7814944 = ref_7764553 # MOV operation
    ref_7814946 = (ref_7814944 | ref_7814940) # OR operation
    ref_7865333 = ref_7814946 # MOV operation
    ref_12450946 = ref_3582215 # MOV operation
    ref_12954856 = ref_3582215 # MOV operation
    ref_13005210 = ref_12954856 # MOV operation
    ref_13005224 = (0xF & ref_13005210) # AND operation
    ref_13055603 = ref_13005224 # MOV operation
    ref_13055617 = ((ref_13055603 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_13106004 = ref_12450946 # MOV operation
    ref_13106008 = ref_13055617 # MOV operation
    ref_13106010 = (ref_13106008 | ref_13106004) # OR operation
    ref_13156397 = ref_13106010 # MOV operation
    ref_14012987 = ref_13156397 # MOV operation
    ref_14113743 = ref_14012987 # MOV operation
    ref_14113751 = (ref_14113743 >> (0x3 & 0x3F)) # SHR operation
    ref_14113758 = ref_14113751 # MOV operation
    ref_14164132 = ref_14113758 # MOV operation
    ref_14164146 = (0xF & ref_14164132) # AND operation
    ref_14264927 = ref_14164146 # MOV operation
    ref_14264933 = (0x1 | ref_14264927) # OR operation
    ref_14668080 = ref_1667420 # MOV operation
    ref_14718434 = ref_14668080 # MOV operation
    ref_14718446 = ref_14264933 # MOV operation
    ref_14718448 = ((ref_14718434 << ((ref_14718446 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_15121595 = ref_1667420 # MOV operation
    ref_15575111 = ref_13156397 # MOV operation
    ref_15675867 = ref_15575111 # MOV operation
    ref_15675875 = (ref_15675867 >> (0x3 & 0x3F)) # SHR operation
    ref_15675882 = ref_15675875 # MOV operation
    ref_15726256 = ref_15675882 # MOV operation
    ref_15726270 = (0xF & ref_15726256) # AND operation
    ref_15827051 = ref_15726270 # MOV operation
    ref_15827057 = (0x1 | ref_15827051) # OR operation
    ref_15927842 = ref_15827057 # MOV operation
    ref_15927844 = ((0x40 - ref_15927842) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_15927852 = ref_15927844 # MOV operation
    ref_15978234 = ref_15121595 # MOV operation
    ref_15978238 = ref_15927852 # MOV operation
    ref_15978240 = (ref_15978238 & 0xFFFFFFFF) # MOV operation
    ref_15978242 = (ref_15978234 >> ((ref_15978240 & 0xFF) & 0x3F)) # SHR operation
    ref_15978249 = ref_15978242 # MOV operation
    ref_16028631 = ref_14718448 # MOV operation
    ref_16028635 = ref_15978249 # MOV operation
    ref_16028637 = (ref_16028635 | ref_16028631) # OR operation
    ref_16431784 = ref_7865333 # MOV operation
    ref_16885300 = ref_6403972 # MOV operation
    ref_16935654 = ref_16885300 # MOV operation
    ref_16935668 = ((0x369A4780 + ref_16935654) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_16986056 = ref_16431784 # MOV operation
    ref_16986060 = ref_16935668 # MOV operation
    ref_16986062 = (((sx(0x40, ref_16986060) * sx(0x40, ref_16986056)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_17036446 = ref_16028637 # MOV operation
    ref_17036450 = ref_16986062 # MOV operation
    ref_17036452 = (((sx(0x40, ref_17036450) * sx(0x40, ref_17036446)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_17086836 = ref_17036452 # MOV operation
    ref_17187603 = ref_17086836 # MOV operation
    ref_17187605 = ref_17187603 # MOV operation
    endb = ref_17187605


else:
    ref_17187925 = SymVar_0
    ref_17187940 = ref_17187925 # MOV operation
    ref_17998537 = ref_17187940 # MOV operation
    ref_18099293 = ref_17998537 # MOV operation
    ref_18099299 = (0x1D2C27F0 | ref_18099293) # OR operation
    ref_18149678 = ref_18099299 # MOV operation
    ref_18149692 = ((ref_18149678 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_18552754 = ref_17187940 # MOV operation
    ref_18653510 = ref_18552754 # MOV operation
    ref_18653516 = (0x1D2C27F0 | ref_18653510) # OR operation
    ref_18754297 = ref_18653516 # MOV operation
    ref_18754305 = (ref_18754297 >> (0x37 & 0x3F)) # SHR operation
    ref_18754312 = ref_18754305 # MOV operation
    ref_18804694 = ref_18149692 # MOV operation
    ref_18804698 = ref_18754312 # MOV operation
    ref_18804700 = (ref_18804698 | ref_18804694) # OR operation
    ref_18855087 = ref_18804700 # MOV operation
    ref_19610912 = ref_17187940 # MOV operation
    ref_20064428 = ref_18855087 # MOV operation
    ref_20114782 = ref_20064428 # MOV operation
    ref_20114796 = ((ref_20114782 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_20517943 = ref_18855087 # MOV operation
    ref_20618699 = ref_20517943 # MOV operation
    ref_20618707 = (ref_20618699 >> (0x33 & 0x3F)) # SHR operation
    ref_20618714 = ref_20618707 # MOV operation
    ref_20669096 = ref_20114796 # MOV operation
    ref_20669100 = ref_20618714 # MOV operation
    ref_20669102 = (ref_20669100 | ref_20669096) # OR operation
    ref_20719489 = ref_19610912 # MOV operation
    ref_20719493 = ref_20669102 # MOV operation
    ref_20719495 = (ref_20719493 | ref_20719489) # OR operation
    ref_20769882 = ref_20719495 # MOV operation
    ref_20769884 = ((ref_20769882 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_20769885 = ((ref_20769882 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_20769886 = ((ref_20769882 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_20769887 = ((ref_20769882 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_20769888 = ((ref_20769882 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_20769889 = ((ref_20769882 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_20769890 = ((ref_20769882 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_20769891 = (ref_20769882 & 0xFF) # Byte reference - MOV operation
    ref_21576101 = ref_17187940 # MOV operation
    ref_21626455 = ref_21576101 # MOV operation
    ref_21626469 = ((0x6402BE2 + ref_21626455) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_21676857 = ref_21626469 # MOV operation
    ref_22432682 = ref_17187940 # MOV operation
    ref_22533438 = ref_22432682 # MOV operation
    ref_22533444 = (0x3544223F | ref_22533438) # OR operation
    ref_22986985 = ref_21676857 # MOV operation
    ref_23390107 = ref_20769882 # MOV operation
    ref_23440469 = ref_22986985 # MOV operation
    ref_23440473 = ref_23390107 # MOV operation
    ref_23440475 = (((sx(0x40, ref_23440473) * sx(0x40, ref_23440469)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_23490863 = ref_23440475 # MOV operation
    ref_23490865 = (((sx(0x40, ref_23490863) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_23541249 = ref_22533444 # MOV operation
    ref_23541253 = ref_23490865 # MOV operation
    ref_23541255 = (((sx(0x40, ref_23541253) * sx(0x40, ref_23541249)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_23591639 = ref_23541255 # MOV operation
    ref_24347549 = ref_21676857 # MOV operation
    ref_24851459 = ref_23591639 # MOV operation
    ref_24901813 = ref_24851459 # MOV operation
    ref_24901827 = (0x1F & ref_24901813) # AND operation
    ref_24952206 = ref_24901827 # MOV operation
    ref_24952220 = ((ref_24952206 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_25002607 = ref_24347549 # MOV operation
    ref_25002611 = ref_24952220 # MOV operation
    ref_25002613 = (ref_25002611 | ref_25002607) # OR operation
    ref_25053000 = ref_25002613 # MOV operation
    ref_29638652 = ref_23591639 # MOV operation
    ref_29689006 = ref_29638652 # MOV operation
    ref_29689022 = ((((0x0) << 64 | ref_29689006) / 0x8) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_29739405 = ref_29689022 # MOV operation
    ref_29739407 = ((ref_29739405 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_29739408 = ((ref_29739405 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_29739409 = ((ref_29739405 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_29739410 = ((ref_29739405 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_29739411 = ((ref_29739405 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_29739412 = ((ref_29739405 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_29739413 = ((ref_29739405 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_29739414 = (ref_29739405 & 0xFF) # Byte reference - MOV operation
    ref_30444821 = ref_20769889 # MOVZX operation
    ref_30545581 = (ref_30444821 & 0xFF) # MOVZX operation
    ref_31250989 = ref_20769886 # MOVZX operation
    ref_31956385 = (ref_31250989 & 0xFF) # MOVZX operation
    ref_31956387 = (ref_31956385 & 0xFF) # Byte reference - MOV operation
    ref_32057157 = (ref_30545581 & 0xFF) # MOVZX operation
    ref_32762553 = (ref_32057157 & 0xFF) # MOVZX operation
    ref_32762555 = (ref_32762553 & 0xFF) # Byte reference - MOV operation
    ref_33467961 = ref_20769884 # MOVZX operation
    ref_33568721 = (ref_33467961 & 0xFF) # MOVZX operation
    ref_34274129 = ref_20769891 # MOVZX operation
    ref_34979525 = (ref_34274129 & 0xFF) # MOVZX operation
    ref_34979527 = (ref_34979525 & 0xFF) # Byte reference - MOV operation
    ref_35080297 = (ref_33568721 & 0xFF) # MOVZX operation
    ref_35785693 = (ref_35080297 & 0xFF) # MOVZX operation
    ref_35785695 = (ref_35785693 & 0xFF) # Byte reference - MOV operation
    ref_36491101 = ref_29739410 # MOVZX operation
    ref_36591861 = (ref_36491101 & 0xFF) # MOVZX operation
    ref_37297269 = ref_29739414 # MOVZX operation
    ref_38002665 = (ref_37297269 & 0xFF) # MOVZX operation
    ref_38002667 = (ref_38002665 & 0xFF) # Byte reference - MOV operation
    ref_38103437 = (ref_36591861 & 0xFF) # MOVZX operation
    ref_38808833 = (ref_38103437 & 0xFF) # MOVZX operation
    ref_38808835 = (ref_38808833 & 0xFF) # Byte reference - MOV operation
    ref_39665415 = ((((((((ref_34979527) << 8 | ref_20769885) << 8 | ref_32762555) << 8 | ref_20769887) << 8 | ref_20769888) << 8 | ref_31956387) << 8 | ref_20769890) << 8 | ref_35785695) # MOV operation
    ref_39766171 = ref_39665415 # MOV operation
    ref_39766179 = (ref_39766171 >> (0x3 & 0x3F)) # SHR operation
    ref_39766186 = ref_39766179 # MOV operation
    ref_39816560 = ref_39766186 # MOV operation
    ref_39816574 = (0xF & ref_39816560) # AND operation
    ref_39917355 = ref_39816574 # MOV operation
    ref_39917361 = (0x1 | ref_39917355) # OR operation
    ref_40320508 = ((((((((ref_29739407) << 8 | ref_29739408) << 8 | ref_29739409) << 8 | ref_38002667) << 8 | ref_29739411) << 8 | ref_29739412) << 8 | ref_29739413) << 8 | ref_38808835) # MOV operation
    ref_40370862 = ref_40320508 # MOV operation
    ref_40370874 = ref_39917361 # MOV operation
    ref_40370876 = ((ref_40370862 << ((ref_40370874 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_40774023 = ((((((((ref_29739407) << 8 | ref_29739408) << 8 | ref_29739409) << 8 | ref_38002667) << 8 | ref_29739411) << 8 | ref_29739412) << 8 | ref_29739413) << 8 | ref_38808835) # MOV operation
    ref_41227539 = ((((((((ref_34979527) << 8 | ref_20769885) << 8 | ref_32762555) << 8 | ref_20769887) << 8 | ref_20769888) << 8 | ref_31956387) << 8 | ref_20769890) << 8 | ref_35785695) # MOV operation
    ref_41328295 = ref_41227539 # MOV operation
    ref_41328303 = (ref_41328295 >> (0x3 & 0x3F)) # SHR operation
    ref_41328310 = ref_41328303 # MOV operation
    ref_41378684 = ref_41328310 # MOV operation
    ref_41378698 = (0xF & ref_41378684) # AND operation
    ref_41479479 = ref_41378698 # MOV operation
    ref_41479485 = (0x1 | ref_41479479) # OR operation
    ref_41580270 = ref_41479485 # MOV operation
    ref_41580272 = ((0x40 - ref_41580270) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_41580280 = ref_41580272 # MOV operation
    ref_41630662 = ref_40774023 # MOV operation
    ref_41630666 = ref_41580280 # MOV operation
    ref_41630668 = (ref_41630666 & 0xFFFFFFFF) # MOV operation
    ref_41630670 = (ref_41630662 >> ((ref_41630668 & 0xFF) & 0x3F)) # SHR operation
    ref_41630677 = ref_41630670 # MOV operation
    ref_41681059 = ref_40370876 # MOV operation
    ref_41681063 = ref_41630677 # MOV operation
    ref_41681065 = (ref_41681063 | ref_41681059) # OR operation
    ref_42084212 = ref_25053000 # MOV operation
    ref_42537728 = ref_23591639 # MOV operation
    ref_42588082 = ref_42537728 # MOV operation
    ref_42588096 = ((0x369A4780 + ref_42588082) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_42638484 = ref_42084212 # MOV operation
    ref_42638488 = ref_42588096 # MOV operation
    ref_42638490 = (((sx(0x40, ref_42638488) * sx(0x40, ref_42638484)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_42688874 = ref_41681065 # MOV operation
    ref_42688878 = ref_42638490 # MOV operation
    ref_42688880 = (((sx(0x40, ref_42688878) * sx(0x40, ref_42688874)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_42739264 = ref_42688880 # MOV operation
    ref_42840031 = ref_42739264 # MOV operation
    ref_42840033 = ref_42840031 # MOV operation
    endb = ref_42840033


print endb & 0xffffffffffffffff