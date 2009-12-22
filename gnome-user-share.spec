Summary: GNOME user file sharing
Name: gnome-user-share
Version: 2.28.2
Release: %mkrel 1
License: GPLv2+
Group: System/Servers
URL: http://www.gnome.org
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Suggests: apache
Suggests: apache-mod_dnssd >= 0.6
Requires: obex-data-server >= 0.3
BuildRequires: apache-mod_dnssd
BuildRequires: libGConf2-devel
BuildRequires: libglade2.0-devel
BuildRequires: libnotify-devel
BuildRequires: gnome-bluetooth-devel
BuildRequires: dbus-glib-devel
BuildRequires: libcanberra-devel
BuildRequires: unique-devel
BuildRequires: intltool
BuildRequires: gnome-doc-utils
BuildRequires: GConf2
%description
This program enables user to share directories through Webdav or Bluetooth (over ObexFTP).

%prep
%setup -q

%build
%configure2_5x --with-modules-path=%_sysconfdir/httpd/extramodules
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std
%find_lang %name --with-gnome
for omf in %buildroot%_datadir/omf/*/%name-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done


%clean
rm -rf $RPM_BUILD_ROOT

%post
%post_install_gconf_schemas desktop_gnome_file_sharing
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas desktop_gnome_file_sharing

%postun
%clean_icon_cache hicolor

%files -f %name.lang
%defattr(-,root,root,-)
%doc README ChangeLog NEWS
%_sysconfdir/xdg/autostart/gnome-user-share.desktop
%{_sysconfdir}/gconf/schemas/desktop_gnome_file_sharing.schemas
%{_bindir}/*
%{_datadir}/gnome-user-share
%_datadir/applications/gnome-user-share-properties.desktop
%_libexecdir/gnome-user-share
%_datadir/icons/hicolor/*/apps/*.*
%dir %_datadir/omf/%name
%_datadir/omf/%name/%name-C.omf

