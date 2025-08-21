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
%bcond_without	zxing		# QRcode support via zxing-cpp-nu
#
Summary:	Audio/Video real-time streaming
Summary(pl.UTF-8):	Przesyłanie strumieni audio/video w czasie rzeczywistym 
Name:		mediastreamer
Version:	5.4.17
Release:	2
License:	AGPL v3+
Group:		Libraries
#Source0Download: https://gitlab.linphone.org/BC/public/mediastreamer2/tags
Source0:	https://gitlab.linphone.org/BC/public/mediastreamer2/-/archive/%{version}/mediastreamer2-%{version}.tar.bz2
# Source0-md5:	0d16486bc086c9fdad8c6c17d104056b
Patch0:		build.patch
Patch1:		%{name}-cmake-link.patch
Patch2:		libupnp-1.14.patch
Patch3:		%{name}-cmake-datadir.patch
Patch4:		%{name}-cmake-install-pkgconfig.patch
Patch5:		%{name}-cmake-SDL.patch
Patch6:		%{name}-types.patch
Patch7:		ffmpeg_5_0_fixes.patch
Patch8:		%{name}-cmake-find.patch
URL:		https://www.linphone.org/technical-corner/mediastreamer2-ortp
%{?with_opengl:BuildRequires:	OpenGL-GLX-devel}
%{?with_sdl:BuildRequires:	SDL-devel >= 1.2.0}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	aom-devel
%{?with_arts:BuildRequires:	artsc-devel}
%{?with_bcg729:BuildRequires:	bcg729-devel >= 1.1.1-2}
%{?with_matroska:BuildRequires:	bcmatroska2-devel >= 5.3}
BuildRequires:	bctoolbox-devel >= 5.3.0
%{?with_bv16:BuildRequires:	bv16-floatingpoint-devel}
%{?with_zrtp:BuildRequires:	bzrtp-devel >= 5.3.0}
BuildRequires:	cmake >= 3.22
BuildRequires:	dav1d-devel
BuildRequires:	doxygen
# libavcodec >= 51.0.0, libswscale >= 0.7.0
BuildRequires:	ffmpeg-devel >= 4.4
BuildRequires:	gettext-tools
%{?with_opengl:BuildRequires:	glew-devel >= 1.5}
BuildRequires:	intltool >= 0.40
BuildRequires:	libgsm-devel
BuildRequires:	libjpeg-turbo-devel
%{?with_pcap:BuildRequires:	libpcap-devel}
%{?with_srtp:BuildRequires:	libsrtp2-devel >= 2}
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libtheora-devel >= 1.0-0.alpha7
BuildRequires:	libupnp-devel >= 1.8
BuildRequires:	libv4l-devel
BuildRequires:	libvpx-devel >= 0.9.6
BuildRequires:	libyuv-devel
BuildRequires:	opus-devel >= 0.9.0
BuildRequires:	ortp-devel >= 5.3.0
BuildRequires:	pkgconfig
%{?with_portaudio:BuildRequires:	portaudio-devel}
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel >= 0.9.21}
BuildRequires:	python3 >= 1:3
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sed >= 4.0
%{?with_spandsp:BuildRequires:	spandsp-devel >= 0.0.6}
BuildRequires:	speex-devel >= 1:1.2-beta3
BuildRequires:	speexdsp-devel >= 1.2-beta3
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXv-devel
%{?with_zxing:BuildRequires:	zxing-cpp-nu-devel}
%{?with_bcg729:Requires:	bcg729 >= 1.1.1-2}
%{?with_matroska:Requires:	bcmatroska2 >= 5.3}
Requires:	bctoolbox >= 5.3.0
%{?with_zrtp:Requires:	bzrtp >= 5.3.0}
%{?with_opengl:Requires:	glew >= 1.5}
Requires:	libtheora >= 1.0-0.alpha7
Requires:	libvpx >= 0.9.6
Requires:	opus >= 0.9.0
Requires:	ortp >= 5.3.0
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
%{?with_bcg729:Requires:	bcg729-devel >= 1.1.1-2}
%{?with_matroska:Requires:	bcmatroska2-devel >= 5.3}
Requires:	bctoolbox-devel >= 5.3.0
%{?with_bv16:Requires:	bv16-floatingpoint-devel}
%{?with_zrtp:Requires:	bzrtp-devel >= 5.3.0}
Requires:	ffmpeg-devel >= 4.4
%{?with_opengl:Requires:	glew-devel >= 1.5}
%{?with_srtp:Requires:	libsrtp2-devel >= 2}
Requires:	libtheora-devel >= 1.0-0.alpha7
Requires:	libupnp-devel >= 1.8
Requires:	libv4l-devel
Requires:	libvpx-devel >= 0.9.6
Requires:	opus-devel >= 0.9.0
Requires:	ortp-devel >= 5.3.0
%{?with_portaudio:Requires:	portaudio-devel}
%{?with_pulseaudio:Requires:	pulseaudio-devel >= 0.9.21}
Requires:	spandsp-devel >= 0.0.6
Requires:	speex-devel >= 1:1.2-beta3
Requires:	speexdsp-devel >= 1.2-beta3
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
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1

