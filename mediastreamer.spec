Summary:	Audio/Video real-time streaming
Name:		mediastreamer
Version:	2.3.0
Release:	6
License:	LGPL
Group:		Libraries
Source0:	http://mirror.lihnidos.org/GNU/savannah/linphone/mediastreamer/%{name}-%{version}.tar.gz
# Source0-md5:	867d539cf11e942dcbfd08d4b3182397
URL:		http://www.tcpdump.org/
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	ffmpeg-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libgsm-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libtheora-devel
BuildRequires:	libv4l-devel
BuildRequires:	ortp-devel >= 0.16.1
BuildRequires:	pkgconfig
BuildRequires:	speex-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mediastreamer2 is a GPL licensed library to make audio and video
real-time streaming and processing. Written in pure C, it is based
upon the oRTP library.

%package devel
Summary:	Header files and develpment documentation for mediastreamer
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and develpment documentation for mediastreamer.

%package static
Summary:	Static mediastreamer library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static mediastreamer library.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libmediastreamer.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmediastreamer.so.0

%files devel
%defattr(644,root,root,755)
%doc help/doc/html
%attr(755,root,root) %{_libdir}/libmediastreamer.so
%{_libdir}/libmediastreamer.la
%{_includedir}/mediastreamer2
%{_pkgconfigdir}/mediastreamer.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmediastreamer.a
