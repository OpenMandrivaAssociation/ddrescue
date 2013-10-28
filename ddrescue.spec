%bcond_without	uclibc

Summary:	Data recovery tool
Name:		ddrescue
Version:	1.17
Release:	2
License:	GPLv3+
Group:		System/Kernel and hardware
Source0:	http://ftp.gnu.org/gnu/ddrescue/%{name}-%{version}.tar.lz
Patch0:		0001-hack-around-build-issues-with-uClibc-crapping-out-on.patch
# for this stupid, almost none used format with lzma algorithm trying to compete with xz
# utils... 
BuildRequires:	lzip
URL:		http://www.gnu.org/software/ddrescue/ddrescue.html
%if %{with uclibc}
BuildRequires:	uClibc-devel uClibc++-devel
%endif

%description
GNU ddrescue is a data recovery tool. It copies data from one file or block 
device (hard disc, cdrom, etc) to another, trying hard to rescue data in 
case of read errors.

Ddrescue does not truncate the output file if not asked to. So, every time 
you run it on the same output file, it tries to fill in the gaps.

The basic operation of ddrescue is fully automatic. That is, you don't have 
to wait for an error, stop the program, read the log, run it in reverse mode.

If you use the logfile feature of ddrescue, the data is rescued very 
efficiently (only the needed blocks are read). Also you can interrupt the 
rescue at any time and resume it later at the same point.

Automatic merging of backups: If you have two or more damaged copies of a file,
cdrom, etc, and run ddrescue on all of them, one at a time, with the same 
output file, you will probably obtain a complete and error-free file. This is 
so because the probability of having damaged areas at the same places on 
different input files is very low. Using the logfile, only the needed blocks 
are read from the second and successive copies.

The logfile is periodically saved to disc. So in case of a crash you can 
resume the rescue with little recopying.

Also, the same logfile can be used for multiple commands that copy different 
areas of the file, and for multiple recovery attempts over different subsets.

Ddrescue aligns its I/O buffer to the sector size so that it can be used to 
read from raw devices. For efficiency reasons, also aligns it to the memory 
page size if page size is a multiple of sector size. 

%package -n	uclibc-%{name}
Summary:	Data recovery tool (uClibc build)
Group:		System/Kernel and hardware

%description -n	uclibc-%{name}
GNU ddrescue is a data recovery tool. It copies data from one file or block 
device (hard disc, cdrom, etc) to another, trying hard to rescue data in 
case of read errors.

Ddrescue does not truncate the output file if not asked to. So, every time 
you run it on the same output file, it tries to fill in the gaps.

The basic operation of ddrescue is fully automatic. That is, you don't have 
to wait for an error, stop the program, read the log, run it in reverse mode.

If you use the logfile feature of ddrescue, the data is rescued very 
efficiently (only the needed blocks are read). Also you can interrupt the 
rescue at any time and resume it later at the same point.

Automatic merging of backups: If you have two or more damaged copies of a file,
cdrom, etc, and run ddrescue on all of them, one at a time, with the same 
output file, you will probably obtain a complete and error-free file. This is 
so because the probability of having damaged areas at the same places on 
different input files is very low. Using the logfile, only the needed blocks 
are read from the second and successive copies.

The logfile is periodically saved to disc. So in case of a crash you can 
resume the rescue with little recopying.

Also, the same logfile can be used for multiple commands that copy different 
areas of the file, and for multiple recovery attempts over different subsets.

Ddrescue aligns its I/O buffer to the sector size so that it can be used to 
read from raw devices. For efficiency reasons, also aligns it to the memory 
page size if page size is a multiple of sector size. 

%prep
%setup -q
%patch0 -b .fputc~

%build
export CONFIGURE_TOP="$PWD"
%if %{with uclibc}
mkdir -p uclibc
pushd uclibc
%uclibc_configure
%make CXXFLAGS="%{uclibc_cflags}" LDFLAGS="%{ldflags}"
popd
%endif

mkdir -p glibc
pushd glibc
%configure
%make CXXFLAGS="%{optflags}" LDFLAGS="%{ldflags}"
popd

%install
%if %{with uclibc}
%makeinstall_std -C uclibc
%endif

%makeinstall_std -C glibc

%files
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_infodir}/*
%{_mandir}/*/*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}%{_bindir}/*
%endif

%changelog
* Fri Jun 08 2012 Andrey Bondrov <abondrov@mandriva.org> 1.15-2
+ Revision: 803255
- Drop some legacy junk

* Thu Feb 23 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.15-1
+ Revision: 779361
- update to 1.15

* Fri Aug 26 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.14-1
+ Revision: 697234
- clean out legacy junk
- new version

* Sun Aug 29 2010 Funda Wang <fwang@mandriva.org> 1.13-1mdv2011.0
+ Revision: 574134
- new version 1.13

* Wed Apr 07 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.12-1mdv2010.1
+ Revision: 532805
- Final 1.12

* Mon Feb 15 2010 Funda Wang <fwang@mandriva.org> 1.12-0.rc2.1mdv2010.1
+ Revision: 506199
- 1.12 rc2

* Mon Jul 13 2009 Frederik Himpe <fhimpe@mandriva.org> 1.11-1mdv2010.0
+ Revision: 395569
- Update to new version 1.11
- Rediff string format patch

* Mon Feb 23 2009 Frederik Himpe <fhimpe@mandriva.org> 1.10-1mdv2009.1
+ Revision: 344291
- Update to new version 1.10
- Fix source URL
- Build with -Werror=format-security

* Thu Nov 20 2008 Frederik Himpe <fhimpe@mandriva.org> 1.9-1mdv2009.1
+ Revision: 305234
- Update to new version 1.9

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.8-3mdv2009.0
+ Revision: 243989
- rebuild

* Mon Feb 25 2008 Frederik Himpe <fhimpe@mandriva.org> 1.8-1mdv2008.1
+ Revision: 174941
- New upstream version
- Remove NEWS file: it contains nothing more than the changes of the
  latest version, which is already included in the same concise way in
  ChangeLog

* Mon Feb 18 2008 Frederik Himpe <fhimpe@mandriva.org> 1.7-1mdv2008.1
+ Revision: 171934
- New upstream version
- New license policy

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.6-2mdv2008.1
+ Revision: 170795
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Dec 12 2007 Emmanuel Andry <eandry@mandriva.org> 1.6-1mdv2008.1
+ Revision: 117616
- New version

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 1.3-2mdv2008.0
+ Revision: 69910
- info file must be unregistered before being uninstalled
- kill file require on info-install


* Wed Dec 20 2006 Lenny Cartier <lenny@mandriva.com> 1.3-1mdv2007.0
+ Revision: 100455
- Update to 1.3

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org> 1.2-2mdv2007.0
+ Revision: 53220
- rebuild
- Import ddrescue

