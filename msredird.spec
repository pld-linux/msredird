# TODO: init script and sysconfig file with necessary environment variables
Summary:	RFC 2217-compliant multi-threaded serial port redirector
Summary(pl):	Wielow±tkowy program przekierowuj±cy port szeregowy zgodny z RFC 2217
Name:		msredird
Version:	0.2
Release:	0.1
License:	GPL
Group:		Networking
Source0:	ftp://metalab.unc.edu/pub/Linux/system/serial/%{name}-%{version}.tgz
# Source0-md5:	601cd4cddd8839aecfaf0d362066577e
URL:		http://www.asymmetrica.com/software/msredird/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/msredird

%description
msredird is serial port redirector, or simply, modem sharing server
program. The concept is very novel and already standardized by RFC
2217. msredird is an implementation of that standard, also known as
Telnet Com Port Control Option, in server mode.

%description -l pl
msredir jest programem przekierowuj±cym porty szeregowe lub, innymi
s³owy, programem pozwalaj±cym na wspó³dzielenie modemów. Jest
implementacj± standardu RFC 2217 (Telnet Com Port Control Option
protocol) w trybie serwera.

%prep
%setup -q

%build
%{__make} -C src \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I./include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir},/var/log/msredird}

install bin/msredird $RPM_BUILD_ROOT%{_sbindir}
install etc/msredird.conf $RPM_BUILD_ROOT%{_sysconfdir}
ln -sf /var/log/msredird $RPM_BUILD_ROOT%{_sysconfdir}/log

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{README,INSTALL,errorcodes.txt,sample.output}
%attr(755,root,root) %{_sbindir}/*
%dir %{_sysconfdir}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/msredird.conf
%{_sysconfdir}/log
/var/log/msredird
