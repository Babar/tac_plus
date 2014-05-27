Summary: TACACS+ Daemon
Name: tacacs+
Group: Networking/Servers
Version: F4.0.4.19
Release: 7fb
License: Cisco

Packager: Cooper Lees <cooper@fb.com>
Vendor: Shrubbery Networks

Source: %{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, bison, flex, m4, pam-devel, tcp_wrappers, tcp_wrappers-devel
Requires: pam, tcp_wrappers

%description
IPv4 Tacacs+ Daemon for Linux

%prep
%setup

%build
%configure --enable-acls --enable-uenable
%{__make}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -Dp -m0755 tac_plus.sysvinit %{buildroot}%{_initrddir}/tac_plus
### Clean up buildroot
%{__rm} -f %{buildroot}%{_infodir}/dir

%post

%preun

%clean
%{__rm} -rf %{buildroot}

%files

/usr/include/tacacs.h
/usr/bin/tac_pwd
/usr/bin/tac_plus
/usr/share/tacacs+/users_guide
/usr/share/tacacs+/tac_convert
/usr/share/tacacs+/do_auth.py
/usr/share/man/man5/tac_plus.conf.5.gz
/usr/share/man/man8/tac_pwd.8.gz
/usr/share/man/man8/tac_plus.8.gz
/usr/share/man/man3/regexp.3.gz
/usr/lib64/libtacacs.so.1.0.0
/usr/lib64/libtacacs.so.1
/usr/lib64/libtacacs.so
/usr/lib64/libtacacs.a
/usr/lib64/libtacacs.la
/etc/rc.d/init.d/tac_plus

%changelog
