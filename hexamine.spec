%define name	hexamine
%define version	0.2.1
%define rel	2
%define release	%mkrel %rel

Summary:	Hexagonal Minesweeper
Name:		%{name}
Version:	%{version}
Release:	%{release}
Requires:	pygame
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Group:		Games/Puzzles
License:	GPL
URL:		http://sourceforge.net/projects/%{name}
BuildRequires:  imagemagick
BuildArch:	noarch
BuildRoot:	%_tmppath/%{name}-build

%description
A puzzle game, based on Minesweeper idea.
It introduces hexagonal grid, 3 different mine powers and extended 
neighborhood information. All the above allows to present non trivial 
but mostly solvable game situations even for most experienced player.

You can configure the game using system wide or user configuration file.

%prep

%setup -q -n %{name}
perl -pi -e "s#./skins#%{_gamesdatadir}/%{name}/skins#g" hexamine.py
convert -size 16x16 skins/basic/hextile_flag_4.png %{name}-16.png
convert -size 32x32 skins/basic/hextile_flag_4.png %{name}-32.png
convert -size 48x48 skins/basic/hextile_flag_4.png %{name}-48.png

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_gamesbindir}
install -m 755 %{name}.py %{buildroot}%{_gamesbindir}
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{name}/skins/basic/
install -m 644 skins/basic/* %{buildroot}%{_gamesdatadir}/%{name}/skins/basic/
install -d -m 755 %{buildroot}/%{_sysconfdir}
install -m 644 %{name}.conf %{buildroot}/%{_sysconfdir}

#icons
install -d -m 755 %{buildroot}/%{_miconsdir}
install -m 644 %{name}-16.png %{buildroot}/%{_miconsdir}/%{name}.png
install -d -m 755 %{buildroot}/%{_iconsdir}
install -m 644 %{name}-32.png %{buildroot}/%{_iconsdir}/%{name}.png
install -d -m 755 %{buildroot}/%{_liconsdir}
install -m 644 %{name}-48.png %{buildroot}/%{_liconsdir}/%{name}.png

#old debian-type menu
install -d -m 755 %{buildroot}%{_menudir}
cat > %{buildroot}%{_menudir}/%{name} << EOF
?package(%name): needs="x11" \
	section="More Applications/Games/Puzzles" \
	title="Hexamine" \
	longtitle="%{summary}" \
	command="%{_gamesbindir}/%{name}.py" \
	icon="%{name}.png" \
	xdg="true"
EOF

#xdg menu
install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Hexamine
Comment=%{summary}
Exec=%{_gamesbindir}/%{name}.py
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;LogicGame;X-MandrivaLinux-MoreApplications-Games-Puzzles;
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc ABOUT README
%attr(0755,root,games) %{_gamesbindir}/%{name}.py
%{_gamesdatadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

