Summary:	Audio/Video real-time streaming
Name:		mediastreamer
Version:	2.9.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://mirror.lihnidos.org/GNU/savannah/linphone/mediastreamer/%{name}-%{version}.tar.gz
# Source0-md5:	f2ea0fe731a363749a81b6eaac22a62c
Patch0:		%{name}-imagedir.patch
URL:		http://www.linphone.org/eng/documentation/dev/mediastreamer2.html
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
BuildRequires:	ortp-devel >= 0.21.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	spandsp-devel
BuildRequires:	speex-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xxd
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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static \
	--disable-tests

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Remove duplicated documentation
rm -r $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/html/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README help/doc/html
%attr(755,root,root) %{_libdir}/libmediastreamer_base.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmediastreamer_base.so.3
%attr(755,root,root) %{_libdir}/libmediastreamer_voip.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmediastreamer_voip.so.3
%{_pixmapsdir}/%{name}

%files devel
%defattr(644,root,root,755)
%doc help/doc/html
%attr(755,root,root) %{_libdir}/libmediastreamer_base.so
%attr(755,root,root) %{_libdir}/libmediastreamer_voip.so
%{_libdir}/libmediastreamer_base.la
%{_libdir}/libmediastreamer_voip.la
%{_includedir}/mediastreamer2
%{_pkgconfigdir}/mediastreamer.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmediastreamer_base.a
%{_libdir}/libmediastreamer_voip.a
