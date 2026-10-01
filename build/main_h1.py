"""Hybrid: boatlee_v29's action tape + our v22 market model as the selling overlay.

The tape supplies every physical action (farmer / hands) and every macro buy
(HIRE, BUY_SEED, BUY_ANIMAL, BUY_PRODUCT, BUY_LAND). Only the SELL side is ours.

Two measured facts drive the design:

1. boatlee_v29's own `_adaptive_market` overlay never fires -- the tape empties
   the shed every turn, so there is never an "unscheduled" surplus for it to
   sell. Disabling it reproduces v29 bit-for-bit on every seed. Its 0.97 pool
   score is the tape, not the overlay.
2. The market is a per-slot lockstep auction: at slot i both players quote off
   the same inventory. So the only way to out-earn an identical tape is to move
   the same units to an EARLIER turn -- the opponent then sells into inventory
   we already raised. Selling a turn early is worth ~+$1.7k in the mirror.

So the overlay's job is to decide, per item per turn, how much of the shed to
release now instead of on the tape's schedule. That decision uses v22's market
model: `market_price`, `mean_drain` (which prices in shops that have NOT
unlocked yet), `forecast`, opponent-aware `supply`, glut/tight bias, and hinge
metering -- plus a hard carve-out for WHEAT, which is animal feed and must never
be sold out from under the tape's PICKUP schedule.
"""

import base64
import math
import types
import zlib

