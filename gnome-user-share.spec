Summary: GNOME user file sharing
Name: gnome-user-share
Version: 3.0.3
Release: 1
License: GPLv2+
Group: System/Servers
URL: http://www.gnome.org
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.28
BuildRequires:	pkgconfig(gnome-bluetooth-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libnautilus-extension)
BuildRequires:	pkgconfig(libnotify)

Suggests: apache
Suggests: apache-mod_dnssd >= 0.6
Requires: obex-data-server >= 0.3

%description
This program enables user to share directories through Webdav or Bluetooth 
(over ObexFTP).

%prep
%setup -q

%build
%configure2_5x \
	--with-modules-path=%{_sysconfdir}/httpd/modules \
	--disable-schemas-install \
	--disable-scrollkeeper

%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%find_lang %{name} --with-gnome

%post
%post_install_gconf_schemas desktop_gnome_file_sharing

%preun
%preun_uninstall_gconf_schemas desktop_gnome_file_sharing

%files -f %{name}.lang
%doc README ChangeLog NEWS
%{_sysconfdir}/xdg/autostart/gnome-user-share.desktop
%{_sysconfdir}/gconf/schemas/desktop_gnome_file_sharing.schemas
%{_bindir}/*
%{_libexecdir}/gnome-user-share
%{_libdir}/nautilus/extensions-3.0/libnautilus-share-extension.so
%{_datadir}/applications/gnome-user-share-properties.desktop
%{_datadir}/gnome-user-share
%{_datadir}/icons/hicolor/*/apps/*.*

