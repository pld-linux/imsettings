Summary:	Delivery framework for general Input Method configuration
#Summary(pl.UTF-8):	-
Name:		imsettings
Version:	1.2.4
Release:	3
License:	LGPL
Group:		Applications/System
Source0:	http://imsettings.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	aa4fdd4b24015c925ed53a6be24a790e
Patch0:		%{name}-constraint-of-language.patch
Patch1:		%{name}-no-bash.patch
URL:		http://code.google.com/p/imsettings/
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	glib2 >= 1:2.26.0
BuildRequires:	libgxim-devel >= 0.3.1
BuildRequires:	libnotify-devel
BuildRequires:	xfconf-devel
BuildRequires:	xorg-lib-libX11-devel
Requires:	imsettings-desktop-module = %{version}-%{release}
Requires:	imsettings-libs = %{version}-%{release}
Requires:	xinitrc-ng
Requires:	xorg-app-xinit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains the core DBus services and some utilities.

#%description -l pl.UTF-8

%package libs
Summary:	IMSettings library
Summary(pl.UTF-8):	Biblioteka IMSettings
Group:		Libraries

%description libs
IMSettings library.

%description libs -l pl.UTF-8
Biblioteka imsettings.

%package devel
Summary:	Header files for IMSettings library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki IMSettings
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

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

%package        xim
Summary:	XIM support on imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser

%description    xim
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains a module to get this working with XIM.

%package        gnome2
Summary:	GNOME 2 support on imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser
Provides:	imsettings-desktop-module = %{version}-%{release}

%description    gnome2
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains a module to get this working on GNOME 2.

%package        gnome3
Summary:	GNOME 3 support on imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser
Provides:	imsettings-desktop-module = %{version}-%{release}

%description    gnome3
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains a module to get this working on GNOME 3.

%package        qt
Summary:	Qt support on imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser
Provides:	imsettings-desktop-module = %{version}-%{release}

%description    qt
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains a module to get this working on Qt applications.

%package        xfce
Summary:	Xfce support on imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser
Requires:	xfce4-settings >= 4.6.0
Provides:	imsettings-desktop-module = %{version}-%{release}

%description    xfce
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains a module to get this working on Xfce.

%package        lxde
Summary:	LXDE support on imsettings
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
#Requires:	lxde-settings-daemon
Requires:	lxsession
Provides:	imsettings-desktop-module = %{version}-%{release}

%description    lxde
IMSettings is a framework that delivers Input Method settings and
applies the changes so they take effect immediately without any need
to restart applications or the desktop.

This package contains a module to get this working on LXDE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
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
%attr(755,root,root) %{_libdir}/libimsettings.so.[0-9]

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libimsettings.so
%{_pkgconfigdir}/imsettings.pc
%{_includedir}/imsettings
%{_gtkdocdir}/imsettings

%files static
%defattr(644,root,root,755)
%{_libdir}/libimsettings.a

%files  xim
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/imsettings-xim
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-xim.so

%files  gnome2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-gconf.so

%files  gnome3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-gsettings.so

%files  qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-qt.so

%files  xfce
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-xfce.so

%files  lxde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libimsettings-lxde.so