# The tape is embedded rather than loaded from disk: Kaggle exec's main.py with no
# __file__ defined, so anything path-based dies before the agent ever runs.
_TAPE_B85 = "c-qyyXOpVhx+whpRGt6Ow&Dhz&I?9dm~+5{*;!LTKtxFrR7CylFBrPDyJy&E-+Sx5YgO&l490l!c+wcSUteFlw5+l@N@4=KtOVfzK}qZI%R*LP>J-PRJZ%WNp|am!Utj<Gzj#rRRsCg7X>2t7_DIW$`S!5VWa;hUAn^15{x9d>SvKFRwwm3S<YmTpL8cfDbl!hwSXvepmDM!x3i$gRjW~l03(o&V2R5fI*cr`8%EDcpX^AchopmV2fjfP8PB%vz5luE+=76K(rGvL7?yR|i9g2J%Z7Cs|s(ZLR!;|X`x^^A&45)L_rPs46BVv+IjuvEBuV%?p^EhB#QLi*J5}{&}8-n#?-OJ6VCmHWzDR5jn)&r^9?6hnz$X<wK(y7^DoD_n*Iq}3&IBgCQZkCW-P$D@Uqh436QKc+)unbV*#9PNh(=F)>ECY)$CS=%RRXosyJJ82Ac(`gB_@>!23yiBi9^=u&T8s}eXsAn;hOFUc-RafbN*&L+QjVWQ23*}c^W=tkFI}&yV{4IT<CSx+YE3{*=tH?85ueConFUX7t6i^anNXrJYE-=nzOGFd+`M3DjXabwfI!bon?@(u20~Kiz+~aP>DJ^lILxU~xKnS?>m9sG5)%`~$elp+McH(%>vRuB*o?vk1I!33Sf^3!Sjuhupg$X67D_B4PpERcFl@z1^{~Z*5&yDZ-sHxk{-JU>OKp#7x;q&;ORQVtQ@;Tc(L=}2^H#NbD0JAp+$hXLZJ*y0t7N!}0_^6ZFF(Sq@X6njt!5}fi|&k9Z@UAtlGqeAW8FTl+RJmbv>2X>`-63sXQ{oC0;f?B2zG~qY`Bc}W^AM{Wa>kf7)=-~kXC@I7##$aa@}Puvgy&mN-idiv5}0W%WFLwo8VS{sZ<LF=xrZ*NH9nMLpDKRCo4!U61zz_w+fGFmM6>Alj#yp;f^eoMWYl97wM5Kp5uMF;jhNa;1-4U?Zqn4Sn2C^h%$_0BPh{kw*iT@WrfUpv;L#FiEwz#JJwYs)UKSnMwus@t|IJJ++yFVCJM+|r^XtjSGpd+9q+EpGgFE}vDzU#&5KK{%Jqs1Q-%9Y(H+6U@(fVb?sj_MEEG;H>j>YNT7^7>@3?iDbhpA?dhgw3le?t{_HAN*6WJryI%y#@Z8s>S+EUKVW-ZseOiS=ocV#DofLI&h?Rcks2n_-`rN=LG2Cud8;sB_OOkXr5HpcoOaxOqc6$g6fiW-8(gggQk_@3MX-Sxih?apHoo#^%AyOLj*V$o>H-I%%!@3y1XOA(;hjHJbM8^$JKY;Ux>WE<PTOu)VDl<-E<4-$vXxk4=3gH$FZsrb$_PDjl=OvKuKEZp;x#ds?<-HRwCMk%Pq<;vL|QdcQ>a5yF~Z}B+BgVt&Z3?mV;<TXNVt#2KJ2X8?uEL`AW-Ce~~-C^S#LZbVIVrH6Sk}s9cLC)k>{wS79mf{fZtpNdJlWL+Z!dpAGz3N=>Zcbh!!R>R%NcF@!et#Jq;LSZw_FMbre7+j5&*?-G_cjKVEulc;COO$NT3?G2sdIGOgnF!2E=qdH&F;X6FBY#$I0VQ@B#|3u%rXp=AQUHk=Dv|nbw?);+o)|g$QNVlIEneGV>HkY1Li2wod+w6dP@$t6|>mhR0>qxtVlp52MsnoBIcd<V;YvO5Yg_y1A*D$Jie^T(JDUE3Y8&}?g==AjV5NrY)Oe+Sc!wG=~1v{1P;e5gO$I%!)&{%l<<O&_Lkx$pe!BgOaayEWHwXSqn!vh>8Wbc)2LDNWpmkS0BWPXGMckZpKe3}hLivVZX)r$5Q!#YJUNQuxu840EhzrL@GQ$3gXmP?V0vkVg3slBAnm4;yB5TH7ZZP{n9O#8B^B5#yj*y~2a!2kkGl3tB(*1@z-GT<i;3!bdOYzER;?evO)_A31d`eTGov1n%jp(k0$Gp8@J2m{j^XnfTO|qbJAQy-GatD;L>nd|p#lEng1P!6Gw*Tn%%m2NV5?<_z|49uCuWA3cx@&ndT@Lt9y(}rt4y;VZW|lS0CJ4cKHmZFrJ$`XmD<kVU6l%FZQ^n%v?nkq^ctxl6nCex(y)z2&Ym7U<p#)nT9bM$+nK<feG-QjnHAae?#`XXVxEJeXFxuz<-+{X^!rSsG|y!ghYT*9a(ZsTyD)b<kx(a#es{7w7DvrUd7NLD2(N3Ikr|!E2xH-vwK!T?g-=~<yFC&*9NELYbtXmx*6GZ2J;l7PB$ZvHDSrV&_)N-$?x)F9!=FG${K7qt$y!3<md5}!Waf)vd)ct&sdct$x#X4Qt;4H5>-7XZ<qSUvj+7-XVdUN;wZ-7J-Bl)rYaj2d;>e(|^gs<fo|z8Y)QFk}o7+sI*Qa8E2^sK!kx6D&FQH|I2KE&?O_xSt)kH=RuBGKo!e@rIS^ofY<zvGBKv&&TE)T#-m4G(mO?-~v(`_q8=;>gd9g)MqK{%Ft?CG?F(4~tCRN?I`wcbWXi^}1ogxt&hdB68`rw4FU>#tkGuF}re>XC7MaDoc05$9|7I-E`wv$|)H4n$9|;TEjD>EHBau%+Y$-*!loWDLX!zhc0-`Z*DD$F)V6^C7fcO0*D77zF%TdAU}FalBha^0hq;^cs3Y;HrsLc@-jovL_!en++Ei7`VNhb}(A~u$9A-rOGLt3V=Xtvkvva+5#5Lt?b<)?1DKZ@Ky`P2R_X@#zG*%4%WdKjdlZpYO(__XPJT!BS+nMRcA)MZf(|U9YKF=cGjvRU`Ayl@%g|z<;FPHK2U&4Hl@t6upy~|f44FDLfvI7d&4FfJREk|Mo0|MVH%sxjnbqfo)mRt391fLlbXTyhlppNsK~Mo`=o4rp%#j*0V-fE{kYY6_b^FSyY?p8TQHvu)RqJ@5*uYYgU}&Z>NRV6uF?yIQtLKf*Xyn@YEJg)m{1(B*{sX8-e<<_cAL>XbDtlsrd!FOuOqrfhVI|d`c^DN1hW*2n_)`!(8kVK)k~N+1qpL?>oayEGM3NkYnR5&7r{-QrugZm>o0|p@&SxyJLTeHm}?z}zL;2GshU4J?fG}RWTWq{;G^k!ZbrCpVec#0f!RYSz0z)V@bfb=;mcGqq%evBM`YH{E5kLNbcsvvh=@WVNUkQ7aw)$mCFR1Na}A`Np$-cr+%i`OP*aCn!VctCo2!kr-9CLN8zx_Gv&3qRja;cTk6OI2NpI?m>kx%&J|?Dm{l%OwO)ko+yHruobab4nv@*lPq>SyW0FWvUb=UdGWY*oSzpNzATT8FTwRCQ{gP^e5%b6@Et@1*5-VYonGq1ZY>mh2M58<>NJ?)C?brEo}iByL39gJcszcxT&K02V?N;1XtcsF~9wUuSm&hz4n(9}E${bUN3srb30NQ79zLm}Z<t!Y_LY`=Hc6<TcxAw?TX^T@F(S2!V*<(q@<S@g_0Ww+Gyx|2ZIKesBbvC`;~yoVn5(}}*BD3<a?Uz?b2<#=y~$)%!YPzxl4jar3W+X|f%EldORHnZjBu!4rX+j0b{3Pr7xCVHd&q7Z^0d~?j~p;CN7Zy>51&bW6<XfISJ)geQRtsEJfb)o!pH1LF0Sa4BFV(ot4Sak9HOf8JG0Fo(rWnnf6N|E5OTOL~>;(&ExS+2hA?9ZsFBznTg-zb$yG1;pVBGmUV&G9k1POitEo|Fxw#SrA}5i$$MVz6gN9LRxtAM%Vkq#O77j77MR!D2Sj+KDlSq_k#CFOeg|z!>gptVeN;Kw*#q2Lzm^22m5)iN1ac*m{A*e3Kx&<RTKN8;Oj+;zk*SUsV=`ntvW!D83DZnB`V)R>SIQ$Q&LCEgHj$u0pgk7u<1lU=L{(b+ug?GNoAcbEV2BF_e!5Nq;5R^3?i0b6o&(%sw_%HQJ*0`XL2waRwEZ0)?41G8XDd>2|@6oL;{Oa!8@<X(p?uq!w#|{bXL4wp2+tX}%7)D$cgyK|xLJ>0_|jN%hqb=PyaX_}pLX^oYWDWtb-mjrqLp@|(TZa9JZxa-@|+`Z*;|BI`-YTPhW_B8*1EGSQYQ4Z!P0v20TDOqwIjPIBRzJ5x$_O5^-C#Ka|A3e`@ke4P48h(0FkwVk`v(W=x46()TVC4F$$wVIX}n{CVm+C{?DyJyH5W3X=F6f#-?8H4+1c%Ft5hfaJ&aUlTNqFM->B@LB`wNgNQ=o5uLIg+x8(ZM}|2$<ORo9L$C0oo+!FD>|_pO2)8IZ;8XSuKI{)!ktr!|)Od0Yy0FPw2)tm6PXusOxK@nMy~UO#|C#k5#582FbCh04`#M{diccWZa=m3h#<5aXy*s*!?m@g7rZV0#-z~Bqi$Y^>k`R<9+cMDX?-3sgG)HVMkC)*_cWrwyhzR#<FGgcwfQlPIme}E>I`RGehSkf!WwHJ;irBwV$EUh)8*rSaF!640@kT;w_xU6Wc<=NYvu1PL5`ybtC9kWs_Wnpk(T}11YJkO$L6$O@;crJW#d?qlvTgVb7OFCy61@Ntj`&QI$^i242OYbgz_&a^B&vO7G05C$Q1A1bJ8v+O@to8UvxC+?!3Lkdo>5vvIx`ApLY{7LlVBz2n6@qEeWo#RBe)FFGM=oemcEvU_}D@fEGrwcwGcwv0sx7<f<mhG{eDDpQTDv&~{`m-c7(m~6B|y;FjnOqOe%L(|Jdgqzb?WiX2n9ReiyR)|U<S=^s(9=P@v4QI;jAj{7qYbZq2+|3lqn`^Vtgo|5cye-kQ9TXV4`&`4QAEjfvk;zo2z^=l1ySaSf90S)P0W-_YBs?L(d_ixPtHEeSKaiF1e3cW{%GfM*c+kp)1SmCakux7HhU-kIKH`#%yf-<|?3!IT<u;;?QEbYtlHna(TKMCdl(3G`jGC%UO6dq}Rp(=Xm~|GLGJqqPD-@o=yK$5C=>Qt8cwJ<w=Pqkz<`k%sEH)rqNm9&lzRd=A6ZHz%#&RH-#yc=0<bWNj25WsrEda@w)MoJ7G+H80v(YFYNDJ&D4rBA~p)D_3)PV?NYVcGhD*J}Zhf@R4H$50<VH)b##;5m=i9J?VmU^?&&uiffPn_NGtlzAbe3g_yo`}IFG#WKZXWVL8W<8Qg(BaNmV5D6PS(3vz+&i|dk-8bx+&Lql>u^5WoOB1RE?S+Ikj=tc?~&SM$-AoJyk=N<D}c+L1;GH)VD3xy(&<G=O3asF$MU5UGE#DtxXy{|`BDcqv&~A4@G{<;y6TylY1Q-D{8T)+<qULa$OE2DM@BKSU8z<nm)>3OGl_`1pVE4j;W->sr-;X0ZU{vr#T}b?`iSlQCzuOcRf}5o(fXO}2TQeWja+gfG};z6RrM5|a6@c2I_Oa(94~J4j$dsKV(pwY8T(?K44F$b?%v2gw{j}ufO|0~F@9vot&}t+z)^x8wTwKD*Ib@6VrbAhV-5y^E(S6Dx{)5q*s-78X10<9N+Au-A7bW!^mgSSw5X3|%NL$B#{(l%3zbI2TuHP``leA2ZVA*2Zik$I+{o|hR$eL*zywS;yyKL`Z4&_iaW69<Q*m|S00X-iJ(}G&$^4|7NANnLDQlrF=IaX{Z?{@g)i+ZTx#;>xq{;&j5Bg@QC7t#p%Llm*Wr*msnn@tUtiI|N&Z9xJ0WrmLN8aU-so3ryCQYtO(R>`V$}${W5amk4mE5Ni&2R$@0hX`X3THjNCettEjzu}uB?5-uqwvZg=$-_Q>v~N)^eC?6&1`dA7A?(${CXlZLITqsnCaSNnDzNrM6jy&@a?MLYS9V4ZBPT>hPD>oAeKoM@+2s?{HbV2-(rzyX3bR&GXU=9H6j``U0G7uSHRt%K=V28dOhm2HUnW>Z%_(@l(>L_=kxBAZ9C*(z3?vi)ZCPH4}54ay#b<ufpk?0^+)kT$4-ROg|U?xd7yS}S8Dp^$z}7T@Kt5M01^t>T#aj4C9BQd{?0U3<Lj%0R2)$4f;+Vu0$!9l#oVQC7~t|;kQS>WWKARknZ2i3+6@W+n%OVi%WSb_Z+}F|wlgG^<UJY4E2;8=1uTHu>g|Nut<77(QZ#Lb`PQk|T5Ew6+G_ZNf$lC2<R-(FM686=poSfa`xw}#h9Pi$oF273-N~3nXgaY=|0Nlpj3MF3hL%e~&8_!b>gekA5!bRG-ulX^ZFzix)~L(P0HALlR;9C%Hz+uK*cY^Y9|@pQVVbI!C-Kc5-9`^1er>dj^eJ^150VR>>!BR#o>^00OAJ@_Wj)^NnFmD=9Ams%&?W~KZFRkFSsu^8HJTgZ3SgJ2Q$<@Jz2>B`ohm2K0jWiDQ#9!XV{Quey2DK6v}?>=(S+_z<{-7tGO<V%s;G^LH7pD9VmgCWO$fEzaw1@Wr|P6!@|vB>^n~@x*#XGWXLp6{Hnro<m!6ZcKx)#;Lr_dF71xp3;m~i^%gr2DUXWE>4f@L&lo{oBn;p(6d9}_{a(o&PDp|j;e_D3xM-Ul|f%4Ftpqoit4>sggWQEq|b4F&x7#+j<>48tc4c`n9yyV`9=7d;mjUHmaSWT2pK0_(EbMe7Au?`~f*qp7kW2`w{pLNl_%VNWGcVb$;UeFBeQc>Q^wRBh(8tHy0nwAD#J;TF-##s2kzdYzZxvaI6$*JqZD|5GCpja*$Cu8pQKuI*Gr|EcQ)Wk&Oz@~D_F62Ucei9UhR>ySryeSn8cX+6{KMcBf0LpE9=>n1(Gh~Z)#~^n-t`t_$K~DF_7twyVZnR1}oi>^&O>w#7-5rx(?P~teh@_P{G+hdNxNI?K|A4mIO1}VAxBcp76AgO9ST5q}hTFU{)|T}W-4wx0q`%(uOYz3Wbq@KKC&g0;=7$HcU^|m-+C+M2X)~D7J$Nc7ObQ7ECx^kD9UYFls&qX2mPM((B5Qe~Z|&M-!8St8cGCM8s|~|*>^uV8L$@n572sqqI9zS|y%4k-54dx64uPZK4B`$;yfPs3V~J~xQu8t*uHEfJ!Hp{AZb(umKve0M(<qjRwf1To#6)Oq$la|x2(a-nSQz#;ad@2SmV5OWaYSNnqE<V!0CeI%Wg(^zb;l83gG#%(VMWHly?8#?=9y$Xcm_Moz%J>ji}i&yU5(;Fq_@Rf<ec+V=UCjbQ$wtyWI}o0woMPEsh5e9jhs)72SW2zkra~6Vlf*;n>j$4@1g^V+n@;_BL_4OG>Zg}gHV@UrM<~c3ZKG3nb73G%rz+YvITFvL(83NZ!6B*D<L0E>KhN&jMM^(kBE*d)WT|2hKD6axwJD~rQ(D}r=!tA*I!rC{uQ&+k(qSbSckS=7gt4QqgY1W1H?@Lscf|jOc9mpq@TzQBQhUdM(6nj)a?>WHRLL0>}*)8v?3%0<m1dN3dG{Ip`D!sO8F!kDz0+V>NK+SCeOt}pCoFh&3P>Kiioc^hvFwt?z@Z4!Ky?IJz#}ePla7LlJE^`MC{-$`7F8QAB_tsAMNcO0XN1`IWFxlm|#I{NxNzv58%0Ua=OpAWx1AuheMxHQa16`UIUwJDO%5*#n_OOjybxdE#=)9<jgLAGK6tVZ7qWCb2Yqy<A*_|z8STL;YMC=7_p@QWAPp^E>*00n~^J?p%F9>U3$hW&Prp7MT70RVY&fnxatJAR-A|~s4^rZt=+*7)NprM&7S=Og*RqMCD_c(a>tal(GGilyQr$G(YQkTHjPuv)!v9;88fQlc`}%74TP8KrCDX-qa%=8?pevE(8xeb?j-qKiV&^(Fe=xaYA2!^v$BE^lJnKh;8Y*Yt?W_c$W1tg<!})gwIRQyyOjA68p0#o-G*B2Alg~-HDT23w2M{GvER+t6UjVqh>olo+U;%e9e^U7=y&nvcI=_$u_(j&ZN(LLdv^nDJW5BaM?)^c{$sgjuomP;jLtys`+TF(84Zqd>q%ms&mYWKyUJlH16b0>aKHl<5!mYNcY^`e5|&`;oRg6uS1ZHlG9AWZKx97jB*Mk&9Bupa2$*6~qL-T#I$1u34s-E(qDUJXdODqJu0@7y7yBwTEY?egsv%Rn=MN~=0-0fK6ZF^-O__C!)<X7FrPT<W_!Ck%8yM~=a!B=Qsv1orBX4m%vrW7n&+%ezlx@kLUTj+STi#(sIf@e{5N?mT6uLa7Q&=w^-?V38Yt__-sU<bt6??-u(&=SFgI2L%XJ&r4&@R=}C9hA(prGib`4d|9YN={In@a5$Tq4TuJv|aGZyIEj0yMSK>U9soCK25x@kp#phKp^wGtBj<z$mnJHAmj4dx<sL8lAvWWvic<CGb=hNp^k5)D9CGm1U12cjg+R@R5=U$Jlu$<KAtN!p_yGLapdvK{QcgQ>Yaej1M99#J&TB=Xq)z8U#YrIa!JV9i$PMW2;CNObuh9!m@FqJuQ7$Y;q%}rKfsA<S3m^K+sR*xk949>`L*|J~Sr>Tk61tn6P)47BqQRYREtU=x*CBuLqwe`9?ONEaVlTcbc7JSnJa3U=xeG1|Uybt^5KNJ;E+9=!zMPffJP>w#V@PgiG$3oz<e2=TIZz?hbn~W3}H#2BL4m==$8t_4AoVZs9vux>_c`F=iS1ycoq#u3QNyNmf9}AIiaCq`H8bX9cE>X}`d`tA%wueopiolfxL#a%M3f38|g_ekm`{frw?{r8dAc4rCo$E|<K|?Bz98JY<DVE29s&4Kx`yJA?SlweXvm8SS-X*uY{cH`36Fz1gD5iBY2aV{HbV$K!k{v-WHg{IVA21*Mb3YXUWbp%~a;3N%TkV=e>Vqx_+=cUeWC*Ds9&$?`VmTk-i6ms2X^wz?W`^Nh$wnNh^OrArNESez>ZFY0Qoy>2Sw+QWz-cHkLR#-<V}1_pyc3QC>|sa!dA7RUNRtD%Q8YVeky8P5zp7)x(qk1t9XgErDeTTH>zO3p`;tJm>%7f8C$&DXpga?1>}fNL0#j7G#2iIpnJd?lH+szan{a{j6Yce0dZ0HsB$$?WR;v#(K_9I!QRX>n_iStk!O0T_fmhoF}(l<HN%8#4_E@FT_SP}mw$b0DY3Gi%wXOO+kg-h)k8NlZ<%i3x-l?2Xf;Yre>w!smfGUp3vejS>*lmD?RTtyeyp-fqw4#G?#A?2r%D><!Gdnyvo4=JuEiajtbqfe+8zhgKoBJzzV^orLFf*EddOBr&ovSs=MDg%*f^=nfor3_Y$`;c#Pdmc#Rze<Do_a4D!H%otRq6Uk~>%~?>RL6-tYk?JZU9L+}-tzAitM*PxblrN|Dg%}(U4nv;JmaU9ok6oKbw*#Wd^{M5lO8G`bX?NlZ7PZgIKy+Q4^2xw_K9~7GHI_OUi%>vttxCJhrj?i$XDC%$;iY)jYeGm_M!h<}tdH0+!xfZJ>S(PdJI&<|$2M5cyCbmRx$9=+W3UYnP8(-6nw{W!o-m;;xP<Kj>9p9%-g3Lllsi2l+0m5IL8-?g(`3GHm<hQfQg|Jm)nZA%CsV}ov-QZDE2~0R(Bq0Y*)DvR<Q=>6C@UC#i0P+%Tqg)O=lSu*oD`EYiv~EcZ+a*T@~sD}qS_H*cU7CA;T2{IX1VVsbHR>x?6HJ0h%7_RV{|;odFP52iH9<A&$)yZrCf2iVtDBc+4~JOfvFNH<>u|;5*$Wx&^QJgB320RmlfYa$+tPMKE=bS{u-TbQ<^^>+F;hoT!h%{V6~jJm|c^ogo;E3BU})uT5-Ki$98c-nGNc=lH;I`_bj!VNGDA;d!XXW40fQ{PA?H^mUbH+t<YVr*=BFdS3UW9E+Q5K+T5jvj`j19@l}D7rRkMg*h?iU=k8*;HpVrJZk<wLJ&Wl6tRBr_(+((G-aw5RPhd6QN4nEs0*|?2KYo@<R%%n*>G4K~2oB}I7$1~2t#KU{W~dg~k&R87qzymOMUEbx85Pt`u|ElWk??}?ba<qQBv@>k36#a`%7x;#yHJ!se;`1E3@#UH^KLViW8z!6FPv7<7{)5#BB)iBQFceWmTR;*YA;7fU|H;@hAvXEomuhZb*0^8L>y*ntL!F7O<b$-STv@ww&4!#b;egK<WdcmYz@;X9x$uNsB1vwaA7NGh&+ppV@Que@kXGzFD@b*`lKzQXQ;A1#w@m=cOzMDcH$aTz-4r{$0NacOt1_=AUIz|Qe)NYkK;aXdk`sB55&n&#|D#PjYp~}m*K`ymfGYKy|}eW9kA$nB|(c6g$7;v5Ye_nI36DPTS%f^_PVGQ0HeUPHh{yeN}&iA<`tKo7@vg9k;`>4&;_-Sl#%vSOi`Qo@p@0&==0f;O0<AgPqbnNH^I@fT@+hIS9!H^dH5DF$Ci`%Tp{A4ARLrXI~(=j<oxKLtU{x9;4E^Md@4^y#frXbE{}HfORdYZgB!<2EwQ$?#+i^>fwSq-v{{CTL|z-<>;7R_P+=hsMa;BMX{Xfn0Y7e;76~@J)3n)jS-D_aSHLCK?<`O4VJb7LyUP4BxLnSq(Rtq^C!`MSQk6m_I;gEfzItrhk5Ij8sKU35c)349SA8+JDm8M5)K!7i-WT;1T;&CkN`-@|f|ic6xz4dYr3#5)2W>A>Q=vnj>RYc8wKyo~ZXQQ*pUa44%e7{uxuF$-jz#4)Rn0Ea(|nr9&c?}e$Kc{v#a}kOTl}2BS{Wc?g}R|*QH*a!$!x5IK~;Bq99CPJhb;DsSX&Qmf|73=B+*4-51_}=iLy7tB%WM!CkA9KBk858W0am?x)rKmFsv(0s7uZg*P)eXy`k9{p>X?dMZ=~wJ(Mg6J!lZApDoMRt_xgy2Xd|iHf#%7oo|-SmfPPa#@WmeR<lAVLrTZvq8y-^NNWzPt7WLnrdGqiT<qxH!lt<cOT`pXImN7cq7n*;14YS4_AQsc8>xnA6Gaj+L0^_VR=wg?G<_eK(JsVKpVGrI6sEaub0&B;>7j2pvG|JTB(GU7iTEIJ$I}NI?sl!gyiJDY8)QAAqWw~ptwbuqIDuL0i~*ye;DT-hF@J(*%j$Noq72T)?VU9hhM7vK6W#({VmoRFi=zeY$_&xGaZ0HaI}F-&YaGZ7qs>?o3g@<9t+J9VYLRYgr3pXZK{aZ<+<EA2sTC5u(^jc^2HcA1FY_&Z42)doO>{n5#O)H4vg&eb3A+|k$;Cz_SH?XDsWV6KYL+g}ph9SCxahNHWTQA2>!?ftQqy@9XrK7F(y3C_R(6`s#=M!DGF}?pkzWaLVn{utN=&I|&TPV_;Ym#&ivGS_is0%n;ZIt#%>-RUQ@%3S=_V@f@Qz6MX~mqohb1#ACRPe9ZTVd@mq>N@auw5xMr*BCv_K-fHXuBB*3`1G&BL%>SoFQrJUZq=pf^=8;-e_n?BvmnhE%bo4$ks?IHtE_+Z8$sZOAE+U!_xJEeDBI7>-6wW9vqHy<r$HM$`3%QMF6!JYP%bfhmG_Bte_dD8KXB4ym{Eb<k=k0$9TUzb|#gvzA<e#UNOv&$Z+-9h!;0`hEoELj@ty_pTc&w%9HNZ6Zg3WLT{R6a1<h7!CYgQBStG?P?X4liBjQU!n@@p;QkFopEkR_`nS^Th!=b=8SC8DSse>c{A!*u8sm^N8`@HS`F(XrtNq$(-Ib;_+!U4JcedxT{h=kIPa@V#by<sxx`S%V;8+az?x+@UHCXnO|^NNX6lovT>|@Xoufelop{qsd}Pm@?9^}<-}uAb71}%>;t1STgFQ`*XS)<e$UBVPv$f!OxsjSk*x2MUEoPA)p~5Jcu(Oa!>byMdyq=@JSNmeUU-64vz^{|gz+3i$9t7!Us7!GbtcJPd!7r$A+nO#rHGcw*7f1eig?C3Y+)2hj4_iCse6vKSv6)39@)^rbXZwVmuml?Qt)9xQj-if=98E@B50MBG8(VFnd?FVE_T-+o<*Is27qm&pRRM!QqLzi?karj?skQnsS>0yA{i1*-7qjG{oGdBcAT&k@=5$C^uqmzw8;gV3^qaY{5C~?Q8+VV7CsZVhmP-}^jiS@$F<hz6wa`r6FHU+Bi_vYc&}}ajZ_m;QoLV&2q29_&CqiS(NQ)k^Z1TL6JK|#lTW=z$h{ns~NhTI{3-JVo2SAyu<<dTAzTkm@?jMLpMx4(LX^y)oMk$fB3_yTRlAf%mb;|4r>b%4Py}d{69b7<-UK61stk(CGNzt$_c0(t0D3#5E=(X}0B<R^UQ)N=Di<mp9*%39e-sD-e6<hi0oMl2f53D7qnczxP&6s4*%7Qj>yD<fx`;A4?EY(oB-&`l>kX7p>dvY{A%WTuyS}g$c3gA1In@GDfPsT>bUZ6*^kh8o@kr_zg-MYBP{XhwiEGCf+hjoYXnza-*u4n-dbdP7AZz4q;vLfu^KnFMHN>sA54^bzY(OODd8KY@A)!_V@UZOZ?x8f}ysqChh!B83TbZ*mlCFn^+kWjwCL|X`$)%$VajH0{7D$e$+LJG(y7RYoXiTNZ{_O<te7?()6Hc^FkXSV@W?nD>scwm)FR}04}o=#=v_1Si8BxY)<qh}N}&q_%<xB~0wJQE3@tKlIH&4b&5OWIIS>uBf(wi)4#W&-rqQfci#&1pts0Rn(FaHj6(+g%x4>HAF`EyaztJj^X373gHL``idG?qr7E%lQ(MqI-ye)Uxr$#?t7D5os5ji9nzc!nU<>K2|)Za4%!F0PDDcT&qSuI;bb>q}+|gNUL(r4@+!w(lFLh!D1z&lAD^$I)K*vm4iv}a<~}F5cr{NxqT=w7Cj3*&kfP_*%Ml0n+ba)rM!oBXNsr3zdSx!fgFoPiT-9pWRv6o0?AD{;~L;Jo86`t9>lvys-2d*Ern`8xVShD!X<Lqj?cio8&*Pfz}3$0*_c-<W_hzYUw25RU@qgsDGfyS1EgU42Uoe98|><8Dvgg!JiN53oix2qlr@{NA-f%<)f0>-hts;ZyEzBjBy{p>8x6?SjPRr@$m+3NFIi}h-*xi(nc9Lq*Fbe+t!^+g1*nnLT)=UrU+~BRZ*2E`KGxbz2XiP>09!QFR9AwjK~X+S>>w*xHZ~|a%%9aTtZ6N|(esqo-Uxw3>*XP_^`DYdK04Y(xU|;YA~_)7cXwCea3V8Sw?;3W(yO^sxVN@Td9Im8tV(h>BCOWF(2h{y+77^cRF6)CwK`(5X4?$_HP&C*&LAt@?lQzGG(>{y$;v1b+UDdFm|k~ht-O6@RrcpFJHs3z3OVGb+ZoUfxqGN3ktZ=}<V*Qjobk>!Fhw#h35uNNF~Gf!offvsm3M$}w1Y8I(imi2>n>x1a7gBt)Dnn#iAr%CJ7M_F2NVJ+kFdy%rB)=HOKZl6PMeseszspE=i>i@pzpUk_OFJ%2%xVJ^xywAD-pA5uh?*|>4UfDZZF#_+RxU1|JRHC5B$%I^(s)BKGSqodHv@lfP8y-WeoP?v;C)aI(@sYLjLVlCmZ{)SS-BbcQBv6T|k}Q-V((&o*mnhifxBz)E@6vTJ2ezXchYTUiY2w*Ic$<B*r!Z@U>VjzuNeQm14H{3f*XYZC59g>}C07QlpC3omstBBin0zF+WH2oB7JD+ivwfL$&|t_K55-S0rqtZ)?U`qG?mxB8rzK!&VD_{r2{@nlH}sL^0cVr{V#K4f0OYN6L%6Sw363!pvt0!lvjQYPZp9^(xikZ-KteE@g>Ek?77ES)yLNGWN#N9rUA6K5%)ue(%Asi<cS4>fn|V4EEd0nl-<@*n^ZI=*gxmvCuzPeEi~t*LX?ODT!w9vl*V&?-QJVR8}`s>E-hFy94zR9CV#$59_RI>)ZZ=(slI?>(zd?>Ac{4LrGJDK+Odfysr8J*Y(9$h~6hWqWLiKO$N@#F*AzRd07Il|G6W(KG_62Q|!&iD$XCbNiVW$oB1<F>z&Bg1*M9tYHLT}HT|~cBANRe$bs<VwVmyDUw__}ds(`qBu2AW{<tiaRmPUu<J`-~Ki6SidU=9<U3vxm6Z-iGRixClE$An(zXNrf{}I-s`DiR<1Db1hf!)M_Tx>?N(|iYz{odBGB2cEy^tTuI0?_{7WYV6<3L5(YKY(<Eb6w&9zXNtgHCquE${(O!#%-WBeK#_n2)Vre;Q;#SkmUUFl6VnV3B0_4uIQ~tmMDSeq}fG`H)(u(dEoHPB)&46>lAjcu(ZxH4!Jg_3$+hyy$cQcc31Uh1}@`whJUT#x9#F!y1asH2JaL+?3v5E@9bV@B?kO)x1@{qXO8AoO5#}Xjr70+K<JL<O2&^H2|sP>{?0%z^MCwv2mbTtla8)XA2guz0z0!s<cRFsiy~|M<DS%2^MS4Xw-?i<!?Csd#2>J|nVv_GI|mPFuX?%Scy&-dYvG6a^T+<@U7<9q=r3SZV%U9ARb}<tOV3o;+n)o+y<GnO!b!d2t$e*$czxtgrD)c%99g~Fj}v0Qy<CRg`Lt&_c6R$L?}x}sph)dOhcjnB<ZPvHR};I<fo#1Y(9f%9dNYj+SZBArxuj22UetKO_!|%PY?u$TKiTk;elM`ECUBwT=Q~Y_N3*?b#Rp_>^4hU1GgDcG;@{+T*+}=@c@f5^?fI*He4Tgk1j&cJc#BY!c#-*gT61+CZ?bf7IiiFeMlTPEi>Wyaufljwp}yHE6ZB{jH|Wo4)>ZYd4vE`aZuP$66CqCUw4uCH`{Mza^Va#}-DNtwd~m4Om-nsVX!6J7PPl9S+l%kr*WTWJ_Ek5*7!t4FRC59NMX>w!5b189e-pOemAPeaEPvNn{T95zyR^Pt1MrPsd+o)nzB#rjX*W~grFS2?Wxw+}D{A1AT6kw$zc@PmYO`GJ($VpCd%pNzkcYL4+w#=a**{9+5yv|_-xXN_Z*)FnJokTSS<-pQVBbe6j=kyC-rWuz58VBDwX-r+e|_|C4inB2JGy=#;E}i=7qWleBg_*_8;KnySmp^VE7*X8FNx#@dcuj_{+G`g{$HW|l?!y-*WC?1V%FHd73I4rT#$Wxc?$xUkZ@rOa%{q`&~5EfItw0n<!zF^NuD(LsKT3Nyc@=w?l1n}W+u*a;Dd!+SMt)`pzQ}q)*qAVJ89o8+JN3>+=l=8lZ{-{t;<|H{N2{tWkIfA#S1fg-}U--Ib&~OTTxBBD)}QoCm>!F^>r+M!u)|3XUVNTaQJW@uX}uLOUK^gE?b0-*}VRdh^x5nQNwYZS8IQBns0`BOS0cI{NO^rw!j~+g=+cr=iOlLmVZ;NGvjF;d<j}lZtf{u{VG3t0)qVW92kESqTaJ%)pqTUm0lhAL!|pf1iQ?3#_xTBzYJiPb$^Utcj#Y+uwV8H9^%<ERTsZzLwq3p*YV6I9(MfB2WsE2UWv8Yah^WX{NsJz&u<Sy7aR_?_k8K5n;Tj0Ih(wbW(+IZx|&Jy?y3$amOLxvI^!jItAOnH7jrKaiCz`2PKw0qi}U^>ci<%$esCS|vx<P1u(K5YoU2`N+>%6_EJxYz1(7pyjf;<2pyLp=rL4R~!^;Y1uD!&N1espjIhHfyIlez&S5%oXXx)kL&;6T=8l0uJvxS~L!$kl#%KO?6JN_muf6|UCw-V+)^RYTao-}i3|9y)X&aYq0HU?$;58b@w(hlmk;_))$9z@^b_sw-(jOsQe@tjV77C!uJC58yTPjQlS_*!{fN}nIWpO5l*F0|j$`YYz2UzXfY!gMIR)$De%5xN-C6_4$moP?!Y#PQdMVdOIG2;vIo(XS{xy*3m(tJYX`%f5M^N2%T3If>D`5xp_+pXYf0Je$gU0J-3>jmZIE=W>Q3u=c)o_<9yW@UsZo)qK6*{#pnhjPJRQd{^_8Y1<~hROeTUcr?<toaI(B{;^E_0`arG-(EcEj@{dW;U&&?{etid)%~aD`I|n_|2d;{YCIEsFY9a<{On$DU8Uc6e^>IO`~T2oxcD9862mlI1+P+jl+E3bK-VV5)yLll9oaaU%?A>$4i~x?7pK2&6<tN^<Rd@d_n1oU?#bfUDtO@Ts<B%VZ!i4Mwc~JT%f}hB|NG-U{_`dE6pXH--59KP?R5RYx~|h5*M1d=)695V{_PnP^eZfZ<U5QHk>rWeU(d5;@(wPM{KV1MdFY#<ZKht5?+_mMmZP8Vl%hE8wX4XVbHbYje_ll8{Q2V_1pfJy`22er%BQy3LbVB>sfP5JOa5vbIf3u(DCzgRMN#?fEvJ0w=3WOsXByh_Vh)$7w@LPNXY})2QQlrATYtY{?px9^)34~a>jUnxp?;SZJnfO&io`7?{$r;1#Xk6KF`8~?RL{F&c1@EUYrjIf_raf9llPGO+W_qp-oFU~@9^H-)^)>OS^ajW>Plqbj`c(C_O|wmZStAncSrU=J6m|D_HT^Yuq1Y`gSYPT6Q~=u|1ADMpZYI0yf^H;cG)A&jDJ3c_Un|ZGkDPO!wbmK(OrTcdMFObR|cG71^Fo3XIJv$%D}e|ap>po+aq6>(tmP8Z(H(*gX}WJdAca<&165aWixb{^}B-WQ|A3V>-7!QFCCoo>vWCxbMIdrxjIL+&~<Ju+b!B9N;Q8un0{RF&kGWSzr*)+_G9$=cv=3>OAxjnPgf}UR<l$sI}rYLX+2yR`qw`%;Yjq`%fD_LXU0;hVE)U2`!Fc-j6H-tj0iTv_R!->o#F+1C}a;gu3@Ih3*CN>1@8k(O1*$V?*sRhv~ihe58GarW@p?LIQ%^ty^OJ%=D0sy<vEU3?KeS($M+Y`{2LJXJK}(+DTShKy*{jgABUe-z|IP%X-F>}wBcu*kHZ(LpNAZ-ABH0K(9PlAxO2$;G&r*<afBRxfAhvP9F9DX-X_D}gU)n&liCi`#yC@0b>`Tz1IS@P<eh}vQ4PJkD>sP7-`_Yte0b}6%^3b#q1?#3%@A!DVLrW!zz=V~LVY){zq+__8Q`TYE9tUozFx0b+@{F_^E_~=;Qz4;@k@-pD&#(cVy>;S%Y$Sa?d(dUJ><B#-(Ljzze&Z@ajf_lkuQCQ|6g=o9y=-*qW)iKmDs{`u;0@gr#q=Viu98(;s3XprDa39_pY7p^V`{~tW&}>d#b#<_GNy1D*VrLy?p7CJBR1?;*XWtADiQUU3%D19OAF(%zGTW*z>3E`lSnUY4U$~Pph(WeecZt0{K-a@BN3Tq~$_@&8hX8Zw)VZiYmoo`}Onz2_^9&CHz}xZtA-XKWk4h<^oU8?g8jM6aSxH3i(CL{AOae8zG68;4j;L*KX^>rIOpQqS&5G(%;@8c2@oH{;Iu?S;$vOj6Hgj?=2a*%lVp;eK<b28~7dn&B$%!5AU27?`8N|xFTg6#7yHkiE`?s3-=$|M~|189IF2Lw5Kk^PdAsY<bE;p`r>)+qclD*_<S|*>2B29)tX-(PCu@)lUBw~IP|YpzV*M~C;bY{CDz*@7J^JYpN(JNyjOK!T$Zvqe290C*QWmO8FGoTJ?En_|H>9_1`d6)@Lw-@v-;bjuTm$c6nN@NQgiKcqs6A?YU9xDl>3hIHu|Acd5<9Avp@P^H*YP*$9q5TfW9Q~cEa?Y{o6&;uT#ONBl1g?xqCbSOuk9(ZSaff?{@cL$-|51WscM?ORr}4)0Wx$s@oWJIoG%v>St!2v(`5@K6nWy^}gLU`n7NPbQJjU-G{XC)6%#6@zb04MDpR)b4K~_;vuzs82y}Me!VyCeROHH{M#q3_eB2BC#}i<!BOi6H9VZ9KI45qOa0JVe()!^>i<(C?oC1W>DP&u6ZX66J}+AQi5rLe`?ZdzjFH{)vZ2i$(SGcze=wYDgZ&E_j`93z`Ngn)z0xr*=OUYP!1Q_T?JU$zU4P+v-Z~PWvR6T;Zg&zd!hGZ6W9RSY=|0Qjx#e=1`>_Y5v#NB-VZqNS)`f!4!~Rdz)Uzxe%c{#o!p|T+5bOx}kF<Vxyz1-fmp*FkZD-%kQyxHnzXAXL5xn~)Ycot!rqi{%ri_7`?Oy_v@creb$#T@?<_#|`SXE^i2mkJck=aX^?<2su^M7~1zECf7!+crTa9LGRZN@QMKsHcO5llPK+9i*}%bn&c5#OI-U3q)Fx%SNBd#BB5BRU-#2c*wtGZwV<<uq-BVQ2X5{Z(*x{X=io`RB_M4|0BViICIkbiCqweVqDb2z>98y#9nfxBMRAI{4?ZEP!9-J<xA2TiiUJ<BZ?C_TR20!p!L>Jsf1*uCPRc=s#cf(I0qtYS-N(>ZQ850g1x!Ujq?&=1UOazo*0L2Yv|y4gWO^r<L{<j2QeijNpChQ_uL*QNMF8@+NJ^9v*SOH6~ww{tm{4oIgNu`klXka%-&L2LhiLKeR$$KivEOd}wall${=YJ}r6gsXrLiug*TcI34@94tf8RvyqSIBJWgzUz}7v4}EcX@~Oq}AD`r3eEmb>^^j@3*C&5CU-=)Nt^Da+#r@J&S&=uy7n;(R4sMZRY=^hCcaQUpk?rwq5wR~z-Zq>Ii;AJrOG;zyptxH)T^@bOKEhL3fx6x0bi_*8=`{DwoJQOBX$b61RGNd)E^TGQ8UOz2*qE1WYt<cA|8U&%H>WtiIv%DNN^vNjT~~ZOBz{PD9}>^cIr0DTGvR+DZM~d)XrFS{>+t`kEcb73*ga>He|f#`p&L273CXFBAMF0}>Duj___B?!18>(*oM8C<GNxUctj}@rqsx6e!g}(#f0NYy4-d32TDqKM|LIKo1G={jbUnHLaAJK01bzGMF*x+`Ci)Z5uK+szi~F2Umr&lK@Sn4j54^m0+;7W&--G|;nZHa6zPhkx3+nTPtK~mubDs~^o<BhR75TnDK>8XA^!aL>roHRnQ8DkA5k5)bw(O6Wc0PP4AgC<Gn6pc3;8v7<tU9i3gU=<$m(`3-G%p(B^-S;U^6MA5^XHSm*PmaMST?JdwD}k5`nPKf5Bg%|+lMMo$p4J>!{gjwu2*Po`g!I!@GR2Ldb%zDH}$02(Nun`3-6JFX0=Z>^Z$BzKHh)qj6c-)*P85qXQBCa5PmQ4e}6{tyqLR2%g^n&_tX1Ndim4Vzrg(MzW<Ew!x8!4Zu{Q?`m0_45R#s2q$h3yN#`~~@YhR!Er{z<^wZKeTlf$RKVFe|{rMZnUoN~~h<N?^3F!x0`GET4O^d%q{pl{o`xh*4VNT_)efqzu-`-l2_7uBh{POhj2GKEu>n=^)x)DL!IXHws|HeMQ-THX>++n!A`Dz#ZM=HEy^nXVA@y5zmxc}V(_Ak&r-iZ0-rvIg}{|4~my_!#eKimbphSO_f3Hf%1YNu3J{|$Zq-cG(B7yYS@{!<I=A>O|Azur5^znJ+&V16nCuSnf5U21zN)?Tiq%cZ)zeB8+2z6Rw~mf>xK)?Q>uFkh&J^OF?Lf(7q1RPSGnYIlHZ>5|54@}=y4af+*dX>SeKz@?GM+BvA`?ALoo@kL?T^$Vq606P_r@cpfVGcIl0$1ih!mwf*Z6YndY_x2+1d|+uq`m2=rv6uK>8eP7?yL?FTH?8e2`8s{kt8{ww4(KbzUre}EO_y$_^VctmT&KjP96$AVtor<k$AS`sIdu`{ho7cksK=9AJKP1swrzcww3Lm<U$1!7kaN!SSf+efc{>rg<G*}E^7-}UF6v`j<eJaDt@`p)|Bn|uogMnC&*h&QRBxXjIoO@gbv_&}y)^;8_yF-Mq`&@j<Ez<!aaH}RWq)pAd}`JG;b#DDpXn4Y|FPdanajt|=O2E!;}ah1+3CIi_{;r^s1F&^`%k=l{wa<>eRKa2)cfzcJifB`+W!YOzN9h"

