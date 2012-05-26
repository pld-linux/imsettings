#
# Conditional build:
%bcond_without	xfce	# Xfce support module
#
Summary:	Delivery framework for general Input Method configuration
Summary(pl.UTF-8):	Szkielet do ogólnej konfiguracji method wprowadzania znaków
Name:		imsettings
Version:	1.2.9
Release:	1
License:	LGPL v2+
Group:		Applications/System
#Source0Download: http://code.google.com/p/imsettings/downloads/list
Source0:	http://imsettings.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	3e4b97705bca1fba195e3a0cabd253d5
Patch0:		%{name}-constraint-of-language.patch
Patch1:		%{name}-no-bash.patch
Patch2:		glib.patch
URL:		http://code.google.com/p/imsettings/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	dbus-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
# "fallback support in GTK+"
#BuildRequires:	gtk+3-devel >= 3.3.3
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libgxim-devel >= 0.3.1
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	pkgconfig
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
Requires:	glib2 >= 1:2.26.0

%description libs
IMSettings library.

%description libs -l pl.UTF-8
Biblioteka imsettings.

%package devel
Summary:	Header files for IMSettings library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki IMSettings
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.26.0

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

%package xim
Summary:	XIM support on imsettings
Summary(pl.UTF-8):	Obsługa XIM dla imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser
Requires:	libgxim >= 0.3.1

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

%package gnome2
Summary:	GNOME 2 (GConf) support on imsettings
Summary(pl.UTF-8):	Obsługa GNOME 2 (GConf) dla imsettings
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure \
	--disable-silent-rules \
	--with-xinputsh=50-xinput.sh \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/imsettings/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README

%{_sysconfdir}/X11/xinit/xinitrc.d/50-xinput.sh
%dir %{_sysconfdir}/X11/xinit/xinput.d
%{_sysconfdir}/X11/xinit/xinput.d/*.conf
%{_sysconfdir}/xdg/autostart/imsettings-start.desktop

%attr(755,root,root) %{_bindir}/imsettings-reload
%attr(755,root,root) %{_bindir}/imsettings-list
%attr(755,root,root) %{_bindir}/imsettings-info
%attr(755,root,root) %{_bindir}/imsettings-check
%attr(755,root,root) %{_bindir}/imsettings-switch

%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/imsettings-daemon
%attr(755,root,root) %{_libdir}/xinputinfo.sh
%{_datadir}/dbus-1/services/imsettings-daemon.service
%{_pixmapsdir}/imsettings-unknown.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libimsettings.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libimsettings.so.5
%{_libdir}/girepository-1.0/IMSettings-1.2.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libimsettings.so
%{_pkgconfigdir}/imsettings.pc
%{_includedir}/imsettings
%{_datadir}/gir-1.0/IMSettings-1.2.gir
%{_gtkdocdir}/imsettings

%files static
%defattr(644,root,root,755)
%{_libdir}/libimsettings.a

%files xim
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/imsettings-xim
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-xim.so

%files gnome2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-gconf.so

%files gnome3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-gsettings.so

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-qt.so

%if %{with xfce}
%files xfce
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-xfce.so
%endif

%files lxde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-lxde.so
