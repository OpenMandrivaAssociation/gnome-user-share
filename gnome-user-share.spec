Summary: Gnome user file sharing
Name: gnome-user-share
Version: 0.20
Release: %mkrel 1
License: GPL
Group: System/Servers
URL: http://www.gnome.org
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: avahi
Requires: apache
Requires: apache-mod_dav
BuildRequires: apache
BuildRequires: libGConf2-devel
BuildRequires: libavahi-client-devel libavahi-glib-devel
BuildRequires: libglade2.0-devel
BuildRequires: perl-XML-Parser
BuildRequires: GConf2
%description
gnome-user-share is a small package that binds together various free
software projects to bring easy to use user-level file sharing to the
masses.

The program is meant to run in the background when the user is logged
in, and when file sharing is enabled a webdav server is started that
shares the $HOME/Public folder. The share is then published to all
computers on the local network using mDNS/rendezvous, so that it shows
up in the Network location in Gnome.

The dav server used is apache, so you need that installed. Howl is
used for mDNS support, so you need to have that installed and
mDNSResolver running.

%prep
%setup -q

%build
%configure2_5x --with-httpd-version=2.2
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%post_install_gconf_schemas desktop_gnome_file_sharing

%preun
%preun_uninstall_gconf_schemas desktop_gnome_file_sharing

%files -f %name.lang
%defattr(-,root,root,-)
%doc README ChangeLog NEWS
%{_bindir}/*
%{_datadir}/gnome-user-share
%_datadir/applications/gnome-user-share-properties.desktop
%_datadir/gnome/autostart/gnome-user-share.desktop
%{_sysconfdir}/gconf/schemas/desktop_gnome_file_sharing.schemas
%_libexecdir/gnome-user-share