_M = types.ModuleType("_hybtape_boatlee29")
exec(compile(zlib.decompress(base64.b85decode(_TAPE_B85)).decode("utf-8"),
             "tape_boatlee29.py", "exec"), _M.__dict__)

_M._adaptive_market = lambda action, obs, step: action
_M._FR_ITEMS = ()

# ---------------------------------------------------------------- market model
CROPS = {
    "WHEAT":      {"seed": 10,  "first": 2,  "myd": 4,  "interval": 0, "maxy": 6, "ongoing": False},
    "CARROT":     {"seed": 20,  "first": 2,  "myd": 3,  "interval": 0, "maxy": 4, "ongoing": False},
    "TOMATO":     {"seed": 50,  "first": 8,  "myd": 8,  "interval": 1, "maxy": 4, "ongoing": True},
    "STRAWBERRY": {"seed": 100, "first": 10, "myd": 10, "interval": 2, "maxy": 4, "ongoing": True},
    "MELON":      {"seed": 80,  "first": 10, "myd": 12, "interval": 0, "maxy": 6, "ongoing": False},
}
ANIMALS = {
    "GOOSE": {"cost": 300, "struct": "COOP",    "first": 4, "interval": 1, "held": 4, "product": "EGG"},
    "COW":   {"cost": 400, "struct": "PASTURE", "first": 8, "interval": 2, "held": 6, "product": "MILK"},
    "SHEEP": {"cost": 500, "struct": "PASTURE", "first": 6, "interval": 3, "held": 6, "product": "WOOL"},
}
PRODUCTS = ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER"]
MARKET_PARAMS = {
    "WHEAT":      {"base":  25, "T": 400, "bf": "sqrt",   "bt": 0.80, "af": "log",    "at": 0.20},
    "CARROT":     {"base":  35, "T": 450, "bf": "hinge",  "bt": 1.00, "af": "sqrt",   "at": 0.70},
    "TOMATO":     {"base":  60, "T": 200, "bf": "hinge",  "bt": 0.40, "af": "sqrt",   "at": 0.60},
    "STRAWBERRY": {"base": 120, "T": 100, "bf": "sqrt",   "bt": 0.70, "af": "linear", "at": 1.60},
    "MELON":      {"base": 250, "T": 300, "bf": "log",    "bt": 0.20, "af": "sq",     "at": 3.60},
    "EGG":        {"base":  50, "T": 332, "bf": "hinge",  "bt": 0.40, "af": "log",    "at": 0.20},
    "MILK":       {"base": 160, "T": 122, "bf": "sqrt",   "bt": 0.60, "af": "linear", "at": 1.60},
    "WOOL":       {"base": 200, "T": 105, "bf": "log",    "bt": 0.20, "af": "sq",     "at": 3.20},
    "FERTILIZER": {"base": 100, "T": 200, "bf": "linear", "bt": 0.40, "af": "linear", "at": 0.40},
}
SHOPS = {
    "BAKERY":         ["EGG", "WHEAT"],
    "PIZZA_SHOP":     ["MILK", "TOMATO", "WHEAT"],
    "BRUNCH_SPOT":    ["EGG", "WHEAT", "STRAWBERRY"],
    "YARN_STORE":     ["WOOL"],
    "ICE_CREAM_SHOP": ["STRAWBERRY", "MILK", "WHEAT"],
    "PET_CAFE":       ["CARROT"],
    "SMOOTHIE_SHOP":  ["STRAWBERRY", "MILK"],
    "FARMERS_MARKET": ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY"],
}
EXP_PULL = {p: 0.0 for p in PRODUCTS}
for _shop, _prods in SHOPS.items():
    _m = 2.0 if len(_prods) == 1 else 1.0
    for _p in _prods:
        EXP_PULL[_p] += _m / len(SHOPS)
