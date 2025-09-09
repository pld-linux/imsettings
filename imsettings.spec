#
# Conditional build:
%bcond_without	apidocs		# gtk-doc based API documentation
%bcond_without	gconf		# GNOME 2.x (GConf) support module
%bcond_with	mateconf	# MATE <= 1.4 (MateConf) support module
%bcond_without	xfce		# Xfce support module
%bcond_without	static_libs	# static library
#
Summary:	Delivery framework for general Input Method configuration
Summary(pl.UTF-8):	Szkielet do ogólnej konfiguracji method wprowadzania znaków
Name:		imsettings
Version:	1.8.10
Release:	1
License:	LGPL v2+
Group:		Applications/System
#Source0Download: https://gitlab.com/tagoh/imsettings/-/releases
Source0:	https://gitlab.com/tagoh/imsettings/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	ebad666e92bc4da59ba3947b9275d8fb
Patch0:		%{name}-constraint-of-language.patch
Patch1:		%{name}-no-bash.patch
URL:		https://gitlab.com/tagoh/imsettings/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
%{?with_gconf:BuildRequires:	GConf2-devel >= 2.0}
BuildRequires:	dbus-devel
BuildRequires:	desktop-file-utils
BuildRequires:	docbook2X
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.70.0
BuildRequires:	gobject-introspection-devel >= 1.30.0
# for fallback support in GTK+
BuildRequires:	gtk+2-devel >= 2:2.24.11
BuildRequires:	gtk+3-devel >= 3.3.3
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libgxim-devel >= 0.5.0
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libtool >= 2:2.2
%{?with_mateconf:BuildRequires:	mate-conf-devel}
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
%{?with_xfce:BuildRequires:	xfconf-devel}
BuildRequires:	xorg-lib-libX11-devel
Requires:	%{name}-desktop-module = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libnotify >= 0.7.0
Requires:	xinitrc-ng
Requires:	xorg-app-xinit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains the core DBus services and some utilities.

%description -l pl.UTF-8
IMSettings to szkielet udostępniający ustawienia metod wprowadzania
znaków (Input Method) i wykonujący zmiany tak, że wchodzą w życie
natychmiast bez potrzeby restartu aplikacji ani środowiska
graficznego.

Ten pakiet zawiera główne usługi DBus oraz trochę narzędzi.

%package libs
Summary:	IMSettings library
Summary(pl.UTF-8):	Biblioteka IMSettings
Group:		Libraries
Requires:	glib2 >= 1:2.70.0

%description libs
IMSettings library.

%description libs -l pl.UTF-8
Biblioteka imsettings.

%package devel
Summary:	Header files for IMSettings library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki IMSettings
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.70.0

%description devel
Header files for IMSettings library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki IMSettings.

%package static
Summary:	Static IMSettings library
Summary(pl.UTF-8):	Statyczna biblioteka IMSettings
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static IMSettings library.

%description static -l pl.UTF-8
Statyczna biblioteka IMSettings.

%package apidocs
Summary:	API documentation for IMSettings library
Summary(pl.UTF-8):	Dokumentacja API biblioteki IMSettings
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for IMSettings library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki IMSettings.

%package cinnamon
Summary:	Cinnamon (via GSettings) support on imsettings
Summary(pl.UTF-8):	Obsługa Cinnamon (poprzez GSettings) dla imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser
Provides:	%{name}-desktop-module = %{version}-%{release}

%description cinnamon
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains a module to get this working on Cinnamon (using
GSettings).

%description cinnamon -l pl.UTF-8
IMSettings to szkielet udostępniający ustawienia metod wprowadzania
znaków (Input Method) i wykonujący zmiany tak, że wchodzą w życie
natychmiast bez potrzeby restartu aplikacji ani środowiska
graficznego.

Ten pakiet zawiera moduł umożliwiający to dla aplikacji Cinnamon
(korzystających z GSettings).

