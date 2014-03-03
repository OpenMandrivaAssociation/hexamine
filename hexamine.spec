Summary:	Hexagonal Minesweeper
Name:		hexamine
Version:	0.2.1
Release:	6
License:	GPLv2+
Group:		Games/Puzzles
Url:		http://sourceforge.net/projects/hexamine
Source0:	http://prdownloads.sourceforge.net/hexamine/%{name}-%{version}.tar.bz2
Source1:	%{name}.6
BuildRequires:	imagemagick
Requires:	pygame
BuildArch:	noarch

%description
A puzzle game, based on Minesweeper idea.

It introduces hexagonal grid, 3 different mine powers and extended
neighborhood information. All the above allows to present non trivial
but mostly solvable game situations even for most experienced player.

You can configure the game using system wide or user configuration file.

%files
%doc ABOUT README
%attr(0755,root,games) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}
perl -pi -e "s#./skins#%{_gamesdatadir}/%{name}/skins#g" hexamine.py
convert -size 16x16 skins/basic/hextile_flag_4.png %{name}-16.png
convert -size 32x32 skins/basic/hextile_flag_4.png %{name}-32.png
convert -size 48x48 skins/basic/hextile_flag_4.png %{name}-48.png

%build

%install
install -d -m 755 %{buildroot}%{_gamesbindir}
install -m 755 %{name}.py %{buildroot}%{_gamesbindir}/%{name}
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

#xdg menu
install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Hexamine
Comment=%{summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;LogicGame;
EOF

#man page
install -d -m 755 %{buildroot}/%{_mandir}/man6
install -m 644 %{SOURCE1} %{buildroot}/%{_mandir}/man6/%{name}.6