SHOP_INTERVAL = 3
MAX_SHOPS = 8
TICKS_PER_DAY = 6
I0 = 10000
HINGE_GAIN = 8.0
LAST_DAY = 29

P = dict(
    mode="lookahead",       # 'off' | 'greedy' | 'lookahead' | 'model'
    items=["STRAWBERRY", "MILK", "WOOL", "FERTILIZER", "MELON", "CARROT", "TOMATO", "EGG"],
    lookahead=40,           # how many turns of scheduled sales to pull forward
    wheat=1,                # 1 -> also manage WHEAT (it is animal feed: keep a reserve)
    wheat_days=1.0,         # days of feed to leave in the shed before selling any
    wheat_start=300,        # step before which WHEAT is never touched
    fert_keep=0,            # fertilizer units to hold back
    start_step=0,           # overlay stays silent before this step
    price_gate=0.0,         # skip a pull-forward if price/base is below this
    hold_gain=0.0,          # >0: hold when the 1-turn forecast beats spot by this much
    sell_bias_glut=2.2,     # v22 pacing multipliers, used by mode='model'
    sell_bias_tight=2.0,
    hinge_meter=0.5,
    shed_target=88,
    unlock_trust=1.0,
    opp_weight=0.85,
    opp_mirror=0.7,
    mine_w=0.7,
    horizon_days=0.6,
    sells_first=0,          # 1 always reorder | 2 reorder only when nothing is truncated
    sell_sort=0,            # 1 -> order our SELLs by gross value, high first
    tranche=99,             # cap on units pulled forward per item per turn
    drain_gate=4,           # 0 fixed | 1 boatlee's veto | 2 tick-free block | 3 per-item
    window_cap=24,          # ceiling on the per-item tick-free window
    win4=[0, 4, 3, 2],      # drain_gate=4: window by step %% 4
    hold_horizon=0.2,       # days ahead the hold test forecasts
    opp_press=0.0,          # weight on the opponent's pipeline inside that forecast
    endgame_day=30,         # from this day on, liquidate everything (30 = never; the tape does it)
)


