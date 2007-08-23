%define name	ddrescue
%define version 1.3
%define release %mkrel 2

Summary:	GNU ddrescue is a data recovery tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Kernel and hardware
Source0:	%name-%version.tar.bz2
URL:		http://www.gnu.org/software/ddrescue/ddrescue.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(post): info-install
Requires(preun): info-install
    
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

%prep 
%setup -q -n %name-%{version}

%build

./configure  \
        --program-prefix=%{?_program_prefix} \
        --prefix=%{_prefix} \
        --datadir=%{_datadir} \
        --includedir=%{_includedir} \
        --mandir=%{_mandir} \
        --infodir=%{_infodir}

%make CXXFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p $RPM_BUILD_ROOT/%_mandir/man1
install -m644 doc/ddrescue.1 $RPM_BUILD_ROOT/%_mandir/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info


%files
%defattr(-,root,root,0755) 
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_infodir}/*
%{_mandir}/*/*