%package gnome2
Summary:	GNOME 2 (GConf) support on imsettings
Summary(pl.UTF-8):	Obsługa GNOME 2 (GConfa) dla imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser
Provides:	%{name}-desktop-module = %{version}-%{release}

%description gnome2
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains a module to get this working on GNOME 2 (using
GConf).

%description gnome2 -l pl.UTF-8
IMSettings to szkielet udostępniający ustawienia metod wprowadzania
znaków (Input Method) i wykonujący zmiany tak, że wchodzą w życie
natychmiast bez potrzeby restartu aplikacji ani środowiska
graficznego.

Ten pakiet zawiera moduł umożliwiający to dla aplikacji GNOME 2
(korzystających z GConfa).

%package gnome3
Summary:	GNOME 3 (GSettings) support on imsettings
Summary(pl.UTF-8):	Obsługa GNOME 3 (GSettings) dla imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser
Provides:	%{name}-desktop-module = %{version}-%{release}

%description gnome3
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains a module to get this working on GNOME 3 (using
GSettings).

%description gnome3 -l pl.UTF-8
IMSettings to szkielet udostępniający ustawienia metod wprowadzania
znaków (Input Method) i wykonujący zmiany tak, że wchodzą w życie
natychmiast bez potrzeby restartu aplikacji ani środowiska
graficznego.

Ten pakiet zawiera moduł umożliwiający to dla aplikacji GNOME 3
(korzystających z GSettings).

%package lxde
Summary:	LXDE support on imsettings
Summary(pl.UTF-8):	Obsługa LXDE dla imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
#Requires:	lxde-settings-daemon
Requires:	lxsession
Provides:	%{name}-desktop-module = %{version}-%{release}

%description lxde
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains a module to get this working on LXDE.

%description lxde -l pl.UTF-8
IMSettings to szkielet udostępniający ustawienia metod wprowadzania
znaków (Input Method) i wykonujący zmiany tak, że wchodzą w życie
natychmiast bez potrzeby restartu aplikacji ani środowiska
graficznego.

Ten pakiet zawiera moduł umożliwiający to dla aplikacji LXDE.

%package mate-conf
Summary:	MATE <= 1.4 (MateConf) support on imsettings
Summary(pl.UTF-8):	Obsługa MATE <= 1.4 (MateConfa) dla imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser
Provides:	%{name}-desktop-module = %{version}-%{release}

%description mate-conf
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains a module to get this working on MATE <= 1.4
(using MateConf).

%description mate-conf -l pl.UTF-8
IMSettings to szkielet udostępniający ustawienia metod wprowadzania
znaków (Input Method) i wykonujący zmiany tak, że wchodzą w życie
natychmiast bez potrzeby restartu aplikacji ani środowiska
graficznego.

Ten pakiet zawiera moduł umożliwiający to dla aplikacji MATE <= 1.4
(korzystających z MateConfa).

%package mate
Summary:	MATE 1.5+ (mate-settings) support on imsettings
Summary(pl.UTF-8):	Obsługa MATE 1.5+ (mate-settings) dla imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser
Provides:	%{name}-desktop-module = %{version}-%{release}

%description mate
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains a module to get this working on MATE 1.5+ (using
mate-settings).

%description mate -l pl.UTF-8
IMSettings to szkielet udostępniający ustawienia metod wprowadzania
znaków (Input Method) i wykonujący zmiany tak, że wchodzą w życie
natychmiast bez potrzeby restartu aplikacji ani środowiska
graficznego.

Ten pakiet zawiera moduł umożliwiający to dla aplikacji MATE 1.5+
(korzystających z mate-settings).

%package qt
Summary:	Qt support on imsettings
Summary(pl.UTF-8):	Obsługa Qt dla imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser
Provides:	%{name}-desktop-module = %{version}-%{release}

%description qt
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains a module to get this working on Qt applications.