def _shape(func, x, T):
    if x < 0.0:
        x = 0.0
    if func == "linear":
        return x
    if func == "sq":
        return x * x
    if func == "sqrt":
        return math.sqrt(x)
    if func == "log":
        return math.log(1.0 + x)
    if func == "hinge":
        if not T or T <= 0:
            return x
        u = x / T
        d = u - 1.0
        return u + HINGE_GAIN * (d * d if d > 0 else 0.0)
    return x


def market_price(item, inv):
    p = MARKET_PARAMS[item]
    base, T = p["base"], p["T"]
    if inv < I0:
        amp = p["bt"] * base / _shape(p["bf"], T, T)
        price = base + amp * _shape(p["bf"], I0 - inv, T)
    else:
        amp = p["at"] * base / _shape(p["af"], T, T)
        price = base - amp * _shape(p["af"], inv - I0, T)
    v = int(round(price))
    return 1 if v < 1 else v


# --------------------------------------------------------------- tape lookahead
# CUM[item][t] = units of `item` the tape schedules over steps 0..t-1.
_NSTEP = len(_M._ACTIONS)
CUM = {p: [0] * (_NSTEP + 1) for p in PRODUCTS}
SCHED = {p: [0] * _NSTEP for p in PRODUCTS}
for _s, _a in enumerate(_M._ACTIONS):
    for _o in (_a.get("market") or []):
        if len(_o) >= 3 and _o[0] == "SELL" and _o[1] in SCHED:
            try:
                SCHED[_o[1]][_s] += max(0, int(_o[2]))
            except (TypeError, ValueError):
                pass
