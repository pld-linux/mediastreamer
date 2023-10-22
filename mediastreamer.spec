#
# Conditional build:
%bcond_with	pcap		# audio playing from PCAP files
%bcond_without	static_libs	# static library
# transport
%bcond_without	srtp		# SRTP (secure RTP) support
%bcond_without	zrtp		# support for RFC 6189: Media Path Key Agreement for Unicast Secure RTP
# audio I/O
%bcond_without	alsa		# ALSA sound I/O support
%bcond_with	arts		# aRts sound I/O support
%bcond_with	oss		# OSS support (deprecated)
%bcond_with	portaudio	# PortAudio sound I/O support
%bcond_without	pulseaudio	# PulseAudio sound I/O support
# audio codecs
%bcond_without	bcg729		# support for G279AnnexB in RTC3389 implementation of Comfort Noise Payload
%bcond_without	bv16		# BV16 codec support
%bcond_without	spandsp		# G726 codec support via spandsp
# video I/O
%bcond_without	opengl		# X11+OpenGL rendering support
%bcond_without	sdl		# SDL support
# video codecs
%bcond_without	matroska	# Matroska support via bcmatroska2
%bcond_without	zxing		# QRcode support via zxing-cpp
#
Summary:	Audio/Video real-time streaming
Summary(pl.UTF-8):	Przesyłanie strumieni audio/video w czasie rzeczywistym 
Name:		mediastreamer
# note: 5.2.x is AGPL-licensed; see DEVEL-5.2 branch
Version:	5.2.109
Release:	0.1
License:	GPL v3+
Group:		Libraries
#Source0Download: https://gitlab.linphone.org/BC/public/mediastreamer2/tags
Source0:	https://gitlab.linphone.org/BC/public/mediastreamer2/-/archive/%{version}/mediastreamer2-%{version}.tar.bz2
# Source0-md5:	fb37d1ea973015e3c648d219d2ff3dda
Patch0:		build.patch
Patch1:		%{name}-cmake-link.patch
Patch2:		libupnp-1.14.patch
Patch3:		%{name}-cmake-datadir.patch
Patch4:		%{name}-cmake-install-pkgconfig.patch
Patch5:		%{name}-cmake-SDL.patch
Patch6:		%{name}-types.patch
Patch10:	%{name}-gcc.patch
URL:		http://www.linphone.org/technical-corner/mediastreamer2/overview
%{?with_opengl:BuildRequires:	OpenGL-GLX-devel}
%{?with_sdl:BuildRequires:	SDL-devel >= 1.2.0}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	artsc-devel}
%{?with_bcg729:BuildRequires:	bcg729-devel >= 1.1.1-1}
%{?with_matroska:BuildRequires:	bcmatroska2-devel >= 5.1}
BuildRequires:	bctoolbox-devel >= 0.4.0
%{?with_bv16:BuildRequires:	bv16-floatingpoint-devel}
%{?with_zrtp:BuildRequires:	bzrtp-devel >= 5.2.51}
BuildRequires:	cmake >= 3.1
BuildRequires:	doxygen
# libavcodec >= 51.0.0, libswscale >= 0.7.0
BuildRequires:	ffmpeg-devel
BuildRequires:	gettext-tools
%{?with_opengl:BuildRequires:	glew-devel >= 1.5}
BuildRequires:	intltool >= 0.40
BuildRequires:	libgsm-devel
BuildRequires:	libjpeg-turbo-devel
%{?with_pcap:BuildRequires:	libpcap-devel}
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libtheora-devel >= 1.0-0.alpha7
BuildRequires:	libupnp-devel >= 1.8
BuildRequires:	libv4l-devel
BuildRequires:	libvpx-devel >= 0.9.6
BuildRequires:	libyuv-devel
BuildRequires:	opus-devel >= 0.9.0
BuildRequires:	ortp-devel >= 5.1
BuildRequires:	pkgconfig
%{?with_portaudio:BuildRequires:	portaudio-devel}
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel >= 0.9.21}
BuildRequires:	python3 >= 1:3
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sed >= 4.0
%{?with_spandsp:BuildRequires:	spandsp-devel >= 0.0.6}
BuildRequires:	speex-devel >= 1:1.2-beta3
BuildRequires:	speexdsp-devel >= 1.2-beta3
%{?with_srtp:BuildRequires:	libsrtp2-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXv-devel
%{?with_zxing:BuildRequires:	zxing-cpp-devel}
%{?with_bcg729:Requires:	bcg729 >= 1.1.1-1}
%{?with_matroska:Requires:	bcmatroska2 >= 5.1}
Requires:	bctoolbox >= 0.4.0
%{?with_zrtp:Requires:	bzrtp >= 5.2.109}
%{?with_opengl:Requires:	glew >= 1.5}
Requires:	libtheora >= 1.0-0.alpha7
Requires:	libvpx >= 0.9.6
Requires:	opus >= 0.9.0
Requires:	ortp >= 5.2.109
%{?with_pulseaudio:Requires:	pulseaudio-libs >= 0.9.21}
Requires:	spandsp >= 0.0.6
Requires:	speex >= 1:1.2-beta3
Requires:	speexdsp >= 1.2-beta3
Obsoletes:	mediastreamer-plugin-msbcg729 < 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mediastreamer2 is a GPL licensed library to make audio and video
real-time streaming and processing. Written in pure C, it is based
upon the oRTP library.

%description -l pl.UTF-8
Mediastreamer2 to udostępniona na licencji GPL biblioteka do
przesyłania i przetwarzania strumieni audio/video w czasie
rzeczywistym. Jest napisana w czystym C, oparta na bibliotece oRTP.

%package devel
Summary:	Header files and development documentation for mediastreamer libraries
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do bibliotek mediastreamer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_opengl:Requires:	OpenGL-devel}
%{?with_alsa:Requires:	alsa-lib-devel}
%{?with_bcg729:Requires:	bcg729-devel >= 1.1.1-1}
%{?with_matroska:Requires:	bcmatroska2-devel >= 5.1}
Requires:	bctoolbox-devel >= 0.4.0
%{?with_bv16:Requires:	bv16-floatingpoint-devel}
%{?with_zrtp:Requires:	bzrtp-devel >= 5.2.51}
Requires:	ffmpeg-devel
%{?with_opengl:Requires:	glew-devel >= 1.5}
Requires:	libtheora-devel >= 1.0-0.alpha7
Requires:	libupnp-devel >= 1.8
Requires:	libv4l-devel
Requires:	libvpx-devel >= 0.9.6
Requires:	opus-devel >= 0.9.0
Requires:	ortp-devel >= 5.1
%{?with_portaudio:Requires:	portaudio-devel}
%{?with_pulseaudio:Requires:	pulseaudio-devel >= 0.9.21}
Requires:	spandsp-devel >= 0.0.6
Requires:	speex-devel >= 1:1.2-beta3
Requires:	speexdsp-devel >= 1.2-beta3
%{?with_srtp:Requires:	libsrtp2-devel}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXv-devel

