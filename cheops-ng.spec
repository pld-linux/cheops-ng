Summary:	Network management tool
Summary(pl):	Narz�dzie zarz�dania sieci�
Name:		cheops-ng
Version:	0.1.12
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tgz
# Source0-md5:	da59e555f57f29bcd4a0aad4c6c28bf6
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-use_system_libadns.patch
Patch2:		%{name}-gcc33.patch
URL:		http://cheops-ng.sourceforge.net/
BuildRequires:	adns-devel
BuildRequires:	bison
BuildRequires:	gnome-libs-devel
BuildRequires:	libxml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cheops-ng is a network management tool for mapping and monitoring your
network. It has host/network discovery functionality and OS detection,
and does a port scan of each computer to tell what services are
running. It can probe FTP, HTTP, ssh, SMTP, NNTP, IMAP, and VNC to see
what version and type of server is running on those ports.

%description -l pl
Cheops-ng jest narz�dziem zarz�dania sieci� s�u��cym do tworzenia map
i monitorowania sieci. Ma mo�liwo�� znajdowania urz�dze� w sieci,
identyfikacji systemu operacyjnego, skanowania port�w w celu
identyfikacji popularnych us�ug sieciowych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
mv -f aclocal.m4 acinclude.m4
%{__aclocal}
%{__autoconf}
cp -f %{_datadir}/automake/{config.,missing}* .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_pixmapsdir}/*
