**Descripcion**


**Solucion**

```bash
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Pico CTF 2021]
└─$ strings warm 
/lib64/ld-linux-x86-64.so.2
libc.so.6
puts
printf
__cxa_finalize
strcmp
__libc_start_main
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
=y       
=W       
=Z       
AWAVI
AUATL
[]A\A]A^A_
Hello user! Pass me a -h to learn what I can do!
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}
I don't know what '%s' means! I do know what -h means though!
;*3$"
GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0
/usr/lib/gcc/x86_64-linux-gnu/7/include
/usr/include/x86_64-linux-gnu/bits
/usr/include
warm.c
stddef.h
types.h
libio.h
stdio.h
sys_errlist.h
_IO_buf_end
_old_offset
sys_nerr
_IO_save_end
short int
size_t
_IO_write_ptr
_flags
_IO_buf_base
_markers
_IO_read_end
stderr
_lock
long int
_cur_column
_IO_2_1_stderr_
_IO_FILE_plus
_pos
argv
_sbuf
_IO_FILE
unsigned char
argc
_IO_2_1_stdin_
_IO_marker
_shortbuf
_IO_write_base
_unused2
_IO_read_ptr
short unsigned int
warm.c
/opt/hacksports/shared/staging/Wave a flag_6_3020485019993253/problem_files
main
_next
__pad1
__pad2
__pad3
__pad4
__pad5
long unsigned int
_IO_write_end
__off64_t
__off_t
_chain
GNU C11 7.5.0 -mtune=generic -march=x86-64 -g -fstack-protector-strong
_IO_backup_base
stdin
_flags2
_mode
_IO_read_base
_vtable_offset
_IO_save_base
sys_errlist
_fileno
stdout
_IO_2_1_stdout_
_IO_lock_t
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.7698
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
warm.c
__FRAME_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
_ITM_deregisterTMCloneTable
puts@@GLIBC_2.2.5
_edata
printf@@GLIBC_2.2.5
__libc_start_main@@GLIBC_2.2.5
__data_start
strcmp@@GLIBC_2.2.5
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_csu_init
__bss_start
main
__TMC_END__
_ITM_registerTMCloneTable
__cxa_finalize@@GLIBC_2.2.5
.symtab
.strtab
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.data
.bss
.comment
.debug_aranges
.debug_info
.debug_abbrev
.debug_line
.debug_str

┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Pico CTF 2021]                                                                            
└─$ ./warm 
Hello user! Pass me a -h to learn what I can do!
                                                                             
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Pico CTF 2021]                                                                            
└─$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}

```
picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}

**Notas Adicionales**