%description devel
Header files and development documentation for mediastreamer
libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do bibliotek mediastreamer.

%package static
Summary:	Static mediastreamer libraries
Summary(pl.UTF-8):	Statyczne biblioteki mediastreamer
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static mediastreamer libraries.

%description static -l pl.UTF-8
Statyczne biblioteki mediastreamer.

%prep
%setup -q -n mediastreamer2-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch10 -p1

# cmake checks for python3, so don't require python 2 as well
%{__sed} -i -e '1s,/usr/bin/python$,%{__python3},' tools/xxd.py

%{__sed} -i -e 's/"-Werror" /"-Werror" "-Wno-error=address"/' CMakeLists.txt

%build
install -d builddir
cd builddir
# NLS missing in cmake
CPPFLAGS="%{rpmcppflags} -DENABLE_NLS=1 -DGETTEXT_PACKAGE=\"mediastreamer\" -DLOCALEDIR=\"%{_localedir}\""
# note: NON_FREE_CODECS refer to H263, H264, MPEG4 via libavcodec
%cmake .. \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib} \
	-DDISABLE_BC_PACKAGE_SEARCH:BOOL=OFF \
	%{!?with_alsa:-DENABLE_ALSA=OFF} \
	%{?with_arts:-DENABLE_ARTSC=ON} \
	%{!?with_bv16:-DENABLE_BV16=OFF} \
	%{?with_spandsp:-DENABLE_G726=ON} \
	%{!?with_bcg729:-DENABLE_G729=OFF} \
	%{?with_bcg729:-DENABLE_G729B_CNG=ON} \
	%{!?with_opengl:-DENABLE_GL=OFF} \
	%{!?with_opengl:-DENABLE_GLX=OFF} \
	%{!?with_matroska:-DENABLE_MKV=OFF} \
	-DENABLE_NON_FREE_CODECS=ON \
	%{?with_oss:-DENABLE_OSS=ON} \
	%{?with_pcap:-DENABLE_PCAP=ON} \
	%{?with_portaudio:-DENABLE_PORTAUDIO=ON} \
	%{?with_pulseaudio:-DENABLE_PULSEAUDIO=ON} \
	%{!?with_zxing:-DENABLE_QRCODE=OFF} \
	%{?with_sdl:-DENABLE_SDL=ON} \
	%{!?with_srtp:-DENABLE_SRTP=OFF} \
	%{!?with_static_libs:-DENABLE_STATIC=OFF} \
	-DENABLE_UNIT_TESTS=OFF \
	%{!?with_zrtp:-DENABLE_ZRTP=OFF}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C builddir install \
	DESTDIR=$RPM_BUILD_ROOT

