Summary:	Data recovery tool
Name:		ddrescue
Version:	1.29.1
Release:	1
License:	GPLv3+
Group:		System/Kernel and hardware
URL:		https://www.gnu.org/software/ddrescue/ddrescue.html
Source0:	https://ftp.gnu.org/gnu/ddrescue/%{name}-%{version}.tar.lz
BuildRequires:	lzip

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
%setup -q

%build
%configure
%make_build CXXFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
%make_install

%files
%doc AUTHORS README
%{_bindir}/*
%{_infodir}/*
%{_mandir}/*/*
