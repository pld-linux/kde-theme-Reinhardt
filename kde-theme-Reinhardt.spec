%define		_theme 	reinhardt
%define		_theme_ver 0.6.3
%define         _icons_ver 0.9
%define         _splash_ver 0.1
%define         _gdm_ver 0.2

Summary:	KDE theme - %{_theme}
Summary(pl.UTF-8):	Motyw KDE - %{_theme}
Name:		kde-theme-%{_theme}
Version:	%{_theme_ver}
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/5962-%{_theme}style-%{version}.tar.bz2
# Source0-md5:	65dcd0ba30ee19aa630c3ee3dc25b31b
Source1:	slickerwallpaper.png
Source2:	http://slicker.sourceforge.net/%{_theme}icons-%{_icons_ver}-svg.tar.bz2
# Source2-md5:	e34ac71369898d76d289032c8c4d3dca
Source3:	http://www.kde-look.org/content/files/9399-myreinhart.kcsrc
# Source3-md5:	9df54d0b9137e59bea3339ee096e77d5
Source4:	http://www.kde-look.org/content/files/7021-slickersplash-0.1.tar.bz2
# Source4-md5:	f609df4c9fe6a0fa08d1320efbb168e9
Source5:	http://www.kde-look.org/content/files/9411-reinhardt.kcsrc
# Source5-md5:	15f86c7f4b05d37532e2b812dd234b56
Source6:	http://www.kde-look.org/content/files/9948-reinhardtgdm-0.2.tar.bz2
# Source6-md5:	de2335b4802cc713f7f120591985cf63
Patch0:		%{_theme}-admin.patch.bz2
URL:		http://www.kde-look.org/content/show.php?content=5962
# Also: http://www.kde-look.org/content/show.php?content=5993
# Also: http://www.kde-look.org/content/show.php?content=6153
# Also: http://www.kde-look.org/content/show.php?content=9399
# Also: http://www.kde-look.org/content/show.php?content=7021
# Also: http://www.kde-look.org/content/show.php?content=9411
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

%description
%{_theme} is a slicker theme that was designed to look nice with
slicker. To developer's surprise, this style looks good even without
slicker.

%description -l pl.UTF-8
%{_theme} to motyw stworzony by współgrał z aplikacją slicker. Ku
zaskoczeniu twórców, styl ten jednak okazał się pięknie wyglądać nawet
bez slickera.

%package -n kde-style-%{_theme}
Summary:	KDE style - %{_theme}
Summary(pl.UTF-8):	Styl do KDE - %{_theme}
Group:		Themes
URL:		http://www.kde-look.org/content/show.php?content=5962
Version:	%{_theme_ver}
License:	GPL
Requires:	kdelibs
Obsoletes:	kde-style-slicker

%description -n kde-style-%{_theme}
A completely flat, minimalist style without 3D effects. Without losing
speed and simplicity it acomplishes great usability.

%description -n kde-style-%{_theme} -l pl.UTF-8
Zupełnie płaski, minimalistyczny styl bez efektów 3D. Dzięki swojej
prostocie jest szybki i bardzo funkcjonalny.

%package -n kde-icons-%{_theme}
Summary:	KDE style - %{_theme}
Summary(pl.UTF-8):	Styl do KDE - %{_theme}
Group:		Themes
Version:	%{_icons_ver}
URL:		http://www.kde-look.org/content/show.php?content=6153
License:	LGPL
Requires:	kdelibs
Obsoletes:	kde-icons-slicker

%description -n kde-icons-%{_theme}
Flat, simple, icons with gray outlines.

%description -n kde-icons-%{_theme} -l pl.UTF-8
Płaskie, prost ikony z szarymi obwódkami.

%package -n kde-colorscheme-my%{_theme}
Summary:	Color scheme for KDE style - my%{_theme}
Summary(pl.UTF-8):	Schemat kolorów do stylu KDE - my%{_theme}
Group:		Themes
Requires:	kdebase-core
License:	GPL
Version:	0.1
URL:		http://www.kde-look.org/content/show.php?content=9399
Conflicts:	kde-colorscheme-reinhardt < 1

%description -n kde-colorscheme-my%{_theme}
A color scheme with pale beige menu and window background and blue
selection background.

%description -n kde-colorscheme-my%{_theme} -l pl.UTF-8
Schemat kolorów z wyblakłym beżowym tłem okna i menu oraz niebieskim
tłem zaznaczenia.