# disable completeness check incompatible with split packaging
%{__sed} -i -e '/^foreach(target .*IMPORT_CHECK_TARGETS/,/^endforeach/d; /^unset(_IMPORT_CHECK_TARGETS)/d' $RPM_BUILD_ROOT%{_datadir}/Mediastreamer2/cmake/Mediastreamer2Targets.cmake

# missing from install in cmake
install builddir/tools/msaudiocmp $RPM_BUILD_ROOT%{_bindir}
%if %{with pcap}
install builddir/tools/pcap_playback $RPM_BUILD_ROOT%{_bindir}
%endif
for f in po/*.po ; do
	lang=$(basename "$f" .po)
	install -d $RPM_BUILD_ROOT%{_localedir}/${lang}/LC_MESSAGES
	msgfmt -v -o $RPM_BUILD_ROOT%{_localedir}/${lang}/LC_MESSAGES/%{name}.mo "$f"
done

# for external plugins
install -d $RPM_BUILD_ROOT%{_libdir}/mediastreamer/plugins

# we don't need another copy
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/OpenGL
# Remove duplicated documentation
%{__rm} -r $RPM_BUILD_ROOT/usr/share/doc/mediastreamer2-5.1.0/html

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/mediastream
%attr(755,root,root) %{_bindir}/mkvstream
%attr(755,root,root) %{_bindir}/msaudiocmp
%{?with_pcap:%attr(755,root,root) %{_bindir}/pcap_playback}
%attr(755,root,root) %{_libdir}/libmediastreamer.so.11
%dir %{_libdir}/mediastreamer
%dir %{_libdir}/mediastreamer/plugins
%{_datadir}/mediastreamer

%files devel
%defattr(644,root,root,755)
%doc builddir/help/doc/html/*.{css,html,js,png}
%attr(755,root,root) %{_libdir}/libmediastreamer.so
%{_includedir}/mediastreamer2
%{_pkgconfigdir}/mediastreamer.pc
%dir %{_datadir}/Mediastreamer2
%{_datadir}/Mediastreamer2/cmake

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmediastreamer.a
%endif
