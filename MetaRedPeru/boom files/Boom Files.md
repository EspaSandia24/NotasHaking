**Descripcion**

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/MetaRedPeru/boom files]
└─$ sudo grep -lir 'flag' big-files                            
[sudo] contraseña para espasandia24: 
big-files/rbgkhxrktuzuedgcrjpba.txt
big-files/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt
big-files/folder_xehkkhqjny/folder_pfsaielbxe/folder_lntmdthbff/folder_slmyfnbxwf/mdhjamupibegddiitry.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_acommpmsrxd.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_bdsbhdklnqiceltmn.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_bgypcmmzeoseuzbjkd.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_cbhapglzqed.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_fkxcqivfbixrpvnxijsl.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_hjvryvewu.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_hrxfjedcvypsuifurgg.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_hufanpmbsfmcplmzdoyd.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_kznplditsjenjjdfgulfq.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_mrkgaxybdxeode.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_nxdiqzbwitittoqrh.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_ojygeqgflb.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_pjmeaqiqyzgnkfbygm.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_sspponqejdignblhu.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_ugjaltgsgukndxtik.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_uyfmoxhozohdyliqhr.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_vtdtezslpmtxdgilmpizpf.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_xftgsikcdwgbjrffowdk.txt
big-files/folder_xtshijybzy/folder_ciinwksnzo/file_yjmafqiynyfxrtwrjjsmxx.txt
big-files/folder_hxarnwdtrd/xsdewwuiuzrhcnrk.txt
                                                                                
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/MetaRedPeru/boom files]
└─$ sudo grep -lir 'flag{' big-files           
big-files/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt
                                                                                
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/MetaRedPeru/boom files]
└─$ cd big-files/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/
                                                                                
┌──(espasandia24㉿kali)-[~/…/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee]
└─$ ls 
afeztzks.txt                     file_vxohilsrtnly.txt
cpuzajaleqzervfixar.txt          file_yvotyrokxjvqhbuqrypmiud.txt
cwhygeprfyzmiparx.txt            lgdtdxerinx.txt
eyzwmjpfjhmbzguzdv.txt           mjklvtcnaxgzlm.txt
fhqyyhzhrdlssnhzkx.txt           nfkabgmhaoriktvkeduoy.txt
file_daguxiuldqwbure.txt         nfocmtivsvx.txt
file_gmdriqvgccw.txt             oldcrjwlmrdkpfnljxxlh.txt
file_guazbrmmfmcmcrmdxv.txt      pbylavhd.txt
file_inpvdaeexvncjiolkyw.txt     phmgcrlnnkocv.txt
file_jswrnvjktlhvgf.txt          plvdzxpgjuhdaa.txt
file_jzyynitgpohnuwgjezii.txt    qpphoecoxwvgnzmxrzkrqmu.txt
file_kzjrfdqgwzjo.txt            sgejbmtarvtzxaaio.txt
file_kzjtlrukjqwrxwquajn.txt     twglkrpjdrulsnevhcctg.txt
file_luaovhpmcukwu.txt           wcpudscvpllsmciefqjgnawz.txt
file_mskzagnt.txt                whzxrpivpqld.txt
file_naegjrxpwwpjccto.txt        wiottidmlmrcsz.txt
file_oolkedrcfevbttmvogjoc.txt   wlltnuzygm.txt
file_ptwhjysaohwkkxczmkvzf.txt   ygsxfvedd.txt
file_rjidzhedowpqggziyzfya.txt   yvhdekwlmoi.txt
file_toyxuduaiukatlstyzglpu.txt
                                                                                
┌──(espasandia24㉿kali)-[~/…/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee]
└─$ cat whzxrpivpqld.txt 
The information in the registry would take thousand of years to review.Flag{gr3p_1s_m4g1c}

```
flag{gr3p_1s_m4g1c}
**Notas Adicionales**