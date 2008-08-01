Name:           rovclock
Version:        0.6e
Release:        %mkrel 4
Epoch:          0
Summary:        Radeon overclocking utility
License:        GPL
Group:          System/Kernel and hardware
URL:            http://www.hasw.net/linux/
Source0:        http://www.hasw.net/linux/rovclock-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Rovclock is a Radeon overclocking utility.

The cards that are reported to work are:

Radeon 7500
Radeon 8500
Radeon 9000
Radeon 9100
Radeon 9500 (Pro)
Radeon 9550
Radeon 9600
Mobility FireGL T2
Mobility Radeon 9600 M10
Radeon 9700 (Pro)
Radeon X550
Radeon X800XL

%prep
%setup -q

%build
%{make} CC=%{__cc} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -a %{name} %{buildroot}%{_bindir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root,0755)
%doc ChangeLog COPYING README 
%attr(0755,root,root) %{_bindir}/%{name}


