# TODO:
# - switch to mbledtls when 2.x is supported (mbed_ssl_init instead of ssl_init)
# - dtls (polarssl/mbedtls >= 1.4 with DTLS-SRTP support, not released yet)
#
# Conditional build:
%bcond_without	bcg729		# support for G279AnnexB in RTC3389 implementation of Comfort Noise Payload
%bcond_without	srtp		# SRTP (secure RTP) support
%bcond_without	zrtp		# support for RFC 6189: Media Path Key Agreement for Unicast Secure RTP
%bcond_without	matroska	# Matroska support via libebml2/libmatroska2
%bcond_without	opengl		# X11+OpenGL rendering support
%bcond_with	pcap		# audio playing from PCAP files
# audio I/O
%bcond_without	alsa		# ALSA sound I/O support
%bcond_with	arts		# aRts sound I/O support
%bcond_with	portaudio	# PortAudio sound I/O support
%bcond_without	pulseaudio	# PulseAudio sound I/O support
%bcond_without	static_libs	# static library
#
Summary:	Audio/Video real-time streaming
Summary(pl.UTF-8):	Przesyłanie strumieni audio/video w czasie rzeczywistym 
Name:		mediastreamer
Version:	2.12.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://download-mirror.savannah.gnu.org/releases/linphone/mediastreamer/%{name}-%{version}.tar.gz
# Source0-md5:	1ca115e94a718638fbecf8352c169861
Patch0:		%{name}-imagedir.patch
Patch1:		%{name}-ffmpeg.patch
Patch2:		%{name}-werror.patch
URL:		http://www.linphone.org/technical-corner/mediastreamer2/overview
%{?with_opengl:BuildRequires:	OpenGL-GLX-devel}
BuildRequires:	SDL-devel >= 1.2.0
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	artsc-devel}
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
%{?with_bcg729:BuildRequires:	bcg729-devel >= 1.0}
%{?with_zrtp:BuildRequires:	bzrtp-devel >= 1.0.0}
BuildRequires:	doxygen
# libavcodec >= 51.0.0, libswscale >= 0.7.0
BuildRequires:	ffmpeg-devel
BuildRequires:	gettext-tools
%{?with_opengl:BuildRequires:	glew-devel >= 1.5}
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	intltool >= 0.40
BuildRequires:	libgsm-devel
%{?with_pcap:BuildRequires:	libpcap-devel}
BuildRequires:	libtheora-devel >= 1.0-0.alpha7
BuildRequires:	libtool >= 2:2
BuildRequires:	libupnp-devel >= 1.6
BuildRequires:	libupnp-devel < 1.7
BuildRequires:	libv4l-devel
BuildRequires:	libvpx-devel >= 0.9.6
%{?with_matroska:BuildRequires:	matroska-foundation-devel}
BuildRequires:	opus-devel >= 0.9.0
BuildRequires:	ortp-devel >= 0.24.0
BuildRequires:	pkgconfig
BuildRequires:	polarssl-devel
%{?with_portaudio:BuildRequires:	portaudio-devel}
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel >= 0.9.21}
BuildRequires:	sed >= 4.0
BuildRequires:	spandsp-devel >= 0.0.6
BuildRequires:	speex-devel >= 1:1.2-beta3
BuildRequires:	speexdsp-devel >= 1.2-beta3
%{?with_srtp:BuildRequires:	srtp-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xxd
%{?with_bcg729:Requires:	bcg729 >= 1.0}
%{?with_zrtp:Requires:	bzrtp >= 1.0.0}
%{?with_opengl:Requires:	glew >= 1.5}
Requires:	libtheora >= 1.0-0.alpha7
Requires:	libupnp >= 1.6
Requires:	libvpx >= 0.9.6
Requires:	opus >= 0.9.0
Requires:	ortp >= 0.24.0
%{?with_pulseaudio:Requires:	pulseaudio-libs >= 0.9.21}
Requires:	spandsp >= 0.0.6
Requires:	speex >= 1:1.2-beta3
Requires:	speexdsp >= 1.2-beta3
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
%{?with_bcg729:Requires:	bcg729-devel >= 1.0}
%{?with_zrtp:Requires:	bzrtp-devel >= 1.0.0}
Requires:	ffmpeg-devel
%{?with_opengl:Requires:	glew-devel >= 1.5}
Requires:	libtheora-devel >= 1.0-0.alpha7
Requires:	libupnp-devel >= 1.6
Requires:	libupnp-devel < 1.7
Requires:	libv4l-devel
Requires:	libvpx-devel >= 0.9.6
%{?with_matroska:Requires:	matroska-foundation-devel}
Requires:	opus-devel >= 0.9.0
Requires:	ortp-devel >= 0.24.0
Requires:	polarssl-devel
%{?with_portaudio:Requires:	portaudio-devel}
%{?with_pulseaudio:Requires:	pulseaudio-devel >= 0.9.21}
Requires:	spandsp-devel >= 0.0.6
Requires:	speex-devel >= 1:1.2-beta3
Requires:	speexdsp-devel >= 1.2-beta3
%{?with_srtp:Requires:	srtp-devel}
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
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-alsa%{!?with_alsa:=no} \
	%{?with_arts:--enable-artsc} \
	%{?with_bcg729:--enable-bcg729} \
	--enable-external-ortp \
	%{!?with_opengl:--disable-glx} \
	%{!?with_matroska:--disable-matroska} \
	%{?with_pcap:--enable-pcap} \
	%{?with_portaudio:--enable-portaudio} \
	--enable-pulseaudio%{!?with_pulseaudio:=no} \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	%{!?with_zrtp:--disable-zrtp} \
	%{!?with_srtp:--with-srtp=none}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	install_sh=/usr/bin/install

# for external plugins
install -d $RPM_BUILD_ROOT%{_libdir}/mediastreamer/plugins

# Remove duplicated documentation
%{__rm} -r $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/html

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mediastream
%attr(755,root,root) %{_bindir}/msaudiocmp
%{?with_pcap:%attr(755,root,root) %{_bindir}/pcap_playback}
%attr(755,root,root) %{_libdir}/libmediastreamer_base.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmediastreamer_base.so.6
%attr(755,root,root) %{_libdir}/libmediastreamer_voip.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmediastreamer_voip.so.6
%dir %{_libdir}/mediastreamer
%dir %{_libdir}/mediastreamer/plugins
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

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmediastreamer_base.a
%{_libdir}/libmediastreamer_voip.a
%endif