%description qt -l pl.UTF-8
IMSettings to szkielet udostępniający ustawienia metod wprowadzania
znaków (Input Method) i wykonujący zmiany tak, że wchodzą w życie
natychmiast bez potrzeby restartu aplikacji ani środowiska
graficznego.

Ten pakiet zawiera moduł umożliwiający to dla aplikacji Qt.

%package xfce
Summary:	Xfce support on imsettings
Summary(pl.UTF-8):	Obsługa Xfce dla imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser
Requires:	xfce4-settings >= 4.6.0
Provides:	%{name}-desktop-module = %{version}-%{release}

%description xfce
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains a module to get this working on Xfce.

%description xfce -l pl.UTF-8
IMSettings to szkielet udostępniający ustawienia metod wprowadzania
znaków (Input Method) i wykonujący zmiany tak, że wchodzą w życie
natychmiast bez potrzeby restartu aplikacji ani środowiska
graficznego.

Ten pakiet zawiera moduł umożliwiający to dla aplikacji Xfce.

%package xim
Summary:	XIM support on imsettings
Summary(pl.UTF-8):	Obsługa XIM dla imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser
Requires:	libgxim >= 0.5.0

%description xim
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains a module to get this working with XIM.

%description xim -l pl.UTF-8
IMSettings to szkielet udostępniający ustawienia metod wprowadzania
znaków (Input Method) i wykonujący zmiany tak, że wchodzą w życie
natychmiast bez potrzeby restartu aplikacji ani środowiska
graficznego.

Ten pakiet zawiera moduł umożliwiający to dla usługi XIM.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%{__sed} -i -e '/po\/Makefile\.in/d' configure.ac

install -d m4macros

%build
%{__gtkdocize}
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	DB2MAN=/usr/bin/docbook2X2man \
	%{?with_apidocs:--enable-gtk-doc} \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-xinputsh=50-xinput.sh \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/imsettings/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/imsettings/*.a
%endif

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{eu_ES,eu}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README

%attr(755,root,root) %{_sysconfdir}/X11/xinit/xinitrc.d/50-xinput.sh
%{_sysconfdir}/X11/xinit/xinput.d/none.conf
%{_sysconfdir}/X11/xinit/xinput.d/xcompose.conf
%{_sysconfdir}/X11/xinit/xinput.d/xim.conf
%{_sysconfdir}/xdg/autostart/imsettings-start.desktop

%attr(755,root,root) %{_bindir}/imsettings-reload
%attr(755,root,root) %{_bindir}/imsettings-list
%attr(755,root,root) %{_bindir}/imsettings-info
%attr(755,root,root) %{_bindir}/imsettings-switch

%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-systemd-gtk.so
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-systemd-qt.so

%{_libexecdir}/imsettings-functions
%attr(755,root,root) %{_libexecdir}/imsettings-check
%attr(755,root,root) %{_libexecdir}/imsettings-daemon
%attr(755,root,root) %{_libexecdir}/xinputinfo.sh
%attr(755,root,root) %{_libexecdir}/imsettings-target-checker.sh
%{_datadir}/dbus-1/services/com.redhat.imsettings.service
%{_pixmapsdir}/imsettings-unknown.png

%{_mandir}/man1/imsettings-*.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libimsettings.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libimsettings.so.5
%{_libdir}/girepository-1.0/IMSettings-1.8.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libimsettings.so
%{_pkgconfigdir}/imsettings.pc
%{_includedir}/imsettings
%{_datadir}/gir-1.0/IMSettings-1.8.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libimsettings.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/imsettings
%endif

%files cinnamon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-cinnamon-gsettings.so

%if %{with gconf}
%files gnome2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-gconf.so
%endif

%files gnome3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-gsettings.so

%files lxde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-lxde.so

%if %{with mateconf}
%files mate-conf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-mateconf.so
%endif

%files mate
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-mate-gsettings.so

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-qt.so

%if %{with xfce}
%files xfce
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-xfce.so
%endif

%files xim
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/imsettings-xim
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-xim.so