for _p in PRODUCTS:
    _run = 0
    for _s in range(_NSTEP):
        CUM[_p][_s] = _run
        _run += SCHED[_p][_s]
    CUM[_p][_NSTEP] = _run


def _sched_window(item, lo, hi):
    """Units of `item` scheduled over steps lo..hi inclusive."""
    lo = max(0, lo)
    hi = min(_NSTEP - 1, hi)
    if hi < lo:
        return 0
    return CUM[item][hi + 1] - CUM[item][lo]


class Overlay:
    """v22's market model, re-pointed at a tape's shed instead of v22's own farm."""

    def __init__(self):
        self.reset(0)

    def reset(self, step):
        self.last_step = step
        self.debt = {}      # units pulled forward, repaid from the tape's later orders
        self.sold_today = {}
        self.day = -1
        self.opp_pipe = {p: 0.0 for p in PRODUCTS}

    # ------------------------------------------------------------- observation
    def observe(self, obs, step):
        me = int(_M._get(obs, "player", 0) or 0)
        farms = list(_M._get(obs, "farms", []) or [])
        self.me = me
        self.farm = farms[me] if me < len(farms) else {}
        priv = _M._get(obs, "private", {}) or {}
        self.shed = dict(_M._get(priv, "shed", {}) or {})
        self.invs = list(_M._get(priv, "inventories", []) or [])
        market = _M._get(obs, "market", {}) or {}
        self.inv = dict(_M._get(market, "inventory", {}) or {})
        self.price = dict(_M._get(market, "prices", {}) or {})
        town = _M._get(obs, "town", {}) or {}
        self.shops = list(_M._get(town, "unlocked_shops", []) or [])
        self.day = step // 24
        self.hour = step % 24
        self.day_left = LAST_DAY - self.day
        self.drain = self.drain_rates(self.shops)
        self.n_animals = 0
        self.pipeline = {p: 0.0 for p in PRODUCTS}
        for row in (_M._get(self.farm, "tiles", []) or []):
            for t in row or []:
                if not isinstance(t, dict):
                    continue
                if t.get("kind") == "PLANT":
                    self.pipeline[t["crop"]] += self.plant_future(t)
                elif "animal" in t:
                    self.n_animals += 1
                    a = ANIMALS[t["animal"]]
                    rem = max(0, self.day_left - 1)
                    per = min(1 + a["interval"], a["held"]) / a["interval"]
                    self.pipeline[a["product"]] += t["yield_units"] + rem * per
                    self.pipeline["FERTILIZER"] += rem
        for p in PRODUCTS:
            self.pipeline[p] += self.shed.get(p, 0) + self.carried(p)
        if step % 6 == 0 or self.opp_pipe is None:
            self.opp_pipe = self.scan_opponent(farms[1 - me] if len(farms) > 1 else {})

    def carried(self, p):
        return sum(iv.get(p, 0) for iv in self.invs)

    def plant_future(self, t):
        cd = CROPS[t["crop"]]
        age = self.day - t["planted_day"]
        if not cd["ongoing"]:
            room = cd["maxy"] - t["yield_units"]
            last = min(cd["myd"], age + self.day_left)
            days = max(0, last - max(age, (cd["myd"] + 1) // 2) + 1)
            return t["yield_units"] + min(room, days)
        k = age - cd["first"]
        done = (k // cd["interval"] + 1) if k >= 0 else 0
        left = max(0, cd["maxy"] - done)
        left = min(left, self.day_left // max(1, cd["interval"]) + 1)
        return t["yield_units"] + left * 1.5

    def scan_opponent(self, farm):
        pipe = {p: 0.0 for p in PRODUCTS}
        for row in (_M._get(farm, "tiles", []) or []):
            for t in row or []:
                if not isinstance(t, dict):
                    continue
                if t.get("kind") == "PLANT":
                    pipe[t["crop"]] += self.plant_future(t)
                elif "animal" in t:
                    a = ANIMALS[t["animal"]]
                    rem = max(0, self.day_left - 1)
                    per = min(1 + a["interval"], a["held"]) / a["interval"]
                    pipe[a["product"]] += t["yield_units"] + rem * per
                    pipe["FERTILIZER"] += rem
        return pipe

    # ------------------------------------------------------------ market model
    def drain_rates(self, shops):
        d = {p: 0.0 for p in PRODUCTS}
        for shop in shops:
            prods = SHOPS.get(shop)
            if not prods:
                continue
            mult = 2.0 if len(prods) == 1 else 1.0
            for p in prods:
                d[p] += mult * 6.0
        for p in PRODUCTS:
            if p != "FERTILIZER":
                d[p] += 1.0
        return d

    def mean_drain(self, item, days_ahead):
        """Average daily town pull over the next `days_ahead` days, counting shops
        that have not unlocked yet -- today's shop list badly under-prices the
        whole first half of the game."""
        n = int(days_ahead)
        if n <= 0:
            return self.drain[item]
        base = 1.0 if item != "FERTILIZER" else 0.0
        known = self.drain[item] - base
        n_now = len(self.shops)
        tot = 0.0
        for t in range(self.day, self.day + n + 1):
            future = max(0, min(MAX_SHOPS, (t + 1) // SHOP_INTERVAL) - n_now)
            tot += known + base + future * TICKS_PER_DAY * EXP_PULL[item] * P["unlock_trust"]
        return tot / (n + 1)

    def forecast(self, item, days_ahead, extra=0.0):
        d = self.mean_drain(item, days_ahead)
        return market_price(item, self.inv[item] - d * days_ahead + extra)

    def supply(self, item, horizon=None):
        """Committed supply reaching the shared pool inside `horizon` days, scaled
        so a season-long pipeline is not charged against a few days of drain."""
        if horizon is None or self.day_left <= 0:
            scale = 1.0
        else:
            scale = min(1.0, float(horizon) / max(1.0, self.day_left))
        mine = self.pipeline[item] * scale * P["mine_w"]
        theirs = max(self.opp_pipe[item] * scale, mine * P["opp_mirror"])
        return mine + theirs * P["opp_weight"]

    # ------------------------------------------------------------------ policy
    def model_q(self, item, avail):
        """v22's pacing: clear stock+pipeline by day 29, front-loaded under glut,
        held back while the town is still short, metered on a hinge curve."""
        horizon = max(1, self.day_left + 1)
        total = max(avail, self.pipeline[item])
        q = total / horizon
        q *= P["sell_bias_glut"] if total > self.drain[item] * horizon else P["sell_bias_tight"]
        if MARKET_PARAMS[item]["bf"] == "hinge" and self.inv[item] < I0:
            q *= P["hinge_meter"]
        q = int(math.ceil(q)) - self.sold_today.get(item, 0)
        shed_total = sum(max(0, v) for k, v in self.shed.items() if k in PRODUCTS)
        carried_total = sum(sum(v for k, v in iv.items() if k in PRODUCTS) for iv in self.invs)
        overflow = shed_total + carried_total - P["shed_target"]
        if overflow > 0:
            q = max(q, min(avail, int(math.ceil(overflow * avail / max(1, shed_total)))))
        return max(0, q)

    def window(self, item, step):
        """How many turns of the tape's schedule it is safe to pull into `step`.

        The town consumes on steps divisible by 4 (24 for the town centre) and it
        does so AFTER the market resolves. So a unit moved from step s back to
        step t skips every consumption tick in [t, s-1] and prints against a
        fuller market. Inside one 4-step block there is no tick to skip, and
        moving a unit earlier inside the block is pure profit in a mirror: the
        opponent then sells into inventory we already raised."""
        g = int(P["drain_gate"])
        k = int(P["lookahead"])
        if g == 0:
            return k
        if g == 1:  # boatlee's rule: never pull across a tick, at any depth
            return 0 if _M._town_demand_now({"town": {"unlocked_shops": self.shops}},
                                            item, step) > 0 else k
        if g == 4:  # explicit per-phase window, swept to find the shape
            return min(k, int(P["win4"][step % 4]))
        if g == 2:  # pull only as far as the end of the current tick-free block
            free = (4 - (step % 4)) % 4
            return min(k, free)
        # g == 3: per-item. Shops pull every 4 steps but only for what they sell,
        # and the town centre pulls every 24 -- except FERTILIZER, which no shop
        # and no town centre ever consumes. Fertiliser therefore has no tick to
        # respect at all: its inventory only ratchets up, so releasing it before
        # the opponent does is free money.
        shop = 0.0
        for s in self.shops:
            prods = SHOPS.get(s)
            if prods and item in prods:
                shop += 2.0 if len(prods) == 1 else 1.0
        cap = int(P["window_cap"])
        for d in range(0, cap + 1):
            s = step + d
            pull = shop if s % 4 == 0 else 0.0
            if item != "FERTILIZER" and s % 24 == 0:
                pull += 1.0
            if pull > 0:
                return min(k, d)
        return min(k, cap)

    def hold(self, item):
        """True when the market model says this unit is worth more next turn.

        The town consumes every 4 steps, so an item can be a third cheaper on a
        pre-drain turn than on the turn after it. `forecast` prices the drain in
        (including shops that have not unlocked yet); `supply` prices in what the
        opponent's visible tiles are about to dump on top of us."""
        spot = float(self.price.get(item, 0) or 0)
        if spot <= 0:
            return False
        base = MARKET_PARAMS[item]["base"]
        if P["price_gate"] > 0 and spot < base * P["price_gate"]:
            return True
        if P["hold_gain"] > 0:
            h = float(P["hold_horizon"])
            nxt = self.forecast(item, h, extra=self.supply(item, h) * P["opp_press"])
            if (nxt - spot) / spot > P["hold_gain"]:
                return True
        return False

    def __call__(self, action, obs, step):
        if step == 0 or step < self.last_step:
            self.reset(step)
        self.last_step = step
        if P["mode"] == "off" or step < int(P["start_step"]):
            return action
        self.observe(obs, step)
        if self.hour == 0:
            self.sold_today = {}

        action = _M._copy_action(action)
        market = [list(o) for o in (action.get("market") or [])]

        # 1. Repay what we pulled forward, out of the tape's own later orders.
        #    Anything still owed after this turn is forgiven -- the tape's sell
        #    quantities are aspirational (it orders far more than the shed holds),
        #    so carrying a ledger forward would silently choke real sales.
        if self.debt:
            kept = []
            for o in market:
                if len(o) >= 3 and o[0] == "SELL" and self.debt.get(o[1], 0) > 0:
                    try:
                        n = max(0, int(o[2]))
                    except (TypeError, ValueError):
                        n = 0
                    cut = min(n, self.debt[o[1]])
                    self.debt[o[1]] -= cut
                    n -= cut
                    if n <= 0:
                        continue
                    o = [o[0], o[1], n]
                kept.append(o)
            market = kept
            self.debt = {}

        items = [i for i in P["items"] if i in PRODUCTS]
        if P["wheat"] and step >= int(P["wheat_start"]):
            items = items + ["WHEAT"]
        endgame = self.day >= int(P["endgame_day"])

        extra = {}
        for item in items:
            stock = max(0, int(self.shed.get(item, 0) or 0))
            reserve = _M._pickup_reserve(action, item)
            if item == "WHEAT":
                reserve += int(self.n_animals * P["wheat_days"])
            elif item == "FERTILIZER":
                reserve += int(P["fert_keep"])
            already = sum(max(0, int(o[2])) for o in market
                          if len(o) >= 3 and o[0] == "SELL" and o[1] == item)
            surplus = stock - reserve - already
            if surplus <= 0:
                continue
            if endgame:
                extra[item] = surplus
                continue
            if P["mode"] == "greedy":
                want = surplus
            else:
                # Pull the next `lookahead` turns of the tape's own schedule
                # forward into this turn.
                k = self.window(item, step)
                if k <= 0:
                    continue
                want = _sched_window(item, step + 1, step + k)
                if P["mode"] == "model":
                    want = max(want, self.model_q(item, surplus))
            want = min(surplus, want, int(P["tranche"]))
            if want <= 0:
                continue
            if self.hold(item):
                continue
            extra[item] = want
            self.debt[item] = self.debt.get(item, 0) + want

        # 2. Merge our extra units into the existing order for that item, or add
        #    a new order. Slot order is preserved for everything we do not touch.
        for item, q in extra.items():
            hit = next((o for o in market
                        if len(o) >= 3 and o[0] == "SELL" and o[1] == item), None)
            if hit is not None:
                hit[2] = max(0, int(hit[2])) + q
            else:
                market.append(["SELL", item, int(q)])

        # Reordering is only safe while nothing falls off the 10-order cliff: the
        # tape fills all ten slots in the opening and dropping one of its buys
        # costs far more than an earlier print is worth.
        if P["sells_first"] and (P["sells_first"] == 1 or len(market) <= 10):
            sells = [o for o in market if len(o) >= 1 and o[0] == "SELL"]
            rest = [o for o in market if not (len(o) >= 1 and o[0] == "SELL")]
            if P["sell_sort"]:
                sells.sort(key=lambda o: -float(self.price.get(o[1], 0) or 0) * o[2])
            market = sells + rest
        action["market"] = market[:10]
        return action


_OVER = {0: Overlay(), 1: Overlay()}


def agent(obs):
    # The tape runs exactly once per turn: `_weed_repair_action` keeps state
    # keyed to what it emitted, so a retry inside an except: block would
    # desynchronise it. Only the overlay is guarded.
    action = _M.agent(obs)
    try:
        fallback = int(_M._get(obs, "day", 0) or 0) * 24 + int(_M._get(obs, "hour", 0) or 0)
        raw = _M._get(obs, "step", None)
        step = int(raw) if raw is not None else fallback
        step = min(max(0, step), _NSTEP - 1)
        seat = _M._seat(obs)
        return _M._align_hands(_OVER[seat](action, obs, step), obs)
    except Exception:
        return action