# cmake checks for python3, so don't require python 2 as well
%{__sed} -i -e '1s,/usr/bin/python$,%{__python3},' tools/xxd.py

%{__sed} -i -e 's/"-Werror" /"-Werror" "-Wno-error=address" "-Wno-error=unused-parameter"/' CMakeLists.txt

%build
configure() {
set -x
builddir="$1"
shift
# note: NON_FREE_FEATURES refer to H263, H264, MPEG4 via libavcodec
%cmake -B "$builddir" \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib} \
	%{!?with_alsa:-DENABLE_ALSA=OFF} \
	%{?with_arts:-DENABLE_ARTSC=ON} \
	%{!?with_bv16:-DENABLE_BV16=OFF} \
	%{?with_spandsp:-DENABLE_G726=ON} \
	%{!?with_bcg729:-DENABLE_G729=OFF} \
	%{?with_bcg729:-DENABLE_G729B_CNG=ON} \
	%{!?with_opengl:-DENABLE_GL=OFF} \
	%{!?with_opengl:-DENABLE_GLX=OFF} \
	%{!?with_matroska:-DENABLE_MKV=OFF} \
	-DENABLE_NON_FREE_FEATURES=ON \
	%{?with_oss:-DENABLE_OSS=ON} \
	%{?with_pcap:-DENABLE_PCAP=ON} \
	%{?with_portaudio:-DENABLE_PORTAUDIO=ON} \
	%{?with_pulseaudio:-DENABLE_PULSEAUDIO=ON} \
	%{!?with_zxing:-DENABLE_QRCODE=OFF} \
	%{?with_sdl:-DENABLE_SDL=ON} \
	%{!?with_srtp:-DENABLE_SRTP=OFF} \
	-DENABLE_UNIT_TESTS=OFF \
	%{!?with_zrtp:-DENABLE_ZRTP=OFF} \
	"$@"
}

# NLS missing in cmake
# GSM_USE_BUILD_INTERFACE to include <gsm.h> instead of <gsm/gsm.h>
CPPFLAGS="%{rpmcppflags} -DENABLE_NLS=1 -DGETTEXT_PACKAGE=\\\"mediastreamer\\\" -DLOCALEDIR=\\\"%{_localedir}\\\" -DGSM_USE_BUILD_INTERFACE=1"
# CPPFLAGS are not used, so append
CFLAGS="%{rpmcflags} $CPPFLAGS"
CXXFLAGS="%{rpmcxxflags} $CPPFLAGS"

%if %{with static_libs}
configure builddir-static \
	-DBUILD_SHARED_LIBS=OFF

%{__make} -C builddir-static
%endif

configure builddir

%{__make} -C builddir

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} -C builddir-static install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C builddir install \
	DESTDIR=$RPM_BUILD_ROOT

# missing from install in cmake
install builddir/tools/mediastreamer2-msaudiocmp $RPM_BUILD_ROOT%{_bindir}
%if %{with pcap}
install builddir/tools/mediastreamer2-pcap_playback $RPM_BUILD_ROOT%{_bindir}
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
%{__rm} -r $RPM_BUILD_ROOT/usr/share/doc/mediastreamer2-5.4.0/html

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/mediastreamer2-mediastream
%attr(755,root,root) %{_bindir}/mediastreamer2-mkvstream
%attr(755,root,root) %{_bindir}/mediastreamer2-msaudiocmp
%if %{with pcap}
%attr(755,root,root) %{_bindir}/mediastreamer2-pcap-playback
%endif
%attr(755,root,root) %{_bindir}/mediastreamer2-player
%attr(755,root,root) %{_bindir}/mediastreamer2-recorder
%attr(755,root,root) %{_libdir}/libmediastreamer2.so.11
%dir %{_libdir}/mediastreamer
%dir %{_libdir}/mediastreamer/plugins
%{_datadir}/mediastreamer

%files devel
%defattr(644,root,root,755)
%doc builddir/help/doc/html/*.{css,html,js,png}
%attr(755,root,root) %{_libdir}/libmediastreamer2.so
%{_includedir}/mediastreamer2
%{_pkgconfigdir}/mediastreamer.pc
%dir %{_datadir}/Mediastreamer2
%{_datadir}/Mediastreamer2/cmake

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmediastreamer2.a
%endif
