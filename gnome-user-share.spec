%define _disable_rebuild_configure 1
%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	GNOME user file sharing
Name:		gnome-user-share
Version:	3.32.0.1
Release:	1
License:	GPLv2+
Group:		System/Servers
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-user-share/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0) >= 2.28
BuildRequires:	pkgconfig(gnome-bluetooth-1.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libnautilus-extension)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libsystemd)
Suggests:	apache
Suggests:	apache-mod_dnssd >= 0.6
Requires:	obex-data-server >= 0.3

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

%make_build

%install
%make_install
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README ChangeLog NEWS
%{_libexecdir}/gnome-user-share-webdav
%{_libdir}/nautilus/extensions-3.0/libnautilus-share-extension.so
%{_datadir}/applications/gnome-user-share-webdav.desktop
%{_datadir}/gnome-user-share
%{_datadir}/GConf/gsettings/gnome-user-share.convert
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.file-sharing.gschema.xml
%{_userunitdir}/gnome-user-share-webdav.service