%package -n kde-colorscheme-%{_theme}
Summary:	Color scheme for KDE style - %{_theme}
Summary(pl.UTF-8):	Schemat kolorów do stylu KDE - %{_theme}
License:	Public Domain
Version:	1
Group:		Themes
URL:		http://www.kde-look.org/content/show.php?content=9411
Requires:	kdebase-core

%description -n kde-colorscheme-%{_theme}
A color scheme with grey window/menu/selection background and pale
pink list background.

%description -n kde-colorscheme-%{_theme} -l pl.UTF-8
Schemat kolorów z szarym tłem okna, menu i zaznaczenia oraz wyblakłym
różowym tłem list rozwijanych.

%package -n kde-wallpaper-%{_theme}
Summary:	KDE wallpaper - %{_theme}
Summary(pl.UTF-8):	Tapeta do KDE - %{_theme}
License:	GPL
Group:		Themes
# Contains /usr/share/wallpapers
Requires:	kdebase
Obsoletes:	kde-wallpaper-slicker

%description -n kde-wallpaper-%{_theme}
Gray background with the Reinhardt style KDE logo in the bottom right
corner and a gradiented gray/white login background for GNOME/KDE
Display Managers.

%description -n kde-wallpaper-%{_theme} -l pl.UTF-8
Szare tło z logiem KDE z motywu ikon Reinhardt w prawy dolnym rogu
oraz ekran logowania do GDM/KDM z biało-szarym gradientem.

%package -n kde-splash-%{_theme}
Summary:	Reinhardt splash screen
Summary(pl.UTF-8):	Ekran startowy - Reinhardt
License:	GPL
Version:	%{_splash_ver}
Group:		X11/Amusements
URL:		http://www.kde-look.org/content/show.php?content=7021
Requires:	kdebase-desktop

%description -n kde-splash-%{_theme}
A dark/violet grey gradiented splash screen with a KDE logo in the
Reinhardt style.

%description -n kde-splash-%{_theme} -l pl.UTF-8
Ekran startowy z gradientem kolorów od ciemno-szarego do
fioletowo-szarego, z logiem KDE w stylu Reinhardt.

%package -n gdm-theme-%{_theme}
Summary:	A Reinhardt theme for the GNOME Display Manager
Summary(pl.UTF-8):	Motyw Reinhardt do GDM
License:	LGPL
Version:	%{_gdm_ver}
Group:		Themes
URL:		http://www.kde-look.org/content/show.php?content=9948
Requires:	gdm

%description -n gdm-theme-%{_theme}
A simple,flat, grey and white GDM theme.

%description -n gdm-theme-%{_theme} -l pl.UTF-8
Płaski, prosty, biało-szary motyw do GDM.

%prep
%setup -q -n %{_theme}style-%{_theme_ver}
%patch0 -p0

%build
cp -f %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"

install -d $RPM_BUILD_ROOT%{_iconsdir}
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes
install -d $RPM_BUILD_ROOT%{_datadir}/wallpapers
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/%{_theme}

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/wallpapers

%{__tar} xfj %{SOURCE2} -C $RPM_BUILD_ROOT%{_iconsdir}

install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes/myreinhart.kcsrc
rm -rf tmp
mkdir tmp
%{__tar} xfj %{SOURCE4} -C tmp
%{__tar} xfj tmp/slickersplash-%{_splash_ver}/Slicker.tar.bz2 -C $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes
cp -f tmp/slickersplash-%{_splash_ver}/splash.png $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/Slicker
cp -f tmp/slickersplash-%{_splash_ver}/login_bg.jpg $RPM_BUILD_ROOT%{_datadir}/wallpapers

install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes/reinhart.kcsrc

%{__tar} xfj %{SOURCE6} -C tmp
cp -rf tmp/reinhardtgdm-%{_gdm_ver}/*.* $RPM_BUILD_ROOT%{_datadir}/gdm/themes/%{_theme}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-style-%{_theme}
%defattr(644,root,root,755)
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/reinhardt.themerc

%files -n kde-splash-%{_theme}
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/*

%files -n kde-colorscheme-%{_theme}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/reinhart.kcsrc

%files -n kde-colorscheme-my%{_theme}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/myreinhart.kcsrc

%files -n kde-wallpaper-%{_theme}
%defattr(644,root,root,755)
%{_datadir}/wallpapers/*

%files -n kde-icons-%{_theme}
%defattr(644,root,root,755)
%{_iconsdir}/*

%files -n gdm-theme-%{_theme}
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/%{_theme}
